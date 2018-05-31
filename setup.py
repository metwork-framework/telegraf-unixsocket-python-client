#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of telegraf-unixsocket-python-client library
# released under the 3-Clause BSD license.
# See the LICENSE file for more information.


from setuptools import setup, find_packages

DESCRIPTION = "A tiny and very limited python client to send metrics to " \
    "influxdb/telegraf through an unix socket"

with open('requirements.txt') as reqs:
    install_requires = [
        line for line in reqs.read().split('\n')
        if (line and not line.startswith('--')) and (";" not in line)]

setup(
    name='telegraf-unixsocket-client',
    version="0.0.1",
    author="Fabien MARTY",
    author_email="fabien.marty@gmail.com",
    url="https://github.com/metwork-framework/"
    "telegraf-unixsocket-python-client",
    packages=find_packages(),
    license='BSD',
    download_url='https://github.com/metwork-framework/'
    'telegraf-unixsocket-python-client',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development',
    ]
)
