#!/usr/bin/env python3
import sys
import gzip

filename_gff = sys.argv[1]


def get_IDs(tmp_str):
    rv = {'name': 'NoName'}
    for tmp in tmp_str.split(';'):
        if tmp.startswith('ID='):
            rv['ID'] = tmp.split('=')[1]
        if tmp.startswith('Parent='):
            rv['Parent'] = tmp.split('=')[1]
        if tmp.startswith('transcript_id='):
            rv['tx_id'] = tmp.split('=')[1]
        if tmp.startswith('Name='):
            rv['name'] = tmp.split('=')[1]
    return rv


rna2gene = dict()
gene_names = dict()
tx_count = dict()

f_gff = open(filename_gff, 'r')
if filename_gff.endswith('.gz'):
    f_gff = gzip.open(filename_gff, 'rt')

for line in f_gff:
    if not line.startswith('#'):
        tokens = line.strip().split("\t")
        tmp_mol_type = tokens[2]
        tmp_attr = tokens[8]
        if tmp_mol_type == 'gene':
            tmp_IDs = get_IDs(tokens[8])
            gene_names[tmp_IDs['ID']] = tmp_IDs['name']
        elif tmp_mol_type == 'tRNA' or tmp_mol_type == 'rRNA':
            tmp_IDs = get_IDs(tokens[8])
            gene_names[tmp_IDs['ID']] = tmp_IDs['name']
        elif tmp_mol_type == 'mRNA' or tmp_mol_type == 'lnc_RNA':
            tmp_IDs = get_IDs(tokens[8])
            tmp_tx_id = tmp_IDs['ID']
            rna2gene[tmp_tx_id] = tmp_IDs['Parent']
            tx_count[tmp_tx_id] = {'exon': 1, 'CDS': 1}
f_gff.close()

f_gff = open(filename_gff, 'r')
for line in f_gff:
    is_error = 1

    if line.startswith('#'):
        continue

    tokens = line.strip().split("\t")
    tmp_mol_type = tokens[2]
    tmp_attr = tokens[8]

    if tmp_mol_type == 'gene':
        tmp_IDs = get_IDs(tokens[8])
        tmp_gene_id = tmp_IDs['ID']
        tmp_gene_name = gene_names[tmp_gene_id]

        tmp_attr = 'gene_id "%s"; ' % tmp_gene_id
        tmp_attr += 'gene_name "%s"; ' % tmp_gene_name
        is_error = 0

    elif tmp_mol_type == 'tRNA' or tmp_mol_type == 'rRNA':
        tmp_IDs = get_IDs(tokens[8])
        tmp_gene_id = tmp_IDs['ID']
        tmp_gene_name = gene_names[tmp_gene_id]

        tmp_attr = 'gene_id "%s"; ' % tmp_gene_id
        tmp_attr += 'gene_name "%s"; ' % tmp_gene_name
        is_error = 0

    elif tmp_mol_type == 'mRNA' or tmp_mol_type == 'lnc_RNA':
        tmp_IDs = get_IDs(tokens[8])
        tmp_tx_id = tmp_IDs['ID']
        tmp_gene_id = rna2gene[tmp_tx_id]
        tmp_gene_name = gene_names[tmp_gene_id]

        tmp_attr = 'gene_id "%s"; ' % tmp_gene_id
        tmp_attr += 'transcript_id "%s"; ' % tmp_tx_id
        tmp_attr += 'gene_name "%s"; ' % tmp_gene_name
        is_error = 0

    elif tmp_mol_type == 'exon' or tmp_mol_type == 'CDS':
        tmp_IDs = get_IDs(tokens[8])
        tmp_tx_id = tmp_IDs['Parent']

        if tmp_tx_id not in rna2gene:
            # for tRNA and rRNA
            if tmp_tx_id in gene_names:
                tmp_gene_id = tmp_tx_id
                tmp_gene_name = gene_names[tmp_gene_id]
                if tmp_tx_id not in tx_count:
                    tx_count[tmp_tx_id] = {'exon': 1, 'CDS': 1}
                tmp_count = tx_count[tmp_tx_id][tmp_mol_type]

                tmp_attr = 'gene_id "%s"; ' % tmp_gene_id
                tmp_attr += 'transcript_id "%s"; ' % tmp_tx_id
                tmp_attr += 'exon_number "%d"; ' % tmp_count
                tmp_attr += 'gene_name "%s"; ' % tmp_gene_name
                tx_count[tmp_tx_id][tmp_mol_type] += 1
                is_error = 0
            else:
                sys.stderr.write('Error in ID: %s\n' % (line.strip()))
                is_error = 1
        else:
            tmp_gene_id = rna2gene[tmp_tx_id]
            tmp_gene_name = gene_names[tmp_gene_id]
            tmp_count = tx_count[tmp_tx_id][tmp_mol_type]
            tmp_attr = 'gene_id "%s"; ' % tmp_gene_id
            tmp_attr += 'transcript_id "%s"; ' % tmp_tx_id
            tmp_attr += 'exon_number "%d"; ' % tmp_count
            tmp_attr += 'gene_name "%s";' % tmp_gene_name
            tx_count[tmp_tx_id][tmp_mol_type] += 1
            is_error = 0

    if is_error == 0:
        print("%s\t%s" % ('\t'.join(tokens[:8]), tmp_attr))
f_gff.close()
