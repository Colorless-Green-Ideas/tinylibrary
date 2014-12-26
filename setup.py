#! /usr/bin/env python

from setuptools import setup
setup(name="tinylibrary",
      version="0.1a1",
      packages=["tinylibrary"],
      # scripts=[],
      author="Jack Laxson",
      author_email="jackjrabbit@gmail.com",
      description="Simple django app to manage a small library",
      # license="GPL v2 or later",
      install_requires=["django", "xmltodict", "requests"],
      url="https://github.com/Colorless-Green-Ideas/tinylibrary",
      # classifiers=["License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",]
      )
