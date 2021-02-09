---
bib:
  abstract: 'Predictive trace analysis (PTA) is an effective ap- proach for detecting
    subtle bugs in concurrent programs. Existing PTA techniques, however, are typically
    based on adhoc algorithms tailored to low-level errors such as data races or atomicity
    violations, and are not applicable to high-level properties such as "a resource
    must be authenticated before use" and "a collection cannot be modified when being
    iterated over". In addition, most techniques assume as input a globally ordered
    trace of events, which is expensive to collect in practice as it requires synchronizing
    all threads. In this paper, we present GPredict: a new technique that realizes
    PTA for generic concurrency properties. Moreover, GPredict does not require a
    global trace but only the local traces of each thread, which incurs much less
    runtime overhead than existing techniques. Our key idea is to uniformly model
    violations of concurrency properties and the thread causality as constraints over
    events. With an existing SMT solver, GPredict is able to precisely predict property
    violations allowed by the causal model. Through our evaluation using both benchmarks
    and real world applications, we show that GPredict is effective in expressing
    and predicting generic property violations. Moreover, it reduces the runtime overhead
    of existing techniques by 54\% on DaCapo benchmarks on average.'
  author:
  - first: Jeff
    last: Huang
  - first: Qingzhou
    last: Luo
  - first: Grigore
    last: Rosu
  author_id: Jeff Huang and Qingzhou Luo and Grigore Rosu
  author_ids:
  - jeff-huang
  - qingzhou-luo
  - grigore-rosu
  authors:
  - id: jeff-huang
    text: Jeff Huang
  - id: qingzhou-luo
    text: Qingzhou Luo
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of the 37th International Conference on Software Engineering
    (ICSE'15)
  booktitle_acronym: ICSE'15
  booktitle_url: http://2015.icse-conferences.org/
  category:
  - fsl
  - runtime_verification
  - testing
  date: 2015-05-01
  doi: http://dx.doi.org/10.1109/ICSE.2015.96
  id: huang-luo-rosu-2015-icse
  month: May
  pages: 847-857
  presentation: 2015-05-22-huang-luo-rosu-ICSE
  project_name: jPredictor
  project_url: http://fsl.cs.illinois.edu/jPredictor
  publisher: ACM
  title: 'GPredict: Generic Predictive Concurrency Analysis'
  type: inproceedings
  year: '2015'
layout: paper
title: 'GPredict: Generic Predictive Concurrency Analysis'
---
