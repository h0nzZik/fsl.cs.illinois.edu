---
bib:
  abstract: With the explosion of software size, checking conformance of implementation
    to specification becomes an increasingly important but also hard problem. Current
    practice based on ad-hoc testing does not provide correctness guarantees, while
    highly confident traditional formal methods like model checking and theorem proving
    are still too expensive to become common practice. In this paper we present a
    paradigm for combining formal specification with implementation, called monitoring-oriented
    programming (MoP), providing a light-weighted formal method to check conformance
    of implementation to specification at runtime. System requirements are expressed
    using formal specifications given as annotations inserted at various user selected
    places in programs. Efficient monitoring code using the same target language as
    the implementation is then automatically generated during a pre-compilation stage.
    The generated code has the same effect as a logical checking of requirements and
    can be used in any context, in particular to trigger user defined actions, when
    requirements are violated. Our proposal is language- and logic- independent, and
    we argue that it smoothly integrates other interesting system development paradigms,
    such as design by contract and aspect oriented programming. A prototype has been
    implemented for Java, which currently supports requirements expressed using past
    time and future time linear temporal logics, as well as extended regular expressions.
  author:
  - first: Feng
    last: Chen
  - first: Grigore
    last: Ro\c{s}u
  author_id: Feng Chen and Grigore Rosu
  author_ids:
  - feng-chen
  - grigore-rosu
  authors:
  - id: feng-chen
    text: Feng Chen
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of 3rd International Workshop on Runtime Verification (RV'03)
  booktitle_acronym: RV'03
  booktitle_url: https://rtg.cis.upenn.edu/rv2003
  category:
  - fsl
  date: 2003-06-01
  doi: http://dx.doi.org/10.1016/S1571-0661(04)81045-4
  id: chen-rosu-2003-rv
  month: June
  pages: 108-127
  project_name: MOP
  project_url: http://fsl.cs.illinois.edu/mop
  publisher: Elsevier
  series: Electronic Notes in Theoretical Computer Science
  title: 'Towards Monitoring-Oriented Programming: A Paradigm Combining Specification
    and Implementation'
  type: inproceedings
  volume: 89(2)
  year: '2003'
layout: paper
title: 'Towards Monitoring-Oriented Programming: A Paradigm Combining Specification
  and Implementation'
---
