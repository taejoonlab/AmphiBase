#!/usr/bin/env python3
import os
import sys
import gzip

self_name = os.path.basename(__file__)
usage_mesg = 'Usage: %s <fasta> <chromosome|scaffold>' % self_name

if len(sys.argv) != 3:
    sys.stderr.write('%s\n' % usage_mesg)
    sys.exit(1)

filename_fa = sys.argv[1]
seq_type = sys.argv[2]

if not os.access(filename_fa, os.R_OK):
    sys.stderr.write('%s\n' % usage_mesg)
    sys.exit(1)

if seq_type not in ['chromosome', 'scaffold']:
    sys.stderr.write('%s\n' % usage_mesg)
    sys.exit(1)

f_fa = open(filename_fa, 'r')
if filename_fa.endswith('.gz'):
    f_fa = gzip.open(filename_fa, 'rt')

for line in f_fa:
    if line.startswith('>'):
        tmp_h = line.strip().lstrip('>')

        if seq_type == 'chromosome':
            if tmp_h.startswith('chrUn'):
                is_print = 0
            else:
                is_print = 1
        elif seq_type == 'scaffold':
            if tmp_h.startswith('chrUn'):
                is_print = 1
            else:
                is_print = 0
        else:
            sys.stderr.write('Unknown seq_tyoe: %s\n' % seq_type)
            sys.exit(1)

        if is_print > 0:
            print(line.strip())
    elif is_print > 0:
        print(line.strip())
f_fa.close()
