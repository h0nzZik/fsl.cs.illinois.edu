---
bib:
  abstract: Parametric properties are behavioral properties over program events that
    depend on one or more parameters. Parameters are bound to concrete data or objects
    at runtime, which makes parametric properties particularly suitable for stating
    multi-object relationships or protocols. Monitoring parametric properties independently
    of the employed formalism involves slicing traces with respect to parameter instances
    and sending these slices to appropriate non-parametric monitor instances. The
    number of such instances is theoretically unbounded and tends to be enormous in
    practice, to an extent that how to efficiently manage monitor instances has become
    one of the most challenging problems in runtime verification. The previous formalism-independent
    approach was only able to do the obvious, namely to garbage collect monitor instances
    when all bound parameter objects were garbage collected. This led to pathological
    behaviors where unnecessary monitor instances were kept for the entire length
    of a program. This paper proposes a new approach to garbage collecting monitor
    instances. Unnecessary monitor instances are collected lazily to avoid creating
    undue overhead. This lazy collection, along with some careful engineering, has
    resulted in RV, the most efficient parametric monitoring system to date. Our evaluation
    shows that the average overhead of RV in the DaCapo benchmark is 15%, which is
    two times lower than that of JavaMOP and orders of magnitude lower than that of
    Tracematches.
  authors: [Dongyun Jin, Patrick O'Neil Meredith, Dennis Griffith, Grigore Rosu]
  booktitle: Proceedings of the 32nd ACM SIGPLAN conference on Programming Language
    Design and Implementation (PLDI'11)
  booktitle_acronym: PLDI'11
  booktitle_url: http://pldi11.cs.utah.edu
  categories: [fsl, runtime_verification]
  date: 2011-06-01
  id: jin-meredith-griffith-rosu-2011-pldi
  pages: 415-424
  project_url: http://fsl.cs.illinois.edu/mop
  publisher: ACM
  title: Garbage Collection for Monitoring Parametric Properties
layout: paper
title: Garbage Collection for Monitoring Parametric Properties
---
