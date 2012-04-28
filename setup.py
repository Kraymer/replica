#!/usr/bin/env python

# Copyright (c) 2012 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

import os
import sys

from setuptools import setup

def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='replica',
      version='0.1.0',
      description='id3 metadata file cloner',
      long_description=open('README.md').read(),
      author='Fabrice Laporte',
      author_email='tunecrux@gmail.com',
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

      classifiers=[
          'Topic :: Multimedia :: Sound/Audio',
          'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
          'License :: OSI Approved :: MIT License',
          'Environment :: Console',
      ],
)
