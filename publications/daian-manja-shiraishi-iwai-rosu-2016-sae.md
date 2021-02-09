---
abstract: The Runtime Verification ECU (RV-ECU) is a new development platform for
  checking and enforcing the safety of automotive bus communications and software
  systems. RV-ECU uses runtime verification, a formal analysis subfield geared at
  validating and verifying systems as they run, to ensure that all manufacturer and
  third-party safety specifications are complied with during the operation of the
  vehicle. By compiling formal safety properties into code using a certifying compiler,
  the RV-ECU executes only provably correct code that checks for safety violations
  as the system runs. RV-ECU can also recover from violations of these properties,
  either by itself in simple cases or together with safe message-sending libraries
  implementable on third-party control units on the bus. RV-ECU can be updated with
  new specifications after a vehicle is released, enhancing the safety of vehicles
  that have already been sold and deployed. Currently a prototype, RV-ECU is meant
  to eventually be deployed as global and local ECU safety monitors, ultimately responsible
  for the safety of the entire vehicle system. We describe its overall architecture
  and implementation, and demonstrate monitoring of safety specifications on the CAN
  bus. We use past automotive recalls as case studies to demonstrate the potential
  of updating the RV-ECU as a cost effective and practical alternative to software
  recalls, while requiring the development of rigorous, formal safety specifications
  easily sharable across manufacturers, OEMs, regulatory agencies and even car owners.
authors: [Philip Daian, Bhargava Manja, Shinichi Shiraishi, Akihito Iwai, Grigore
    Rosu]
categories: [fsl, runtime_verification]
date: 2016-04-01
id: daian-manja-shiraishi-iwai-rosu-2016-sae
title: 'RV-ECU: Maximum Assurance In-Vehicle Safety Monitoring'
---
