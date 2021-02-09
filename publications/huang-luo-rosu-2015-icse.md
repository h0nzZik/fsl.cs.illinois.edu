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
  authors: [Jeff Huang, Qingzhou Luo, Grigore Rosu]
  categories: [fsl, runtime_verification, testing]
  date: 2015-05-01
  id: huang-luo-rosu-2015-icse
  title: 'GPredict: Generic Predictive Concurrency Analysis'
layout: paper
---
