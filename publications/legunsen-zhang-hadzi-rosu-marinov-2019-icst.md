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
  authors: [Owolabi Legunsen, Yi Zhang, Milica Hadzi-Tanovic, Grigore Rosu, Darko
      Marinov]
  categories: [fsl, javamop, runtime_verification]
  date: 2019-04-01
  id: legunsen-zhang-hadzi-rosu-marinov-2019-icst
  title: Techniques for Evolution-Aware Runtime Verification
layout: paper
---
