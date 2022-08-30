#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

long_description = ""
with open('README.rst') as f:
    long_description = f.read()

# Fixes a version conflict between numpy and scipy on python 3.9+
scipy = "scipy" if sys.version_info < (3, 9) else "scipy>=1.7"

setup(
    name='ImageHash',
    version='4.2.1',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['imagehash'],
    package_data={'imagehash': ['py.typed']},
    data_files=[('images', ['tests/data/imagehash.png'])],
    scripts=['find_similar_images.py'],
    url='https://github.com/JohannesBuchner/imagehash',
    license='2-clause BSD License',
    description='Image Hashing library',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    install_requires=[
        "six",
        "numpy",
        scipy,       # for phash
        "pillow",      # or PIL
        "PyWavelets",  # for whash
    ],
    test_suite='tests',
    tests_require=['pytest>=3'],
)
