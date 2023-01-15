# LinkML Project Cookiecutter

A [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for projects using [`Linkml`](https://github.com/linkml/linkml).


## Standard Protocol

### Step 1: Create a virtual environment

Create a Python virtual environment. You can read [this 
guide](https://realpython.com/python-virtual-environments-a-primer/) to learn more about them and how to create one.
We suggest using poetry, but you can use any tool you like.  Please note, most LinkML tools work best in Python 3.8 or higher.

An example using poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```bash
mkdir linkml-projects
cd linkml-projects
poetry init # creates a new poetry project with pyproject.toml.  Note this is not a new linkml project, it is just a virtual environment to install cruft.
poetry add click==8.0.4
poetry install # this creates your virtual environment.
```

Add `poetry-dynamic-versioning` as a plugin
```
poetry self add "poetry-dynamic-versioning[plugin]"
```

### Step 2: Install the cruft tool in your virtual environment
This tool will help you keep your project up to date with the latest LinkML tools and best practices.

In your poetry virtual environment:

```bash
poetry add cruft
```

### Step 3:  Use cruft to create your brand new LinkML project:

In your poetry virtual environment:

```bash
poetry shell
cruft create https://github.com/linkml/linkml-project-cookiecutter
```

You will be prompted for a few values.  The defaults are fine for most projects, but do name your project something 
that makes sense to you!  The interactive session will guide you through the process:

- `project_name`: Name of the project, use kebab-case with no spaces. Suggestions:
    - `patient-observation-schema`
    - `sample-collection-metadata`
    - `resume-standard`
- `project_description`: Description of the project.
    - A single brief sentence is recommended
    - Can easily be modified later
- `full_name`: Your name
- `email`: your email
- `main_schema_class`:
    - This is used to generate an example schema which you can edit
    - The value of this field is ignored if this is a schemasheets project
    - You can always change this later
    - Examples: `Person`, `Observation`, `Sample`, `Entry`, `Gene`, `Event`
- `create_python_project`
    - If "Yes", set this up as a python project
    - Select Yes if you want to make data classes that can be used by developers
- `use_schemasheets`
    - If "Yes", set this to obtain your schema from [schemasheets](https://linkml.io/schemasheets)
- `google_sheet_id`
    - Ignore/use default value if answer to previous question was "No"
    - If you are using schemasheets then enter your google doc ID here
    - If you like you can leave the default value, and this will use the demo schema
- `google_sheet_tabs`
    - Ignore/use default value if not using schemasheets
    - If you are using schemasheets, enter a space-separated list of tabs
    - your tabs in your sheet MUST NOT have spaces in them
- `github_token_for_pypi_deployment`:
   - The github token name which aligns with your autogenerated PyPI token for making releases.
   - This helps automated releases to PyPI
   - This should be ignored if this is not a python project
   - Even if this is a python project, you can leave blank and fill in later

This will generate the project folder abiding by the template configuration specified by `linkml-project-cookiecutter` in the [`cookiecutter.json`](https://github.com/linkml/linkml-project-cookiecutter/blob/main/cookiecutter.json) file. 

This will generate the project folder very similar to what is mentioned in the [linkml-project-template](https://github.com/linkml/linkml-project-template) project.

See [linkml/linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter) for more docs.

### Step 4: Setup the LinkML project

Change to the folder your generated project is in

```bash
cd my-awesome-schema  # using the folder example above
```

Connect project to Git
```bash
git init
git remote add origin https://github.com/my-org/my-awesome-schema.git
```

Setup the LinkML project
```bash
make setup
```

### Step 5: Edit the schema

Edit the schema (the .yaml file) in the linkml-projects/my-awesome-schema/src/my_awesome_schema/schema folder
```bash
nano src/my_awesome_schema/schema/my_awesome_schema.yaml
```

### Step 6: Validate the schema

```bash
make test
```

### Step 7: Auto-generate your documentation locally.
LinkML generates schema documenation automatically.  Step 7 here, allows you to preview the documentation
that LinkML generates before pushing to GitHub.  Note, this template comes with GitHub
Actions that autogenerate this documentation on release of your schema repository at a URL like this one:
https://my-user-or-organization.github.io/my-awesome-schema/ 

```bash
make serve
```

### Step 8: Create a github project

8a: Go to https://github.com/new and follow the instructions, being sure to NOT add a README or .gitignore file (this
cookiecutter template will take care of this for you)

8b: Add the remote to your local git repository`

```bash
git remote add origin https://github.com/my-user-or-organization/my-awesome-schema.git
git branch -M main
git push -u origin main
```

### Step 9: Deploy documentation

`make deploy`

### Step 10: Register the schema

See [How to register a schema](../faq/contributing)

## Keeping your project up to date

In order to be up-to-date with the template, first check if there is a mismatch between the project's boilerplate 
code and the template by running:

```bash
poetry shell
cruft check
```

This indicates if there is a difference between the current project's boilerplate code and the latest version of the 
project template. If the project is up-to-date with the template:

```
SUCCESS: Good work! Project's cruft is up to date and as clean as possible :).
```

Otherwise, it will indicate that the project's boilerplate code is not up-to-date by the following:

```
FAILURE: Project's cruft is out of date! Run `cruft update` to clean this mess up.
```

For viewing the difference, run `cruft diff`. This shows the difference between the project's boilerplate code and the 
template's latest version.

After running `cruft update`, the project's boilerplate code will be updated to the latest version of the template.

