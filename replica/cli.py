#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2021 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

from __future__ import print_function
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


def replicate(args):
    """Clone id3 and eventually paths"""
    if not check_args(args):
        return 1
    print("Cloning id3 metadata...", end="")
    cloner.clone_id3(args["src"], args["dst"])
    print("done")
    if args["filename"] or args["update"]:
        print("Renaming files.........", end="")
        cloner.clone_path(args["src"], args["dst"], args["update"])
        if args["src_dir"] and not args["update"]:
            try:
                cloner.clone_dirpath(args["src_dir"], args["dst_dir"])
            except OSError as e:
                print("failed\n%s" % e)
                return 1
        print("done")
    return 0


def get_mp3_paths(path):
    """Return mp3 files located at path"""
    res = [path]
    if os.path.isdir(path):
        res = fnmatch.filter(sorted(os.listdir(path)), "*.mp3")
        res = [os.path.join(path, x) for x in res]
    return res


def expand_args(args):
    """Edit/add entries to args dictionary"""
    for (key_files, key_dir) in zip(("src", "dst"), ("src_dir", "dst_dir")):
        args[key_dir] = get_mp3_paths(args[key_files])  # expand files
        if args[key_dir]:
            # if expanded, then original src was a dir, so swap the dict values
            args[key_dir], args[key_files] = args[key_files], args[key_dir]

    if args["partial"]:
        # Find a donor for each recipient
        regex = r"(\d+)(\D+)"
        src_selection = []
        dst_selection = []
        for dst in args["dst"]:
            m = re.match(regex, os.path.basename(dst))
            tracknum_dst = int(m.group(1))
            for src in args["src"]:
                m = re.match(regex, os.path.basename(src))
                tracknum_src = int(m.group(1))
                if tracknum_dst == tracknum_src:
                    src_selection.append(src)
                    dst_selection.append(dst)
        args["src"] = src_selection
        args["dst"] = dst_selection
    return args


def check_args(args):
    """Check arguments validity"""
    if len(args["src"]) != len(args["dst"]):
        print("Error: SRC and DEST must have same number of files")
        return False
    return True


@click.command(
    context_settings=dict(help_option_names=["-h", "--help"]), help="The id3 cloner"
)
@click.argument(
    "src",
    type=click.Path(exists=True),
    metavar="SRC",
    nargs=1,
    help="the id3 donor (file or directory).",
)
@click.argument(
    "dst",
    type=click.Path(exists=True),
    metavar="DEST",
    nargs=1,
    help="the id3 recipient (file or directory).",
)
@click.option("-f", "--filename", default=False, is_flag=True, help="clone filenames.")
@click.option(
    "-u",
    "--update",
    default=False,
    is_flag=True,
    help="clone absolute paths. Warning: SRC files will be overwritten.",
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
def replica_cli(src, dest, filename, update, partial):
    logging.debug("new session %s", str(datetime.now()))
    # res = replicate(args)
    # exit(res)


def main(argv=None):
    replica_cli()


if __name__ == "__main__":
    sys.exit(main())
