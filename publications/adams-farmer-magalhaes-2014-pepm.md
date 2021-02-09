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
  authors: [Michael D. Adams, Andrew Farmer, Jose Pedro Magalhaes]
  categories: [fsl]
  date: 2014-01-01
  id: adams-farmer-magalhaes-2014-pepm
  title: Optimizing {SYB} is Easy!
layout: paper
---
