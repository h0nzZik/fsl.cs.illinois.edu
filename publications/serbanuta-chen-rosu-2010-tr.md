---
abstract: 'This paper shows that it is possible to build a theoretically maximal and
  sound causal model for concurrent computations from a given execution trace. For
  an observed execution, the proposed model comprises all consistent executions which
  can be derived from it using only knowledge about the execution machine. The existence
  of such a model is of great theoretical value. First, by comprising all feasible
  executions, it can be used to prove soundness of other causal models: indeed, several
  models underlying existing techniques are shown to be embedded into the maximal
  model, so all these models are sound. Second, since it is maximal, the proposed
  model allows for natural and causal-model-independent definitions of trace-based
  properties; this paper proposes maximal definitions for causal dataraces and causal
  atomicity. Finally, although defined axiomatically, the set of traces comprised
  by the proposed model are shown to be effectively constructed from an initial observed
  trace. Thus, maximal causal models are not only theoretically relevant, but they
  are also amenable for developing practical analysis tools.'
authors: [Traian Florin Serbanuta, Feng Chen, Grigore Rosu]
categories: [fsl, runtime_verification]
date: 2010-09-01
id: serbanuta-chen-rosu-2010-tr
title: Maximal Causal Models for Sequentially Consistent Multithreaded Systems
---
