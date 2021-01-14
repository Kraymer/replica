#!/usr/bin/env python

import os
import unittest
import shutil
import tempfile
from replica import tagger

DEMO_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo.mp3"
)
BLANK_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo_blank.mp3"
)


class TaggerTest(unittest.TestCase):
    def setUp(self):
        tmp_dir = tempfile.mkdtemp(prefix="replica_")
        self.demo_file = os.path.join(tmp_dir, "demo.mp3")
        self.blank_file = os.path.join(tmp_dir, "demo_blank.mp3")
        shutil.copyfile(DEMO_RSRC, self.demo_file)
        shutil.copyfile(BLANK_RSRC, self.blank_file)

    def test_get_tags(self):
        res = tagger.get_tags(self.demo_file)
        self.assertEqual(res["TIT2"].text[0], u"Llama Whippin' Intro")
        res = tagger.get_tags(self.blank_file)
        self.assertTrue("TIT2" not in res)

    def test_set_tags(self):
        tagger.set_tags(self.blank_file, tagger.get_tags(self.demo_file))
        res = tagger.get_tags(self.blank_file)
        self.assertEqual(res["TIT2"].text[0], u"Llama Whippin' Intro")
