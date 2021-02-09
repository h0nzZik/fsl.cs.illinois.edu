---
bib:
  abstract: 'This paper presents matching logic, a first-order logic (FOL) variant
    for specifying and reasoning about structure by means of patterns and pattern
    matching. Its sentences, the patterns, are constructed using variables, symbols,
    connectives and quantifiers, but no difference is made between function and predicate
    symbols. In models, a pattern evaluates into a power-set domain (the set of values
    that match it), in contrast to FOL where functions and predicates map into a regular
    domain. Matching logic uniformly generalizes several logical frameworks important
    for program analysis, such as: propositional logic, algebraic specification, FOL
    with equality, and separation logic. Patterns can specify separation requirements
    at any level in any program configuration, not only in the heaps or stores, without
    any special logical constructs for that: the very nature of pattern matching is
    that if two structures are matched as part of a pattern, then they can only be
    spatially separated. Like FOL, matching logic can also be translated into pure
    predicate logic, at the same time admitting its own sound and complete proof system.
    A practical aspect of matching logic is that FOL reasoning remains sound, so off-the-shelf
    provers and SMT solvers can be used for matching logic reasoning. Matching logic
    is particularly well-suited for reasoning about programs in programming languages
    that have a rewrite-based operational semantics.'
  authors: [Grigore Rosu]
  categories: [fsl, executable_semantics, logics, matching_logic, program_verification,
    programming_languages]
  date: 2015-07-01
  id: rosu-2015-rta
  title: Matching Logic --- Extended Abstract
layout: paper
---
