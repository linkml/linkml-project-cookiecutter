from pathlib import Path
from .{{cookiecutter.__project_slug}} import *

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "{{cookiecutter.__project_slug}}.yaml"
