#!/usr/bin/env python
"""
A script for aggregating statistics generated for multiple batches of frame
files, giving statistiscs for the entire collection.
Stefan Countryman
"""

import sys
import os
import runavg as r

# exit if no arguments
if len(sys.argv) == 1:
    print 'Not enough arguments.'
    print 'Usage: ' + sys.argv[0] + ' channel aggregate_outfile_prefix infile_prefix1 ...'
    print 'Or, type ' + sys.argv[0] + ' -c'
    print 'For a list of valid channel names.'
    exit(1)

if sys.argv[1] == '-c':
    print 'Channel name may be one of the following:'
    for c in r.ch.keys():
        print '\t' + str(c)
    exit()
else:
    channel = sys.argv[1]

# Make sure channel specified is one of the options for which this script
# is configued. If it is, declare the full channel name.
if r.aggregate.has_key(channel):
    print '\n' + r.now() + ' Channel ' + channel + ' selected.'
else:
    raise ValueError('channel provided must be one of the following: ' + str(r.aggregate.keys()))

# Aggregate
aggregate_prefix = sys.argv[2]
infile_prefixes  = sys.argv[3:]
r.aggregate[channel](aggregate_prefix, infile_prefixes)
