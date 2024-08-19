# This file defines tasks to be run with the duty command runner.
# Docs: https://pawamoy.github.io/duty/usage/

import sys
from pathlib import Path

try:
    from duty import duty
    from dotenv import dotenv_values
except ImportError:
    print("Please install duty and python-dotenv with\n"
          "  pipx install duty\n"
          "  pipx inject duty python-dotenv")
    sys.exit(1)

config = {
    **dotenv_values(".env.public"),  # load shared development variables
    #**dotenv_values(".env.secret"),  # load sensitive variables
    #**os.environ,  # override loaded values with environment variables
}

RUN = "poetry run"
SCHEMA_NAME = config.get("LINKML_SCHEMA_NAME", "")
SOURCE_SCHEMA_PATH = config.get("LINKML_SCHEMA_SOURCE_PATH")

SRC = "src"
DEST = "project"
PYMODEL = Path(SRC) / SCHEMA_NAME / "datamodel"
DOCDIR = "docs"
EXAMPLEDIR = "examples"
CONFIG_YAML = config.get("LINKML_GENERATORS_CONFIG_YAML", "")
GEN_DOC_ARGS = config.get("LINKML_GENERATORS_GEN_DOC_ARGS", "")

SHEET_MODULE = "{{cookiecutter.__google_sheet_module}}"
SHEET_ID = config.get("LINKML_SCHEMA_GOOGLE_SHEET_ID","")
SHEET_TABS = config.get("LINKML_SCHEMA_GOOGLE_SHEET_TABS", "")
SHEET_MODULE_PATH = Path(SOURCE_SCHEMA_PATH).parent / f"{SHEET_MODULE}.yaml"


# Another output format that shows stdout also in case of successful execution
{% raw %}
PRETTY_FULL = (
    "{% if success %}<green>✓</green>"
    "{% elif nofail %}<yellow>✗</yellow>"
    "{% else %}<red>✗</red>"
    "{% endif %}"
    "<bold>{{ title or command }}</bold>"
    "{% if failure %} ({{ code }}) {% endif %}"
    "{% if output and not quiet %}\n"
    "{{ ('  > ' + command + '\n') if title else '' }}"
    "{{ output|trim|indent(2 * ' ') }}"
    "{% endif %}"
)
{% endraw %}

def check_config():
    if "LINKML_SCHEMA_NAME" not in config:
        print("Error **Project not configured**:\n - See '.env.public'\n")
    else:
        print("Project configuration OK")

def gen_project(ctx):
    """Generate project files from schema."""
    {% if cookiecutter.use_schemasheets == "Yes"  %}
    compile_sheets(ctx)
    {% endif %}
    ctx.run(f"{RUN} gen-project {CONFIG_YAML} -d {DEST} {SOURCE_SCHEMA_PATH}", title="Generating project")
    ctx.run(f"mv {DEST}/*.py {PYMODEL}", title="Moving generated files to datamodel")


{% if cookiecutter.use_schemasheets == "Yes"  %}
def compile_sheets(ctx):
    """Compile goolge sheets to linkml schema."""
    ctx.run(f"{RUN} sheets2linkml --gsheet-id {SHEET_ID} {SHEET_TABS} > {SHEET_MODULE_PATH}.tmp "
            "&& mv {SHEET_MODULE_PATH}.tmp {SHEET_MODULE_PATH}",
            title="Compiling google sheets")
{% endif %}

def gen_examples(ctx):
    """Generate example files from schema."""
    ctx.run(f"cp src/data/examples/* {EXAMPLEDIR}", title="Copying example files")

def gen_doc(ctx):
    """Generate documentation from schema."""
    ctx.run(f"cp -rf {SRC}/docs/* {DOCDIR}", title="Copying documentation files")
    ctx.run(f"{RUN} gen-doc {GEN_DOC_ARGS} -d {DOCDIR} {SOURCE_SCHEMA_PATH}", title="Generating documentation")

@duty
def install(ctx):
    """Install dependencies of the project."""
    ctx.run("poetry install", title="Installing dependencies")

@duty
def setup(ctx):
    """Initial setup (run this first)."""
    # generate products and add everything to github
    check_config()
    ctx.run("git init", title="Initializing git")
    install(ctx)

    gen_project(ctx)
    gen_examples(ctx)

    # gen-doc
    if not Path(f"{DOCDIR}").exists():
        # Todo: make it a duty tool
        ctx.run(Path(f"{DOCDIR}").mkdir(parents=True, exist_ok=True), title="Creating directory for docs")
    gen_doc(ctx)

    ctx.run("git add .cruft.json", title="Adding .cruft.json")
    ctx.run("git add .", title="Adding other untracked files")
    ctx.run("git commit -m 'chore: make setup was run' -a", title="Committing...")

    # This shows how to get full output even on success by using a custom format.
    ctx.run("git status", title="Git status", fmt=f"custom={PRETTY_FULL}")

@duty
def site(ctx):
    """Build the site locally (project & docs)."""
    gen_project(ctx)
    gen_doc(ctx)

def test_examples(ctx, directory="examples/output"):
    """Test examples."""
    if not Path(directory).exists():
        Path(directory).mkdir(parents=True, exist_ok=True)
    ctx.run(
        f"{RUN} linkml-run-examples "
        "--output-formats json "
		"--output-formats yaml "
		"--counter-example-input-directory src/data/examples/invalid "
		"--input-directory src/data/examples/valid "
		f"--output-directory {directory} "
		f"--schema {SOURCE_SCHEMA_PATH} > {directory}/README.md",
        title="Testing json and yaml examples"
    )

@duty
def test(ctx):
    """Run tests."""
    # test: test-schema test-python test-examples
    # test-python
    ctx.run(f"{RUN} pytest", title="Running tests")
    # test-schema
    ctx.run(f"{RUN} gen-project {CONFIG_YAML} -d tmp {SOURCE_SCHEMA_PATH}", title="Generating project as test")
    # test-examples
    test_examples(ctx)

@duty
def lint(ctx):
    """Run linkml linter."""
    ctx.run(f"{RUN} linkml-lint {SOURCE_SCHEMA_PATH}", title="Running linkml linter")

@duty
def testdoc(ctx):
    """Test documentation build."""
    gen_doc(ctx)
    # TODO  replace with duty mkdocs callable
    ctx.run(f"{RUN} mkdocs serve", title="Serving documentation on http://127.0.0.1:8000/")

@duty
def deploy(ctx):
    """Deploy the site to GitHub Pages."""
    all(ctx)
    # TODO  replace with duty mkdocs callable
    ctx.run(f"{RUN} mkdocs gh-deploy", title="Deploying documentation to GitHub pages")

@duty
def check(ctx):
    """Check if underlying cookiecutter template has changed."""
    ctx.run("cruft check", title="Running cruft check")
    # run also cruft diff? (makefile is a bit unclear)

@duty
def update(ctx):
    """Update the project."""
    ctx.run("cruft update", title="Running cruft update")
    ctx.run("poetry add -D linkml@latest", title="Updating linkml")

@duty
def all(ctx):
    """Generate all project files."""
    site(ctx)
    gen_examples(ctx)
    gen_doc(ctx)
