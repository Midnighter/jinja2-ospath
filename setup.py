#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    "jinja2"
]

test_requirements = [
    "tox"
]

setup(
    name="jinja2_ospath",
    version="0.1.0",
    description="A Jinja2 extension that introduces the filters basename and dirname.",
    long_description=readme,
    author="Moritz Emanuel Beber",
    author_email="midnighter@posteo.net",
    url="https://github.com/Midnighter/jinja2_ospath",
    packages=find_packages(),
    include_package_data=False,
    install_requires=requirements,
    license="3-Clause BSD License",
    zip_safe=False,
    keywords="jinja2 extension os.path dirname basename",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
