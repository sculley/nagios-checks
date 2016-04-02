#!/usr/bin/env python

from setuptools import setup

setup(
    name='nagios-checks',
    version='0.0.1',
    packages=[],
    scripts=['bin/check_aws_vpn_connection'],
    include_package_data=True,
    license='MIT License',
    author='Sam Culley',
    author_email='sam@samculley.co.uk',
    url='https://www.samculley.co.uk',
    install_requires=['boto3'],
    long_description=open('README.md').read(),
)
