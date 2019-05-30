---
layout: archive
title: ""
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

Preprints and Publications Under Review
======
<ul>{% for post in site.preprints reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

Journal Publications
======
<ul>{% for post in site.publications reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>

Peer-Reviewed Conference Publications
======
<ul>{% for post in site.conferencepubs reversed %}
  {% include archive-single-cv.html %}
{% endfor %}</ul>
