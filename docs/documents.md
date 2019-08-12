---
layout: page
title: Documents
permalink: /documents/
---
<h2>{{ site.data.documents.docs_list_title }}</h2>
<ul>
   {% for item in site.data.documents.docs %}
      <li><a href="{{ item.url }}">{{ item.title }}</a></li>
   {% endfor %}
</ul>

* 
[jekyll-organization]: https://github.com/jekyll
