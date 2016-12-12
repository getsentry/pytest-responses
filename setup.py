#!/usr/bin/env python
"""
pytest-responses
================

py.test integration for responses

:copyright: (c) 2016 David Cramer
:license: Apache 2.0
"""

from setuptools import setup


setup_requires = []

install_requires = [
    'responses',
    'pytest',
]

tests_require = [
    'flake8',
]

extras_require = {
    'tests': tests_require,
}


setup(
    name='pytest-responses',
    version='0.1.0',
    author='David Cramer',
    author_email='dcramer@gmail.com',
    description=(
        'py.test integration for responses'
    ),
    url='https://github.com/getsentry/pytest-responses',
    license='Apache 2.0',
    long_description=open('README.rst').read(),
    py_modules=['pytest_responses'],
    zip_safe=False,
    install_requires=install_requires,
    extras_require=extras_require,
    tests_require=tests_require,
    setup_requires=setup_requires,
    include_package_data=True,
    entry_points={
        'pytest11': [
            'pytest-responses = pytest_responses',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Framework :: Pytest',
    ],
)
