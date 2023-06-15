from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("props2yaml")
except PackageNotFoundError:
    # package is not installed
    pass
