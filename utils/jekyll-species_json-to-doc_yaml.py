#!/usr/bin/env python3
import os
import json

order_list = ['Gymnophiona', 'Caudata', 'Anura']

dirname_species = '../species/'
dirname_data = '../docs/_data/'

for tmp_order in order_list:
    filename_json = os.path.join(dirname_species, 
                                    'Order_%s.json' % tmp_order)

    f_json = open(filename_json, 'r')
    order_json = json.loads(f_json.read())
    f_json.close()

    f_out = open(os.path.join(dirname_data, '%s.yml' % tmp_order), 'w')
    f_out.write('species:\n')
    for tmp_family in sorted(order_json.keys()):
        for tmp_species in sorted(order_json[tmp_family].keys()):
            f_out.write('- species_name: %s\n' % tmp_species)
            f_out.write('  order: %s\n' % tmp_order)
            f_out.write('  family: %s\n' % tmp_family)
            f_out.write('  species_code: %s\n' % order_json[tmp_family][tmp_species])
    f_out.close()
