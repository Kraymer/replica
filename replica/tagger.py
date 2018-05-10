#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2018 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

"""File-level functions to read and write id3 tags.
"""

import copy
import logging
from mutagen import id3, mp3


def get_tags(filepath):
    """Get id3 frames of mp3 file located at given filepath
    """
    try:
        audio = mp3.MP3(filepath)
    except mp3.HeaderNotFoundError:
        audio = {}
        header = id3.ID3()
        header.save(filepath)
        logging.warning("No ID3 header found, creating a new tag")
    return audio


def set_tags(filepath, tag_vals, frames=None):
    """Set id3 frames of file
    """
    try:
        tags = id3.ID3(filepath)
        tags_bak = copy.deepcopy(tags)
        tags.delete()
    except id3.ID3NoHeaderError:
        tags = id3.ID3()
        tags.save(filepath)
        logging.warning("No ID3 header found, created one.")

    try:
        for (tag, val) in tag_vals.items():
            if frames and tag.split('::')[0] not in frames:
                continue
            tags.add(val)
        tags.save(filepath)
    except:
        msg = "Error writing file '%s'" % filepath
        print msg
        if tags_bak:
            tags_bak.save(filepath)  # restore id3
        return False
    return True
