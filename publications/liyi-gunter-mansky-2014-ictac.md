---
bib:
  abstract: Communicating Sequential Processes (CSP) is a well-known formal language
    for describing concurrent systems, where transition semantics for it has been
    given by Brookes, Hoare and Roscoe. In this paper, we present trace refinement
    model analysis tools based on a generalized transition semantics of CSP, which
    we call HCSP, that merges the original transition system with ideas from Floyd-Hoare
    Logic and symbolic computation. This generalized semantics is shown to be sound
    and complete with respect to the original trace semantics. Traces in our system
    are symbolic representations of families of traces as given by the original semantics.
    This more compact representation allows us to expand the original CSP systems
    to effectively and efficiently model check some CSP programs that are difficult
    or impossible for other CSP systems to analyze. In particular, our system can
    handle certain classes of non-deterministic choices as a single transition, while
    the original semantics would treat each choice separately, possibly leading to
    large or unbounded case analyses. All work described in this paper has been carried
    out in the theorem prover Isabelle. This then provides us with a framework for
    automated and interactive analysis of CSP processes. It also gives us the ability
    to extract Ocaml code for an HCSP-based simulator directly from Isabelle. Based
    on the HCSP semantics and traditional trace refinement, we develop an idea of
    symbolic trace refinement and build a model checker based on it. The model checker
    was transcribed by hand into Maude as automatic extraction of Maude code is not
    yet supported by the Isabelle system.
  author:
  - first: Liyi
    last: Li
  - first: Elsa
    last: Gunter
  - first: William
    last: Mansky
  author_id: Liyi Li and Elsa Gunter and William Mansky
  authors:
  - id: liyi-li
    text: Liyi Li
  - id: elsa-gunter
    text: Elsa Gunter
  - id: william-mansky
    text: William Mansky
  booktitle: "Theoretical Aspects of Computing \u2013 ICTAC 2014"
  booktitle_acronym: ICTAC'14
  booktitle_url: http://fmi.unibuc.ro/ictac2014/
  category:
  - executable_semantics
  - logics
  - program_verification
  - programming_languages
  date: 2014-09-01
  doi: http://dx.doi.org/10.1007/978-3-319-10882-7
  id: liyi-gunter-mansky-2014-ictac
  month: Sep
  pages: 295-313
  presentation: 2014-09-18-ICTAC
  project_name: Holistic CSP
  project_url: http://www.cs.illinois.edu/~egunter/fms/HCSP/
  publisher: Springer International Publishing
  title: Symbolic Analysis Tools for CSP
  type: inproceedings
  year: '2014'
layout: paper
title: Symbolic Analysis Tools for CSP
---
