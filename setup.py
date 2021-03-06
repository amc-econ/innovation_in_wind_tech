#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Antoine Mathieu Collin",
    author_email='a.mathieucollin@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Unpacking innovation in wind technologies using nlp on patent data",
    entry_points={
        'console_scripts': [
            'innovation_in_wind_tech=innovation_in_wind_tech.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='innovation_in_wind_tech',
    name='innovation_in_wind_tech',
    packages=find_packages(include=['innovation_in_wind_tech', 'innovation_in_wind_tech.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/amc-econ/innovation_in_wind_tech',
    version='0.1.0',
    zip_safe=False,
)
