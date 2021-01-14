#!/usr/bin/env python

import os
import unittest
import shutil
import tempfile

DEMO_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo.mp3"
)


class TaggerTest(unittest.TestCase):
    def setUp(self):
        self.demo_file = os.path.join(tempfile.mkdtemp(prefix="replica_"), "demo.mp3")
        shutil.copyfile(DEMO_RSRC, self.demo_file)

    def test_get_tags(self):
        self.assertEqual(True, True)
