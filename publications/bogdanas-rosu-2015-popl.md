---
bib:
  abstract: This paper presents K-Java, a complete executable formal semantics of
    Java 1.4. K-Java was extensively tested with a test suite developed alongside
    the project, following the Test Driven Development methodology. In order to maintain
    clarity while handling the great size of Java, the semantics was split into two
    separate definitions -- a static semantics and a dynamic semantics. The output
    of the static semantics is a preprocessed Java program, which is passed as input
    to the dynamic semantics for execution. The preprocessed program is a valid Java
    program, which uses a subset of the features of Java. The semantics is applied
    to model-check multi-threaded programs. Both the test suite and the static semantics
    are generic and ready to be used in other Java-related projects.
  authors: [Denis Bogdanas, Grigore Rosu]
  booktitle: Proceedings of the 42nd Symposium on Principles of Programming Languages
    (POPL'15)
  booktitle_acronym: POPL'15
  booktitle_url: http://popl.mpi-sws.org/2015/
  categories: [fsl, executable_semantics, logics, matching_logic, program_verification,
    programming_languages, semantics, k]
  date: 2015-01-01
  id: bogdanas-rosu-2015-popl
  pages: 445-456
  project_url: https://github.com/kframework/java-semantics
  publisher: ACM
  title: '{K-Java: A Complete Semantics of Java}'
layout: paper
title: '{K-Java: A Complete Semantics of Java}'
---
