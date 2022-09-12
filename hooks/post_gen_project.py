"""Code to run after generating the project."""

import re
import sys
import shutil
from pathlib import Path

shutil.rmtree("licenses")

project_slug = '{{ cookiecutter.__project_slug}}'
create_python_classes = '{{ cookiecutter.create_python_classes}}'

if create_python_classes == "No":
    print("TODO - cleanup python")

print("** PROJECT CREATION COMPLETE **\n")
print("Next steps:")
print("cd {{cookiecutter.project_name}}")
print("make setup")
