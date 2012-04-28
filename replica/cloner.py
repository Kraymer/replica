#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

"""This module contains functions to extract properties of files and apply 
them to others files."""

import os, shutil 
import logging
from replica import tagger

def clone_id3(srcs, dsts):
    '''Apply id3 srcs tags from srcs to dests files'''

    for (src, dst) in zip(srcs, dsts):
        tags = tagger.get_tags(src)
        tagger.set_tags(dst, tags)


def clone_path(srcs, dsts, inplace):
    '''Apply srcs relative filenames to dests files'''

    dst_dir = os.path.dirname(dsts[0])
    for (src, dst) in zip(srcs, dsts):
        if inplace:
            shutil.move(dst, src)
            logging.debug('Exec move %s => %s', dst, src)
        else:
            mv_dst = os.path.join(dst_dir, os.path.basename(src))
            shutil.move(dst, mv_dst)
            logging.debug('Exec move %s => %s', dst, mv_dst)

        
def clone_dirpath(src, dst):
    '''Apply src directory name to dst directory'''

    _, src_base = os.path.split(os.path.normpath(src))
    dst_dir, _ = os.path.split(os.path.normpath(dst))

    shutil.move(dst, os.path.join(dst_dir, src_base))  
