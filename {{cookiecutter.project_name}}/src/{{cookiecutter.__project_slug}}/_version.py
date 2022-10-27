from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version({{cookiecutter.project_name}})
except PackageNotFoundError:
    # package not installed
    __version__ = "0.0.0"