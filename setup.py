#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setu

setup(name='drexel-shaft-protection',
      version='1.0',
      install_requires=[
	'mechanize',
	'lxml'
      ]
)
