"""Data test."""
import os
import glob
import unittest

from linkml_runtime.loaders import yaml_loader
from {{cookiecutter.__project_slug}}.datamodel.{{cookiecutter.__project_slug}} import {{cookiecutter.main_schema_class}}Collection

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(ROOT, "src", "data", "examples", "valid")

EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR, '*.yaml'))

ACCEPTABLE_PREFIX = f"{DATA_DIR}/{{{cookiecutter.main_schema_class}}Collection.class_name}"


class TestData(unittest.TestCase):
    """Test data and datamodel."""

    def test_data(self):
        """Date test."""
        for path in EXAMPLE_FILES:
            if path.startswith(ACCEPTABLE_PREFIX):
                obj = yaml_loader.load(path, target_class={{cookiecutter.main_schema_class}}Collection)
                assert obj
            else:
                print(f"{path} does not match {acceptable_prefix} so will not be tested")
