---
bib:
  abstract: Despite the numerous static and dynamic program analysis techniques in
    the literature, data races remain one of the most common bugs in modern concurrent
    software. Further, the techniques that do exist either have limited detection
    capability or are unsound, meaning that they report false positives. We present
    a sound race detection technique that achieves a provably higher detection capability
    than existing sound techniques. A key insight of our technique is the inclusion
    of abstracted control flow information into the execution model, which increases
    the space of the causal model permitted by classical happens-before or causally-precedes
    based detectors. By encoding the control flow and a minimal set of feasibility
    constraints as a group of first-order logic formulae, we formulate race detection
    as a constraint solving problem. Moreover, we formally prove that our formulation
    achieves the maximal possible detection capability for any sound dynamic race
    detector with respect to the same input trace under the sequential consistency
    memory model. We demonstrate via extensive experimentation that our technique
    detects more races than the other state-of-the-art sound race detection techniques,
    and that it is scalable to executions of real world concurrent applications with
    tens of millions of critical events. These experiments also revealed several previously
    unknown races in real systems (e.g., Eclipse) that have been confirmed or fixed
    by the developers. Our tool is also adopted by Eclipse developers.
  author:
  - first: Jeff
    last: Huang
  - first: Patrick
    last: Meredith
  - first: Grigore
    last: Rosu
  author_id: Jeff Huang and Patrick Meredith and Grigore Rosu
  author_ids:
  - jeff-huang
  - patrick-meredith
  - grigore-rosu
  authors:
  - id: jeff-huang
    text: Jeff Huang
  - id: patrick-meredith
    text: Patrick Meredith
  - id: grigore-rosu
    text: Grigore Rosu
  booktitle: Proceedings of the 35th annual ACM SIGPLAN conference on Programming
    Language Design and Implementation (PLDI'14)
  booktitle_acronym: PLDI'14
  booktitle_url: http://conferences.inf.ed.ac.uk/pldi2014/
  category:
  - fsl
  - runtime_verification
  - testing
  date: 2014-06-01
  doi: http://dx.doi.org/10.1145/2594291.2594315
  id: huang-meredith-rosu-2014-pldi
  month: June
  pages: 337-348
  presentation: 2014-06-10-PLDI
  project_name: jPredictor
  project_url: http://fsl.cs.illinois.edu/jPredictor
  publisher: ACM
  title: Maximal Sound Predictive Race Detection with Control Flow Abstraction
  type: inproceedings
  year: '2014'
bib_url: publications/huang-meredith-rosu-2014-pldi.bib
layout: paper
pdf_url: publications/huang-meredith-rosu-2014-pldi.pdf
title: Maximal Sound Predictive Race Detection with Control Flow Abstraction
---
