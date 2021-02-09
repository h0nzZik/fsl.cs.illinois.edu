---
abstract: Matching logic reachability is an emerging verification approach which uses
  a language-independent proof system to prove program properties based on the operational
  semantics. In this paper we apply this approach in the context of a low-level real-time
  language with interrupts, in which each instruction takes a specified time to execute.
  In particular, we verify that if the interrupts are scheduled with large enough
  intervals, the program execution terminates yielding the correct result. Surprisingly,
  it turns out that matching logic reachability can handle the low-level and real-time
  features of the language just by using their operational semantics, and that language
  specific reasoning is unnecessary.
authors: [Dwight Guth, Andrei Stefanescu, Grigore Rosu]
categories: [fsl, executable_semantics, matching_logic, program_verification, programming_languages]
date: 2013-06-01
id: guth-stefanescu-rosu-2013-lola
title: Low-Level Program Verification using Matching Logic Reachability
---
