#!/usr/bin/python
#from locationator import __version__
from setuptools import setup

__version__ = '0.1.2'


with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
	name='locationator',
	install_requires=install_requires,
	version= __version__,
	description='simple location tool',
	author='Ara Benjamin',
	author_email='ara.benjamin@gmail.com',
	url= "https://github.com/arabenjamin/locationator",
	license='Creative Commons Attribution-Noncommercial-Share Alike license',
	packages=['locationator'],
	classifiers=['Programming Language :: Python :: 2.7'],
	zip_safe=False)
