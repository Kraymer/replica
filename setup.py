#!/usr/bin/env python

# Copyright (c) 2012-2018 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

from setuptools import setup


setup(name='replica',
    version='0.1.2',
    description='id3 metadata file cloner',
    long_description=open('README.md').read(),
    author='Fabrice Laporte',
    author_email='kraymer@gmail.com',
    url='https://github.com/KraYmer/replica',
    license='MIT',
    platforms='ALL',

    packages=[
      'replica',
    ],
    entry_points={
      'console_scripts': [
          'replica = replica.cli:main',
      ],
    },
    install_requires=[
      'mutagen'
    ],
    python_requires='>=2.6, <4',
    classifiers=[
      'Topic :: Multimedia :: Sound/Audio',
      'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
      'License :: OSI Approved :: MIT License',
      'Environment :: Console',
    ])
