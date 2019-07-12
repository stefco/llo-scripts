# add this stuff to a running average
import sys
import os
import numpy as np

# the first argument is the aggregate file prefix, the second, an outfile prefix
aggregate_prefix   = sys.argv[1]
infile_prefix 	   = sys.argv[2]

# set the bitrate for a 16k channel
kbps16 = 16384
sec_per_frame = 64

# load aggregate files (create if needed)
print 'Loading aggregate files with prefix ' + aggregate_prefix + '...'
if os.path.exists(aggregate_prefix + '.sum'):
    print 'Found ' + aggregate_prefix + '.sum, assuming other statistics exist.'
    agg_sum_x       = np.fromfile(aggregate_prefix + '.sum')
    agg_sum_x_sq    = np.fromfile(aggregate_prefix + '.sumsq')
    agg_max_x       = np.fromfile(aggregate_prefix + '.max')
    agg_min_x       = np.fromfile(aggregate_prefix + '.min')
    agg_num_x       = np.fromfile(aggregate_prefix + '.num', dtype=int)
else:
    print 'Did not find ' + aggregate_prefix + '.sum, assuming that no aggregate file exists.'
    agg_sum_x       = np.zeros(kbps16 * sec_per_frame)
    agg_sum_x_sq    = np.zeros(kbps16 * sec_per_frame)
    agg_max_x       = np.zeros(kbps16 * sec_per_frame)
    agg_min_x       = np.zeros(kbps16 * sec_per_frame)
    agg_num_x       = np.array([0])

# load contribution from infiles
print 'Loading stats from ' + infile_prefix + '.'
sum_x       = np.fromfile(infile_prefix + '.sum')
sum_x_sq    = np.fromfile(infile_prefix + '.sumsq')
max_x       = np.fromfile(infile_prefix + '.max')
min_x       = np.fromfile(infile_prefix + '.min')
num_x       = np.fromfile(infile_prefix + '.num', dtype=int)

# TODO assert that the number skipped + number processed equals length of list

# gen statistics
agg_sum_x       +=  sum_x
agg_sum_x_sq    +=  sum_x_sq
agg_max_x       =   np.maximum(agg_max_x, max_x)
agg_min_x       =   np.minimum(agg_min_x, min_x)
agg_num_x[0]    +=  num_x[0]
print 'Done adding ' + infile_prefix + ' to aggregate statistics'

# save text files
agg_sum_x.tofile(aggregate_prefix + '.sum')
agg_sum_x_sq.tofile(aggregate_prefix + '.sumsq')
agg_max_x.tofile(aggregate_prefix + '.max')
agg_min_x.tofile(aggregate_prefix + '.min')
agg_num_x.tofile(aggregate_prefix + '.num')
# agg_sum_x.tofile(aggregate_prefix + '.sum', sep=',')
# agg_sum_x_sq.tofile(aggregate_prefix + '.sumsq', sep=',')
# agg_max_x.tofile(aggregate_prefix + '.max', sep=',')
# agg_min_x.tofile(aggregate_prefix + '.min', sep=',')
# agg_num_x.tofile(aggregate_prefix + '.num', sep=',')

