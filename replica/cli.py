#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Fabrice Laporte - tunecrux.com
# The MIT License http://www.opensource.org/licenses/mit-license.php

"""This module contains all functions to handle command arguments and the
program core workflow defined by replicate.cli.replicate().
Call replica.cli.main() to invoke the CLI."""

from __future__ import print_function 
import os, sys 
import argparse, fnmatch, logging
from datetime import datetime
from replica import cloner 

# Logging config
LOG_FILENAME = '/tmp/replica.log'
LOG_FORMAT = "%(lineno)d:%(levelname)s: "+"%(message)s" 
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,
                    format=LOG_FORMAT)

def replicate(args):
    '''Clone id3 and eventually paths'''

    print('Cloning id3 metadata...', end='')
    cloner.clone_id3(args['src'], args['dst'])
    print(' done')
    if args['filename'] or args['update']:
        print('Renaming files.........', end='')
        cloner.clone_path(args['src'], args['dst'], args['update'])
        if args['src_dir'] and not args['update']:
            try:
                cloner.clone_dirpath(args['src_dir'], args['dst_dir'])  
            except OSError as e:
                print(' failed')
                print(e)
                exit()
        print(' done')  


def get_mp3_paths(path):
    '''Return mp3 files located at path'''

    res = [path]
    if os.path.isdir(path):
        res = fnmatch.filter(os.listdir(path), '*.mp3')
        res = [os.path.join(path, x) for x in res]
    return res


def expand_args(args):
    '''Edit/add entries to args dictionary'''

    args['src'] = args['src'][0]
    args['dst'] = args['dst'][0]
    args['src_dir'] = args['src'] if os.path.isdir(args['src']) else None
    args['dst_dir'] = args['dst'] if os.path.isdir(args['dst']) else None
    args['src']  = get_mp3_paths(args['src'])
    args['dst'] = get_mp3_paths(args['dst'])
    return args

def check_args(args):
    '''Check arguments validity'''
    
    if len(args['src']) != len(args['dst']):
        print('Error: SRC and DEST must have same number of files')
        return 0
    return 1

def get_parser(prog=sys.argv[0]):
    '''Returns the command parser.'''

    parser = argparse.ArgumentParser(\
        description='Clone id3 metadata between mp3 files.',
        epilog='Report bugs to tunecrux@gmail.com',
        prog=os.path.basename(prog))

    parser.add_argument('src', metavar='SRC', nargs=1, 
        help='the id3 donor (file or directory).')
    parser.add_argument('dst', metavar='DEST', nargs=1, 
        help='the id3 recipient (file or directory).')
    parser.add_argument('-f', '--filename', action='store_true', 
        help="clone filenames.")    
    parser.add_argument('-u', '--update', action='store_true', 
        help="clone absolute paths. Warning: SRC files will be overwritten.")

    return parser


def main(argv=None) :
    '(see main.__doc__ below)'

    if argv is None:
        argv = sys.argv 

    parser = get_parser()
    args = vars(parser.parse_args())

    logging.debug('new session %s', str(datetime.now()))
    args = expand_args(args)

    if not check_args(args):
        exit()

    replicate(args)

main.__doc__ = 'Script main function.\n' + get_parser(__file__).format_help()


if __name__ == "__main__":
    sys.exit(main())