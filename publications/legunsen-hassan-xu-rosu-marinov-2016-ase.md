---
bib:
  abstract: Runtime verification can be used to find bugs early, during software development,
    by monitoring test executions against formal specifications (specs). The quality
    of runtime verification depends on the quality of the specs. While previous research
    has produced many specs for the Java API, manually or through automatic mining,
    there has been no large-scale study of their bug-finding effectiveness. We present
    the first in-depth study of the bug-finding effectiveness of previously proposed
    specs. We used JavaMOP to monitor 182 manually written and 17 automatically mined
    specs against more than 18K manually written and 2.1M automatically generated
    tests in 200 open-source projects. The average runtime overhead was under 4.3x.
    We inspected 652 violations of manually written specs and (randomly sampled) 200
    violations of automatically mined specs. We reported 95 bugs, out of which developers
    already accepted or fixed 74. However, most violations, 82.81% of 652 and 97.89%
    of 200, were false alarms. Our empirical results show that (1) runtime verification
    technology has matured enough to incur tolerable runtime overhead during testing,
    and (2) the existing API specifications can find many bugs that developers are
    willing to fix; however, (3) the false alarm rates are worrisome and suggest that
    substantial effort needs to be spent on engineering better specs and properly
    evaluating their effectiveness.
  authors: [Owolabi Legunsen, Wajih Ul Hassan, Xinyue Xu, Grigore Rosu, Darko Marinov]
  booktitle: 31st IEEE/ACM International Conference on Automated Software Engineering
    (ASE'16)
  booktitle_acronym: ASE 2016
  booktitle_url: http://www.ase2016.org/
  categories: [fsl, javamop, runtime_verification]
  date: 2016-09-01
  id: legunsen-hassan-xu-rosu-marinov-2016-ase
  pages: 602-613
  project_url: https://github.com/runtimeverification
  publisher: IEEE/ACM
  title: How Good are the Specs? A Study of the Bug-Finding Effectiveness of Existing
    Java API Specifications
layout: paper
title: How Good are the Specs? A Study of the Bug-Finding Effectiveness of Existing
  Java API Specifications
---
