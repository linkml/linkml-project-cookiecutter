from jinja2.ext import Extension, Environment
import re
import pathlib
import sys

pwd = pathlib.Path(__file__).parent.resolve()
sys.path.append(pwd)

def get_name_from_author(value):
    """Returns just the name from name <email> in author."""
    return re.sub('<[^>]+>',"",value)

class ProjectExtensions(Extension):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)
        environment.filters["get_name_from_author"] = get_name_from_author