# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
  readme = f.read()

setup(
  name='python-dialpad',
  version='0.1.0',
  description='A python wrapper for the Dialpad REST API',
  long_description=readme,
  author='Jake Nielsen',
  author_email='jnielsen@dialpad.com',
  url='https://github.com/dialpad/dialpad-python-sdk',
  packages=find_packages()
)
