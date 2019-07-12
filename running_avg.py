# add this stuff to a running average
import sys
import os
import numpy as np

outfile_prefix 	= sys.argv[1]

# set the bitrate for a 16k channel
kbps16 = 16384
sec_per_frame = 64

# load infile and outfiles (create if needed)
data = np.fromfile(outfile_prefix + '.dat', sep=',')
if os.path.exists(outfile_prefix + '.sum'):
    sum_x       = np.fromfile(outfile_prefix + '.sum')
    sum_x_sq    = np.fromfile(outfile_prefix + '.sumsq')
    max_x       = np.fromfile(outfile_prefix + '.max')
    min_x       = np.fromfile(outfile_prefix + '.min')
    num_x       = np.fromfile(outfile_prefix + '.num', dtype=int)
else:
    sum_x       = np.zeros(kbps16 * sec_per_frame)
    sum_x_sq    = np.zeros(kbps16 * sec_per_frame)
    max_x       = np.zeros(kbps16 * sec_per_frame)
    min_x       = np.zeros(kbps16 * sec_per_frame)
    num_x       = np.array([0])

# gen statistics
sum_x       +=  data
sum_x_sq    +=  np.square(data)
max_x       =   np.maximum(max_x, data)
min_x       =   np.minimum(min_x, data)
num_x[0]    +=  1

# save files
sum_x.tofile(outfile_prefix + '.sum')
sum_x_sq.tofile(outfile_prefix + '.sumsq')
max_x.tofile(outfile_prefix + '.max')
min_x.tofile(outfile_prefix + '.min')
num_x.tofile(outfile_prefix + '.num')

