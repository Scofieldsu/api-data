#!/usr/bin/env python
# coding=utf-8

import os
from setuptools import setup, find_packages
from apidata import version

try:
    import multiprocessing
except ImportError:
    pass


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ""

setup(
    name="api-data",
    version=version,
    packages=find_packages(),
    test_suite="tests",

    # metadata for upload to PyPI
    author="Yu Yuan",
    author_email="yuyuan_v@163.com",
    url="https://github.com/Scofieldsu/api-data.git",
    description=" convert func's __doc__ to API-DATA protocol 's  data ",
    long_description=read('readme.md'),

    # Full list:
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    license="MIT",
    zip_safe=False
)