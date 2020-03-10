---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
This is the webpage of Alexander S. Estes, an industrial postdoctoral fellow at University of Minnesota. In the fall of 2020, I will be joining the Department of Industrial and Systems Engineering at the University of Minnesota. My research interests include optimization, statistics, and data science, often with applications to air traffic management. Please use the links at the top of the page for more about my research interests, my publications, and the talks that I have given.

My CV is available [here](http://asestes1.github.io/files/AlexanderEstesCV.pdf).
## Selected Publications and Preprints
{% assign selectpublications = site.documents | where: 'ispublication', true | where: 'selected', true %}
<ul>{% for post in selectpublications reversed %}
  {% include archive-single-unlinked.html %}
{% endfor %}</ul>

