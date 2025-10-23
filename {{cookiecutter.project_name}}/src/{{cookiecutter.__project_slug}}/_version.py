from importlib.metadata import version, PackageNotFoundError

# Return 0.0.0 if package not installed
__version__ = "0.0.0"

if __package__:
    try:
        __version__ = version(__package__)
    except PackageNotFoundError:
        pass
