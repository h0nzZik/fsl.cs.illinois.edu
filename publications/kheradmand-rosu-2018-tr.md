---
bib:
  abstract: Programmable packet processors and P4 as a programming language for such
    devices have gained significant interest, because their flexibility enables rapid
    development of a diverse set of applications that work at line rate. However,
    this flexibility, combined with the complexity of devices and networks, increases
    the chance of introducing subtle bugs that are hard to discover manually. Worse,
    this is a domain where bugs can have catastrophic consequences, yet formal analysis
    tools for P4 programs / networks are missing. We argue that formal analysis tools
    must be based on a formal semantics of the target language, rather than on its
    informal specification. To this end, we provide an executable formal semantics
    of the P4 language in the K framework. Based on this semantics, K provides an
    interpreter and various analysis tools including a symbolic model checker and
    a deductive program verifier for P4. This paper overviews our formal K semantics
    of P4, as well as several P4 language design issues that we found during our formalization
    process. We also discuss some applications resulting from the tools provided by
    K for P4 programmers and network administrators as well as language designers
    and compiler developers, such as detection of unportable code, state space exploration
    of P4 programs and of networks, bug finding using symbolic execution, data plane
    verification, program verification, and translation validation.
  author:
  - first: Ali
    last: Kheradmand
  - first: Grigore
    last: Ro\c{s}u
  author_id: Ali Kheradmand and Grigore Rosu
  authors:
  - id: ali-kheradmand
    text: Ali Kheradmand
  - id: grigore-rosu
    text: Grigore Rosu
  category:
  - k
  - semantics
  - executable_semantics
  - network_verification
  - translation_validation
  - automated_reasoning
  - program_verification
  - fsl
  date: 2018-04-01
  hidden: 'false'
  id: kheradmand-rosu-2018-tr
  institution: University of Illinois at Urbana-Champaign
  month: April
  number: https://arxiv.org/abs/1804.01468
  project_name: P4K
  project_url: https://github.com/kframework/p4-semantics/
  title: 'P4K: A Formal Semantics of P4 and Applications'
  type: techreport
  year: '2018'
layout: paper
title: 'P4K: A Formal Semantics of P4 and Applications'
---
