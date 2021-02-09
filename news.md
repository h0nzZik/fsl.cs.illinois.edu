---
title: news
layout: default
---


{% for item in  site.data.news %} * **{{item.date}}:** {{item.markdown}}
{% endfor %}

