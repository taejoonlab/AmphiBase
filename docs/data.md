---
layout: page
title: Data
permalink: /data/
---

The collection of genomic data.
You can access the data from Google Cloud Storage (Bucket). 
https://console.cloud.google.com/storage/browser/tklab-amphibase/

# Caudata
<ul>
{% for block in site.data.Caudata.species %}
<li><i>{{ block.species_name }}</i> ( </i>{{block.order}} / {{block.family}}</i>)</li>
{% endfor %}
</ul>

# Gymnophiona
<ul>
{% for block in site.data.Gymnophiona.species %}
<li><i>{{ block.species_name }}</i> ( </i>{{block.order}} / {{block.family}}</i>)</li>
{% endfor %}
</ul>

# Anura
<ul>
{% for block in site.data.Anura.species %}
<li><i>{{ block.species_name }}</i> ( </i>{{block.order}} / {{block.family}}</i>)</li>
{% endfor %}
</ul>

[jekyll-organization]: https://github.com/jekyll
