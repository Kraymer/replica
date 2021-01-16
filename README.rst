.. image:: http://github.com/kraymer/replica/workflows/build/badge.svg
   :target: https://github.com/kraymer/replica/actions
.. image:: https://codecov.io/gh/Kraymer/replica/branch/master/graph/badge.svg?token=ZkNIt7Wobr
   :target: https://codecov.io/gh/Kraymer/replica
.. image:: http://img.shields.io/pypi/v/replica.svg
   :target: https://pypi.python.org/pypi/replica
.. image:: https://img.shields.io/badge/rss-subscribe-orange.svg
   :target: https://github.com/Kraymer/replica/releases.atom
.. image:: https://pepy.tech/badge/replica
   :target: https://pepy.tech/project/replica


.. pypi

Replica, the id3 tags cloner
====

Preamble
----

| 2010.
|
| The 128 kbps mp3 files you piled ud during last decade are aging. Maybe it's time to upgrade your library, 320 kbps is the new kid in town. 
| One thing stops you: the precious personal info you stored in your id3 tags and don't want to lose.

Replica can ease your mp3 library upgrading process by cloning id3 metadata from the original file to the enhanced copy.

Usage
-----

If you replicate full albums, please make sure that tracks filenames are
similarly ordered in both source and destination folders.

::

    $ replica -u Library/Sam_Cooke-Ain_t_that_good_news-128kbps-2003 Incoming/sam_cook-good-news-320kbps
    Cloning id3 metadata... Done
    Renaming files......... Done

In addition to id3 cloning, replica can handle files renaming too so
that *upgrading* mp3 files becomes a no-brainer.

Consider the ``-u`` option to remove the source files and replace them
by their upgraded version. By doing so, it instantly migrates id3
metatags to new files while keeping the information stored by your music
player (ratings, play counts, etc) valid as the tracks filepaths get
unmodified.

Disclaimer
----------

Replica modifies mp3 files with no provision provided to undo the
changes. I would highly recommend a backup of your mp3 prior to running
replica on them.

Install
-------

You can install replica by typing ``pip install replica``.

