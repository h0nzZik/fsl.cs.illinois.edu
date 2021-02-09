---
abstract: Measurement unit safety policy checking is a topic in software analysis
  concerned with ensuring that programs do not violate basic principles of units of
  measurement. Such violations can hide significant domain-specific errors which are
  hard or impossible to find otherwise. Measurement unit analysis by means of automatic
  deduction is addressed in this paper. We draw general design principles for measurement
  unit certification tools and discuss our prototype for the C language, which includes
  both dynamic and static checkers. Our approach is based on assume/assert annotations
  of code, which are properly interpreted by our deduction-based tools and ignored
  by standard compilers. We do not modify the language in order to support units.
  The approach can be extended to incorporate other safety policies without great
  efforts.
authors: [Grigore Rosu, Feng Chen]
categories: [fsl]
date: 2003-10-01
id: rosu-chen-2003-ase
title: Certifying Measurement Unit Safety Policy
---
