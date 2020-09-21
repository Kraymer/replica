#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012-2018 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

from __future__ import print_function
import os
import sys
import argparse
import fnmatch
import logging
import re
import tempfile

from datetime import datetime
from replica import cloner

# Logging config
LOG_FILENAME = os.path.join(tempfile.gettempdir(), 'replica.log')
LOG_FORMAT = "%(lineno)d:%(levelname)s: " + "%(message)s"
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,
                    format=LOG_FORMAT)


def replicate(args):
    """Clone id3 and eventually paths
    """
    if not check_args(args):
        return 1
    print('Cloning id3 metadata...', end='')
    cloner.clone_id3(args['src'], args['dst'])
    print('done')
    if args['filename'] or args['update']:
        print('Renaming files.........', end='')
        cloner.clone_path(args['src'], args['dst'], args['update'])
        if args['src_dir'] and not args['update']:
            try:
                cloner.clone_dirpath(args['src_dir'], args['dst_dir'])
            except OSError as e:
                print('failed\n%s' % e)
                return 1
        print('done')
    return 0


def get_mp3_paths(path):
    """Return mp3 files located at path
    """
    res = [path]
    if os.path.isdir(path):
        res = fnmatch.filter(sorted(os.listdir(path)), '*.mp3')
        res = [os.path.join(path, x) for x in res]
    return res


def expand_args(args):
    """Edit/add entries to args dictionary
    """
    for (key_files, key_dir) in zip(('src', 'dst'), ('src_dir', 'dst_dir')):
        args[key_dir] = get_mp3_paths(args[key_files])  # expand files
        if args[key_dir]:
            # if expanded, then original src was a dir, so swap the dict values
            args[key_dir], args[key_files] = args[key_files], args[key_dir]

    if args['partial']:
        # Find a donor for each recipient
        regex = r'(\d+)(\D+)'
        src_selection = []
        dst_selection = []
        for dst in args['dst']:
            m = re.match(regex, os.path.basename(dst))
            tracknum_dst = int(m.group(1))
            for src in args['src']:
                m = re.match(regex, os.path.basename(src))
                tracknum_src = int(m.group(1))
                if tracknum_dst == tracknum_src:
                    src_selection.append(src)
                    dst_selection.append(dst)
        args['src'] = src_selection
        args['dst'] = dst_selection
    return args


def check_args(args):
    """Check arguments validity
    """
    if len(args['src']) != len(args['dst']):
        print('Error: SRC and DEST must have same number of files')
        return False
    return True


def get_parser(prog=sys.argv[0]):
    """Return the command parser.
    """
    parser = argparse.ArgumentParser(
        description='Clone id3 metadata between mp3 files.',
        epilog='Report bugs to kraymer@gmail.com',
        prog=os.path.basename(prog))

    parser.add_argument('src', metavar='SRC', nargs=1,
                        help='the id3 donor (file or directory).')
    parser.add_argument('dst', metavar='DEST', nargs=1,
                        help='the id3 recipient (file or directory).')
    parser.add_argument('-f', '--filename', action='store_true',
                        help="clone filenames.")
    parser.add_argument('-u', '--update', action='store_true',
        help="clone absolute paths. Warning: SRC files will be overwritten.")
    parser.add_argument('-p', '--partial', action='store_true',
                        help=('authorize partial album cloning by matching'
                        ' folder tracks individually'))
    return parser


def main(argv=None):

    if argv is None:
        argv = sys.argv
    parser = get_parser()
    args = vars(parser.parse_args())
    args['src'] = args['src'][0]
    args['dst'] = args['dst'][0]
    logging.debug('new session %s', str(datetime.now()))
    args = expand_args(args)
    exit(replicate(args))


if __name__ == "__main__":
    sys.exit(main())
