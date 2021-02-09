---
bib:
  abstract: 'Programmers and software engineers agree in unanimity that a useful characteristic
    of the programming languages they use for implementations (C++, Java, etc.) is
    their support for both {\em public} and {\em private} features (types, functions).
    The public features are often called {\em interfaces}. The private part is not
    visible outside the module (class, package) that declares it, but it can be used
    internally to define the visible part. Such distinction helps software engineers
    abstract their work and ignore details which are a main source of confusion and
    errors. We claim that the distinction between private and public features might
    also be a desirable characteristic of formal specifications, not only from the
    practical point of view but also because of at least two important theoretical
    reasons. One is the possibility to finitely specify theories which do not admit
    finite standard presentations. For example, Bergstra and Tucker showed that any
    recursive algebra is a restriction of an initial algebra presented by a finite
    number of equations over a larger signature. Another reason is that it allows
    the user to specify behavioral properties of systems, in the sense that every
    behavioral specification is equivalent to hiding some operators (i.e., making
    them private) in a usual specification. We introduce the notion of {\em module
    specification} as a generalization of the standard specification, having both
    public (or visible) and private features, and then explore their properties at
    an abstract level, categorical. To formalize the notion of ``logical system''''
    we use {\em institutions} enriched with {\em inclusions}, an abstraction of the
    natural notion of inclusion of signatures from particular logics. The {\em visible
    theorems} (or the visible consequences) of a module are those theorems which contain
    only visible symbols, and a model of that module is a model of its visible consequences.
    Five basic operations on module specifications are explored: renaming, hiding,
    enriching, aggregation and parameterization. An internal property of modules,
    {\em conservativeness}, seems to have a decisive role in giving semantics for
    module composition.'
  authors: [Grigore Rosu]
  categories: [logics, programming_languages]
  date: 2000-05-01
  id: rosu-2000-tr
  title: Abstract Semantics for Module Composition
layout: paper
---
