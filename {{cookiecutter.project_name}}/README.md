# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

## Website

[https://{{cookiecutter.github_org}}.github.io/{{cookiecutter.project_name}}](https://{{cookiecutter.github_org}}.github.io/{{cookiecutter.project_name}})

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [{{cookiecutter.__project_slug}}](src/{{cookiecutter.__project_slug}})
    * [schema](src/{{cookiecutter.__project_slug}}/schema) -- LinkML schema
      (edit this)
{%- if cookiecutter.create_python_classes == "Yes" %}
    * [datamodel](src/{{cookiecutter.__project_slug}}/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
{%- endif %}

## Developer Documentation

<details>
To run commands you may use good old make or the command runner [just](https://github.com/casey/just/) which is a better choice on Windows.
Use the `make` command or `duty` commands to generate project artefacts:
* `make help` or `just --list`: list all pre-defined tasks
* `make all` or `just all`: make everything
* `make deploy` or `just deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
