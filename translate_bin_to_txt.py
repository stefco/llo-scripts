# a script for translating the binary aggregated data into plaintext
import sys
import os
import numpy as np

aggregate_prefix   = sys.argv[1]

# load the files
agg_sum_x       = np.fromfile(aggregate_prefix + '.sum')
agg_sum_x_sq    = np.fromfile(aggregate_prefix + '.sumsq')
agg_max_x       = np.fromfile(aggregate_prefix + '.max')
agg_min_x       = np.fromfile(aggregate_prefix + '.min')
agg_num_x       = np.fromfile(aggregate_prefix + '.num', dtype=int)

# save them as text
agg_sum_x.tofile(aggregate_prefix + '.sum.txt', sep='\n')
agg_sum_x_sq.tofile(aggregate_prefix + '.sumsq.txt', sep='\n')
agg_max_x.tofile(aggregate_prefix + '.max.txt', sep='\n')
agg_min_x.tofile(aggregate_prefix + '.min.txt', sep='\n')
agg_num_x.tofile(aggregate_prefix + '.num.txt', sep='\n')
