---
abstract: 'Two programs are fully equivalent if, for the same input, either they both
  diverge or they both terminate with the same result. Full equivalence is an adequate
  notion of equivalence for programs written in deterministic languages. It is useful
  in many contexts, such as capturing the correctness of program transformations within
  the same language, or capturing the correctness of compilers between two different
  languages. In this paper we introduce a language-independent proof system for full
  equivalence, which is parametric in the operational semantics of two languages and
  in a state-similarity relation. The proof system is sound: a proof tree establishes
  the full equivalence of the programs given to it as input. We illustrate it on two
  programs in two different languages (an imperative one and a functional one), that
  both compute the Collatz sequence. The Collatz sequence is an interesting case study
  since it is not known weather the sequence terminates or not; nevertheless, our
  proof system shows that the two programs are fully equivalent (even if we cannot
  establish termination or divergence of either one).'
authors: [Stefan Ciobaca, Dorel Lucanu, Vlad Rusu, Grigore Rosu]
categories: [fsl, executable_semantics, logics, matching_logic, k, program_verification,
  programming_languages]
date: 2016-05-01
id: ciobaca-lucanu-rusu-rosu-2016-faoc
title: A Language-Independent Proof System for Full Program Equivalence
---
