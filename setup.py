from setuptools import setup

setup(
    name="pyshuf2",
    version="0.0.1",
    author="Matthew Yang",
    description="An attempt to bugfix an inexact python clone of GNU shuf and bring it into the modern Python 3 era.",
    license="GPL-3",
    keywords="shuf",
    url="https://github.org/matthewyang204/pyshuf",
    repository="https://github.org/jakekara/pyshuf",
    packages=["pyshuf"],
    entry_points = {
        "console_scripts": ["pyshuf2=pyshuf2.__main__:main"]
    }
)
