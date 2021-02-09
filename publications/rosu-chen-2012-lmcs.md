---
abstract: Analysis of execution traces plays a fundamental role in many program analysis
  approaches, such as runtime verification, testing, monitoring, and specification
  mining. Execution traces are frequently parametric, i.e., they contain events with
  parameter bindings. Each parametric trace usually consists of many meaningful trace
  slices merged together, each slice corresponding to one parameter binding. This
  gives a semantics-based solution to parametric trace analysis. A general-purpose
  parametric trace slicing technique is introduced, which takes each event in the
  parametric trace and dispatches it to its corresponding trace slices. This parametric
  trace slicing technique can be used in combination with any conventional, non-parametric
  trace analysis technique, by applying the later on each trace slice. As an instance,
  a parametric property monitoring technique is then presented. The presented parametric
  trace slicing and monitoring techniques have been implemented and extensively evaluated.
  Measurements of runtime overhead confirm that the generality of the discussed techniques
  does not come at a performance expense when compared with existing parametric trace
  monitoring systems.
authors: [Grigore Rosu, Feng Chen]
categories: [fsl, javamop, logics, runtime_verification]
date: 2012-02-01
id: rosu-chen-2012-lmcs
title: Semantics and Algorithms for Parametric Monitoring
---
