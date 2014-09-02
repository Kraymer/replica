Replica, the id3 cloner 
------------------------

When considering to make a new purchase of mp3 files to get them in better quality, 
losing the id3 metadata in the process may be an hindrance to the upgrade.   
Replica can help you having it both ways by cloning id3 metadata from the original 
file to the enhanced copy. 

Usage
-----

If you replicate full albums, please make sure that tracks filenames are similarly ordered in both source and destination folders.:: 

  $ replica -u Library/Sam_Cooke-Ain_t_that_good_news-128kbps-2003 Incoming/sam_cook-good-news-320kbps
  Cloning id3 metadata... Done
  Renaming files......... Done

In addition to id3 cloning, replica can handle files renaming too so that *upgrading* mp3 files becomes a no-brainer. 
 
Consider the ``-u`` option to remove the source files and replace them by their upgraded version. Preserving filepaths enables you to migrate id3 metatags to new files while keeping the information stored by your music player (such as ratings or play counts) valid.

Disclaimer
----------

Replica modifies mp3 files with no provision provided to undo the changes. I would highly recommend a backup of your mp3 prior to running replica on them.

Install
-------

You can install replica by typing ``pip install replica``.  

Authors
-------

Replica is by `Fabrice Laporte`_.

.. _Fabrice Laporte: mailto:tunecrux@gmail.com