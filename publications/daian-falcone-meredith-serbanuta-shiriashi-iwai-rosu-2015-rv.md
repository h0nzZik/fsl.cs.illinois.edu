---
bib:
  abstract: RV-Android is a new freely available open source runtime library for monitoring
    formal safety properties on Android. RV-Android uses the commercial RV-Monitor
    technology as its core monitoring library generation technology, allowing for
    the verification of safety properties during execution and operating entirely
    in userspace with no kernel or operating system modifications required. RV-Android
    improves on previous Android monitoring work by replacing the JavaMOP framework
    with RV-Monitor, a more advanced monitoring library generation tool with core
    algorithmic improvements that greatly improve resource consumption, efficiency,
    and battery life considerations. We demonstrate the developer usage of RV-Android
    with the standard Android build process, using instrumentation mechanisms effective
    on both Android binaries and source code. Our method allows for both property
    development and advanced application testing through runtime verification. We
    showcase the user frontend of RV-Monitor, which is available for public demo use
    and requires no knowledge of RV concepts. We explore the extra expressiveness
    the MOP paradigm provides over simply writing properties as aspects through two
    sample security properties, and show an example of a real security violation mitigated
    by RV-Android on-device. Lastly, we propose RV as an extension to the next-generation
    Android permissions system debuting in Android M.
  authors: [Philip Daian, Ylies Falcone, Patrick Meredith, Traian Florin Serbanuta,
    Shinichi Shiraishi, Akihito Iwai, Grigore Rosu]
  categories: [fsl, javamop, runtime_verification]
  date: 2015-09-01
  id: daian-falcone-meredith-serbanuta-shiriashi-iwai-rosu-2015-rv
  title: 'RV-Android: Efficient Parametric Android Runtime Verification, a Brief Tutorial'
layout: paper
---
