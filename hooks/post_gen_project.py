"""Code to run after generating the project."""

import re
import sys
import shutil
from pathlib import Path

shutil.rmtree("licenses")

if '{{ cookiecutter.create_python_classes }}' == "No":
    print("TODO - cleanup python")

print("** PROJECT CREATION COMPLETE **\n")
print(f"** {'{{ cookiecutter.__project_slug}}'} **\n")
print("Next steps:")
print("cd {{cookiecutter.project_name}}")
print("make setup")
