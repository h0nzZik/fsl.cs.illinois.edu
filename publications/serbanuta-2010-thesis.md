---
bib:
  abstract: 'A plethora of programming languages have been and continue to be developed
    to keep pace with hardware advancements and the ever more demanding requirements
    of software development. As these increasingly sophisticated languages need to
    be well understood by both programmers and implementors, precise specifications
    are increasingly required. Moreover, the safety and adequacy with respect to requirements
    of programs written in these languages needs to be tested, analyzed, and, if possible,
    proved. This dissertation proposes a rigorous approach to define programming languages
    based on rewriting, which allows to easily design and test language extensions,
    and to specify and analyze safety and adequacy of program executions. To this
    aim, this dissertation describes the K Framework, an executable semantic framework
    inspired from rewriting logic but specialized and optimized for programming languages.
    The K Framework consists of three components: (1) a language definitional technique;
    (2) a specialized notation; and (3) a resource-sharing concurrent rewriting semantics.
    The language definitional technique is a rewriting technique built upon the lessons
    learned from capturing and studying existing operational semantics frameworks
    within rewriting logic, and upon attempts to combine their strengths while avoiding
    their limitations. The specialized notation makes the technical details of the
    technique transparent to the language designer, and enhances modularity, by allowing
    the designer to specify the minimal context needed for a semantic rule. Finally,
    the resource-sharing concurrent semantics relies on the particular form of the
    semantic rules to enhance concurrency, by allowing overlapping rule instances
    (e.g., two threads writing in different locations in the store, which overlap
    on the store entity) to apply concurrently as long as they only overlap on the
    parts they do not change. The main contributions of the dissertation are: (1)
    a uniform recasting of the major existing operational semantics techniques within
    rewriting logic; (2) an overview description of the K Framework and how it can
    be used to define, extend and analyze programming languages; (3) a semantics for
    K concurrent rewriting obtained through an embedding in graph rewriting; and (4)
    a description of the K-Maude tool, a tool for defining programming languages using
    the K technique on top of the Maude rewriting language.'
  author:
  - first: Traian
    last: \c{S}erb\u{a}nu\c{t}\u{a}
    middle: Florin
  author_id: Traian Florin Serbanuta
  author_ids:
  - traian-florin-serbanuta
  authors:
  - id: traian-florin-serbanuta
    text: Traian Florin Serbanuta
  category:
  - fsl
  - programming_languages
  date: 2010-12-01
  doi: https://www.ideals.illinois.edu/handle/2142/18252
  id: serbanuta-2010-thesis
  month: December
  presentation: serbanuta-2010-thesis-slides
  project_name: K
  project_url: http://www.kframework.org
  school: University of Illinois at Urbana-Champaign
  title: A Rewriting Approach to Concurrent Programming Language Design and Semantics
  type: phdthesis
  year: '2010'
layout: paper
title: A Rewriting Approach to Concurrent Programming Language Design and Semantics
---
