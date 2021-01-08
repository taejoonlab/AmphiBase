#!/usr/bin/env python3
import sys
import urllib.request

url_request = 'https://amphibiaweb.org/cgi/amphib_ws_locality?where-isocc=%s&rel-isocc=like'

tmp_count = 1
f_iso = open('iso_country_code.txt', 'r')
for line in f_iso:
    tokens = line.strip().split("\t")
    tmp_country_name = tokens[0]
    tmp_code = tokens[1].lower()

    tmp_rv = urllib.request.urlopen(url_request % tmp_code).read().decode('utf-8')

    sys.stderr.write('%d - %s (%d)\n' % (tmp_count, tmp_country_name, len(tmp_rv)))
    f_out = open('amphibiaweb_locality/amphibiaweb_locality.%s.xml' % tmp_code, 'w')
    f_out.write('%s\n' % tmp_rv)
    f_out.close()
    tmp_count += 1
