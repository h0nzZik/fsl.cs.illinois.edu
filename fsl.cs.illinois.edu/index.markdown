---
layout: page
tag: k
---

Welcome to the **Formal Systems Laboratory (FSL)** of the [Department of Computer
Science] at the [University of Illinois at Urbana-Champaign] (UIUC). FSL was
founded in 2002 by [Grigore Rosu](/fsl//people/grigore-rosu/index.html), when he joined UIUC 
(from [NASA Ames](http://www.nasa.gov/centers/ames/home/index.html)). 
In the FSL, we design and develop:

-   foundational and theoretical models,
-   specification and programming languages, techniques and methodologies,
    as well as
-   software analysis prototypes and tools,

all aiming at increasing the quality of computing systems. 

[comment]: <> ( {% katexmm %} )
[comment]: <> ( Test math $\varphi_1$ $\mathbb{K}$ )
[comment]: <> ( {% endkatexmm %} )

# Current Research Areas

- [Programming Language Design and Semantics](/fsl//projects/pl/index.html)
- [Runtime Verification](/fsl//projects/rv/index.html)
- [Behavioral Specification](/fsl//projects/circ/index.html)

You want to work on these topics? See [Grigore Rosu](/fsl//people/grigore-rosu/index.html)'s list of [Open Problems and Challenges](/fsl//other-pages/open-problems.html).

# Recent Publications

{% assign papers = site.papers | sort: 'date' | reverse | slice: 0,10 %}
{% for paper in papers %} * **{{paper.date | date: "%Y-%m-%d"}}:** {{paper.title}}
{% endfor %}
* [All publications](/fsl//other-pages/news.html)



[Department of Computer Science]: https://cs.illinois.edu
[University of Illinois at Urbana-Champaign]: https://illinois.edu


