---
bib:
  abstract: We present a language-independent verification framework that can be instantiated
    with an operational semantics to automatically generate a program verifier. The
    framework treats both the operational semantics and the program correctness specifications
    as reachability rules between matching logic patterns, and uses the sound and
    relatively complete reachability logic proof system to prove the specifications
    using the semantics. We instantiate the framework with the semantics of one academic
    language, KernelC, as well as with three recent semantics of real-world languages,
    C, Java, and JavaScript, developed independently. We evaluate our approach empirically
    and show that the generated program verifiers can check automatically the full
    functional correctness of challenging heap-manipulating programs implementing
    operations on list and tree data structures, like AVL trees. This is the first
    approach that can turn the operational semantics of real-world languages into
    correct-by-construction automatic verifiers.
  author:
  - first: Andrei
    last: \c{S}tef\u{a}nescu
  - first: Daejun
    last: Park
  - first: Shijiao
    last: Yuwen
  - first: Yilong
    last: Li
  - first: Grigore
    last: Ro\c{s}u
  author_id: Andrei Stefanescu and Daejun Park and Shijiao Yuwen and Yilong Li and
    Grigore Rosu
  authors:
  - id: andrei-stefanescu
    text: Andrei Stefanescu
  - id: daejun-park
    text: Daejun Park
  - id: shijiao-yuwen
    text: Shijiao Yuwen
  - id: yilong-li
    text: Yilong Li
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of the 31th Conference on Object-Oriented Programming, Systems,
    Languages, and Applications (OOPSLA'16)
  booktitle_acronym: OOPSLA'16
  booktitle_url: http://2016.splashcon.org/track/splash-2016-oopsla
  category:
  - fsl
  - k
  - executable_semantics
  - logics
  - matching_logic
  - program_verification
  - programming_languages
  date: 2016-11-01
  doi: http://dx.doi.org/10.1145/2983990.2984027
  id: stefanescu-park-yuwen-li-rosu-2016-oopsla
  month: Nov
  pages: 74-91
  presentation: 2016-11-02-stefanescu-park-yuwen-li-rosu-OOPSLA
  project_name: Matching Logic
  project_url: http://matching-logic.org/
  publisher: ACM
  title: Semantics-Based Program Verifiers for All Languages
  type: inproceedings
  year: '2016'
layout: paper
title: Semantics-Based Program Verifiers for All Languages
---
