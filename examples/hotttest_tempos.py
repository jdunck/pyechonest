#!/usr/bin/env python
# encoding: utf-8
"""
hotttest_tempos.py

Created by Brian Whitman on 2009-06-28.
Copyright (c) 2009 The Echo Nest Corporation. All rights reserved.
"""

import sys
import os
from pyechonest import track, artist, config, util

"""
Show the tempos of the tracks by the hotttest artists. 
"""

# How to set your ECHO_NEST_API_KEY:
#   1) Set the environment variable 'ECHO_NEST_API_KEY' to be your key, or
#   2) Uncomment the next line and add your key between the quotes
#config.ECHO_NEST_API_KEY="YOUR API KEY HERE" 

def main():	
    # For each hottt artist...
    for a in artist.get_top_hottt_artists():
        print a.name
        # Get the latest 15 mp3 files EN's crawlers have found
        for audio in a.audio():
            try:
                # Analyze the URL of the file 
                t = track.upload(audio["url"])
                # And print the BPM
                print audio["title"] + " -- " + str(t.tempo["value"])  + " bpm"  # show the tempo
            # You'll see a lot of API Error 5s because mp3 URLs are very transient. Just catch them and move on.
            except util.EchoNestAPIError:
                print "Problem analyzing " + audio["url"]
                pass

if __name__ == '__main__':
	main()

