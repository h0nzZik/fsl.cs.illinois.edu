---
bib:
  abstract: 'In this paper we present lower bounds and rewriting algorithms for testing
    membership of a word in a regular language described by an extended regular expression.
    Motivated by intuitions from monitoring and testing, where the words to be tested
    (execution traces) are typically much longer than the size of the regular expressions
    (patterns or requirements), and by the fact that in many applications the traces
    are only available incrementally, on an event by event basis, our algorithms are
    based on an event-consumption idea: a just arrived event is ``consumed'''' by
    the regular expression, i.e., the regular expression modifies itself into another
    expression discarding the event. We present an exponential space lower bound for
    monitoring extended regular expressions and argue that the presented rewriting-based
    algorithms, besides their simplicity and elegance, are practical and almost as
    good as one can hope. We experimented with and evaluated our algorithms in Maude.'
  authors: [Grigore Rosu, Mahesh Viswanathan]
  categories: [fsl, executable_semantics, logics, automated_reasoning, rewrite_logic,
    runtime_verification]
  date: 2003-06-01
  id: rosu-viswanathan-2003-rta
  title: Testing Extended Regular Language Membership Incrementally by Rewriting
layout: paper
---
