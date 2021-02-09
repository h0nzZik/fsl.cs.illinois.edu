---
abstract: Coinduction is a major technique employed to prove behavioral properties
  of systems, such as behavioral equivalence. Its automation is highly desirable,
  despite the fact that most behavioral problems are $\Pi_2^0$-complete. Circular
  coinduction, which is at the core of the $\CIRC$ prover, automates coinduction by
  systematically deriving new goals and proving existing ones until, hopefully, all
  goals are proved. Motivated by practical examples, circular coinduction and $\CIRC$
  have been recently extended with several features, such as special contexts, generalization
  and simplification. Unfortunately, none of these extensions eliminates the need
  for case analysis and, consequently, there are still many natural behavioral properties
  that $\CIRC$ cannot prove automatically. This paper presents an extension of circular
  coinduction with case analysis constructs and reasoning, as well as its implementation
  in $\CIRC$. To uniformly prove the soundness of this extension, as well as of past
  and future extensions of circular coinduction and $\CIRC$, this paper also proposes
  a general correct-extension technique based on equational interpolants.
authors: [Eugen-Ioan Goriac, Dorel Lucanu, Grigore Rosu]
categories: [fsl, logics]
date: 2010-11-01
id: goriac-lucanu-rosu-2010-icfem
title: Automating Coinduction with Case Analysis
---
