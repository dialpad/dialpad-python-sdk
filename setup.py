# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def readme():
  with open('README.md') as f:
    return f.read()


setup(
  name='python-dialpad',
  version='2.2.3',
  description='A python wrapper for the Dialpad REST API',
  long_description=readme(),
  long_description_content_type="text/markdown",
  author='Jake Nielsen',
  author_email='jnielsen@dialpad.com',
  license='MIT',
  url='https://github.com/dialpad/dialpad-python-sdk',
  install_requires=[
    'cached-property',
    'certifi',
    'chardet',
    'idna',
    'requests',
    'urllib3'
  ],
  include_package_data=True,
  packages=find_packages()
)
