#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Units tests"""

import os
import tempfile
import shutil
import unittest

from mutagen import id3
from replica import cloner, tagger, cli

TEMPDIR = tempfile.mkdtemp()


def copy_resources():
    shutil.rmtree(TEMPDIR)
    shutil.copytree(os.path.join(os.path.dirname(__file__), 'rsrc'),
                    os.path.join(TEMPDIR, 'rsrc'))


def setup_module():
    copy_resources()


def teardown_module():
    shutil.rmtree(TEMPDIR)


class TestOnDir(unittest.TestCase):

    def setUp(self):
        print TEMPDIR
        copy_resources()
        self.args_good = {'src': [os.path.join(TEMPDIR, 'rsrc/album_alpha')],
                          'dst': [os.path.join(TEMPDIR, 'rsrc/album_num')]}
        self.args_bad = {'src': [os.path.join(TEMPDIR, 'rsrc/album_alpha')],
                         'dst': [os.path.join(TEMPDIR, 'rsrc')]}

    def test_expand_args(self):
        args = cli.expand_args(self.args_good)
        assert (len(args['src']) == len(args['dst']) == 2)

    def test_check_args(self):
        args = cli.expand_args(self.args_good)
        assert cli.check_args(args) == 1

    def test_clone_path(self):
        args = cli.expand_args(self.args_good)
        cloner.clone_path(args['src'], args['dst'], 1)


class TestOnFile(unittest.TestCase):
    def setUp(self):
        copy_resources()
        self.f = os.path.join(TEMPDIR, 'rsrc/album_alpha/01-fileA.mp3')

    def test_set_tags_recover_original(self):
        tags = {'foo': 'bar'}  # incorrect tags
        tags_before = tagger.get_tags(self.f)

        tagger.set_tags(self.f, tags)
        tags_after = tagger.get_tags(self.f)

        assert tags_before == tags_after

    def test_set_tags(self):
        audio = id3.ID3()
        audio.add(id3.TPE1(encoding=3, text=u"foo"))
        tagger.set_tags(self.f, audio)
        assert tagger.get_tags(self.f)['TPE1'].text[0] == u"foo"


if __name__ == '__main__':
    unittest.main()
