.. image:: http://img.shields.io/pypi/v/replica.svg
   :target: https://pypi.python.org/pypi/replica
.. image:: https://img.shields.io/badge/rss-subscribe-orange.svg
   :target: https://github.com/Kraymer/replica/releases.atom
.. image:: https://pepy.tech/badge/replica
   :target: https://pepy.tech/project/replica

.. pypi

Replica, *botox for your music library* 
----

Replica tackles the problem of decaying mp3 files : your 128 kbps mp3 library was at the top of its game 20 years ago 
but looks moribund compared to today standards.

Whether you want to upgrade your files to a better quality while preserving id3 metadata or make the big leap and transfer your library to Spotify ; 
Replica can do magic. 

Usage
-----

::

    usage: replica <command> [<args>]
    
    Commands:
       id3-clone          clone id3 tags from a set of files to another  
       spotify-playlist   create playlist from a local folder or m3u playlist

Cloning existing id3 tags to mp3 files encoded in higher quality  
^^^^

::

    usage: replica id3-clone [-h] [-f] [-u] [-p] SRC DEST    

    Clone id3 metadata between mp3 files.    

    positional arguments:
      SRC             the id3 donor (file or directory).
      DEST            the id3 recipient (file or directory).    

    optional arguments:
      -h, --help      show this help message and exit
      -f, --filename  clone filenames.
      -u, --update    clone absolute paths. Warning: SRC files will be
                      overwritten.
      -p, --partial   authorize partial album cloning by matching folder tracks
                      individually


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

Creating a spotify playlist mirroring existing mp3 files or playlist   
^^^^

::

    usage: replica spotify-playlist [-h] SRC PLAYLIST    

    Create spotify playlist.    

    positional arguments:
      SRC             m3u file or directory
      PLAYLIST        playlist to create  


                      
Disclaimer
----------

Replica modifies mp3 files with no provision provided to undo the
changes. I would highly recommend a backup of your mp3 prior to running
replica on them.

Install
-------

You can install replica by typing ``pip install replica``.

