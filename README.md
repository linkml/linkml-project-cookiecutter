# LinkML Project Cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for projects using [LinkML](https://github.com/linkml/linkml).

## Prerequisites

The following are required and recommended tools for using this cookiecutter and the LinkML project that it generates. This is all one-time setup, so if you have already done it skip to the [next section](#creating-a-new-project)!

  * **Python >= 3.9**

    LinkML tools are mainly written in Python, so you will need a recent Python interpreter to run this generator and to use the generated project.

  * **pipx**

    pipx is a tool for managing isolated Python-based applications. It is the recommended way to install Poetry and cruft. To install pipx follow the instructions here: https://pypa.github.io/pipx/installation/

  * **Poetry**

    Poetry is a Python project management tool. You will use it in your generated project to manage dependencies and build distribution files. The template requires poetry version 2.0 or newer. If you have pipx installed ([alternative installation methods](https://python-poetry.org/docs/#installation) are available) you can install Poetry by running:

     ```shell
     pipx install poetry
     ```

    - For having both Poetry 2.x and Poetry 1.x installed at the same time,
      pipx has the option to install another version with a suffix-modified name,
      here "poetry1",

      ```bash
        `pipx install --suffix=1 "poetry<2.0"`.
      ```

    This project manages project-level configuration. User-level [configuration](https://python-poetry.org/docs/configuration/), if needed, is your responsibility.

  * **Poetry private repository**

    Sandboxed environments have private pypi repositories. Poetry supports project-level [repository](https://python-poetry.org/docs/repositories/), but it is recommended to configure [this plugin](https://pypi.org/project/poetry-plugin-pypi-mirror) to persist repository across all poetry projects (and avoid cookiecutter failure):
    ```shell
    pip3 install poetry-plugin-pypi-mirror --user
    # example, add line to `~/.profile` for persistence
    export POETRY_PYPI_MIRROR_URL = "https://pypi-proxy.myorg.com/repository/pypi-all/simple"
    ```

  * **Poetry Dynamic Versioning Plugin**:

    This plugin automatically updates certain version strings in your generated project when you publish it. Your generated project will automatically be set up to use it. Install it by running:
    ```shell
    poetry self add "poetry-dynamic-versioning[plugin]"
    ```


  * **cruft**

    cruft is a tool for generating projects based on a cookiecutter (like this one!) as well as keeping those projects updated if the original cookiecutter changes. Install it with pipx by running:
    ```shell
    pipx install cruft
    ```
    You may also choose to not have a persistent installation of cruft, in which case you would replace any calls to the `cruft` command below with `pipx run cruft`.


  * **make or just as command runner**

    The project contains a makefile but also a `justfile` with pre-defined complex commands. To execute these commands you either need `make` or [just](https://github.com/casey/just) as an alternative command runner. Especially for Windows users we suggest `just`. Install it by running:
    ```shell
    pipx install rust-just
    ```

## Creating a new project

### Step 1: Generate the project files

To generate a new LinkML project run the following:
```bash
cruft create https://github.com/linkml/linkml-project-cookiecutter
```
Alternatively, to add linkml project files to pre-existing directory,
(perhaps an existing non-linkml project), pass `-f` option:
```bash
cruft create -f https://github.com/linkml/linkml-project-cookiecutter
```

You will be prompted for a few values.  The defaults are fine for most
projects, but do name your project something that makes sense to you!
The interactive session will guide you through the process:

1. `project_name`: Name of the project, use kebab-case with no spaces.
Suggestions:
    - `patient-observation-schema`
    - `sample-collection-metadata`
    - `resume-standard`
2. `github_org`: Your github username or organization name. This is used to construct links to documentation pages.
3. `project_description`: Description of the project.
    - A single brief sentence is recommended
    - Can easily be modified later
4. `full_name`: Your name
5. `email`: Your email
6. `license`: Choose a license for the project. If your desired license is not listed you can update or remove the `LICNSE` file in the generated project.
7. `main_schema_class`:
    - This is used to generate an example schema which you can edit
    - The value of this field is ignored if this is a schemasheets project
    - You can always change this later
    - Examples: `Person`, `Observation`, `Sample`, `Entry`, `Gene`, `Event`
8. `create_python_project`
    - If "Yes", set this up as a python project
    - Select Yes if you want to make data classes that can be used by developers
9. `use_schemasheets`
    - If "Yes", set this to obtain your schema from
    [schemasheets](https://linkml.io/schemasheets)
10. `google_sheet_id`
     - Ignore/use default value if answer to previous question was "No"
     - If you are using schemasheets then enter your google doc ID here
     - If you like you can leave the default value, and this will use the demo schema
11. `google_sheet_tabs`
    - Ignore/use default value if not using schemasheets
    - If you are using schemasheets, enter a space-separated list of tabs
    - your tabs in your sheet MUST NOT have spaces in them
12. `github_token_for_pypi_deployment`:
    - The github token name which aligns with your autogenerated PyPI token for making releases.
    - This helps automated releases to PyPI
    - This should be ignored if this is not a python project
    - Even if this is a python project, you can leave blank and fill in later

### Step 2: Set up the LinkML project

Change to the folder your generated project is in.

Optionally customize your project if needed:

* pass arguments to linkml generators via 'config.yaml' configuration file;
* pass supported environment variables via '.env.public' configuration file;

Setup your project
```bash
cd my-awesome-schema  # using the folder example above
make setup
```

### Step 3: Edit the schema

Edit the schema (the .yaml file) in the
`src/my_awesome_schema/schema` folder

```bash
nano src/my_awesome_schema/schema/my_awesome_schema.yaml
```

### Step 4: Validate the schema

```bash
make test
```

### Step 5: Generate documentation locally

LinkML generates schema documentation automatically. The template comes with GitHub Actions that generate and publish the documentation when you push schema changes to GitHub. The published documentation can be found at a URL like this one:
`https://{github-user-or-organization}.github.io/{project-name}/`

You can also preview the documentation locally before pushing to GitHub by running:

```bash
make serve
```

### Step 6: Create a GitHub project

1. Go to https://github.com/new and follow the instructions, being sure to NOT add a `README` or `.gitignore` file (this cookiecutter template will take care of those files for you)

2. Add the remote to your local git repository

   ```bash
   git remote add origin https://github.com/{github-user-or-organization}/{project-name}.git
   git branch -M main
   git push -u origin main
   ```

3. Configure your repository for deploying the documentation as GitHub pages

* Under Settings > Actions > General in section "Workflow Permissions" mark "Read repository and packages permission".
* Under Pages in section "Build and Deployment":
  * Under "Source" select "Deploy from a branch"
  * Under "Branch" select "gh-pages" and "/ (root)"

### Step 7: Register the schema

See [How to register a schema](https://linkml.io/linkml/faq/contributing.html#how-do-i-register-my-schema)

### Making releases

See [How to Manage Releases of your LinkML Schema](https://linkml.io/linkml/howtos/manage-releases.html)

## Keeping your project up to date

In order to be up-to-date with the template, first check if there is a mismatch
between the project's boilerplate code and the template by running:

```bash
cruft check
```

This indicates if there is a difference between the current project's
boilerplate code and the latest version of the project template. If the project
is up-to-date with the template:

```output
SUCCESS: Good work! Project's cruft is up to date and as clean as possible :).
```

Otherwise, it will indicate that the project's boilerplate code is not
up-to-date by the following:

```output
FAILURE: Project's cruft is out of date! Run `cruft update` to clean this mess up.
```

For viewing the difference, run `cruft diff`. This shows the difference between the project's boilerplate code and the template's latest version.

After running `cruft update`, the project's boilerplate code will be updated to the latest version of the template.
