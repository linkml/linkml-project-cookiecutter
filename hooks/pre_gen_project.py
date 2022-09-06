"""Code to run before generating the project."""

import re
import sys
from jinja2 import environment

MODULE_REGEX = re.compile(r'^[_a-zA-Z][_a-zA-Z0-9]+$')

project_name = '{{ cookiecutter.project_name}}'

if not MODULE_REGEX.match(project_name):
    if "-" in project_name:
        invalid_char = "-"
    elif " " in project_name:
        invalid_char = "<space>"
    else:
        print(
            f'ERROR: {project_name} is not a valid Python module name. Try again with a valid project name.'
        )
        # Exit to cancel project
        sys.exit(1)
    print(
        f'WARNING: {project_name} is not a valid Python module name. Using "_" instead of {invalid_char} for module name.'
    )

def get_name_from_author(author):
    """Returns just the name from name <email> in author."""
    return re.sub('<[^>]+>',"",author)
    
environment.filters["get_name_from_author"] = get_name_from_author