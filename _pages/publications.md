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
{% for post in site.preprints reversed %}
  {% include archive-single.html %}
{% endfor %}

Journal Publications
======
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

Peer-Reviewed Conference Publications
======
{% for post in site.conferencepubs reversed %}
  {% include archive-single.html %}
{% endfor %}
