"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
_readme = (here / "README.md").read_text(encoding="utf-8")
_license = (here / "LICENSE").read_text(encoding="utf-8")

setup(
    name="metaflow-nlp",
    version="0.1.0",
    description="Metaflow NLP toy project",
    long_description=_readme,
    url="https://github.com/dewith/metaflow-nlp/",
    author="Dewith Miramón",
    author_email="dewithmiramon@gmail.com",
    license=_license,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
