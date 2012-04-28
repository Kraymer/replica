#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

"""File-level functions to read and write id3 tags."""

import copy, logging
from mutagen import id3, mp3


def get_tags(path):
    '''Get id3 frames of mp3 file located at given path'''

    try:
        audio = mp3.MP3(path)
    except mp3.HeaderNotFoundError :
        audio = {}
        header = id3.ID3()
        header.save(path)
        logging.warning("No ID3 header found, creating a new tag")
    return audio


def set_tags(path, tagVals, frames=None):
    '''Set id3 frames of files at path'''

    try:
        tags = id3.ID3(path)      
        tags_bak = copy.deepcopy(tags)
        tags.delete()  
    except id3.ID3NoHeaderError :
        tags = id3.ID3()
        tags.save(path)
        logging.warning("No ID3 header found, created one.")

    try:
        for (tag, val) in tagVals.items():
            if frames and tag.split('::')[0] not in frames:
                continue
            tags.add(val)
        tags.save(path)

    except :
        msg = "Error writing file '%s'" % path
        logging.debug(msg, exc_info=True)
        print msg
        if tags_bak:
            tags_bak.save(path) # restore id3

        return False

    return True