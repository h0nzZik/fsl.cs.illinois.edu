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
  authors: [Chris Hathhorn, Chucky Ellison, Grigore Rosu]
  booktitle: Proceedings of the 36th ACM SIGPLAN Conference on Programming Language
    Design and Implementation (PLDI'15)
  booktitle_acronym: PLDI'15
  booktitle_url: http://conf.researchr.org/home/pldi2015
  categories: [fsl, executable_semantics, programming_languages, semantics, k]
  date: 2015-06-01
  id: hathhorn-ellison-rosu-2015-pldi
  pages: 336-345
  project_url: https://github.com/kframework/c-semantics
  publisher: ACM
  title: Defining the Undefinedness of C
layout: paper
title: Defining the Undefinedness of C
---
