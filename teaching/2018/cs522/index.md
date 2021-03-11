---
title: CS 522 -- Fall 2018
layout: default
---

Students enrolled in this class are expected to check this web page
regularly. Lecture notes and important other material will be posted
here.

## Course Description {#course_description}

CS522 is an advanced course on semantics of programming languages.
Various semantic approaches and related aspects will be defined and
investigated. Executable semantics of various programming languages and
paradigms will be discussed, together with major theoretical models.

-   *Meetings*: Tu/Th 9:30 - 10:45, 1103 Siebel Center
-   *Professor*: Grigore Rosu (Office: SC 2110, WWW: <http://fsl.cs.illinois.edu/grosu>, Email: grosu@illinois.edu)
-   *Office hours*: By appointment, very flexible (held by Grigore Rosu in SC 2110)

## Piazza Page {#piazza_page}

[CS522 Piazza Page](https://piazza.com/illinois/fall2018/cs522/home)

## Lecture Notes, Useful Material {#lecture_notes_useful_material}

The links below provide you with useful material for this class,
including complete lecture notes. These materials will be added *by
need* and more topics will be added.

-   [Introduction](CS522-Fall-2018-Introduction.pdf)

-   Conventional Semantic Approaches

    -   [Slides (PDF)](CS522-Fall-2018-Conventional-Executable-Semantics.pdf),
        [Slides (PPTX)](CS522-Fall-2018-Conventional-Executable-Semantics.pptx)
        <font color=red>(incomplete)</font>
    -   [Book material on IMP, Big-Step SOS, Small-Step SOS, and Denotational
        Semantics](CS522-Fall-2018-basic-semantics.pdf)

-   Rewriting Logic and Maude

    -   [slides](CS522-Fall-2018-Maude.pdf) - recommended only for a quick look
    -   [Book material](CS522-Fall-2018-Maude-book.pdf) - recommended

-   ### HW1 (due Tuesday, September 18) {#hw1}

    The following exercises are from the book material above. Do them only in
    Maude (that is, *not* on paper) by modifying [the provided Maude code for
    HW1](CS522-Fall-2018-Maude-HW1.zip): Exercise 56 (page 137); Exercise 70
    (page 155).

    In case you are not familiar with Maude, you are encouraged to do the
    following exercises to warm-up (but please do not include them as part of
    your HW1 submission): Exercise 30; Exercise 32; Exercise 33; Exercise 35;
    Exercise 36. All at pages 80/81.

-   ### HW2 (due Wednesday, October 3 - easy HW, so earlier submission possible and appreciated)

    The following exercises related to denotational semantics are from the book
    material above: Exercises 80, 81, 82 ((page 168; write these up on paper, or
    in a PDF); Exercise 83 (page 169; do it only in Maude (that is, *not* on
    paper) by modifying [the provided Maude code for
    HW2](CS522-Fall-2018-Maude-HW2.zip)).

-   [Book material on IMP++: Challenging Big-Step SOS, Small-Step SOS, and
    Denotational Semantics](CS522-Fall-2018-IMP++.pdf)

-   ### HW3 (due Monday, October 15)

    Combine all the individual extensions of IMP in [the provided Maude code for
    HW3](CS522-Fall-2018-Maude-HW2.zip) into the IMP++ language. Read the book
    material above for all the technical details. You should create a subfolder
    of imp called 6-imp++, and that should have four subfolders, one for each
    semantic style. Provide also three IMP++ programs.

-  [Book material on Modular SOS, Evaluation Contexts, and the CHAM](CS522-Fall-2018-MSOS-RSEC-CHAM.pdf)}`{=mediawiki}

-   ### HW4 (due Monday, October 29)

    Same as HW3 but for the three additional semantic approaches discussed in the
    lecture notes above: MSOS, RSEC, and CHAM. Use
    [this provided Maude code for HW4](CS522-Fall-2018-Maude-HW4.zip).
    Handle also a short essay discussing the advantages and limitations of each of
    the semantic approaches discussed so far in class, assigning a (justified) score
    between 1 and 10 to each of them.

-   Category theory: definition, diagrams, cones and limits, exponentials

    -   [Slides](CS522-Fall-2018-Category-Theory-slides.pdf)

    -   [Hand written notes on category theory properties](CS522-Fall-2018-HandWritten-Category-Theory.zip)

-   Lambda Calculus and Combinatory Logic

    - [Slides](CS522-Fall-2018-Lambda-slides.pdf)

    - [Book material on Lambda Calculus and Combinatory Logic](CS522-Fall-2018-Lambda.pdf)

-  [Hand written notes on CCC models of untyped Lambda Calculus](CS522-Fall-2018-HandWritten-CCC-untyped-lambda.zip)

-   ### HW5 (due Monday, November 12)

    This is a theoretical HW, requiring you to do three proofs using category
    theory. You are strongly encouraged to do \*all\* the exercises in the
    slides, especially if you did not have prior experience with category
    theory. However, for his HW, only handle the following three exercises: (1, easy) Exercise 8 on slide 20 in the
    [category theory slides](CS522-Fall-2018-Category-Theory-slides.pdf)
    (2, easy) Property 1 on "category theory - 3.png" in the
    [hand written notes on category theory properties](CS522-Fall-2018-HandWritten-Category-Theory.zip);
    and (3, harder) Lemma on slide "ccc-untyped-lambda - 3.png" in the
    [hand written notes on CCC models of untyped lambda calculus](CS522-Fall-2018-HandWritten-CCC-untyped-lambda.zip).

-   Simply-Typed Lambda Calculus
    * Basic notions: type system, equational semantics, models, completeness.  [Slides](CS522-Fall-2018-Simply-Typed-Lambda-Calculus.pdf)
    * Cartesian Closed Categories as models for simply-typed lambda-calculus.  [Slides](CS522-Fall-2018-PL-CCC.pdf)

-  ### HW6 (due Friday, November 30 -- can also take the weekend if needed)
  
   Proposition 8 from the slides on simply-typed lambda calculus. Exercises 5 and 6 from the slides on CCCs.

- Recursion, Types, Polymorphism

    - Recursion and Types. [Slides](CS522-Fall-2018-Recursion.pdf)
    - Polymorphism. [Slides](CS522-Fall-2018-Polymorphism.pdf)

-   ### Extra-Credit (due Monday, Dec 17)

    This can be regarded as "Final exam", but it only counts as HW
    (and not project) extra-credit and has the same weight as any of the
    previous HWs. If you got perfect score so far for the 6 HWs above,
    then you do not need to do this extra-credit. Choose one, and only
    one, of the following and do it well (you will get either 10 or 0
    for this extra-credit problem!):
    
    1. Complete this [LAMBDA code snippet](CS522-Fall-2018-Lambda-Extra.zip).
       This covers knowledge about untyped lambda-calculus, fixed-points,
       combinatory logic, and de Bruijn nameless representations.
    
    2. Consider the PCF language with call-by-value (note that the
       slides above define the call-by-name variant). Give it a small-step,
       a big-step, and a denotational semantics in Maude, using the
       representations of these semantic approaches discussed in the first
       part of the class. Provide also 5 (five) PCF programs that can be
       used to test all three of your semantics. You can use the builtins
       provided as part of the previous HWs (you should only need the
       generic substitution from there).
    
    3. This has two problems. The first is to define a type checker for
       the parametric polymorphic lambda-calculus (or System F). The second
       is to define a type checker for the subtype polymorphic
       lambda-calculus. In both cases, make sure that you also include the
       conditional and a few examples showing that your definition works.
       Feel free to pick whatever syntax you want for the various
       constructs (both for terms and for types).
