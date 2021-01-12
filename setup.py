#!/usr/bin/env python

# Copyright (c) 2012-2021 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

import codecs
import os
import re
from setuptools import setup

PKG_NAME = "replica"
DIRPATH = os.path.dirname(__file__)


def read_rsrc(filename, pypi_compat=False):
    """Return content of filename.

       If pypi_compat is True, remove emojis and anything preceding
       `.. pypi` comment if present.
    """
    with codecs.open(os.path.join(DIRPATH, filename), encoding="utf-8") as _file:
        data = _file.read().strip()
        if pypi_compat or filename == "README.rst":
            data = re.sub(r":(\w+\\?)+:", u"", data[data.find(".. pypi"):] or data)
    return data


with codecs.open("{}/__init__.py".format(PKG_NAME), encoding="utf-8") as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE
    ).group(1)


setup(name=PKG_NAME,
    version=version,
    description='id3 metadata file cloner',
    long_description=read_rsrc("README.rst"),
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
    install_requires=read_rsrc("requirements.txt").split("\n"),
    python_requires='>=2.6, <4',
    classifiers=[
      'Topic :: Multimedia :: Sound/Audio',
      'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
      'License :: OSI Approved :: MIT License',
      'Environment :: Console',
    ])
