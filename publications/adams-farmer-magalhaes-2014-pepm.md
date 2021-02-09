---
bib:
  abstract: The most widely used generic-programming system in the Haskell community,
    Scrap Your Boilerplate (SYB), also happens to be one of the slowest. Generic traversals
    in SYB are often an order of magnitude slower than equivalent handwritten, non-generic
    traversals. Thus while SYB allows the concise expression of many traversals, its
    use incurs a significant runtime cost. Existing techniques for optimizing other
    generic-programming systems are not able to eliminate this overhead. This paper
    presents an optimization that completely eliminates this cost. Essentially, it
    is a partial evaluation that takes advantage of domain-specific knowledge about
    the structure of SYB. It optimizes SYB-style traversals to be as fast as handwritten,
    non-generic code, and benchmarks show that this optimization improves the speed
    of SYB-style code by an order of magnitude or more.
  address: New York, NY, USA
  author:
  - first: Michael
    last: Adams
    middle: D.
  - first: Andrew
    last: Farmer
  - first: Jos{\'e}
    last: Magalh{\~a}es
    middle: Pedro
  author_id: Michael D. Adams and Andrew Farmer and Jose Pedro Magalhaes
  author_ids:
  - michael-d.-adams
  - andrew-farmer
  - jose-pedro-magalhaes
  authors:
  - id: michael-d.-adams
    text: Michael D. Adams
  - id: andrew-farmer
    text: Andrew Farmer
  - id: jose-pedro-magalhaes
    text: Jose Pedro Magalhaes
  booktitle: Proceedings of the ACM SIGPLAN 2014 Workshop on Partial Evaluation and
    Program Manipulation
  booktitle_acronym: PEPM'14
  booktitle_url: http://www.program-transformation.org/PEPM14
  category:
  - fsl
  date: 2014-01-01
  doi: http://dx.doi.org/10.1145/2543728.2543730
  id: adams-farmer-magalhaes-2014-pepm
  isbn: 978-1-4503-2619-3
  month: January
  pages: 71-82
  presentation: 2014-01-20-adams-farmer-magalhaes-pepm
  project_name: Optimizing SYB
  project_url: https://github.com/xich/hermit-syb
  publisher: ACM
  title: Optimizing SYB is Easy!
  type: inproceedings
  year: '2014'
layout: paper
title: Optimizing SYB is Easy!
---
