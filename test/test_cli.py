#!/usr/bin/env python

import os
import unittest
import shutil
import tempfile

from click.testing import CliRunner

from replica import cli, tagger

DEMO_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo.mp3"
)
BLANK_RSRC = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), "rsrc", "demo_blank.mp3"
)


def create_singles(tmp_dir):
    demo_file = os.path.join(tmp_dir, "demo.mp3")
    blank_file = os.path.join(tmp_dir, "demo_blank.mp3")
    shutil.copyfile(DEMO_RSRC, demo_file)
    shutil.copyfile(BLANK_RSRC, blank_file)
    return demo_file, blank_file


def create_albums(tmp_dir):
    src_album_dir = os.path.join(tmp_dir, "src_album")
    dst_album_dir = os.path.join(tmp_dir, "dst_album")
    os.mkdir(src_album_dir)
    os.mkdir(dst_album_dir)
    for x in range(8):
        shutil.copyfile(DEMO_RSRC, os.path.join(src_album_dir, "{}.mp3".format(x)))
        if x % 2 == 0:
            shutil.copyfile(
                BLANK_RSRC, os.path.join(dst_album_dir, "0{}.mp3".format(x))
            )
    return src_album_dir, dst_album_dir


class CliTest(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp(prefix="replica_")
        self.demo_file, self.blank_file = create_singles(self.tmp_dir)
        self.src_album_dir, self.dst_album_dir = create_albums(self.tmp_dir)

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_expand_args(self):
        def extract_track_num(filepath):
            return int(filepath.split(os.path.sep)[-1].split(".")[0])

        src, dst = cli.expand_args(self.src_album_dir, self.dst_album_dir)
        self.assertTrue(len(src) == len(dst) * 2)
        src, dst = cli.expand_args(self.src_album_dir, self.dst_album_dir, partial=True)
        self.assertEqual(
            [extract_track_num(x) for x in src], [extract_track_num(x) for x in dst]
        )

    def test_replica_cli(self):
        runner = CliRunner()
        result = runner.invoke(cli.replica_cli, [self.demo_file, self.blank_file])
        self.assertEqual(result.exit_code, 0)
        res = tagger.get_tags(self.blank_file)
        self.assertEqual(res["TIT2"].text[0], u"Llama Whippin' Intro")
