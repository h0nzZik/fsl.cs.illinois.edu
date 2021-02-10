---
bib:
  abstract: Multithreaded programs are hard to develop and test. In order for programs
    to avoid unexpected concurrent behaviors at runtime, for example data-races, synchronization
    mechanisms are typically used to enforce a safe subset of thread interleavings.
    Also, to test multithreaded programs, developers need to enforce the precise thread
    schedules that they want to test. These tasks are nontrivial and error prone.
    This paper presents EnforceMOP, a framework for specifying and enforcing complex
    properties in multithreaded Java programs. A property is enforced at runtime by
    blocking the threads whose next actions would violate it. This way the remaining
    threads, whose execution is safe, can make global progress until the system eventually
    reaches a global state in which the blocked threads can be safely unblocked and
    allowed to execute. Users of EnforceMOP can specify the properties to be enforced
    using the expressive MOP multi-formalism notation, and can provide code to be
    executed at deadlock (when no thread is safe to continue). EnforceMOP was used
    in two different kinds of applications. First, to enforce general properties in
    multithreaded programs, as a formal, semantic alternative to the existing rigid
    and sometimes expensive syntactic synchronization mechanisms. Second, to enforce
    testing desirable schedules in unit testing of multithreaded programs, as an alternative
    to the existing limited and often adhoc techniques. Results show that EnforceMOP
    is able to effectively express and enforce complex properties and schedules in
    both scenarios.
  author:
  - first: Qingzhou
    last: Luo
  - first: Grigore
    last: Rosu
  author_id: Qingzhou Luo and Grigore Rosu
  author_ids:
  - qingzhou-luo
  - grigore-rosu
  authors:
  - id: qingzhou-luo
    text: Qingzhou Luo
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of International Symposium in Software Testing and Analysis
    (ISSTA'13)
  booktitle_acronym: ISSTA'13
  booktitle_url: http://issta2013.inf.usi.ch/
  category:
  - fsl
  - runtime_verification
  - multithreading
  - testing
  - javamop
  date: 2013-07-01
  doi: http://dl.acm.org/citation.cfm?doid=2483760.2483766
  id: luo-rosu-2013-issta
  month: July
  pages: 156-166
  presentation: 2013-07-17-ISSTA
  project_name: EnforceMOP
  project_url: http://fsl.cs.illinois.edu/index.php/Runtime_Verification
  publisher: ACM
  title: 'EnforceMOP: A Runtime Property Enforcement System for Multithreaded Programs'
  type: inproceedings
  year: '2013'
bib_url: publications/luo-rosu-2013-issta.bib
layout: paper
pdf_url: publications/luo-rosu-2013-issta.pdf
title: 'EnforceMOP: A Runtime Property Enforcement System for Multithreaded Programs'
---
