---
abstract: 'A developing field of interest for the distributed systems and applied
  cryptography communities is that of smart contracts: self-executing financial instruments
  that synchronize their state, often through a blockchain. One such smart contract
  system that has seen widespread practical adoption is Ethereum, which has grown
  to a market capacity of 100 billion USD and clears an excess of 500,000 daily transactions.
  Unfortunately, the rise of these technologies has been marred by a series of costly
  bugs and exploits. Increasingly, the Ethereum community has turned to formal methods
  and rigorous program analysis tools. This trend holds great promise due to the relative
  simplicity of smart contracts and bounded-time deterministic execution inherent
  to the Ethereum Virtual Machine (EVM). Here we present KEVM, an executable formal
  specification of the EVM''s bytecode stack-based language built with the \K{} Framework,
  designed to serve as a solid foundation for further formal analyses. We empirically
  evaluate the correctness and performance of KEVM using the official Ethereum test
  suite~\cite{ethereum-tests-url}. To demonstrate the usability, several extensions
  of the semantics are presented and two different-language implementations of the
  ERC20 Standard Token are verified against the ERC20 specification. These results
  are encouraging for the executable semantics approach to language prototyping and
  specification.'
authors: [Everett Hildenbrandt, Manasvi Saxena, Xiaoran Zhu, Nishant Rodrigues, Philip
    Daian, Dwight Guth, Brandon Moore, Yi Zhang, Daejun Park, Andrei Stefanescu, Grigore
    Rosu]
categories: [k, semantics, executable_semantics, evm, ethereum, virtual_machine, fsl]
date: 2018-01-01
id: hildenbrandt-saxena-zhu-rodrigues-daian-guth-moore-zhang-park-rosu-2018-csf
title: 'KEVM: A Complete Semantics of the Ethereum Virtual Machine'
---
