---
bib:
  abstract: Multithreaded code is notoriously hard to develop and test. A multithreaded
    test exercises the code under test with two or more threads. Each test execution
    follows some schedule/interleaving of the multiple threads, and different schedules
    can give different results. Developers often want to enforce a particular schedule
    for test execution, and to do so, they use time delays (sleep in Java). Unfortunately,
    this approach can produce false positives or negatives, and can result in unnecessarily
    long testing time. This paper presents IMUnit, a novel approach to specifying
    and executing schedules for multithreaded tests. A new language is introduced
    that allows explicitly specifying schedules as constraints on the events during
    test execution. A tool that automatically controls the code to execute the specified
    schedule is provided, as well as a tool that helps developers to migrate their
    legacy, sleep-based tests into event-based tests in IMUnit. The latter tool uses
    novel techniques for inferring events and schedules from the executions of sleep-based
    tests. Experience in migrating over 200 tests is described. The inference techniques
    have high precision and recall, of over 75%. IMUnit reduces testing time compared
    to sleep-based tests on average 3.41x.
  author:
  - first: Vilas
    last: Jagannath
  - first: Milos
    last: Gligoric
  - first: Dongyun
    last: Jin
  - first: Qingzhou
    last: Luo
  - first: Grigore
    last: Ro\c{s}u
  - first: Darko
    last: Marinov
  author_id: Vilas Jagannath and Milos Gligoric and Dongyun Jin and Qingzhou Luo and
    Grigore Rosu and Darko Marinov
  authors:
  - id: vilas-jagannath
    text: Vilas Jagannath
  - id: milos-gligoric
    text: Milos Gligoric
  - id: dongyun-jin
    text: Dongyun Jin
  - id: qingzhou-luo
    text: Qingzhou Luo
  - id: grigore-rosu
    text: Grigore Rosu
  - id: darko-marinov
    text: Darko Marinov
  booktitle: Proceedings of the 8th Symposium on the Foundations of Software Engineering
    (FSE'11)
  booktitle_acronym: FSE'11
  booktitle_url: http://2011.esec-fse.org/
  category:
  - fsl
  date: 2011-09-01
  doi: http://doi.acm.org/10.1145/2025113.2025145
  id: jagannath-gligoric-jin-luo-rosu-marinov-2011-fse
  month: September
  pages: 223-233
  publisher: ACM
  title: Improved Multithreaded Unit Testing
  type: inproceedings
  year: '2011'
layout: paper
title: Improved Multithreaded Unit Testing
---
