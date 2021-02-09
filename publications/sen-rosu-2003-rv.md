---
bib:
  abstract: Ordinary software engineers and programmers can easily understand regular
    patterns, as shown by the immense interest in and the success of scripting languages
    like Perl, based essentially on regular expression pattern matching. We believe
    that regular expressions provide an elegant and powerful specification language
    also for {\em monitoring requirements}, because an execution trace of a program
    is in fact a string of states. Extended regular expressions (EREs) add complementation
    to regular expressions, which brings additional benefits by allowing one to specify
    patterns that must {\em not} occur during an execution. Complementation gives
    one the power to express patterns on strings more compactly. In this paper we
    present a technique to generate {\em optimal monitors} from EREs. Our monitors
    are deterministic finite automata (DFA) and our novel contribution is to generate
    them using a modern coalgebraic technique called {\em coinduction}. Based on experiments
    with our implementation, which can be publicly tested and used over the web, we
    believe that our technique is more efficient than the simplistic method based
    on complementation of automata which can quickly lead to a highly-exponential
    state explosion.
  authors: [Koushik Sen, Grigore Rosu]
  categories: [fsl, executable_semantics, logics, automated_reasoning, rewrite_logic,
    runtime_verification, circular_coinduction]
  date: 2003-06-01
  id: sen-rosu-2003-rv
  title: Generating Optimal Monitors for Extended Regular Expressions
layout: paper
---
