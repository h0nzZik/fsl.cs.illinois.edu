---
bib:
  abstract: 'Hoare logics rely on the fact that logic formulae can encode, or specify,
    program states, including environments, stacks, heaps, path conditions, data constraints,
    and so on. Such formula encodings tend to lose the structure of the original program
    state and thus to be complex in practice, making it difficult to relate formal
    systems and program correctness proofs to the original programming language and
    program, respectively. Worse, since programs often manipulate mathematical objects
    such as lists, trees, graphs, etc., one needs to also encode, as logical formulae,
    the process of identifying these objects in the encoded program state. This paper
    proposes atching logic, an alternative to Hoare logics in which the state structure
    plays a crucial role. Program states are represented as algebraic data-types called
    (concrete) configurations, and program state specifications are represented as
    configuration terms with variables and constraints on them, called (configuration)
    patterns. A pattern specifies those configurations that match it. Patterns can
    bind variables to their scope, allowing both for pattern abstraction and for expressing
    loop invariants. Matching logic is tightly connected to rewriting logic semantics
    (RLS): matching logic formal systems can systematically be obtained from executable
    RLS of languages. This relationship allows to prove soundness of matching logic
    formal systems w.r.t. complementary, testable semantics. All notions are exemplified
    using KernelC, a fragment of C with dynamic memory allocation/deallocation.'
  author:
  - first: Grigore
    last: Rosu
  - first: Wolfram
    last: Schulte
  author_id: Grigore Rosu and Wolfram Schulte
  author_ids:
  - grigore-rosu
  - wolfram-schulte
  authors:
  - id: grigore-rosu
    text: Grigore Rosu
  - id: wolfram-schulte
    text: Wolfram Schulte
  category:
  - fsl
  - executable_semantics
  - logics
  - matching_logic
  - program_verification
  - programming_languages
  - k
  - rewrite_logic
  date: 2009-01-01
  hidden: 'false'
  id: rosu-schulte-2009-tr
  institution: University of Illinois at Urbana-Champaign
  month: January
  number: http://hdl.handle.net/2142/10790
  project_name: Matching Logic
  project_url: http://matching-logic.org/
  title: Matching Logic --- Extended Report
  type: techreport
  year: '2009'
bib_url: publications/rosu-schulte-2009-tr.bib
layout: paper
pdf_url: publications/rosu-schulte-2009-tr.pdf
title: Matching Logic --- Extended Report
---
