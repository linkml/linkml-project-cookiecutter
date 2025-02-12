# On Windows the bash shell that comes with Git for Windows should be used.
# If it is not on path, give the path to the executable in the following line.
#set windows-shell := ["C:/Program Files/Git/usr/bin/sh", "-cu"]

# Load environment variables from config.public.mk or specified file
set dotenv-load := true
# set dotenv-filename := env_var_or_default("LINKML_ENVIRONMENT_FILENAME", "config.public.mk")
set dotenv-filename := x'${LINKML_ENVIRONMENT_FILENAME:-config.public.mk}'


# List all commands as default command. The prefix "_" hides the command.
_default: _status
    @just --list

# Set cross-platform Python shebang line (assumes presence of launcher on Windows)
shebang := if os() == 'windows' {
  'py'
} else {
  '/usr/bin/env python3'
}

# Environment variables with defaults
schema_name := env_var_or_default("LINKML_SCHEMA_NAME", "")
source_schema_path := env_var_or_default("LINKML_SCHEMA_SOURCE_PATH", "")

use_schemasheets := env_var_or_default("LINKML_USE_SCHEMASHEETS", "No")
sheet_module := env_var_or_default("LINKML_SCHEMA_GOOGLE_SHEET_MODULE", "")
sheet_ID := env_var_or_default("LINKML_SCHEMA_GOOGLE_SHEET_ID", "")
sheet_tabs := env_var_or_default("LINKML_SCHEMA_GOOGLE_SHEET_TABS", "")
sheet_module_path := source_schema_path / sheet_module + ".yaml"

config_yaml := if env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "") != "" {
  "--config-file " + env_var_or_default("LINKML_GENERATORS_CONFIG_YAML", "")
} else {
  ""
}
gen_doc_args := env_var_or_default("LINKML_GENERATORS_DOC_ARGS", "")
gen_owl_args := env_var_or_default("LINKML_GENERATORS_OWL_ARGS", "")
gen_java_args := env_var_or_default("LINKML_GENERATORS_JAVA_ARGS", "")
gen_ts_args := env_var_or_default("LINKML_GENERATORS_TYPESCRIPT_ARGS", "")

# Directory variables
src := "src"
dest := "project"
pymodel := src / schema_name / "datamodel"
docdir := "docs"
exampledir := "examples"

# Show current project status
_status: _check-config
    @echo "Project: {{schema_name}}"
    @echo "Source: {{source_schema_path}}"

# Run initial setup (run this first)
setup: _check-config _git-init install _gen-project _gen-examples _gendoc _git-add _git-commit

# Install project dependencies
install:
    poetry install

# Check project configuration
_check-config:
    #!{{shebang}}
    import os
    schema_name = os.getenv('LINKML_SCHEMA_NAME')
    if not schema_name:
        print('**Project not configured**:\n - See \'.env.public\'')
        exit(1)
    print('Project-status: Ok')

# Updates project template and LinkML package
update: _update-template _update-linkml

# Update project template
_update-template:
    cruft update

# Update LinkML to latest version
_update-linkml:
    poetry add -D linkml@latest

# Create data harmonizer
_create-data-harmonizer:
    npm init data-harmonizer {{source_schema_path}}

# Generate all project files
alias all := site

# Generate site locally
site: _gen-project _gendoc

# Deploy site
deploy: site
  mkd-gh-deploy

_compile_sheets:
    @if [ "{{use_schemasheets}}" != "No" ]; then \
        poetry run sheets2linkml --gsheet-id {{sheet_ID}} {{sheet_tabs}} > {{sheet_module_path}}.tmp && \
        mv {{sheet_module_path}}.tmp {{sheet_module_path}}; \
    fi

# Generate examples
_gen-examples:
    mkdir -p {{exampledir}}
    cp -r src/data/examples/* {{exampledir}}

# Generate project files
_gen-project: _ensure_pymodel_dir _compile_sheets
    poetry run gen-project {{config_yaml}} -d {{dest}} {{source_schema_path}} && \
    mv {{dest}}/*.py {{pymodel}}
    @if [ ! -z "${{gen_owl_args}}" ]; then \
      mkdir -p {{dest}}/owl || true && \
      poetry run gen-owl {{gen_owl_args}} {{source_schema_path}} > {{dest}}/owl/{{schema_name}}.owl.ttl || true ; \
    fi
    @if [ ! ${{gen_java_args}} ]; then \
      poetry run gen-java {{gen_java_args}} --output-directory {{dest}}/java/ {{source_schema_path}} || true ; \
    fi
    @if [ ! ${{gen_ts_args}} ]; then \
      poetry run gen-typescript {{gen_ts_args}} {{source_schema_path}} > {{dest}}/typescript/{{schema_name}}.ts || true ; \
    fi

# Run all tests
test: _test-schema _test-python _test-examples

# Test schema generation
_test-schema:
    poetry run gen-project {{config_yaml}} -d tmp {{source_schema_path}}

# Run Python unit tests with pytest
_test-python:
    poetry run python -m pytest

# Run example tests
_test-examples: _ensure_examples_output
    poetry run linkml-run-examples \
        --output-formats json \
        --output-formats yaml \
        --counter-example-input-directory src/data/examples/invalid \
        --input-directory src/data/examples/valid \
        --output-directory examples/output \
        --schema {{source_schema_path}} > examples/output/README.md

# Run linting
lint:
    poetry run linkml-lint {{source_schema_path}}

# Generate documentation
_gendoc: _ensure_docdir
    cp -r {{src}}/docs/files/* {{docdir}}
    poetry run gen-doc {{gen_doc_args}} -d {{docdir}} {{source_schema_path}}

# Build docs and run test server
testdoc: _gendoc _serve

# Run documentation server
_serve:
    poetry run mkdocs serve

# Initialize and add everything to git
_git-init-add: _git-init _git-add _git-commit _git-status

# Initialize git repository
_git-init:
    git init

# Add files to git
_git-add:
    touch .cruft.json
    git add .

# Commit files to git
_git-commit:
    git commit -m 'chore: make setup was run' -a

# Show git status
_git-status:
    git status

# Clean all generated files
clean:
    rm -rf {{dest}}
    rm -rf tmp
    rm -rf {{docdir}}/*
    rm -rf {{pymodel}}

# Private recipes
_ensure_pymodel_dir:
    -mkdir -p {{pymodel}}

_ensure_docdir:
    -mkdir -p {{docdir}}

_ensure_examples_output:
    -mkdir -p examples/output

import "project.justfile"
