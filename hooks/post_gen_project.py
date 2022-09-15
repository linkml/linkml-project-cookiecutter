"""Code to run after generating the project."""

import re
import sys
import shutil
from pathlib import Path

shutil.rmtree("licenses")

project_slug = '{{ cookiecutter.__project_slug}}'
create_python_classes = '{{ cookiecutter.create_python_classes}}'
use_schemasheets_option = '{{ cookiecutter.use_schemasheets }}'

if create_python_classes == "No":
    print("TODO - cleanup python")

if use_schemasheets_option == "No":
    print("TODO - Change MakeFile: remove compile-sheets from gen-project")


print("** PROJECT CREATION COMPLETE **\n")
print("Next steps:")
print("cd {{cookiecutter.project_name}}")
print("make setup")
