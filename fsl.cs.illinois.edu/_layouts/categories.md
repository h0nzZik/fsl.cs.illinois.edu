---
layout: default
---

{{ content }}

{% for paper in site.papers %}
{% if paper.tags contains page.tag %}
<h3>{{paper.title}} </h3>
<p>
{{ paper.abstract }}
</p>
{% endif %}
{% endfor %}
