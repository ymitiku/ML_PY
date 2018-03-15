from setuptools import setup,find_packages
from codecs import open 
import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,'README.md'),encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name = "ml_pl",
    version = "0.0.1",
    description="Python packge which contains method used in machine learning projects."
    long_description=long_desc
)