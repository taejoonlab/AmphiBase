#!/usr/bin/env python3
import sys

filename_gff3 = sys.argv[1]

filename_sc_names = '../../scaffold_names'
# Source: ftp://ftp.ncbi.nlm.nih.gov/genomes/Xenopus_laevis/
# Assembly	Genome Center name	RefSeq Accession.version ...
# Xenopus_laevis_v2	chr1L	NW_016694792.1	CM004466.1	GPS_013517260.1
# Xenopus_laevis_v2	chr1S	NW_016694793.1	CM004467.1	GPS_013517261.1
# Xenopus_laevis_v2	Scaffold115629	NW_016802822.1	KV575200.1	GPS_013625290.1
# Xenopus_laevis_v2	Scaffold115630	NW_016802823.1	KV575201.1	GPS_013625291.1
# Xenopus_laevis_v2	MT	NC_001573.1	M10217.1	na

sc2acc = dict()
f_sc_names = open(filename_sc_names, 'r')
for line in f_sc_names:
    if line.startswith('#'):
        continue
    tokens = line.strip().split("\t")
    sc2acc[tokens[1]] = tokens[2]
f_sc_names.close()

f_gff3 = open(filename_gff3, 'r')
for line in f_gff3:
    if line.startswith('#'):
        print(line.strip())
    else:
        tokens = line.strip().split("\t")
        tmp_acc = sc2acc[tokens[0]].replace('.', 'v')
        tokens[0] = 'chrUn_%s' % tmp_acc
        print('\t'.join(tokens))
f_gff3.close()
