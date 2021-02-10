---
bib:
  abstract: We present a negative semantics of the C11 language---a semantics that
    does not just give meaning to correct programs, but also rejects undefined programs.
    We investigate undefined behavior in C and discuss the techniques and special
    considerations needed for formally specifying it. We have used these techniques
    to modify and extend a semantics of C into one that captures undefined behavior.
    The amount of semantic infrastructure and effort required to achieve this was
    unexpectedly high, in the end nearly doubling the size of the original semantics.
    From our semantics, we have automatically extracted an undefinedness checker,
    which we evaluate against other popular analysis tools, using our own test suite
    in addition to a third-party test suite. Our checker is capable of detecting examples
    of all 77 categories of core language undefinedness appearing in the C11 standard,
    more than any other tool we considered. Based on this evaluation, we argue that
    our work is the most comprehensive and complete semantic treatment of undefined
    behavior in C, and thus of the C language itself.
  author:
  - first: Chris
    last: Hathhorn
  - first: Chucky
    last: Ellison
  - first: Grigore
    last: Ro\c{s}u
  author_id: Chris Hathhorn and Chucky Ellison and Grigore Rosu
  author_ids:
  - chris-hathhorn
  - chucky-ellison
  - grigore-rosu
  authors:
  - id: chris-hathhorn
    text: Chris Hathhorn
  - id: chucky-ellison
    text: Chucky Ellison
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of the 36th ACM SIGPLAN Conference on Programming Language
    Design and Implementation (PLDI'15)
  booktitle_acronym: PLDI'15
  booktitle_url: http://conf.researchr.org/home/pldi2015
  category:
  - fsl
  - executable_semantics
  - programming_languages
  - semantics
  - k
  date: 2015-06-01
  doi: http://dx.doi.org/10.1145/2813885.2737979
  id: hathhorn-ellison-rosu-2015-pldi
  month: June
  pages: 336-345
  presentation: 2015-06-16-hathhorn-ellison-rosu-PLDI
  project_name: C Semantics
  project_url: https://github.com/kframework/c-semantics
  publisher: ACM
  title: Defining the Undefinedness of C
  type: inproceedings
  year: '2015'
bib_url: publications/hathhorn-ellison-rosu-2015-pldi.bib
layout: paper
pdf_url: publications/hathhorn-ellison-rosu-2015-pldi.pdf
title: Defining the Undefinedness of C
---
