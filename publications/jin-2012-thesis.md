---
bib:
  abstract: 'Software reliability has become more important than ever in recent years,
    as a wide spectrum of software solutions are being used on various platforms.
    To this end, runtime monitoring is one of the most promising and feasible solutions
    for enhancing software reliability. In particular, runtime monitoring of parametric
    properties (parametric monitoring) has been receiving growing attention for its
    suitability in object-oriented systems. Despite many parametric monitoring approaches
    that have been proposed recently, they are still not widely used in real applications,
    implying that parametric monitoring is not sufficiently practical yet. In this
    dissertation, three perspectives for better practicality of parametric monitoring
    are proposed: expressiveness, efficiency, and scalability. A number of techniques
    on all three perspectives are developed and integrated to the JavaMOP framework,
    which is a formalism-independent, extensible runtime monitoring framework for
    parametric properties. One limitation in expressing parametric properties is that
    the first event must alway initiate all parameters. This limitation is removed
    in the proposed work to improve expressiveness of parametric monitoring. Further,
    a new logical formalism, PTCaRet, is introduced for describing properties of the
    call stack. As for efficiency, the `enable set optimization'', the `indexing cache'',
    and the `monitor garbage collection'' are proposed for optimizing creation of
    monitors, access to monitors, and termination of monitors, respectively. In addition,
    several scalable parametric monitoring techniques are introduced. These techniques,
    for the first time, allow a large number of simultaneous parametric specifications
    to be monitored efficiently. The optimization techniques presented in this dissertation
    were implemented into the JavaMOP framework, yielding JavaMOP 3.0, the latest
    and most efficient version of JavaMOP. Thorough evaluations show that these techniques
    can improve runtime performance of JavaMOP by 3 times on average, and up to 63
    times in some cases; as for memory usage, by 3 times on average. While Tracematches
    and the previous version of JavaMOP crashed on several cases due to out of memory
    errors, the newer version of JavaMOP did not crash on any case during the evaluations.
    Considering that the previous version of JavaMOP was one of the most efficient
    parametric monitoring frameworks in terms of runtime performance, the results
    presented in the dissertation can be argued significant.'
  author:
  - first: Dongyun
    last: Jin
  author_id: Dongyun Jin
  author_ids:
  - dongyun-jin
  authors:
  - id: dongyun-jin
    text: Dongyun Jin
  category:
  - fsl
  - runtime_verification
  date: 2012-08-01
  doi: http://hdl.handle.net/2142/34333
  id: jin-2012-thesis
  month: August
  project_name: MOP
  project_url: http://fsl.cs.illinois.edu/mop
  school: University of Illinois at Urbana-Champaign
  title: Making Runtime Monitoring of Parametric Properties Practical
  type: phdthesis
  year: '2012'
layout: paper
title: Making Runtime Monitoring of Parametric Properties Practical
---
