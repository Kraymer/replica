#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2021 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

"""This module contains functions to extract properties of files and apply
them to others files.
"""

import logging
import os
import shutil
from replica import tagger

logger = logging.getLogger(__name__)


def clone_id3(srcs, dsts):
    """Apply id3 srcs tags from srcs to dests files"""
    logger.info("Cloning id3 metadata...", end="")

    for (src, dst) in zip(srcs, dsts):
        tags = tagger.get_tags(src)
        tagger.set_tags(dst, tags)


def clone_path(srcs, dsts, inplace):
    """Apply srcs relative filenames to dests files"""
    logger.info("Renaming files.........", end="")

    dst_dir = os.path.dirname(dsts[0])
    for (src, dst) in zip(srcs, dsts):
        if inplace:
            # Replace donor by recipient
            shutil.move(dst, src)
        else:
            mv_dst = os.path.join(dst_dir, os.path.basename(src))
            shutil.move(dst, mv_dst)


def clone_dirpath(src, dst):
    """Apply src directory name to dst directory"""
    src_base = os.path.split(os.path.normpath(src))[1]
    dst_dir = os.path.split(os.path.normpath(dst))[0]
    shutil.move(dst, os.path.join(dst_dir, src_base))
