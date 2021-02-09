---
bib:
  abstract: We propose natural proofs, for reasoning with programs that manipulate
    data-structures against complex specifications --- specifications that describe
    the structure of the heap, the data stored within it, and separation and framing
    of sub-structures. Natural proofs are a subclass of proofs that are amenable to
    completely automated reasoning, that provide sound but incomplete procedures,
    and that capture common reasoning tactics in program verification. We develop
    a dialect of separation logic over heaps, called Dryad, with recursive definitions
    that avoids explicit quantification. We develop ways to reason with heaplets using
    classical logic over the theory of sets, and develop natural proofs for reasoning
    using proof tactics involving disciplined unfoldings and formula abstractions.
    Natural proofs are encoded into decidable theories of first-order logic so as
    to be discharged using SMT solvers. We also implement the technique and show that
    a large class of more than 100 correct programs that manipulate data-structures
    are amenable to full functional correctness using the proposed natural proof method.
    These programs are drawn from a variety of sources including standard data-structures,
    the Schorr-Waite algorithm for garbage collection, a large number of low-level
    C routines from the Glib library, the OpenBSD library and the Linux kernel, and
    routines from a secure verified OS-browser project. Our work is the first that
    we know of that can handle such a wide range of full functional verification properties
    of heaps automatically, given pre/post and loop invariant annotations. We believe
    that this work paves the way for the deductive verification technology to be used
    by programmers who do not (and need not) understand the internals of the underlying
    logic solvers, significantly increasing their applicability in building reliable
    systems.
  author:
  - first: Xiaokang
    last: Qiu
  - first: Pranav
    last: Garg
  - first: Andrei
    last: \c{S}tef\u{a}nescu
  - first: Parthasarathy
    last: Madhusudan
  author_id: Xiaokang Qiu and Pranav Garg and Andrei Stefanescu and Parthasarathy
    Madhusudan
  authors:
  - id: xiaokang-qiu
    text: Xiaokang Qiu
  - id: pranav-garg
    text: Pranav Garg
  - id: andrei-stefanescu
    text: Andrei Stefanescu
  - id: parthasarathy-madhusudan
    text: Parthasarathy Madhusudan
  booktitle: Proceedings of the 34th Conference on Programming Language Design and
    Implementation (PLDI'13)
  booktitle_acronym: PLDI'13
  booktitle_url: http://pldi2013.ucombinator.org/
  category:
  - logics
  - program_verification
  - automated_reasoning
  date: 2013-06-01
  doi: http://dx.doi.org/10.1145/2499370.2462169
  id: qiu-garg-stefanescu-madhusudan-2013-pldi
  month: June
  pages: 231-242
  presentation: pldi13_dryad2
  project_name: Dryad
  project_url: http://www.cs.uiuc.edu/~madhu/dryad/
  publisher: ACM
  title: Natural Proofs for Structure, Data, and Separation
  type: inproceedings
  year: '2013'
layout: paper
title: Natural Proofs for Structure, Data, and Separation
---
