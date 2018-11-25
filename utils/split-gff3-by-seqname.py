#!/usr/bin/env python3
import os
import sys

filename_gff = sys.argv[1]

headers = []
gff_list = dict()
gff_list['scaffolds'] = []

f_gff = open(filename_gff, 'r')
for line in f_gff:
    if line.startswith('#'):
        headers.append(line.strip())
    tokens = line.strip().split("\t")
    seq_id = tokens[0]

    if seq_id.startswith('chr') or seq_id.startswith('MT'):
        if seq_id not in gff_list:
            gff_list[seq_id] = []
        gff_list[seq_id].append(line.strip())
    else:
        gff_list['scaffolds'].append(line.strip())
f_gff.close()

for tmp_t in gff_list.keys():
    filename_out = '%s.%s.gff3' % (filename_gff.replace('.gff', ''), tmp_t)
    filename_out = os.path.basename(filename_out)
    f_out = open(filename_out, 'w')
    f_out.write('%s\n' % ('\n'.join(headers)))
    for tmp_line in gff_list[tmp_t]:
        f_out.write('%s\n' % tmp_line)
    f_out.close()
