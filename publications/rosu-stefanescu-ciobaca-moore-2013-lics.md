---
bib:
  abstract: This paper introduces *reachability logic*, a language-independent proof
    system for program verification, which takes an operational semantics as axioms
    and derives *reachability rules*, which generalize Hoare triples. This system
    improves on previous work by allowing operational semantics given with *conditional*
    rewrite rules, which are known to support all major styles of operational semantics.
    In particular, Kahn's big-step and Plotkin's small-step semantic styles are newly
    supported. The reachability logic proof system is shown sound (i.e., partially
    correct) and (relatively) complete. Reachability logic thus eliminates the need
    to independently define an axiomatic and an operational semantics for each language,
    and the non-negligible effort to prove the former sound and complete w.r.t. the
    latter. The soundness result has also been formalized in Coq, allowing reachability
    logic derivations to serve as formal proof certificates that rely only on the
    operational semantics.
  authors: [Grigore Rosu, Andrei Stefanescu, Stefan Ciobaca, Brandon Moore]
  booktitle: Proceedings of the 28th Symposium on Logic in Computer Science (LICS'13)
  booktitle_acronym: LICS'13
  booktitle_url: http://lii.rwth-aachen.de/lics/lics13/
  categories: [fsl, executable_semantics, k, logics, matching_logic, program_verification,
    programming_languages]
  date: 2013-06-01
  id: rosu-stefanescu-ciobaca-moore-2013-lics
  pages: 358-367
  project_url: http://fsl.cs.uiuc.edu/RL
  publisher: IEEE
  title: One-Path Reachability Logic
layout: paper
title: One-Path Reachability Logic
---
