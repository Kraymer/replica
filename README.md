# **Replica**, the id3 cloner.

*Imagine you have a song lacking inner beauty, eg with low bitrate or hissing/crackling noises, etc. In return, it shows off a perfect physic shaped by you to fullfill your wildest dreams (carefully crafted id3 tags).  
So you buys a copy that possesses a purest soul (crystal clear 320kbps) ... only to realize that it needs plastic surgery to make it look like the original.*
  
Replica can help you having it both ways by cloning id3 metadata from the original file to the copy.

    $ replica -u Library/Sam_Cooke-Ain_t_that_good_news-128kbps-2003 Incoming/sam_cook-good-news-320kbps
    Cloning id3 metadata... Done
    Renaming files......... Done


Depending on your music player, you may want to use the `-u` option which remove the source files and replace them by their upgraded version.  
This seemless substitution enables to keep third-party information (as ratings or play counts) untouched.

# Disclaimer

Replica modifies mp3 files with no provision provided to undo the changes. I would highly recommend a backup of your mp3 prior to running replica on them.

# Install

You can install replica by typing ``pip install replica``.  

# Authors

Replica is by [Fabrice Laporte](mailto:tunecrux@gmail.com) 