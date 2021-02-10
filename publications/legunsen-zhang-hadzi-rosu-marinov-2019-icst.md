---
bib:
  abstract: 'Runtime Verification (RV) can help find bugs by monitoring program executions
    against formal properties. De- velopers should ideally use RV whenever they run
    tests, to find more bugs earlier. Despite tremendous research progress, RV still
    incurs high overhead in (1) machine time to monitor properties, and (2) developer
    time to wait for and inspect violations from test executions that do not satisfy
    the properties. Moreover, all prior RV techniques consider only one program version
    and wastefully re-monitor unaffected properties and code as software evolves.
    We present the first evolution-aware RV techniques that re- duce RV overhead across
    multiple program versions. Regression Property Selection (RPS) re-monitors only
    properties that can be violated in parts of code affected by changes, reducing
    machine time and developer time. Violation Message Suppression (VMS) simply shows
    only new violations to reduce developer time; it does not reduce machine time.
    Regression Property Prioritization (RPP) splits RV in two phases: properties more
    likely to find bugs are monitored in a critical phase to provide faster feedback
    to the developers; the rest are monitored in a background phase. We compare our
    techniques with the evolution-unaware (base) RV when monitoring test executions
    in 200 versions of 10 open- source projects. RPS and the RPP critical phase reduce
    the average RV overhead from 9.4x (for base RV) to 1.8x, without missing any new
    violations. VMS reduces the average number of violations 540x, from 54 violations
    per version (for base RV) to one violation per 10 versions.'
  author:
  - first: Owolabi
    last: Legunsen
  - first: Yi
    last: Zhang
  - first: Milica
    last: Hadzi-Tanovic
  - first: Grigore
    last: Ro\c{s}u
  - first: Darko
    last: Marinov
  author_id: Owolabi Legunsen and Yi Zhang and Milica Hadzi-Tanovic and Grigore Rosu
    and Darko Marinov
  author_ids:
  - owolabi-legunsen
  - yi-zhang
  - milica-hadzitanovic
  - grigore-rosu
  - darko-marinov
  authors:
  - id: owolabi-legunsen
    text: Owolabi Legunsen
  - id: yi-zhang
    text: Yi Zhang
  - id: milica-hadzitanovic
    text: Milica Hadzi-Tanovic
  - id: grigore-rosu
    text: Grigore Rosu
  - id: darko-marinov
    text: Darko Marinov
  booktitle: 2019 12th IEEE Conference on Software Testing, Validation and Verification
    (ICST)
  booktitle_acronym: ICST 2019
  booktitle_url: http://icst2019.xjtu.edu.cn/
  category:
  - fsl
  - javamop
  - runtime_verification
  date: 2019-04-01
  doi: https://doi.org/10.1109/ICST.2019.00037
  id: legunsen-zhang-hadzi-rosu-marinov-2019-icst
  month: April
  pages: 300-311
  presentation: 2019-4-26-ICST
  project_name: JavaMOP
  project_url: https://github.com/runtimeverification
  publisher: IEEE
  title: Techniques for Evolution-Aware Runtime Verification
  type: inproceedings
  year: '2019'
bib_url: publications/legunsen-zhang-hadzi-rosu-marinov-2019-icst.bib
layout: paper
pdf_url: publications/legunsen-zhang-hadzi-rosu-marinov-2019-icst.pdf
title: Techniques for Evolution-Aware Runtime Verification
---
