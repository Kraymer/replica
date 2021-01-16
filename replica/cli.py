#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2021 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

import os
import sys
import fnmatch
import logging
import re

from datetime import datetime

import click
import click_log

from replica import cloner

__version__ = "0.1.2"

logger = logging.getLogger(__name__)
click_log.basic_config(logger)


def get_mp3_paths(dirpath):
    """Return mp3 located into dirpath"""
    return [
        os.path.join(dirpath, x)
        for x in fnmatch.filter(sorted(os.listdir(dirpath)), "*.mp3")
    ]


def expand_args(src, dest, partial=False):
    """Expand src and dest into list of filepaths"""
    src_files = get_mp3_paths(src) if os.path.isdir(src) else [src]
    dest_files = get_mp3_paths(dest) if os.path.isdir(dest) else [dest]

    if partial:
        # Find a donor for each recipient
        regex = r"(\d+)(\D+)"
        src_selection = []
        dst_selection = []
        for dst in dest_files:
            m = re.match(regex, os.path.basename(dst))
            tracknum_dst = int(m.group(1))
            for src in src_files:
                m = re.match(regex, os.path.basename(src))
                tracknum_src = int(m.group(1))
                if tracknum_dst == tracknum_src:
                    src_selection.append(src)
                    dst_selection.append(dst)
        return src_selection, dst_selection

    return src_files, dest_files


def check_args(args):
    """Check arguments validity"""
    if len(args["src"]) != len(args["dst"]):
        logger.info("Error: SRC and DEST must have same number of files")
        return False
    return True


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]),
    help="""The id3 cloner.
    Copy id3 tags from SRC (file or directory) to DEST (idem).""",
)
@click.argument(
    "src",
    type=click.Path(exists=True),
    metavar="SRC",
    nargs=1,
)
@click.argument(
    "dst",
    type=click.Path(exists=True),
    metavar="DEST",
    nargs=1,
)
@click.option("-f", "--filename", default=False, is_flag=True, help="clone filenames")
@click.option(
    "-r",
    "--replace",
    default=False,
    is_flag=True,
    help="replace SRC with DEST. Warning: SRC files will be overwritten",
)
@click.option(
    "-p",
    "--partial",
    default=False,
    is_flag=True,
    help=("authorize partial album cloning by matching folder tracks individually"),
)
@click_log.simple_verbosity_option(logger)
@click.version_option()
def replica_cli(src, dst, filename, replace, partial):
    logging.debug("new session %s", str(datetime.now()))
    src, dest = expand_args(src, dst, partial)
    cloner.clone_id3(src, dest)
    # cloner.clone_path(src, dest, replace)
    # cloner.clone_dirpath(args["src_dir"], args["dst_dir"])
    exit(0)


def main(argv=None):
    replica_cli()


if __name__ == "__main__":
    sys.exit(main())
