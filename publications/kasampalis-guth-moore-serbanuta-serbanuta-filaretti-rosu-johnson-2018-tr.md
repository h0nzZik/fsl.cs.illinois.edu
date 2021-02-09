---
bib:
  abstract: Most languages are given an informal semantics until they are implemented,
    so the formal semantics comes later. Consequently, there are usually inconsistencies
    among the informal semantics, the implementation, and the formal semantics. IELE
    is an LLVM-like language for the blockchain that was specified formally and its
    implementation, a virtual machine, generated from the formal specification. Moreover,
    its design was based on problems observed formalizing the semantics of the Ethereum
    Virtual Machine (EVM) and from formally specifying and verifying EVM programs
    (also called "smart contracts"), so even the design decisions made for IELE are
    based on formal specifications. A compiler from Solidity, the predominant high-level
    language for smart contracts, to IELE has also been implemented, so Ethereum contracts
    can now also be executed on IELE. The virtual machine automatically generated
    from the semantics of IELE is shown to be competitive in terms of performance
    with the state of the art and hence can stand as the de facto implementation of
    the language in a production setting. Indeed, IOHK, a major blockchain company,
    is currently experimenting with the IELE VM in order to deploy it as its computational
    layer in a few months. This makes IELE the first practical language that is designed
    and implemented as a formal specification. It took only 10 man-months to develop
    IELE, which demonstrates that the programming language semantics field has reached
    a level of maturity that makes it appealing over the traditional, adhoc approach
    even for pragmatic reasons.
  authors: [Theodoros Kasampalis, Dwight Guth, Brandon Moore, Traian Serbanuta, Virgil
      Serbanuta, Daniele Filaretti, Grigore Rosu, Ralph Johnson]
  categories: [k, semantics, executable_semantics, iele, virtual_machine, fsl]
  date: 2018-07-01
  id: kasampalis-guth-moore-serbanuta-serbanuta-filaretti-rosu-johnson-2018-tr
  title: 'IELE: An Intermediate-Level Blockchain Language Designed and Implemented
    Using Formal Semantics'
layout: paper
---
