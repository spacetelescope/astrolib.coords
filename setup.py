#!/usr/bin/env python
import os
import fnmatch
from setuptools import setup, find_packages, Extension
from version import get_git_version


SOURCES = [
    os.path.join(root, f)
    for root, _, files in os.walk('src')
    for f in files if f.endswith('.c')
]

git_version = get_git_version()
with open('lib/astrolib/coords/version.py', 'w') as version_data:
    version_data.write("__version__ = '{0}'".format(git_version))

setup(
    name = 'astrolib.coords',
    version = git_version,
    author = 'Vicki Laidler',
    author_email = 'help@stsci.edu',
    description = 'Astronomical coordinates & angular separations (OO)',
    url = 'http://www.astrolib.org',
    classifiers = [
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = [
        'nose',
        'numpy',
    ],

    package_dir = {
        '':'lib',
    },
    packages = find_packages('lib/*'),
    ext_modules = [
        Extension('astrolib.coords._pytpm', sources=SOURCES)
    ]
)
