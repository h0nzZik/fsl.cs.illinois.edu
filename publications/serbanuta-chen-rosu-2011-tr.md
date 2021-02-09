---
abstract: 'This paper shows that it is possible to build a maximal and sound causal
  model for concurrent computations from a given execution trace. It is sound, in
  the sense that any program which can generate a trace can also generate all traces
  in its causal model. It is maximal (among sound models), in the sense that by extending
  the causal model of an observed trace with a new trace, the model becomes unsound:
  there exists a program generating the original trace which cannot generate the newly
  introduced trace. Thus, the maximal sound model has the property that it comprises
  all traces which all programs that can generate the original trace can also generate.
  The existence of such a model is of great theoretical value. First, it can be used
  to prove the soundness of non-maximal, and thus smaller, causal models. Second,
  since it is maximal, the proposed model allows for natural and causal-model-independent
  definitions of trace-based properties; this paper proposes maximal definitions for
  causal dataraces and causal atomicity. Finally, although defined axiomatically,
  the set of traces comprised by the proposed model are shown to be effectively constructed
  from the original trace. Thus, maximal causal models are also amenable for developing
  practical analysis tools.'
authors: [Traian Florin Serbanuta, Feng Chen, Grigore Rosu]
categories: [fsl, runtime_verification]
date: 2011-10-01
id: serbanuta-chen-rosu-2011-tr
title: Maximal Causal Models for Sequentially Consistent Systems
---
