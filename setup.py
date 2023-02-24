"""Python setup.py for spotify_terminal_plugin package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("spotify_terminal_plugin", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="spotify_terminal_plugin",
    version=read("spotify_terminal_plugin", "VERSION"),
    description="Awesome spotify_terminal_plugin created by ahmed-ghaf-404",
    url="https://github.com/ahmed-ghaf-404/Spotify-Terminal-Plugin/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="ahmed-ghaf-404",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["spotify_terminal_plugin = spotify_terminal_plugin.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
