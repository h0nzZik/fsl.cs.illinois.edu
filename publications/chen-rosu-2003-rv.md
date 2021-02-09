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
  authors: [Feng Chen, Grigore Rosu]
  categories: [fsl]
  date: 2003-06-01
  id: chen-rosu-2003-rv
  title: 'Towards Monitoring-Oriented Programming: A Paradigm Combining Specification
    and Implementation'
layout: paper
---
