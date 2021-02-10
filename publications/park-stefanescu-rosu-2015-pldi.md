---
bib:
  abstract: 'This paper presents KJS, the most complete and throughly tested formal
    semantics of JavaScript to date. Being executable, KJS has been tested against
    the ECMAScript 5.1 conformance test suite, and passes all 2,782 core language
    tests. Among the existing implementations of JavaScript, only Chrome V8''s passes
    all the tests, and no other semantics passes more than 90\%. In addition to a
    reference implementation for JavaScript, KJS also yields a simple coverage metric
    for a test suite: the set of semantic rules it exercises. Our semantics revealed
    that the ECMAScript 5.1 conformance test suite fails to cover several semantic
    rules. Guided by the semantics, we wrote tests to exercise those rules. The new
    tests revealed bugs both in production JavaScript engines (Chrome V8, Safari WebKit,
    Firefox SpiderMonkey) and in other semantics. KJS is symbolically executable,
    thus it can be used for formal analysis and verification of JavaScript programs.
    We verified non-trivial programs and found a known security vulnerability.'
  author:
  - first: Daejun
    last: Park
  - first: Andrei
    last: \c{S}tef\u{a}nescu
  - first: Grigore
    last: Ro\c{s}u
  author_id: Daejun Park and Andrei Stefanescu and Grigore Rosu
  author_ids:
  - daejun-park
  - andrei-stefanescu
  - grigore-rosu
  authors:
  - id: daejun-park
    text: Daejun Park
  - id: andrei-stefanescu
    text: Andrei Stefanescu
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
  doi: http://dx.doi.org/10.1145/2737924.2737991
  id: park-stefanescu-rosu-2015-pldi
  month: June
  pages: 346-356
  presentation: 2015-06-16-park-stefanescu-rosu-PLDI
  project_name: Semantics
  project_url: https://github.com/kframework/javascript-semantics
  publisher: ACM
  title: 'KJS: A Complete Formal Semantics of JavaScript'
  type: inproceedings
  year: '2015'
bib_url: publications/park-stefanescu-rosu-2015-pldi.bib
layout: paper
pdf_url: publications/park-stefanescu-rosu-2015-pldi.pdf
title: 'KJS: A Complete Formal Semantics of JavaScript'
---
