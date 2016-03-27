#!/usr/bin/env python
import sys
sys.path.insert(1, 'recon')

import os
import fnmatch
import recon.release
from setuptools import setup, find_packages, Extension


version = recon.release.get_info()
recon.release.write_template(version, 'lib/astrolib/coords/')

SOURCES = [
    os.path.join(root, f)
    for root, _, files in os.walk('src')
    for f in files if f.endswith('.c')
]

setup(
    name = 'astrolib.coords',
    version = version.pep386,
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
