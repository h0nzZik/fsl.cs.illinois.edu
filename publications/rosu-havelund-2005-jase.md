---
bib:
  abstract: Techniques for efficiently evaluating future time Linear Temporal Logic
    (abbreviated LTL) formulae on finite execution traces are presented. While the
    standard models of LTL are infinite traces, finite traces appear naturally when
    testing and/or monitoring real applications that only run for limited time periods.
    A finite trace variant of LTL is formally defined, together with an immediate
    executable semantics which turns out to be quite inefficient if used directly,
    via rewriting, as a monitoring procedure. Then three algorithms are investigated.
    First, a simple synthesis algorithm for monitors based on dynamic programming
    is presented; despite the efficiency of the generated monitors, they unfortunately
    need to analyze the trace backwards, thus making them unusable in most practical
    situations. To circumvent this problem, two rewriting-based practical algorithms
    are further investigated, one using rewriting directly as a means for online monitoring,
    and the other using rewriting to generate automata-like monitors, called binary
    transition tree finite state machines (and abbreviated BTT-FSMs). Both rewriting
    algorithms are implemented in Maude, an executable specification language based
    on a very efficient implementation of term rewriting. The first rewriting algorithm
    essentially consists of a set of equations establishing an executable semantics
    of LTL, using a simple formula transforming approach. This algorithm is further
    improved to build automata on-the-fly via caching and reuse of rewrites (called
    memoization), resulting in a very efficient and small Maude program that can be
    used to monitor program executions. The second rewriting algorithm builds on the
    first one and synthesizes provably minimal BTT-FSMs from LTL formulae, which can
    then be used to analyze execution traces online without the need for a rewriting
    system. The presented work is part of an ambitious runtime verification and monitoring
    project at NASA Ames, called {\sc PathExplorer}, and demonstrates that rewriting
    can be a tractable and attractive means for experimenting and implementing logics
    for program monitoring.
  author:
  - first: Grigore
    last: Rosu
  - first: Klaus
    last: Havelund
  author_id: Grigore Rosu and Klaus Havelund
  authors:
  - id: grigore-rosu
    text: Grigore Rosu
  - id: klaus-havelund
    text: Klaus Havelund
  category:
  - fsl
  - logics
  - programming_languages
  - runtime_verification
  - javamop
  date: 2005-01-01
  doi: http://dx.doi.org/10.1007/s10515-005-6205-y
  id: rosu-havelund-2005-jase
  journal: Automated Software Engineering
  journal_acronym: J.ASE
  journal_url: http://link.springer.com/journal/10515
  number: '2'
  pages: 151-197
  project_name: MOP
  project_url: http://fsl.cs.illinois.edu/mop
  title: Rewriting-Based Techniques for Runtime Verification
  type: article
  volume: '12'
  year: '2005'
layout: paper
title: Rewriting-Based Techniques for Runtime Verification
---
