---
layout: page
title: Google Storage Structure
permalink: /documents/GoogleStorageStructure
---

The collection of genomic data.
You can access the data from Google Cloud Storage (Bucket). 
https://console.cloud.google.com/storage/browser/tklab-amphibase/

# Caudata
<ul>
{% for block in site.data.Caudata.species %}
<li>{{ block.species_name }} <i>( {{block.order}} / {{block.family}})</i></li>
{% endfor %}
</ul>

# Gymnophiona
<ul>
{% for block in site.data.Gymnophiona.species %}
<li>{{ block.species_name }} <i>( {{block.order}} / {{block.family}})</i></li>
{% endfor %}
</ul>

# Anura
<ul>
{% for block in site.data.Anura.species %}
<li>{{ block.species_name }} <i>( {{block.order}} / {{block.family}})</i></li>
{% endfor %}
</ul>

[jekyll-organization]: https://github.com/jekyll
