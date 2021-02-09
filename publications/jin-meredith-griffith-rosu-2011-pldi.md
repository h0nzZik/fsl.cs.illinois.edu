---
bib:
  abstract: Parametric properties are behavioral properties over program events that
    depend on one or more parameters. Parameters are bound to concrete data or objects
    at runtime, which makes parametric properties particularly suitable for stating
    multi-object relationships or protocols. Monitoring parametric properties independently
    of the employed formalism involves slicing traces with respect to parameter instances
    and sending these slices to appropriate non-parametric monitor instances. The
    number of such instances is theoretically unbounded and tends to be enormous in
    practice, to an extent that how to efficiently manage monitor instances has become
    one of the most challenging problems in runtime verification. The previous formalism-independent
    approach was only able to do the obvious, namely to garbage collect monitor instances
    when all bound parameter objects were garbage collected. This led to pathological
    behaviors where unnecessary monitor instances were kept for the entire length
    of a program. This paper proposes a new approach to garbage collecting monitor
    instances. Unnecessary monitor instances are collected lazily to avoid creating
    undue overhead. This lazy collection, along with some careful engineering, has
    resulted in RV, the most efficient parametric monitoring system to date. Our evaluation
    shows that the average overhead of RV in the DaCapo benchmark is 15%, which is
    two times lower than that of JavaMOP and orders of magnitude lower than that of
    Tracematches.
  author:
  - first: Dongyun
    last: Jin
  - first: Patrick
    last: Meredith
    middle: O'Neil
  - first: Dennis
    last: Griffith
  - first: Grigore
    last: Ro\c{s}u
  author_id: Dongyun Jin and Patrick O'Neil Meredith and Dennis Griffith and Grigore
    Rosu
  author_ids:
  - dongyun-jin
  - patrick-o'neil-meredith
  - dennis-griffith
  - grigore-rosu
  authors:
  - id: dongyun-jin
    text: Dongyun Jin
  - id: patrick-o'neil-meredith
    text: Patrick O'Neil Meredith
  - id: dennis-griffith
    text: Dennis Griffith
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of the 32nd ACM SIGPLAN conference on Programming Language
    Design and Implementation (PLDI'11)
  booktitle_acronym: PLDI'11
  booktitle_url: http://pldi11.cs.utah.edu
  category:
  - fsl
  - runtime_verification
  date: 2011-06-01
  doi: http://doi.acm.org/10.1145/1993316.1993547
  id: jin-meredith-griffith-rosu-2011-pldi
  month: June
  pages: 415-424
  presentation: jin-meredith-griffith-rosu-2011-pldi-slides
  project_name: MOP
  project_url: http://fsl.cs.illinois.edu/mop
  publisher: ACM
  title: Garbage Collection for Monitoring Parametric Properties
  type: inproceedings
  year: '2011'
layout: paper
title: Garbage Collection for Monitoring Parametric Properties
---
