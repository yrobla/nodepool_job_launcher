#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='nodepool_job_launcher',
    version='0.1.0',
    description="Nodepool Job Launcher acts as a wrapper to nodepool to spin instances and launch jobs to jenkins on demand",
    long_description=readme + '\n\n' + history,
    author="Yolanda Robla",
    author_email='yolanda.robla-mota@hp.com',
    url='https://github.com/yrobla/nodepool_job_launcher',
    packages=[
        'nodepool_job_launcher',
    ],
    package_dir={'nodepool_job_launcher':
                 'nodepool_job_launcher'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='nodepool_job_launcher',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)