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
  authors: [Andrei Stefanescu, Daejun Park, Shijiao Yuwen, Yilong Li, Grigore Rosu]
  categories: [fsl, k, executable_semantics, logics, matching_logic, program_verification,
    programming_languages]
  date: 2016-11-01
  id: stefanescu-park-yuwen-li-rosu-2016-oopsla
  title: Semantics-Based Program Verifiers for All Languages
layout: paper
---
