---
bib:
  abstract: We present a program verification framework based on coinduction, which
    makes it feasible to verify programs directly against an operational semantics,
    without requiring intermediates like axiomatic semantics or verification condition
    generators. Specifications can be written and proved using any predicates on the
    state space of the operational semantics. We implement our approach in Coq, giving
    a certifying language-independent verification framework. The core proof system
    is implemented as a single module imported unchanged into proofs of programs in
    any semantics. A comfortable level of automation is provided by instantiating
    a simple heuristic with tactics for language-specific tasks such as finding the
    successor of a symbolic state, and for domain-specific reasoning about the predicates
    used in a particular specification. This approach also smoothly allows manual
    assistance at points the automation cannot handle. We demonstrate the power of
    our approach by verifying algorithms as complicated as Schorr-Waite graph marking,
    and the versatility by instantiating it for object languages in several styles
    of semantics. Despite the greater flexibility and generality of our approach,
    proof size and proof/certificate-checking time compare favorably with Bedrock,
    another Coq-based certifying program verification framework.
  authors: [Brandon Moore, Grigore Rosu]
  categories: [fsl, executable_semantics, logics, matching_logic, program_verification,
    programming_languages]
  date: 2015-02-01
  id: moore-rosu-2015-tr
  number: http://hdl.handle.net/2142/73177
  project_url: http://matching-logic.org/
  title: Program Verification by Coinduction
layout: paper
title: Program Verification by Coinduction
---
