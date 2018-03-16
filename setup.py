from setuptools import setup,find_packages
from codecs import open 
import os


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here,'README.rst'),encoding="utf-8") as f:
    long_desc = f.read()

setup(
    name = "ml_py",
    version = "0.0.003",
    description="Python packge which contains method used in machine learning projects.",
    long_description=long_desc,
    url = "https://github.com/mitiku1/ML_PY",
    author = "Mitiku Yohannes",
    author_email = "se.mitiku.yohannes@gmail.com",

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Machine learning tools',
    packages=find_packages(include=['ml_py', 'ml_py.image', 'main']),
    install_requires=['keras',"tensorflow"],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/mitiku1/ML_PY/issues',
        'Say Thanks!': 'https://saythanks.io/to/mitiku1',
        'Source': 'https://github.com/mitiku1/ML_PY/',
    },
)