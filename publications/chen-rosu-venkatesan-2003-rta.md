---
bib:
  abstract: Dimensional safety policy checking is an old topic in software analysis
    concerned with ensuring that programs do not violate basic principles of units
    of measurement. Scientific and/or navigation software is routinely dimensional
    and violations of measurement unit safety policies can hide significant domain-specific
    errors which are hard or impossible to find otherwise. Dimensional analysis of
    programs written in conventional programming languages is addressed in this paper.
    We draw general design principles for dimensional analysis tools and then discuss
    our prototypes, implemented by rewriting, which include both dynamic and static
    checkers. Our approach is based on assume/assert annotations of code which are
    properly interpreted by our tools and ignored by standard programming language
    compilers/interpreters. The output of our prototypes consists of warnings that
    list those expressions violating the unit safety policy. These prototypes are
    implemented in the rewriting system Maude, using more than 2,000 rewriting rules.
    This paper presents a non-trivial application of rewriting techniques to software
    analysis.
  authors: [Feng Chen, Grigore Rosu, Ram prasad Venkatesan]
  booktitle: Proceedings of the 14th International Conference on Rewriting Techniques
    and Applications (RTA'03)
  booktitle_acronym: RTA'03
  booktitle_url: http://users.dsic.upv.es/~rdp03/rta/
  categories: [fsl]
  date: 2003-06-01
  id: chen-rosu-venkatesan-2003-rta
  pages: 197-207
  project_url: http://fsl.cs.illinois.edu/mop
  publisher: Lecture Notes in Computer Science (LNCS)
  title: Rule-Based Analysis of Dimensional Safety
layout: paper
title: Rule-Based Analysis of Dimensional Safety
---
