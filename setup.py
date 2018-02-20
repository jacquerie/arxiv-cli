# -*- coding: utf-8 -*-

"""A Python wrapper for the arXiv API."""

from __future__ import absolute_import, division, print_function

import os

from setuptools import find_packages, setup


URL = 'https://github.com/jacquerie/arxiv-cli'

readme = open('README.rst').read()

setup_requires = [
    'autosemver~=0.0,>=0.5.2',
]

install_requires = [
    'click~=6.0,>=6.7',
    'feedparser~=5.0,>=5.2.1',
    'requests~=2.0,>=2.18.4',
    'six~=1.0,>=1.11.0',
]

docs_require = []

tests_require = [
    'flake8-future-import~=0.0,>=0.4.3',
    'mock~=2.0,>=2.0.0',
    'pytest~=3.0,>=3.2.3',
    'pytest-cov~=2.0,>=2.5.1',
    'pytest-httpretty~=0.0,>=0.2.0',
]

extras_require = {
    'docs': docs_require,
    'tests': tests_require,
}

extras_require['all'] = []
for reqs in extras_require.values():
    extras_require['all'].extend(reqs)

packages = find_packages(exclude=['docs'])

setup(
    name='arxiv-cli',
    autosemver={
        'bugtracker_url': URL + '/issues',
    },
    url=URL,
    license='MIT',
    author='Jacopo Notarstefano',
    author_email='jacopo.notarstefano@gmail.com',
    packages=packages,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    description=__doc__,
    long_description=readme,
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    entry_points={
        'console_scripts': [
            'arxiv = arxiv_cli.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
