---
bib:
  abstract: We present a novel program verification approach based on coinduction,
    which takes as input an operational semantics. No intermediates like axiomatic
    semantics or verification condition generators are needed. Specifications can
    be written using any state predicates. We implement our approach in Coq, giving
    a certifying language-independent verification framework. Our proof system is
    implemented as a single module imported unchanged into language-specific proofs.
    Automation is reached by instantiating a generic heuristic with language-specific
    tactics. Manual assistance is also smoothly allowed at points the automation cannot
    handle. We demonstrate the power and versatility of our approach by verifying
    algorithms as complicated as Schorr-Waite graph marking and instantiating our
    framework for object languages in several styles of semantics. Finally, we show
    that our coinductive approach subsumes reachability logic, a recent language-independent
    sound and (relatively) complete logic for program verification that has been instantiated
    with operational semantics of languages as complex as C, Java and JavaScript.
  authors: [Brandon Moore, Lucas Pena, Grigore Rosu]
  categories: [fsl, executable_semantics, logics, matching_logic, program_verification,
    programming_languages]
  date: 2018-04-01
  id: moore-pena-rosu-2018-esop
  title: Program Verification by Coinduction
layout: paper
---
