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
  authors: [Vilas Jagannath, Milos Gligoric, Dongyun Jin, Qingzhou Luo, Grigore Rosu,
    Darko Marinov]
  booktitle: Proceedings of the 8th Symposium on the Foundations of Software Engineering
    (FSE'11)
  booktitle_acronym: FSE'11
  booktitle_url: http://2011.esec-fse.org/
  categories: [fsl]
  date: 2011-09-01
  id: jagannath-gligoric-jin-luo-rosu-marinov-2011-fse
  pages: 223-233
  project_url: ''
  publisher: ACM
  title: Improved Multithreaded Unit Testing
layout: paper
title: Improved Multithreaded Unit Testing
---
