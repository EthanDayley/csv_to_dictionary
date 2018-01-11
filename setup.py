"""
The setup file for csv_to_dictionary
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name="csv_to_dictionary",
        version="1.0.6",
        description="Ultra simple csv to dictionary conversion library",
        long_description=long_description,
        url="https://github.com/EthanDayley/csv_to_dictionary",
        author="Ethan Dayley",
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3"
        ],
        keywords="simple csv dictionary parser",
        packages=["csv_to_dictionary"],
        zip_safe=False
    )
