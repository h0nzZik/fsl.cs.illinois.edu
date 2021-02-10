---
bib:
  abstract: To report a compiler bug, one must often find a small test case that triggers
    the bug. The existing approach to automated test-case reduction, delta debugging,
    works by removing substrings of the original input; the result is a concatenation
    of substrings that delta cannot remove. We have found this approach less than
    ideal for reducing C programs because it typically yields test cases that are
    too large or even invalid (relying on undefined behavior). To obtain small and
    valid test cases consistently, we designed and implemented three new, domain-specific
    test-case reducers. The best of these is based on a novel framework in which a
    generic fixpoint computation invokes modular transformations that perform reduction
    operations. This reducer produces outputs that are, on average, more than 25 times
    smaller than those produced by our other reducers or by the existing reducer that
    is most commonly used by compiler developers. We conclude that effective program
    reduction requires more than straightforward delta debugging.
  author:
  - first: John
    last: Regehr
  - first: Yang
    last: Chen
  - first: Pascal
    last: Cuoq
  - first: Eric
    last: Eide
  - first: Chucky
    last: Ellison
  - first: Xuejun
    last: Yang
  author_id: John Regehr and Yang Chen and Pascal Cuoq and Eric Eide and Chucky Ellison
    and Xuejun Yang
  author_ids:
  - john-regehr
  - yang-chen
  - pascal-cuoq
  - eric-eide
  - chucky-ellison
  - xuejun-yang
  authors:
  - id: john-regehr
    text: John Regehr
  - id: yang-chen
    text: Yang Chen
  - id: pascal-cuoq
    text: Pascal Cuoq
  - id: eric-eide
    text: Eric Eide
  - id: chucky-ellison
    text: Chucky Ellison
  - id: xuejun-yang
    text: Xuejun Yang
  booktitle: Proceedings of the 33rd ACM SIGPLAN conference on Programming Language
    Design and Implementation (PLDI'12)
  booktitle_acronym: PLDI'12
  booktitle_url: http://pldi12.cs.purdue.edu
  category:
  - fsl
  date: 2012-06-01
  doi: http://doi.acm.org/10.1145/2345156.2254104
  id: regehr-chen-cuoq-eide-ellison-yang-pldi-2012
  month: June
  pages: 335-346
  presentation: regehr-chen-cuoq-eide-ellison-yang-pldi-2012-slides
  project_name: C-Reduce
  project_url: http://embed.cs.utah.edu/creduce
  publisher: ACM
  title: Test-Case Reduction for C Compiler Bugs
  type: inproceedings
  year: '2012'
bib_url: publications/regehr-chen-cuoq-eide-ellison-yang-pldi-2012.bib
layout: paper
pdf_url: publications/regehr-chen-cuoq-eide-ellison-yang-pldi-2012.pdf
title: Test-Case Reduction for C Compiler Bugs
---
