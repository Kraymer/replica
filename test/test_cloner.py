#!/usr/bin/env python

import os
import unittest
import shutil
import tempfile
from replica import cloner, tagger

DEMO_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo.mp3"
)
BLANK_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo_blank.mp3"
)


class ClonerTest(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="replica_")
        self.demo_file = os.path.join(self.tmp_dir, "demo.mp3")
        self.blank_file = os.path.join(self.tmp_dir, "demo_blank.mp3")
        shutil.copyfile(DEMO_RSRC, self.demo_file)
        shutil.copyfile(BLANK_RSRC, self.blank_file)

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_clone_id3(self):
        cloner.clone_id3([self.demo_file], [self.blank_file])
        res = tagger.get_tags(self.blank_file)
        self.assertEqual(res["TIT2"].text[0], u"Llama Whippin' Intro")
