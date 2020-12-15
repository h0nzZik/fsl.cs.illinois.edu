---
layout: default
---

{{ content }}

{% assign sorted = site.papers | sort: 'date' | reverse %}
{% assign old_year = 1 %}
{% for paper in sorted %}
    {% if paper.tags contains page.tag %}
        {% assign curr_year = paper.date | date: "%Y" %}
        {% unless curr_year == old_year %}
            <h2> {{curr_year}} </h2>
            {% assign old_year = curr_year %}
        {% endunless %}
        <h3> {{paper.title}} </h3>
        <p>
        {{ paper.abstract }}
        </p>
    {% endif %}
{% endfor %}
