---
permalink: /
title: "About me"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---
This is the webpage of Alexander S. Estes, an industrial postdoctoral fellow at University of Minnesota. My research interests include optimization, statistics, and data science, often with applications to air traffic management. 

Selected Publications and 
{% assign selectpublications = site.documents | where: 'ispublication', true | where: 'selected', true}
{% for post in selectpublications %}
  {% include archive-single-talk-cv.html %}
{% endfor %}

Please use the links at the top of the page for more about my research interests, my publications, and the talks that I have given.
