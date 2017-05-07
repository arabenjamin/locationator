#!/usr/bin/python
from locationator import __version__
from setuptools import setup


setup(
	name='locationator',
	version= __version__,
	description='simple loaction tool',
	author='Ara Benjamin',
	author_email='ara.benjamin@gmail.com',
	url= "https://github.com/arabenjamin/locationator",
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	packages=['locationator'],
	classifiers=['Programming Language :: Python :: 2.7'],
	zip_safe=False)