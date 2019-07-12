#!/usr/bin/env python
"""
A script for computing aggregated statistics over multiple frame files for
a given channel.
Stefan Countryman
"""

import sys
import os
import runavg as r

# exit if no arguments
if len(sys.argv) == 1:
    print 'No arguments provided. Give me more to work with.'
    print 'Usage: ' + sys.argv[0] + ' channel [-m mean_val_file] path_list_file mean_val_file'
    exit(1)

# Grab the channel name and file list to be used (and mean value file path, if specified).
# If flag -c is specified, then return a list of valid channel names.
if sys.argv[1] == '-c':
    print 'Channel name may be one of the following:'
    for c in r.ch.keys():
        print '\t' + str(c)
    exit()
else:
    channel = sys.argv[1]

# Make sure the channel specified is one of the options for which this script
# is configured. If it is, declare the full channel name.
if r.run.has_key(channel):
    print '\n' + r.now() + ' Channel ' + channel + ' selected'
    channel_full_name = r.ch[channel]
else:
    raise ValueError('channel provided must be one of following: ' + str(r.ch.keys()))

# See if a mean value file for the specified channel has been provided
if sys.argv[2] == '-m':
    mean_val_file   = sys.argv[3]
    print 'Mean value file specified as ' + mean_val_file
    path_list_files = sys.argv[4:]
else:
    mean_val_file   = None
    path_list_files = sys.argv[2:]

# Iterate through each file list provided
l = len(path_list_files)
print '\n' + r.now() + ' BEGIN.' + '\n'
for i in range(0, l):
    path_list_file = path_list_files[i]

    # Create an outfile prefix that includes the channel name
    outfile_prefix  = path_list_file + '_' + channel_full_name.translate(None, ' :/') + '_out'
    print r.now() + ' Setting outfile prefix to ' + outfile_prefix

    # check for lock file; if it doesn't exist, create it. If it does, error.
    if os.path.exists(outfile_prefix + '.lock'):
        print ' Frame file list ' + path_list_file + ' is locked; skipping.\n'
    elif os.path.exists(outfile_prefix + '.done'):
        print ' Frame file list ' + path_list_file + ' is done; skipping.\n'
    else:
        os.mknod(outfile_prefix + '.lock')
        print ' Creating lockfile and starting on list. ' + path_list_file + '.\n'
        print '\n' + r.now() + ' STARTING LIST ' + str(i+1) + ' OF ' + str(l) + '\n'
        r.run[channel](path_list_files[i], outfile_prefix, mean_val_file)
        print '\n' + r.now() + ' FINISHED WITH LIST ' + str(i+1) + '.\n'
        os.remove(outfile_prefix + '.lock')
        os.mknod(outfile_prefix + '.done')
        i += 1

