from enum import Enum



class Administrativesex(str, Enum):
     """
     001 - Administrative sex

     F  Female
     M  Male
     O  Other
     U  Unknown
     A  Ambiguous
     N  Not applicable
     """


     F = "F"
     M = "M"
     O = "O"
     U = "U"
     A = "A"
     N = "N"


class Maritalstatus(str, Enum):
     """
     002 - Marital status

     A  Separated
     D  Divorced
     M  Married
     S  Single
     W  Widowed
     C  Common law
     G  Living together
     P  Domestic partner
     R  Registered domestic partner
     E  Legally Separated
     N  Annulled
     I  Interlocutory
     B  Unmarried
     U  Unknown
     O  Other
     T  Unreported
     """


     A = "A"
     D = "D"
     M = "M"
     S = "S"
     W = "W"
     C = "C"
     G = "G"
     P = "P"
     R = "R"
     E = "E"
     N = "N"
     I = "I"
     B = "B"
     U = "U"
     O = "O"
     T = "T"


class Eventtype(str, Enum):
     """
     003 - Event type

     CNQ  QRY/EQQ/SPQ/VQQ/RQQ - Cancel query
     A01  ADT/ACK - Admit/visit notification
     A02  ADT/ACK - Transfer a patient
     A03  ADT/ACK -  Discharge/end visit
     A04  ADT/ACK -  Register a patient
     A05  ADT/ACK -  Pre-admit a patient
     A06  ADT/ACK -  Change an outpatient to an inpatient
     A07  ADT/ACK -  Change an inpatient to an outpatient
     A08  ADT/ACK -  Update patient information
     A09  ADT/ACK -  Patient departing - tracking
     A10  ADT/ACK -  Patient arriving - tracking
     A11  ADT/ACK -  Cancel admit/visit notification
     A12  ADT/ACK -  Cancel transfer
     A13  ADT/ACK -  Cancel discharge/end visit
     A14  ADT/ACK -  Pending admit
     A15  ADT/ACK -  Pending transfer
     A16  ADT/ACK -  Pending discharge
     A17  ADT/ACK -  Swap patients
     A18  ADT/ACK -  Merge patient information (for backward compatibility only)
     A19  QRY/ADR -  Patient query
     A20  ADT/ACK -  Bed status update
     A21  ADT/ACK -  Patient goes on a "leave of absence"
     A22  ADT/ACK -  Patient returns from a "leave of absence"
     A23  ADT/ACK -  Delete a patient record
     A24  ADT/ACK -  Link patient information
     A25  ADT/ACK -  Cancel pending discharge
     A26  ADT/ACK -  Cancel pending transfer
     A27  ADT/ACK -  Cancel pending admit
     A28  ADT/ACK -  Add person information
     A29  ADT/ACK -  Delete person information
     A30  ADT/ACK -  Merge person information (for backward compatibility only)
     A31  ADT/ACK -  Update person information
     A32  ADT/ACK -  Cancel patient arriving - tracking
     A33  ADT/ACK -  Cancel patient departing - tracking
     A34  ADT/ACK -  Merge patient information - patient ID only (for backward compatibility only)
     A35  ADT/ACK -  Merge patient information - account number only (for backward compatibility only)
     A36  ADT/ACK -  Merge patient information - patient ID and account number (for backward compatibility only)
     A37  ADT/ACK -  Unlink patient information
     A38  ADT/ACK - Cancel pre-admit
     A39  ADT/ACK - Merge person - patient ID (for backward compatibility only)
     A40  ADT/ACK - Merge patient - patient identifier list
     A41  ADT/ACK - Merge account - patient account number
     A42  ADT/ACK - Merge visit - visit number
     A43  ADT/ACK - Move patient information - patient identifier list
     A44  ADT/ACK - Move account information - patient account number
     A45  ADT/ACK - Move visit information - visit number
     A46  ADT/ACK - Change patient ID (for backward compatibility only)
     A47  ADT/ACK - Change patient identifier list
     A48  ADT/ACK - Change alternate patient ID (for backward compatibility only)
     A49  ADT/ACK - Change patient account number
     A50  ADT/ACK - Change visit number
     A51  ADT/ACK - Change alternate visit ID
     A52  ADT/ACK - Cancel leave of absence for a patient
     A53  ADT/ACK - Cancel patient returns from a leave of absence
     A54  ADT/ACK - Change attending doctor
     A55  ADT/ACK - Cancel change attending doctor
     A60  ADT/ACK -  Update allergy information
     A61  ADT/ACK - Change consulting doctor
     A62  ADT/ACK - Cancel change consulting doctor
     B01  PMU/ACK - Add personnel record
     B02  PMU/ACK - Update personnel record
     B03  PMU/ACK - Delete personnel re cord
     B04  PMU/ACK - Active practicing person
     B05  PMU/ACK - Deactivate practicing person
     B06  PMU/ACK - Terminate practicing person
     C01  CRM - Register a patient on a clinical trial
     C02  CRM - Cancel a patient registration on clinical trial (for clerical mistakes only)
     C03  CRM - Correct/update registration information
     C04  CRM - Patient has gone off a clinical trial
     C05  CRM - Patient enters phase of clinical trial
     C06  CRM - Cancel patient entering a phase (clerical mistake)
     C07  CRM - Correct/update phase information
     C08  CRM - Patient has gone off phase of clinical trial
     C09  CSU - Automated time intervals for reporting, like monthly
     C10  CSU - Patient completes the clinical trial
     C11  CSU - Patient completes a phase of the clinical trial
     C12  CSU - Update/correction of patient order/result information
     I01  RQI/RPI - Request for insurance information
     I02  RQI/RPL - Request/receipt of patient selection display list
     I03  RQI/RPR - Request/receipt of patient selection list
     I04  RQD/RPI - Request for patient demographic data
     I05  RQC/RCI - Request for patient clinical information
     I06  RQC/RCL - Request/receipt of clinical data listing
     I07  PIN/ACK - Unsolicited insurance information
     I08  RQA/RPA - Request for treatment authorization information
     I09  RQA/RPA - Request for modification to an authorization
     I10  RQA/RPA - Request for resubmission of an authorization
     I11  RQA/RPA - Request for cancellation of an authorization
     I12  REF/RRI - Patient referral
     I13  REF/RRI - Modify patient referral
     I14  REF/RRI - Cancel patient referral
     I15  REF/RRI - Request patient referral status
     J01  QCN/ACK - Cancel query/acknowledge message
     J02  QSX/ACK - Cancel subscription/acknowledge message
     K21  RSP - Get person demographics response
     K22  RSP - Find candidates response
     K23  RSP - Get corresponding identifiers response
     K24  RSP - Allocate identifiers response
     K25  RSP - Personnel Information by Segment Response
     M01  MFN/MFK - Master file not otherwise specified (for backward compatibility only)
     M02  MFN/MFK - Master file - staff practitioner
     M03  MFN/MFK - Master file - test/observation (for backward compatibility only)
     M04  MFN/MFK - Master files charge description
     M05  MFN/MFK - Patient location master file
     M06  MFN/MFK - Clinical study with phases and schedules master file
     M07  MFN/MFK - Clinical study without phases but with schedules master file
     M08  MFN/MFK - Test/observation (numeric) master file
     M09  MFN/MFK - Test/observation (categorical) master file
     M10  MFN/MFK - Test /observation batteries master file
     M11  MFN/MFK - Test/calculated observations master file
     M12  MFN/MFK - Master file notification message
     N01  NMQ/NMR - Application management query message
     N02  NMD/ACK - Application management data message (unsolicited)
     O01  ORM - Order message (also RDE, RDS, RGV, RAS)
     O02  ORR - Order response (also RRE, RRD, RRG, RRA)
     O03  OMD - Diet order
     O04  ORD - Diet order acknowledgement
     O05  OMS - Stock requisition order
     O06  ORS - Stock requisition acknowledgement
     O07  OMN - Non-stock requisition order
     O08  ORN - Non-stock requisition acknowledgement
     O09  OMP - Pharmacy/treatment order
     O10  ORP - Pharmacy/treatment order acknowledgement
     O11  RDE - Pharmacy/treatment encoded order
     O12  RRE - Pharmacy/treatment encoded order acknowledgement
     O13  RDS - Pharmacy/treatment dispense
     O14  RRD - Pharmacy/treatment dispense acknowledgement
     O15  RGV - Pharmacy/treatment give
     O16  RRG - Pharmacy/treatment give acknowledgement
     O17  RAS - Pharmacy/treatment administration
     O18  RRA - Pharmacy/treatment administration acknowledgement
     O19  OMG - General clinical order
     O20  ORG/ORL - General clinical order response
     O21  OML - Laboratory order
     P01  BAR/ACK - Add patient accounts
     P02  BAR/ACK - Purge patient accounts
     P03  DFT/ACK - Post detail financial transaction
     P04  QRY/DSP - Generate bill and A/R statements
     P05  BAR/ACK - Update account
     P06  BAR/ACK - End account
     P07  PEX - Unsolicited initial individual product experience report
     P08  PEX - Unsolicited update individual product experience report
     P09  SUR - Summary product experience report
     P10  BAR/ACK -Transmit  Ambulatory Payment  Classification(APC)
     PC1  PPR - PC/ problem add
     PC2  PPR - PC/ problem update
     PC3  PPR - PC/ problem delete
     PC4  QRY - PC/ problem query
     PC5  PRR - PC/ problem response
     PC6  PGL - PC/ goal add
     PC7  PGL - PC/ goal update
     PC8  PGL - PC/ goal delete
     PC9  QRY - PC/ goal query
     PCA  PPV - PC/ goal response
     PCB  PPP - PC/ pathway (problem-oriented) add
     PCC  PPP - PC/ pathway (problem-oriented) update
     PCD  PPP - PC/ pathway (problem-oriented) delete
     PCE  QRY - PC/ pathway (problem-oriented) query
     PCF  PTR - PC/ pathway (problem-oriented) query response
     PCG  PPG - PC/ pathway (goal-oriented) add
     PCH  PPG - PC/ pathway (goal-oriented) update
     PCJ  PPG - PC/ pathway (goal-oriented) delete
     PCK  QRY - PC/ pathway (goal-oriented) query
     PCL  PPT - PC/ pathway (goal-oriented) query response
     Q01  QRY/DSR - Query sent for immediate response
     Q02  QRY/QCK - Query sent for deferred response
     Q03  DSR/ACK - Deferred response to a query
     Q04  EQQ - Embedded query language query
     Q05  UDM/ACK - Unsolicited display update message
     Q06  OSQ/OSR - Query for order status
     Q07  VQQ - Virtual table query
     Q08  SPQ - Stored procedure request
     Q09  RQQ - event replay query
     Q16  QSB - Create subscription
     Q17  QVR - Query for previous events
     Q21  QBP - Get person demographics
     Q22  QBP - Find candidates
     Q23  QBP - Get corresponding identifiers
     Q24  QBP - Allocate identifiers
     Q25  QBP - Personnel Information by Segment Query
     R01  ORU/ACK - Unsolicited transmission of an observation message
     R02  QRY - Query for results of observation
     R03  QRY/DSR Display-oriented results, query/unsol. update (for backward compatibility only) (Replaced by Q05)
     R04  ORF - Response to query; transmission of requested observation
     R05  QRY/DSR - query for display results (See Q01)
     R06  UDM - unsolicited update/display results (See Q05)
     R07  EDR - enhanced display response
     R08  TBR - tabular data response
     R09  ERP - event replay response
     ROR  ROR - Pharmacy prescription order query response
     R21  OUL - Unsolicited laboratory observation
     RAR  RAR - Pharmacy administration information query response
     RDR  RDR - Pharmacy dispense information query response
     RER  RER - Pharmacy encoded order information query response
     RGR  RGR - Pharmacy dose information query response
     S01  SRM/SRR - Request new appointment booking
     S02  SRM/SRR - Request appointment rescheduling
     S03  SRM/SRR - Request appointment modification
     S04  SRM/SRR - Request appointment cancellation
     S05  SRM/SRR - Request appointment discontinuation
     S06  SRM/SRR - Request appointment deletion
     S07  SRM/SRR - Request addition of service/resource on appointment
     S08  SRM/SRR - Request modification of service/resource on appointment
     S09  SRM/SRR - Request cancellation of service/resource on appointment
     S10  SRM/SRR - Request discontinuation of service/resource on appointment
     S11  SRM/SRR - Request deletion of service/resource on appointment
     S12  SIU/ACK - Notification of new appointment booking
     S13  SIU/ACK - Notification of appointment rescheduling
     S14  SIU/ACK - Notification of appointment modification
     S15  SIU/ACK - Notification of appointment cancellation
     S16  SIU/ACK - Notification of appointment discontinuation
     S17  SIU/ACK - Notification of appointment deletion
     S18  SIU/ACK - Notification of addition of service/resource on appointment
     S19  SIU/ACK - Notification of modification of service/resource on appointment
     S20  SIU/ACK - Notification of cancellation of service/resource on appointment
     S21  SIU/ACK - Notification of discontinuation of service/resource on appointment
     S22  SIU/ACK - Notification of deletion of service/resource on appointment
     S23  SIU/ACK - Notification of blocked schedule time slot(s)
     S24  SIU/ACK - Notification of opened ("unblocked") schedule time slot(s)
     S25  SQM/SQR - Schedule query message and response
     S26  SIU/ACK Notification that patient did not show up for schedule appointment
     T01  MDM/ACK - Original document notification
     T02  MDM/ACK - Original document notification and content
     T03  MDM/ACK - Document status change notification
     T04  MDM/ACK - Document status change notification and content
     T05  MDM/ACK - Document addendum notification
     T06  MDM/ACK - Document addendum notification and content
     T07  MDM/ACK - Document edit notification
     T08  MDM/ACK - Document edit notification and content
     T09  MDM/ACK - Document replacement notification
     T10  MDM/ACK - Document replacement notification and content
     T11  MDM/ACK - Document cancel notification
     T12  QRY/DOC - Document query
     U01  ESU/ACK - Automated equipment status update
     U02  ESR/ACK - Automated equipment status request
     U03  SSU/ACK - Specimen status update
     U04  SSR/ACK - specimen status request
     U05  INU/ACK  - Automated equipment inventory update
     U06  INR/ACK - Automated equipment inventory request
     U07  EAC/ACK - Automated equipment command
     U08  EAR/ACK - Automated equipment response
     U09  EAN/ACK - Automated equipment notification
     U10  TCU/ACK - Automated equipment test code settings update
     U11  TCR/ACK - Automated equipment test code settings request
     U12  LSU/ACK - Automated equipment log/service update
     U13  LSR/ACK - Automated equipment log/service request
     V01  VXQ - Query for vaccination record
     V02  VXX - Response to vaccination query returning multiple PID matches
     V03  VXR - Vaccination record response
     V04  VXU - Unsolicited vaccination record update
     Varies  MFQ/MFR - Master files query (use event same as asking for e.g., M05 - location)
     W01  ORU - Waveform result, unsolicited transmission of requested information
     W02  QRF - Waveform result, response to query
     """


     CNQ = "CNQ"
     A01 = "A01"
     A02 = "A02"
     A03 = "A03"
     A04 = "A04"
     A05 = "A05"
     A06 = "A06"
     A07 = "A07"
     A08 = "A08"
     A09 = "A09"
     A10 = "A10"
     A11 = "A11"
     A12 = "A12"
     A13 = "A13"
     A14 = "A14"
     A15 = "A15"
     A16 = "A16"
     A17 = "A17"
     A18 = "A18"
     A19 = "A19"
     A20 = "A20"
     A21 = "A21"
     A22 = "A22"
     A23 = "A23"
     A24 = "A24"
     A25 = "A25"
     A26 = "A26"
     A27 = "A27"
     A28 = "A28"
     A29 = "A29"
     A30 = "A30"
     A31 = "A31"
     A32 = "A32"
     A33 = "A33"
     A34 = "A34"
     A35 = "A35"
     A36 = "A36"
     A37 = "A37"
     A38 = "A38"
     A39 = "A39"
     A40 = "A40"
     A41 = "A41"
     A42 = "A42"
     A43 = "A43"
     A44 = "A44"
     A45 = "A45"
     A46 = "A46"
     A47 = "A47"
     A48 = "A48"
     A49 = "A49"
     A50 = "A50"
     A51 = "A51"
     A52 = "A52"
     A53 = "A53"
     A54 = "A54"
     A55 = "A55"
     A60 = "A60"
     A61 = "A61"
     A62 = "A62"
     B01 = "B01"
     B02 = "B02"
     B03 = "B03"
     B04 = "B04"
     B05 = "B05"
     B06 = "B06"
     C01 = "C01"
     C02 = "C02"
     C03 = "C03"
     C04 = "C04"
     C05 = "C05"
     C06 = "C06"
     C07 = "C07"
     C08 = "C08"
     C09 = "C09"
     C10 = "C10"
     C11 = "C11"
     C12 = "C12"
     I01 = "I01"
     I02 = "I02"
     I03 = "I03"
     I04 = "I04"
     I05 = "I05"
     I06 = "I06"
     I07 = "I07"
     I08 = "I08"
     I09 = "I09"
     I10 = "I10"
     I11 = "I11"
     I12 = "I12"
     I13 = "I13"
     I14 = "I14"
     I15 = "I15"
     J01 = "J01"
     J02 = "J02"
     K21 = "K21"
     K22 = "K22"
     K23 = "K23"
     K24 = "K24"
     K25 = "K25"
     M01 = "M01"
     M02 = "M02"
     M03 = "M03"
     M04 = "M04"
     M05 = "M05"
     M06 = "M06"
     M07 = "M07"
     M08 = "M08"
     M09 = "M09"
     M10 = "M10"
     M11 = "M11"
     M12 = "M12"
     N01 = "N01"
     N02 = "N02"
     O01 = "O01"
     O02 = "O02"
     O03 = "O03"
     O04 = "O04"
     O05 = "O05"
     O06 = "O06"
     O07 = "O07"
     O08 = "O08"
     O09 = "O09"
     O10 = "O10"
     O11 = "O11"
     O12 = "O12"
     O13 = "O13"
     O14 = "O14"
     O15 = "O15"
     O16 = "O16"
     O17 = "O17"
     O18 = "O18"
     O19 = "O19"
     O20 = "O20"
     O21 = "O21"
     P01 = "P01"
     P02 = "P02"
     P03 = "P03"
     P04 = "P04"
     P05 = "P05"
     P06 = "P06"
     P07 = "P07"
     P08 = "P08"
     P09 = "P09"
     P10 = "P10"
     PC1 = "PC1"
     PC2 = "PC2"
     PC3 = "PC3"
     PC4 = "PC4"
     PC5 = "PC5"
     PC6 = "PC6"
     PC7 = "PC7"
     PC8 = "PC8"
     PC9 = "PC9"
     PCA = "PCA"
     PCB = "PCB"
     PCC = "PCC"
     PCD = "PCD"
     PCE = "PCE"
     PCF = "PCF"
     PCG = "PCG"
     PCH = "PCH"
     PCJ = "PCJ"
     PCK = "PCK"
     PCL = "PCL"
     Q01 = "Q01"
     Q02 = "Q02"
     Q03 = "Q03"
     Q04 = "Q04"
     Q05 = "Q05"
     Q06 = "Q06"
     Q07 = "Q07"
     Q08 = "Q08"
     Q09 = "Q09"
     Q16 = "Q16"
     Q17 = "Q17"
     Q21 = "Q21"
     Q22 = "Q22"
     Q23 = "Q23"
     Q24 = "Q24"
     Q25 = "Q25"
     R01 = "R01"
     R02 = "R02"
     R03 = "R03"
     R04 = "R04"
     R05 = "R05"
     R06 = "R06"
     R07 = "R07"
     R08 = "R08"
     R09 = "R09"
     ROR = "ROR"
     R21 = "R21"
     RAR = "RAR"
     RDR = "RDR"
     RER = "RER"
     RGR = "RGR"
     S01 = "S01"
     S02 = "S02"
     S03 = "S03"
     S04 = "S04"
     S05 = "S05"
     S06 = "S06"
     S07 = "S07"
     S08 = "S08"
     S09 = "S09"
     S10 = "S10"
     S11 = "S11"
     S12 = "S12"
     S13 = "S13"
     S14 = "S14"
     S15 = "S15"
     S16 = "S16"
     S17 = "S17"
     S18 = "S18"
     S19 = "S19"
     S20 = "S20"
     S21 = "S21"
     S22 = "S22"
     S23 = "S23"
     S24 = "S24"
     S25 = "S25"
     S26 = "S26"
     T01 = "T01"
     T02 = "T02"
     T03 = "T03"
     T04 = "T04"
     T05 = "T05"
     T06 = "T06"
     T07 = "T07"
     T08 = "T08"
     T09 = "T09"
     T10 = "T10"
     T11 = "T11"
     T12 = "T12"
     U01 = "U01"
     U02 = "U02"
     U03 = "U03"
     U04 = "U04"
     U05 = "U05"
     U06 = "U06"
     U07 = "U07"
     U08 = "U08"
     U09 = "U09"
     U10 = "U10"
     U11 = "U11"
     U12 = "U12"
     U13 = "U13"
     V01 = "V01"
     V02 = "V02"
     V03 = "V03"
     V04 = "V04"
     Varies = "Varies"
     W01 = "W01"
     W02 = "W02"


class Patientclass(str, Enum):
     """
     004 - Patient class

     E  Emergency
     I  Inpatient
     O  Outpatient
     P  Preadmit
     R  Recurring patient
     B  Obstetrics
     C  Commercial Account
     N  Not Applicable
     U  Unknown
     """


     E = "E"
     I = "I"
     O = "O"
     P = "P"
     R = "R"
     B = "B"
     C = "C"
     N = "N"
     U = "U"


class Race(str, Enum):
     """
     005 - Race

     1002-5  American Indian or Alaska Native
     2028-9  Asian
     2054-5  Black or African American
     2076-8  Native Hawaiian or Other Pacific Islander
     2106-3  White
     2131-1  Other Race
     """


     _1002_5 = "1002-5"
     _2028_9 = "2028-9"
     _2054_5 = "2054-5"
     _2076_8 = "2076-8"
     _2106_3 = "2106-3"
     _2131_1 = "2131-1"


class Religion(str, Enum):
     """
     006 - Religion

     AGN  Agnostic
     ATH  Atheist
     BAH  Baha'i
     BUD  Buddhist
     BMA  Buddhist: Mahayana
     BTH  Buddhist: Theravada
     BTA  Buddhist: Tantrayana
     BOT  Buddhist: Other
     CFR  Chinese Folk Religionist
     CHR  Christian
     ABC  Christian: American Baptist Church
     AMT  Christian: African Methodist Episcopal
     AME  Christian: African Methodist Episcopal Zion
     ANG  Christian: Anglican
     AOG  Christian: Assembly of God
     BAP  Christian: Baptist
     CAT  Christian: Roman Catholic
     CRR  Christian: Christian Reformed
     CHS  Christian: Christian Science
     CMA  Christian: Christian Missionary Alliance
     COC  Christian: Church of Christ
     COG  Christian: Church of God
     COI  Christian: Church of God in Christ
     COM  Christian: Community
     COL  Christian: Congregational
     EOT  Christian: Eastern Orthodox
     EVC  Christian: Evangelical Church
     EPI  Christian: Episcopalian
     FWB  Christian: Free Will Baptist
     FRQ  Christian: Friends
     GRE  Christian: Greek Orthodox
     JWN  Christian: Jehovah's Witness
     LUT  Christian: Lutheran
     LMS  Christian: Lutheran Missouri Synod
     MEN  Christian: Mennonite
     MET  Christian: Methodist
     MOM  Christian: Latter-day Saints
     NAZ  Christian: Church of the Nazarene
     ORT  Christian: Orthodox
     COT  Christian: Other
     PRC  Christian: Other Protestant
     PEN  Christian: Pentecostal
     COP  Christian: Other Pentecostal
     PRE  Christian: Presbyterian
     PRO  Christian: Protestant
     QUA  Christian: Friends
     REC  Christian: Reformed Church
     REO  Christian: Reorganized Church of Jesus Christ-LDS
     SAA  Christian: Salvation Army
     SEV  Christian: Seventh Day Adventist
     SOU  Christian: Southern Baptist
     UCC  Christian: United Church of Christ
     UMD  Christian: United Methodist
     UNI  Christian: Unitarian
     UNU  Christian: Unitarian Universalist
     WES  Christian: Wesleyan
     WMC  Christian: Wesleyan Methodist
     CNF  Confucian
     ERL  Ethnic Religionist
     HIN  Hindu
     HVA  Hindu: Vaishnavites
     HSH  Hindu: Shaivites
     HOT  Hindu: Other
     JAI  Jain
     JEW  Jewish
     JCO  Jewish: Conservative
     JOR  Jewish: Orthodox
     JOT  Jewish: Other
     JRC  Jewish: Reconstructionist
     JRF  Jewish: Reform
     JRN  Jewish: Renewal
     MOS  Muslim
     MSU  Muslim: Sunni
     MSH  Muslim: Shiite
     MOT  Muslim: Other
     NAM  Native American
     NRL  New Religionist
     NOE  Nonreligious
     OTH  Other
     SHN  Shintoist
     SIK  Sikh
     SPI  Spiritist
     VAR  Unknown
     """


     AGN = "AGN"
     ATH = "ATH"
     BAH = "BAH"
     BUD = "BUD"
     BMA = "BMA"
     BTH = "BTH"
     BTA = "BTA"
     BOT = "BOT"
     CFR = "CFR"
     CHR = "CHR"
     ABC = "ABC"
     AMT = "AMT"
     AME = "AME"
     ANG = "ANG"
     AOG = "AOG"
     BAP = "BAP"
     CAT = "CAT"
     CRR = "CRR"
     CHS = "CHS"
     CMA = "CMA"
     COC = "COC"
     COG = "COG"
     COI = "COI"
     COM = "COM"
     COL = "COL"
     EOT = "EOT"
     EVC = "EVC"
     EPI = "EPI"
     FWB = "FWB"
     FRQ = "FRQ"
     GRE = "GRE"
     JWN = "JWN"
     LUT = "LUT"
     LMS = "LMS"
     MEN = "MEN"
     MET = "MET"
     MOM = "MOM"
     NAZ = "NAZ"
     ORT = "ORT"
     COT = "COT"
     PRC = "PRC"
     PEN = "PEN"
     COP = "COP"
     PRE = "PRE"
     PRO = "PRO"
     QUA = "QUA"
     REC = "REC"
     REO = "REO"
     SAA = "SAA"
     SEV = "SEV"
     SOU = "SOU"
     UCC = "UCC"
     UMD = "UMD"
     UNI = "UNI"
     UNU = "UNU"
     WES = "WES"
     WMC = "WMC"
     CNF = "CNF"
     ERL = "ERL"
     HIN = "HIN"
     HVA = "HVA"
     HSH = "HSH"
     HOT = "HOT"
     JAI = "JAI"
     JEW = "JEW"
     JCO = "JCO"
     JOR = "JOR"
     JOT = "JOT"
     JRC = "JRC"
     JRF = "JRF"
     JRN = "JRN"
     MOS = "MOS"
     MSU = "MSU"
     MSH = "MSH"
     MOT = "MOT"
     NAM = "NAM"
     NRL = "NRL"
     NOE = "NOE"
     OTH = "OTH"
     SHN = "SHN"
     SIK = "SIK"
     SPI = "SPI"
     VAR = "VAR"


class Admissiontype(str, Enum):
     """
     007 - Admission type

     A  Accident
     E  Emergency
     L  Labor and Delivery
     R  Routine
     N  Newborn (Birth in healthcare facility)
     U  Urgent
     C  Elective
     """


     A = "A"
     E = "E"
     L = "L"
     R = "R"
     N = "N"
     U = "U"
     C = "C"


class Acknowledgmentcode(str, Enum):
     """
     008 - Acknowledgment code

     AA  Original mode: Application Accept - Enhanced mode: Application acknowledgment: Accept
     AE  Original mode: Application Error - Enhanced mode: Application acknowledgment: Error
     AR  Original mode: Application Reject - Enhanced mode: Application acknowledgment: Reject
     CA  Enhanced mode: Accept acknowledgment: Commit Accept
     CE  Enhanced mode: Accept acknowledgment: Commit Error
     CR  Enhanced mode: Accept acknowledgment: Commit Reject
     """


     AA = "AA"
     AE = "AE"
     AR = "AR"
     CA = "CA"
     CE = "CE"
     CR = "CR"


class Ambulatorystatus(str, Enum):
     """
     009 - Ambulatory status

     A0  No functional limitations
     A1  Ambulates with assistive device
     A2  Wheelchair/stretcher bound
     A3  Comatose; non-responsive
     A4  Disoriented
     A5  Vision impaired
     A6  Hearing impaired
     A7  Speech impaired
     A8  Non-English speaking
     A9  Functional level unknown
     B1  Oxygen therapy
     B2  Special equipment (tubes, IVs, catheters)
     B3  Amputee
     B4  Mastectomy
     B5  Paraplegic
     B6  Pregnant
     """


     A0 = "A0"
     A1 = "A1"
     A2 = "A2"
     A3 = "A3"
     A4 = "A4"
     A5 = "A5"
     A6 = "A6"
     A7 = "A7"
     A8 = "A8"
     A9 = "A9"
     B1 = "B1"
     B2 = "B2"
     B3 = "B3"
     B4 = "B4"
     B5 = "B5"
     B6 = "B6"


class Transactiontype(str, Enum):
     """
     017 - Transaction type

     CG  Charge
     CD  Credit
     PY  Payment
     AJ  Adjustment
     CO  Co-payment
     """


     CG = "CG"
     CD = "CD"
     PY = "PY"
     AJ = "AJ"
     CO = "CO"


class Admitsource(str, Enum):
     """
     023 - Admit source

     1  Physician referral
     2  Clinic referral
     3  HMO referral
     4  Transfer from a hospital
     5  Transfer from a skilled nursing facility
     6  Transfer from another health care facility
     7  Emergency room
     8  Court/law enforcement
     9  Information not available
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"
     _7 = "7"
     _8 = "8"
     _9 = "9"


class Priority(str, Enum):
     """
     027 - Priority

     S  Stat (do immediately)
     A  As soon as possible (a priority lower than stat)
     R  Routine
     P  Preoperative (to be done prior to surgery)
     T  Timing critical (do as near as possible to requested time)
     """


     S = "S"
     A = "A"
     R = "R"
     P = "P"
     T = "T"


class Orderstatus(str, Enum):
     """
     038 - Order status

     A  Some, but not all, results available
     CA  Order was canceled
     CM  Order is completed
     DC  Order was discontinued
     ER  Error, order not found
     HD  Order is on hold
     IP  In process, unspecified
     RP  Order has been replaced
     SC  In process, scheduled
     """


     A = "A"
     CA = "CA"
     CM = "CM"
     DC = "DC"
     ER = "ER"
     HD = "HD"
     IP = "IP"
     RP = "RP"
     SC = "SC"


class Conditioncode(str, Enum):
     """
     043 - Condition code

     01  Military service related
     02  Condition is employment related
     03  Patient covered by insurance not reflected here
     04  HMO enrollee
     05  Lien has been filed
     06  ESRD patient in first 18 months of entitlement covered by employer group health insurance
     07  Treatment of non-terminal condition for hospice patient
     08  Beneficiary would not provide information concerning other insurance coverage
     09  Neither patient nor spouse is employed
     10  Patient and/or spouse is employed but no EGHP exists
     11  Disabled beneficiary but no LGHP
     13  Payer codes.
     16  Payer codes.
     14  Payer codes.
     12 ... 16  Payer codes.
     12  Payer codes.
     15  Payer codes.
     18  Maiden name retained
     19  Child retains mother's name
     20  Beneficiary requested billing
     21  Billing for Denial Notice
     26  VA eligible patient chooses to receive services in a Medicare certified facility
     27  Patient referred to a sole community hospital for a diagnostic laboratory test
     28  Patient and/or spouse's EGHP is secondary to Medicare
     29  Disabled beneficiary and/or family member's LGHP is secondary to Medicare
     31  Patient is student (full time-day)
     32  Patient is student (cooperative/work study program)
     33  Patient is student (full time-night)
     34  Patient is student (Part time)
     36  General care patient in a special unit
     37  Ward accommodation as patient request
     38  Semi-private room not available
     39  Private room medically necessary
     40  Same day transfer
     41  Partial hospitalization
     46  Non-availability statement on file
     48  Psychiatric residential treatment centers for children and adolescents
     55  SNF bed not available
     56  Medical appropriateness
     57  SNF readmission
     60  Day outlier
     61  Cost outlier
     62  Payer code
     66  Provider does not wish cost outlier payment
     67  Beneficiary elects not to use life time reserve (LTR) days
     68  Beneficiary elects to use life time reserve (LTR) days
     70  Self-administered EPO
     71  Full care in unit
     72  Self-care in unit
     73  Self-care training
     74  Home
     75  Home - 100% reimbursement
     76  Back-up in facility dialysis
     77  Provider accepts or is obligated/required due to a contractual arrangement or law to accept payment by a primary payer as payment in full
     78  New coverage not implemented by HMO
     79  Corf services provided off-site
     80  Pregnant
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _07 = "07"
     _08 = "08"
     _09 = "09"
     _10 = "10"
     _11 = "11"
     _13 = "13"
     _16 = "16"
     _14 = "14"
     _12_____16 = "12 ... 16"
     _12 = "12"
     _15 = "15"
     _18 = "18"
     _19 = "19"
     _20 = "20"
     _21 = "21"
     _26 = "26"
     _27 = "27"
     _28 = "28"
     _29 = "29"
     _31 = "31"
     _32 = "32"
     _33 = "33"
     _34 = "34"
     _36 = "36"
     _37 = "37"
     _38 = "38"
     _39 = "39"
     _40 = "40"
     _41 = "41"
     _46 = "46"
     _48 = "48"
     _55 = "55"
     _56 = "56"
     _57 = "57"
     _60 = "60"
     _61 = "61"
     _62 = "62"
     _66 = "66"
     _67 = "67"
     _68 = "68"
     _70 = "70"
     _71 = "71"
     _72 = "72"
     _73 = "73"
     _74 = "74"
     _75 = "75"
     _76 = "76"
     _77 = "77"
     _78 = "78"
     _79 = "79"
     _80 = "80"


class Whatsubjectfilter(str, Enum):
     """
     048 - What subject filter

     ADV  Advice/diagnosis
     ANU  Nursing unit lookup (returns patients in beds, excluding empty beds)
     APN  Patient name lookup
     APP  Physician lookup
     ARN  Nursing unit lookup (returns patients in beds, including empty beds)
     APM  Medical record number query, returns visits for a medical record number
     APA  Account number query, return matching visit
     CAN  Cancel.  Used to cancel a query
     DEM  Demographics
     FIN  Financial
     GID  Generate new identifier
     GOL  Goals
     MRI  Most recent inpatient
     MRO  Most recent outpatient
     NCK  Network clock
     NSC  Network status change
     NST  Network statistic
     ORD  Order
     OTH  Other
     PRB  Problems
     PRO  Procedure
     RES  Result
     RAR  Pharmacy administration information
     RER  Pharmacy encoded order information
     RDR  Pharmacy dispense information
     RGR  Pharmacy give information
     ROR  Pharmacy prescription information
     SAL  All schedule related information, including open slots, booked slots, blocked slots
     SBK  Booked slots on the identified schedule
     SBL  Blocked slots on the identified schedule
     SOP  Open slots on the identified schedule
     SSA  Time slots available for a single appointment
     SSR  Time slots available for a recurring appointment
     STA  Status
     VXI  Vaccine Information
     XID  Get cross-referenced identifiers
     SOF  First open slot on the identified schedule after the start date/time
     """


     ADV = "ADV"
     ANU = "ANU"
     APN = "APN"
     APP = "APP"
     ARN = "ARN"
     APM = "APM"
     APA = "APA"
     CAN = "CAN"
     DEM = "DEM"
     FIN = "FIN"
     GID = "GID"
     GOL = "GOL"
     MRI = "MRI"
     MRO = "MRO"
     NCK = "NCK"
     NSC = "NSC"
     NST = "NST"
     ORD = "ORD"
     OTH = "OTH"
     PRB = "PRB"
     PRO = "PRO"
     RES = "RES"
     RAR = "RAR"
     RER = "RER"
     RDR = "RDR"
     RGR = "RGR"
     ROR = "ROR"
     SAL = "SAL"
     SBK = "SBK"
     SBL = "SBL"
     SOP = "SOP"
     SSA = "SSA"
     SSR = "SSR"
     STA = "STA"
     VXI = "VXI"
     XID = "XID"
     SOF = "SOF"


class Diagnosistype(str, Enum):
     """
     052 - Diagnosis type

     A  Admitting
     W  Working
     F  Final
     """


     A = "A"
     W = "W"
     F = "F"


class Checkdigitscheme(str, Enum):
     """
     061 - Check digit scheme

     NPI  Check digit algorithm in the US National Provider Identifier
     ISO  ISO 7064: 1983
     M10  Mod 10 algorithm
     M11  Mod 11 algorithm
     """


     NPI = "NPI"
     ISO = "ISO"
     M10 = "M10"
     M11 = "M11"


class Eventreason(str, Enum):
     """
     062 - Event reason

     01  Patient request
     02  Physician/health practitioner order
     03  Census management
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"


class Relationship(str, Enum):
     """
     063 - Relationship

     SEL  Self
     SPO  Spouse
     DOM  Life partner
     CHD  Child
     GCH  Grandchild
     NCH  Natural child
     SCH  Stepchild
     FCH  Foster child
     DEP  Handicapped dependent
     WRD  Ward of court
     PAR  Parent
     MTH  Mother
     FTH  Father
     CGV  Care giver
     GRD  Guardian
     GRP  Grandparent
     EXF  Extended family
     SIB  Sibling
     BRO  Brother
     SIS  Sister
     FND  Friend
     OAD  Other adult
     EME  Employee
     EMR  Employer
     ASC  Associate
     EMC  Emergency contact
     OWN  Owner
     TRA  Trainer
     MGR  Manager
     NON  None
     UNK  Unknown
     OTH  Other
     """


     SEL = "SEL"
     SPO = "SPO"
     DOM = "DOM"
     CHD = "CHD"
     GCH = "GCH"
     NCH = "NCH"
     SCH = "SCH"
     FCH = "FCH"
     DEP = "DEP"
     WRD = "WRD"
     PAR = "PAR"
     MTH = "MTH"
     FTH = "FTH"
     CGV = "CGV"
     GRD = "GRD"
     GRP = "GRP"
     EXF = "EXF"
     SIB = "SIB"
     BRO = "BRO"
     SIS = "SIS"
     FND = "FND"
     OAD = "OAD"
     EME = "EME"
     EMR = "EMR"
     ASC = "ASC"
     EMC = "EMC"
     OWN = "OWN"
     TRA = "TRA"
     MGR = "MGR"
     NON = "NON"
     UNK = "UNK"
     OTH = "OTH"


class Specimenactioncode(str, Enum):
     """
     065 - Specimen action code

     A  Add ordered tests to the existing specimen
     G  Generated order; reflex order
     L  Lab to obtain specimen from patient
     O  Specimen obtained by service other than Lab
     P  Pending specimen; Order sent prior to delivery
     R  Revised order
     S  Schedule the tests specified below
     """


     A = "A"
     G = "G"
     L = "L"
     O = "O"
     P = "P"
     R = "R"
     S = "S"


class Employmentstatus(str, Enum):
     """
     066 - Employment status

     F  Full Time
     1  Full time employed
     P  Part Time
     2  Part time employed
     D  Per Diem
     4  Self-employed,
     C  Contract, per diem
     L  Leave of absence (e.g. Family leave, sabbatical, etc.)
     T  Temporarily unemployed
     3  Unemployed
     5  Retired
     6  On active military duty
     O  Other
     9  Unknown
     """


     F = "F"
     _1 = "1"
     P = "P"
     _2 = "2"
     D = "D"
     _4 = "4"
     C = "C"
     L = "L"
     T = "T"
     _3 = "3"
     _5 = "5"
     _6 = "6"
     O = "O"
     _9 = "9"


class Hospitalservice(str, Enum):
     """
     069 - Hospital service

     MED  Medical Service
     SUR  Surgical Service
     URO  Urology Service
     PUL  Pulmonary Service
     CAR  Cardiac Service
     """


     MED = "MED"
     SUR = "SUR"
     URO = "URO"
     PUL = "PUL"
     CAR = "CAR"


class Specimensourcecodes(str, Enum):
     """
     070 - Specimen source codes

     ABS  Abscess
     AMN  Amniotic fluid
     ASP  Aspirate
     BPH  Basophils
     BIFL  Bile fluid
     BLDA  Blood  arterial
     BBL  Blood bag
     BLDC  Blood  capillary
     BPU  Blood product unit
     BLDV  Blood  venous
     BON  Bone
     BRTH  Breath (use EXHLD)
     BRO  Bronchial
     BRN  Burn
     CALC  Calculus (=Stone)
     CDM  Cardiac muscle
     CNL  Cannula
     CTP  Catheter tip
     CSF  Cerebral spinal fluid
     CVM  Cervical mucus
     CVX  Cervix
     COL  Colostrum
     BLDCO  Cord blood
     CBLD  Cord blood
     CNJT  Conjunctiva
     CUR  Curettage
     CYST  Cyst
     DIAF  Dialysis fluid
     DOSE  Dose med or substance
     DRN  Drain
     DUFL  Duodenal fluid
     EAR  Ear
     EARW  Ear wax (cerumen)
     ELT  Electrode
     ENDC  Endocardium
     ENDM  Endometrium
     EOS  Eosinophils
     RBC  Erythrocytes
     EYE  Eye
     EXHLD  Exhaled gas (=breath)
     EXG  Exhaled gas (=breath)
     FIB  Fibroblasts
     FLT  Filter
     FIST  Fistula
     FLU  Body fluid, unsp
     GAS  Gas
     GAST  Gastric fluid/contents
     GEN  Genital
     GENC  Genital cervix
     GENL  Genital lochia
     GENV  Genital vaginal
     HAR  Hair
     IHG  Inhaled Gas
     IT  Intubation tube
     ISLT  Isolate
     LAM  Lamella
     WBC  Leukocytes
     LN  Line
     LNA  Line arterial
     LNV  Line venous
     LIQ  Liquid NOS
     LYM  Lymphocytes
     MAC  Macrophages
     MAR  Marrow
     MEC  Meconium
     MBLD  Menstrual blood
     MLK  Milk
     MILK  Breast milk
     NAIL  Nail
     NOS  Nose (nasal passage)
     ORH  Other
     PAFL  Pancreatic fluid
     PAT  Patient
     PRT  Peritoneal fluid /ascites
     PLC  Placenta
     PLAS  Plasma
     PLB  Plasma bag
     PLR  Pleural fluid (thoracentesis fld)
     PMN  Polymorphonuclear neutrophils
     PPP  Platelet poor plasma
     PRP  Platelet rich plasma
     PUS  Pus
     RT  Route of medicine
     SAL  Saliva
     SMN  Seminal fluid
     SEM  Seminal fluid
     SER  Serum
     SKN  Skin
     SKM  Skeletal muscle
     SPRM  Spermatozoa
     SPT  Sputum
     SPTC  Sputum - coughed
     SPTT  Sputum - tracheal aspirate
     STON  Stone (use CALC)
     STL  Stool = Fecal
     SWT  Sweat
     SNV  Synovial fluid (Joint fluid)
     TEAR  Tears
     THRT  Throat
     THRB  Thrombocyte (platelet)
     TISS  Tissue
     TISG  Tissue gall bladder
     TLGI  Tissue large intestine
     TLNG  Tissue lung
     TISPL  Tissue placenta
     TSMI  Tissue small intestine
     TISU  Tissue ulcer
     TUB  Tube NOS
     ULC  Ulcer
     UMB  Umbilical blood
     UMED  Unknown medicine
     URTH  Urethra
     UR  Urine
     URC  Urine clean catch
     URT  Urine catheter
     URNS  Urine sediment
     USUB  Unknown substance
     VOM  Vomitus
     VITF  Vitreous Fluid
     BLD  Whole blood
     BDY  Whole body
     WAT  Water
     WICK  Wick
     WND  Wound
     WNDA  Wound abscess
     WNDE  Wound exudate
     WNDD  Wound drainage
     XXX  To be specified in another part of the message
     """


     ABS = "ABS"
     AMN = "AMN"
     ASP = "ASP"
     BPH = "BPH"
     BIFL = "BIFL"
     BLDA = "BLDA"
     BBL = "BBL"
     BLDC = "BLDC"
     BPU = "BPU"
     BLDV = "BLDV"
     BON = "BON"
     BRTH = "BRTH"
     BRO = "BRO"
     BRN = "BRN"
     CALC = "CALC"
     CDM = "CDM"
     CNL = "CNL"
     CTP = "CTP"
     CSF = "CSF"
     CVM = "CVM"
     CVX = "CVX"
     COL = "COL"
     BLDCO = "BLDCO"
     CBLD = "CBLD"
     CNJT = "CNJT"
     CUR = "CUR"
     CYST = "CYST"
     DIAF = "DIAF"
     DOSE = "DOSE"
     DRN = "DRN"
     DUFL = "DUFL"
     EAR = "EAR"
     EARW = "EARW"
     ELT = "ELT"
     ENDC = "ENDC"
     ENDM = "ENDM"
     EOS = "EOS"
     RBC = "RBC"
     EYE = "EYE"
     EXHLD = "EXHLD"
     EXG = "EXG"
     FIB = "FIB"
     FLT = "FLT"
     FIST = "FIST"
     FLU = "FLU"
     GAS = "GAS"
     GAST = "GAST"
     GEN = "GEN"
     GENC = "GENC"
     GENL = "GENL"
     GENV = "GENV"
     HAR = "HAR"
     IHG = "IHG"
     IT = "IT"
     ISLT = "ISLT"
     LAM = "LAM"
     WBC = "WBC"
     LN = "LN"
     LNA = "LNA"
     LNV = "LNV"
     LIQ = "LIQ"
     LYM = "LYM"
     MAC = "MAC"
     MAR = "MAR"
     MEC = "MEC"
     MBLD = "MBLD"
     MLK = "MLK"
     MILK = "MILK"
     NAIL = "NAIL"
     NOS = "NOS"
     ORH = "ORH"
     PAFL = "PAFL"
     PAT = "PAT"
     PRT = "PRT"
     PLC = "PLC"
     PLAS = "PLAS"
     PLB = "PLB"
     PLR = "PLR"
     PMN = "PMN"
     PPP = "PPP"
     PRP = "PRP"
     PUS = "PUS"
     RT = "RT"
     SAL = "SAL"
     SMN = "SMN"
     SEM = "SEM"
     SER = "SER"
     SKN = "SKN"
     SKM = "SKM"
     SPRM = "SPRM"
     SPT = "SPT"
     SPTC = "SPTC"
     SPTT = "SPTT"
     STON = "STON"
     STL = "STL"
     SWT = "SWT"
     SNV = "SNV"
     TEAR = "TEAR"
     THRT = "THRT"
     THRB = "THRB"
     TISS = "TISS"
     TISG = "TISG"
     TLGI = "TLGI"
     TLNG = "TLNG"
     TISPL = "TISPL"
     TSMI = "TSMI"
     TISU = "TISU"
     TUB = "TUB"
     ULC = "ULC"
     UMB = "UMB"
     UMED = "UMED"
     URTH = "URTH"
     UR = "UR"
     URC = "URC"
     URT = "URT"
     URNS = "URNS"
     USUB = "USUB"
     VOM = "VOM"
     VITF = "VITF"
     BLD = "BLD"
     BDY = "BDY"
     WAT = "WAT"
     WICK = "WICK"
     WND = "WND"
     WNDA = "WNDA"
     WNDE = "WNDE"
     WNDD = "WNDD"
     XXX = "XXX"


class DiagnosticservicesectionID(str, Enum):
     """
     074 - Diagnostic service section ID

     AU  Audiology
     BG  Blood Gases
     BLB  Blood Bank
     CUS  Cardiac Ultrasound
     CTH  Cardiac Catheterization
     CT  CAT Scan
     CH  Chemistry
     CP  Cytopathology
     EC  Electrocardiac (e.g., EKG,  EEC, Holter)
     EN  Electroneuro (EEG, EMG,EP,PSG)
     HM  Hematology
     ICU  Bedside ICU Monitoring
     IMG  Diagnostic Imaging
     IMM  Immunology
     LAB  Laboratory
     MB  Microbiology
     MCB  Mycobacteriology
     MYC  Mycology
     NMS  Nuclear Medicine Scan
     NMR  Nuclear Magnetic Resonance
     NRS  Nursing Service Measures
     OUS  OB Ultrasound
     OT  Occupational Therapy
     OTH  Other
     OSL  Outside Lab
     PHR  Pharmacy
     PAR  Parasitology
     PAT  Pathology (gross & histopath, not surgical)
     PT  Physical Therapy
     PHY  Physician (Hx. Dx, admission note, etc.)
     PF  Pulmonary function
     RAD  Radiology
     RX  Radiograph
     RUS  Radiology ultrasound
     RC  Respiratory Care (therapy)
     RT  Radiation therapy
     SR  Serology
     SP  Surgical Pathology
     TX  Toxicology
     URN  Urinalysis
     VUS  Vascular Ultrasound
     VR  Virology
     XRC  Cineradiograph
     """


     AU = "AU"
     BG = "BG"
     BLB = "BLB"
     CUS = "CUS"
     CTH = "CTH"
     CT = "CT"
     CH = "CH"
     CP = "CP"
     EC = "EC"
     EN = "EN"
     HM = "HM"
     ICU = "ICU"
     IMG = "IMG"
     IMM = "IMM"
     LAB = "LAB"
     MB = "MB"
     MCB = "MCB"
     MYC = "MYC"
     NMS = "NMS"
     NMR = "NMR"
     NRS = "NRS"
     OUS = "OUS"
     OT = "OT"
     OTH = "OTH"
     OSL = "OSL"
     PHR = "PHR"
     PAR = "PAR"
     PAT = "PAT"
     PT = "PT"
     PHY = "PHY"
     PF = "PF"
     RAD = "RAD"
     RX = "RX"
     RUS = "RUS"
     RC = "RC"
     RT = "RT"
     SR = "SR"
     SP = "SP"
     TX = "TX"
     URN = "URN"
     VUS = "VUS"
     VR = "VR"
     XRC = "XRC"


class Messagetype(str, Enum):
     """
     076 - Message type

     ACK  General acknowledgment message
     ADR  ADT response
     ADT  ADT message
     BAR  Add/change billing account
     CRM  Clinical study registration message
     CSU  Unsolicited study data message
     DFT  Detail financial transactions
     DOC  Document response
     DSR  Display response
     EAC  Automated equipment command message
     EAN  Automated equipment notification message
     EAR  Automated equipment response message
     EDR  Enhanced display response
     EQQ  Embedded query language query
     ERP  Event replay response
     ESR  Automated equipment status update acknowledgement message
     ESU  Automated equipment status update message
     INR  Automated equipment inventory request message
     INU  Automated equipment inventory update message
     LSR  Automated equipment log/service request message
     LSU  Automated equipment log/service update message
     MCF  Delayed Acknowledgement (Retained for backward compatibility only)
     MDM  Medical document management
     MFD  Master files delayed application acknowledgment
     MFK  Master files application acknowledgment
     MFN  Master files notification
     MFQ  Master files query
     MFR  Master files response
     NMD  Application management data message
     NMQ  Application management query message
     NMR  Application management response message
     OMD  Dietary order
     OMG  General clinical order message
     OML  Laboratory order message
     OMN  Non-stock requisition order message
     OMP  Pharmacy/treatment order message
     OMS  Stock requisition order message
     ORD  Dietary order - General order acknowledgment message
     ORF  Query for results of observation
     ORG  General clinical order acknowledgement message
     ORL  Laboratory acknowledgement message (unsolicited)
     ORM  Pharmacy/treatment order message
     ORN  Non-stock requisition - General order acknowledgment message
     ORP  Pharmacy/treatment order acknowledgement message
     ORR  General order response message response to any ORM
     ORS  Stock requisition - General order acknowledgment message
     ORU  Unsolicited transmission of an observation message
     OSQ  Query response for order status
     OSR  Query response for order status
     OUL  Unsolicited laboratory observation message
     PEX  Product experience message
     PGL  Patient goal message
     PIN  Patient insurance information
     PMU  Add personnel record
     PPG  Patient pathway message (goal-oriented)
     PPP  Patient pathway message (problem-oriented)
     PPR  Patient problem message
     PPT  Patient pathway goal-oriented response
     PPV  Patient goal response
     PRR  Patient problem response
     PTR  Patient pathway problem-oriented response
     QBP  Query by parameter
     QCK  Deferred query
     QCN  Cancel query
     QRY  Query, original mode
     QSB  Create subscription
     QSX  Cancel subscription/acknowledge message
     QVR  Query for previous events
     ROR  Pharmacy/treatment order response
     RAR  Pharmacy/treatment administration information
     RAS  Pharmacy/treatment administration message
     RCI  Return clinical information
     RCL  Return clinical list
     RDE  Pharmacy/treatment encoded order message
     RDR  Pharmacy/treatment dispense information
     RDS  Pharmacy/treatment dispense message
     RDY  Display based response
     REF  Patient referral
     RER  Pharmacy/treatment encoded order information
     RGR  Pharmacy/treatment dose information
     RGV  Pharmacy/treatment give message
     RPA  Return patient authorization
     RPI  Return patient information
     RPL  Return patient display list
     RPR  Return patient list
     RQA  Request patient authorization
     RQC  Request clinical information
     RQI  Request patient information
     RQP  Request patient demographics
     RQQ  Event replay query
     RRA  Pharmacy/treatment administration acknowledgement message
     RRD  Pharmacy/treatment dispense acknowledgment message
     RRE  Pharmacy/treatment encoded order acknowledgment message
     RRG  Pharmacy/treatment give acknowledgment message
     RRI  Return referral information
     RSP  Segment pattern response
     RTB  Tabular response
     SIU  Schedule information unsolicited
     SPQ  Stored procedure request
     SQM  Schedule query message
     SQR  Schedule query response
     SRM  Schedule request message
     SRR  Scheduled request response
     SSR  Specimen status request message
     SSU  Specimen status update message
     SUR  Summary product experience report
     TBR  Tabular data response
     TCR  Automated equipment test code settings request message
     TCU  Automated equipment test code settings update message
     UDM  Unsolicited display update message
     VQQ  Virtual table query
     VXQ  Query for vaccination record
     VXR  Vaccination record response
     VXU  Unsolicited vaccination record update
     VXX  Response for vaccination query with multiple PID matches
     """


     ACK = "ACK"
     ADR = "ADR"
     ADT = "ADT"
     BAR = "BAR"
     CRM = "CRM"
     CSU = "CSU"
     DFT = "DFT"
     DOC = "DOC"
     DSR = "DSR"
     EAC = "EAC"
     EAN = "EAN"
     EAR = "EAR"
     EDR = "EDR"
     EQQ = "EQQ"
     ERP = "ERP"
     ESR = "ESR"
     ESU = "ESU"
     INR = "INR"
     INU = "INU"
     LSR = "LSR"
     LSU = "LSU"
     MCF = "MCF"
     MDM = "MDM"
     MFD = "MFD"
     MFK = "MFK"
     MFN = "MFN"
     MFQ = "MFQ"
     MFR = "MFR"
     NMD = "NMD"
     NMQ = "NMQ"
     NMR = "NMR"
     OMD = "OMD"
     OMG = "OMG"
     OML = "OML"
     OMN = "OMN"
     OMP = "OMP"
     OMS = "OMS"
     ORD = "ORD"
     ORF = "ORF"
     ORG = "ORG"
     ORL = "ORL"
     ORM = "ORM"
     ORN = "ORN"
     ORP = "ORP"
     ORR = "ORR"
     ORS = "ORS"
     ORU = "ORU"
     OSQ = "OSQ"
     OSR = "OSR"
     OUL = "OUL"
     PEX = "PEX"
     PGL = "PGL"
     PIN = "PIN"
     PMU = "PMU"
     PPG = "PPG"
     PPP = "PPP"
     PPR = "PPR"
     PPT = "PPT"
     PPV = "PPV"
     PRR = "PRR"
     PTR = "PTR"
     QBP = "QBP"
     QCK = "QCK"
     QCN = "QCN"
     QRY = "QRY"
     QSB = "QSB"
     QSX = "QSX"
     QVR = "QVR"
     ROR = "ROR"
     RAR = "RAR"
     RAS = "RAS"
     RCI = "RCI"
     RCL = "RCL"
     RDE = "RDE"
     RDR = "RDR"
     RDS = "RDS"
     RDY = "RDY"
     REF = "REF"
     RER = "RER"
     RGR = "RGR"
     RGV = "RGV"
     RPA = "RPA"
     RPI = "RPI"
     RPL = "RPL"
     RPR = "RPR"
     RQA = "RQA"
     RQC = "RQC"
     RQI = "RQI"
     RQP = "RQP"
     RQQ = "RQQ"
     RRA = "RRA"
     RRD = "RRD"
     RRE = "RRE"
     RRG = "RRG"
     RRI = "RRI"
     RSP = "RSP"
     RTB = "RTB"
     SIU = "SIU"
     SPQ = "SPQ"
     SQM = "SQM"
     SQR = "SQR"
     SRM = "SRM"
     SRR = "SRR"
     SSR = "SSR"
     SSU = "SSU"
     SUR = "SUR"
     TBR = "TBR"
     TCR = "TCR"
     TCU = "TCU"
     UDM = "UDM"
     VQQ = "VQQ"
     VXQ = "VXQ"
     VXR = "VXR"
     VXU = "VXU"
     VXX = "VXX"


class Abnormalflags(str, Enum):
     """
     078 - Abnormal flags

     L  Below low normal
     H  Above high normal
     LL  Below lower panic limits
     HH  Above upper panic limits
     <  Below absolute low-off instrument scale
     >  Above absolute high-off instrument scale
     N  Normal (applies to non-numeric results)
     A  Abnormal (applies to non-numeric results)
     AA  Very abnormal (applies to non-numeric units, analogous to panic limits for numeric units)
     null  No range defined, or normal ranges don't apply
     U  Significant change up
     D  Significant change down
     B  Better--use when direction not relevant
     W  Worse--use when direction not relevant
     S  Susceptible*
     R  Resistant*
     I  Intermediate*
     MS  Moderately susceptible*
     VS  Very susceptible*
     """


     L = "L"
     H = "H"
     LL = "LL"
     HH = "HH"
     _ = "<"
     _ = ">"
     N = "N"
     A = "A"
     AA = "AA"
     null = "null"
     U = "U"
     D = "D"
     B = "B"
     W = "W"
     S = "S"
     R = "R"
     I = "I"
     MS = "MS"
     VS = "VS"


class Natureofabnormaltesting(str, Enum):
     """
     080 - Nature of abnormal testing

     A  An age-based population
     N  None - generic normal range
     R  A race-based population
     S  A sex-based population
     """


     A = "A"
     N = "N"
     R = "R"
     S = "S"


class Outliertype(str, Enum):
     """
     083 - Outlier type

     D  Outlier days
     C  Outlier cost
     """


     D = "D"
     C = "C"


class Observationresultstatuscodesinterpretation(str, Enum):
     """
     085 - Observation result status codes interpretation

     C  Record coming over is a correction and thus replaces a final result
     D  Deletes the OBX record
     F  Final results; Can only be changed with a corrected result.
     I  Specimen in lab; results pending
     N  Not asked; used to affirmatively document that the observation identified in the OBX was not sought when the universal service ID in OBR-4 implies that it would be sought.
     O  Order detail description only (no result)
     P  Preliminary results
     R  Results entered -- not verified
     S  Partial results
     X  Results cannot be obtained for this observation
     U  Results status change to final without retransmitting results already sent as 'preliminary.'  E.g., radiology changes status from preliminary to final
     W  Post original as wrong, e.g., transmitted for wrong patient
     """


     C = "C"
     D = "D"
     F = "F"
     I = "I"
     N = "N"
     O = "O"
     P = "P"
     R = "R"
     S = "S"
     X = "X"
     U = "U"
     W = "W"


class Querypriority(str, Enum):
     """
     091 - Query priority

     D  Deferred
     I  Immediate
     """


     D = "D"
     I = "I"


class Re_admissionindicator(str, Enum):
     """
     092 - Re-admission indicator

     R  Re-admission
     """


     R = "R"


class Releaseinformation(str, Enum):
     """
     093 - Release information

     Y  Yes
     N  No
1312
     """


     Y = "Y"
     N = "N"


class Typeofagreement(str, Enum):
     """
     098 - Type of agreement

     S  Standard
     U  Unified
     M  Maternity
     """


     S = "S"
     U = "U"
     M = "M"


class Whentocharge(str, Enum):
     """
     100 - When to charge

     D  On discharge
     O  On receipt of order
     R  At time service is completed
     S  At time service is started
     T  At a designated date/time
     """


     D = "D"
     O = "O"
     R = "R"
     S = "S"
     T = "T"


class Delayedacknowledgmenttype(str, Enum):
     """
     102 - Delayed acknowledgment type

     D  Message received, stored for later processing
     F  acknowledgment after processing
     """


     D = "D"
     F = "F"


class ProcessingID(str, Enum):
     """
     103 - Processing ID

     D  Debugging
     P  Production
     T  Training
     """


     D = "D"
     P = "P"
     T = "T"


class VersionID(str, Enum):
     """
     104 - Version ID

     2.0  Release 2.0
     2.0D  Demo 2.0
     2.1  Release 2. 1
     2.2  Release 2.2
     2.3  Release 2.3
     2.3.1  Release 2.3.1
     2.4  Release 2.4
     """


     _2_0 = "2.0"
     _2_0D = "2.0D"
     _2_1 = "2.1"
     _2_2 = "2.2"
     _2_3 = "2.3"
     _2_3_1 = "2.3.1"
     _2_4 = "2.4"


class Sourceofcomment(str, Enum):
     """
     105 - Source of comment

     L  Ancillary (filler) department is source of comment
     P  Orderer (placer) is source of comment
     O  Other system is source of comment
     """


     L = "L"
     P = "P"
     O = "O"


class Query_responseformatcode(str, Enum):
     """
     106 - Query-response format code

     D  Response is in display format
     R  Response is in record-oriented format
     T  Response is in tabular format
     """


     D = "D"
     R = "R"
     T = "T"


class Deferredresponsetype(str, Enum):
     """
     107 - Deferred response type

     B  Before the Date/Time specified
     L  Later than the Date/Time specified
     """


     B = "B"
     L = "L"


class Queryresultslevel(str, Enum):
     """
     108 - Query results level

     O  Order plus order status
     R  Results without bulk text
     S  Status only
     T  Full results
     """


     O = "O"
     R = "R"
     S = "S"
     T = "T"


class Reportpriority(str, Enum):
     """
     109 - Report priority

     R  Routine
     S  Stat
     """


     R = "R"
     S = "S"


class Dischargedisposition(str, Enum):
     """
     112 - Discharge disposition

     16  
     25  Expired to be defined at state level, if necessary
     24  Expired to be defined at state level, if necessary
     23  Expired to be defined at state level, if necessary
     21  Expired to be defined at state level, if necessary
     19  
     26  Expired to be defined at state level, if necessary
     17  
     22  Expired to be defined at state level, if necessary
     15  
     14  
     13  
     12  
     11  
     10  
     18  
     36  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     39  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     37  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     27  Expired to be defined at state level, if necessary
     35  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     34  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     33  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     32  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     28  Expired to be defined at state level, if necessary
     38  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     31  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     29  Expired to be defined at state level, if necessary
     01  Discharged to home or self care (routine discharge)
     02  Discharged/transferred to another short term general hospital for inpatient care
     03  Discharged/transferred to skilled nursing facility (SNF)
     04  Discharged/transferred to an intermediate care facility (ICF)
     05  Discharged/transferred to another type of institution for inpatient care or referred for outpatient services to another institution
     06  Discharged/transferred to home under care of organized home health service organization
     07  Left against medical advice or discontinued care
     08  Discharged/transferred to home under care of Home IV provider
     09  Admitted as an inpatient to this hospital
     10  19  Discharge to be defined at state level, if necessary
     20  Expired (i.e. dead)
     21 ... 29  Expired to be defined at state level, if necessary
     30  Still patient or expected to return for outpatient services (i.e. still a patient)
     31 ... 39  Still patient to be defined at state level, if necessary  (i.e. still a patient)
     40  Expired (i.e. died) at home
     41  Expired (i.e. died) in a medical facility; e.g., hospital, SNF, ICF, or free standing hospice
     42  Expired (i.e. died)  - place unknown
     """


     _16 = "16"
     _25 = "25"
     _24 = "24"
     _23 = "23"
     _21 = "21"
     _19 = "19"
     _26 = "26"
     _17 = "17"
     _22 = "22"
     _15 = "15"
     _14 = "14"
     _13 = "13"
     _12 = "12"
     _11 = "11"
     _10 = "10"
     _18 = "18"
     _36 = "36"
     _39 = "39"
     _37 = "37"
     _27 = "27"
     _35 = "35"
     _34 = "34"
     _33 = "33"
     _32 = "32"
     _28 = "28"
     _38 = "38"
     _31 = "31"
     _29 = "29"
     _01 = "01"
     _02 = "02"
     _03 = "03"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _07 = "07"
     _08 = "08"
     _09 = "09"
     _10_NEL_19 = "10  19"
     _20 = "20"
     _21_____29 = "21 ... 29"
     _30 = "30"
     _31_____39 = "31 ... 39"
     _40 = "40"
     _41 = "41"
     _42 = "42"


class Bedstatus(str, Enum):
     """
     116 - Bed status

     C  Closed
     H  Housekeeping
     O  Occupied
     U  Unoccupied
     K  Contaminated
     I  Isolated
     """


     C = "C"
     H = "H"
     O = "O"
     U = "U"
     K = "K"
     I = "I"


class OrderControlcodes(str, Enum):
     """
     119 - Order Control codes

     NW  New order/service
     OK  Order/service accepted & OK
     UA  Unable to accept order/service
     PR  Previous Results with new order/service
     CA  Cancel order/service request
     OC  Order/service canceled
     CR  Canceled as requested
     UC  Unable to cancel
     DC  Discontinue order/service request
     OD  Order/service discontinued
     DR  Discontinued as requested
     UD  Unable to discontinue
     HD  Hold order request
     OH  Order/service held
     UH  Unable to put on hold
     HR  On hold as requested
     RL  Release previous hold
     OE  Order/service released
     OR  Released as requested
     UR  Unable to release
     RP  Order/service replace request
     RU  Replaced unsolicited
     RO  Replacement order
     RQ  Replaced as requested
     UM  Unable to replace
     PA  Parent order/service
     CH  Child order/service
     XO  Change order/service request
     XX  Order/service changed, unsol.
     UX  Unable to change
     XR  Changed as requested
     DE  Data errors
     RE  Observations/Performed Service to follow
     RR  Request received
     SR  Response to send order/service status request
     SS  Send order/service status request
     SC  Status changed
     SN  Send order/service number
     NA  Number assigned
     CN  Combined result
     RF  Refill order/service request
     AF  Order/service refill request approval
     DF  Order/service refill request denied
     FU  "Order/service refilled, unsolicited"
     OF  Order/service refilled as requested
     UF  Unable to refill
     LI  Link order/service to patient care problem or goal
     UN  Unlink order/service from patient care problem or goal
     """


     NW = "NW"
     OK = "OK"
     UA = "UA"
     PR = "PR"
     CA = "CA"
     OC = "OC"
     CR = "CR"
     UC = "UC"
     DC = "DC"
     OD = "OD"
     DR = "DR"
     UD = "UD"
     HD = "HD"
     OH = "OH"
     UH = "UH"
     HR = "HR"
     RL = "RL"
     OE = "OE"
     OR = "OR"
     UR = "UR"
     RP = "RP"
     RU = "RU"
     RO = "RO"
     RQ = "RQ"
     UM = "UM"
     PA = "PA"
     CH = "CH"
     XO = "XO"
     XX = "XX"
     UX = "UX"
     XR = "XR"
     DE = "DE"
     RE = "RE"
     RR = "RR"
     SR = "SR"
     SS = "SS"
     SC = "SC"
     SN = "SN"
     NA = "NA"
     CN = "CN"
     RF = "RF"
     AF = "AF"
     DF = "DF"
     FU = "FU"
     OF = "OF"
     UF = "UF"
     LI = "LI"
     UN = "UN"


class Responseflag(str, Enum):
     """
     121 - Response flag

     E  Report exceptions only
     R  Same as E, also Replacement and Parent-Child
     D  Same as R, also other associated segments
     F  Same as D, plus confirmations explicitly
     N  Only the MSA segment is returned
     """


     E = "E"
     R = "R"
     D = "D"
     F = "F"
     N = "N"


class Chargetype(str, Enum):
     """
     122 - Charge type

     CH  Charge
     CO  Contract
     CR  Credit
     DP  Department
     GR  Grant
     NC  No Charge
     PC  Professional
     RS  Research
     """


     CH = "CH"
     CO = "CO"
     CR = "CR"
     DP = "DP"
     GR = "GR"
     NC = "NC"
     PC = "PC"
     RS = "RS"


class Resultstatus(str, Enum):
     """
     123 - Result status

     O  Order received; specimen not yet received
     I  No results available; specimen received, procedure incomplete
     S  No results available; procedure scheduled, but not done
     A  Some, but not all, results available
     P  Preliminary: A verified early result is available, final results not yet obtained
     C  Correction to results
     R  Results stored; not yet verified
     F  Final results; results stored and verified.  Can only be changed with a corrected result.
     X  No results available; Order canceled.
     Y  No order on record for this test.  (Used only on queries)
     Z  No record of this patient. (Used only on queries)
     """


     O = "O"
     I = "I"
     S = "S"
     A = "A"
     P = "P"
     C = "C"
     R = "R"
     F = "F"
     X = "X"
     Y = "Y"
     Z = "Z"


class Transportationmode(str, Enum):
     """
     124 - Transportation mode

     CART  Cart - patient travels on cart or gurney
     PORT  The examining device goes to patient's location
     WALK  Patient walks to diagnostic service
     WHLC  Wheelchair
     """


     CART = "CART"
     PORT = "PORT"
     WALK = "WALK"
     WHLC = "WHLC"


class Valuetype(str, Enum):
     """
     125 - Value type

     AD  Address
     CE  Coded Entry
     CF  Coded Element With Formatted Values
     CK  Composite ID With Check Digit
     CN  Composite ID And Name
     CP  Composite Price
     CX  Extended Composite ID With Check Digit
     DT  Date
     ED  Encapsulated Data
     FT  Formatted Text (Display)
     MO  Money
     NM  Numeric
     PN  Person Name
     RP  Reference Pointer
     SN  Structured Numeric
     ST  String Data.
     TM  Time
     TN  Telephone Number
     TS  Time Stamp (Date & Time)
     TX  Text Data (Display)
     XAD  Extended Address
     XCN  Extended Composite Name And Number For Persons
     XON  Extended Composite Name And Number For Organizations
     XPN  Extended Person Name
     XTN  Extended Telecommunications Number
     """


     AD = "AD"
     CE = "CE"
     CF = "CF"
     CK = "CK"
     CN = "CN"
     CP = "CP"
     CX = "CX"
     DT = "DT"
     ED = "ED"
     FT = "FT"
     MO = "MO"
     NM = "NM"
     PN = "PN"
     RP = "RP"
     SN = "SN"
     ST = "ST"
     TM = "TM"
     TN = "TN"
     TS = "TS"
     TX = "TX"
     XAD = "XAD"
     XCN = "XCN"
     XON = "XON"
     XPN = "XPN"
     XTN = "XTN"


class Quantitylimitedrequest(str, Enum):
     """
     126 - Quantity limited request

     CH  Characters
     LI  Lines
     PG  Pages
     RD  Records
     ZO  Locally defined
     """


     CH = "CH"
     LI = "LI"
     PG = "PG"
     RD = "RD"
     ZO = "ZO"


class Allergentype(str, Enum):
     """
     127 - Allergen type

     DA  Drug allergy
     FA  Food allergy
     MA  Miscellaneous allergy
     MC  Miscellaneous contraindication
     EA  Environmental Allergy
     AA  Animal Allergy
     PA  Plant Allergy
     LA  Pollen Allergy
     """


     DA = "DA"
     FA = "FA"
     MA = "MA"
     MC = "MC"
     EA = "EA"
     AA = "AA"
     PA = "PA"
     LA = "LA"


class Allergyseverity(str, Enum):
     """
     128 - Allergy severity

     SV  Severe
     MO  Moderate
     MI  Mild
     U  Unknown
     """


     SV = "SV"
     MO = "MO"
     MI = "MI"
     U = "U"


class Visitusercode(str, Enum):
     """
     130 - Visit user code

     TE  Teaching
     HO  Home
     MO  Mobile Unit
     PH  Phone
     """


     TE = "TE"
     HO = "HO"
     MO = "MO"
     PH = "PH"


class Procedurepractitioneridentifiercodetype(str, Enum):
     """
     133 - Procedure practitioner identifier code type

     AN  Anesthesiologist/Anesthetist
     PR  Procedure MD/ Surgeon
     RD  Radiologist
     RS  Resident
     NP  Nurse Practitioner
     CM  Certified Nurse Midwife
     SN  Scrub Nurse
     PS  Primary Surgeon
     AS  Assistant Surgeon
     """


     AN = "AN"
     PR = "PR"
     RD = "RD"
     RS = "RS"
     NP = "NP"
     CM = "CM"
     SN = "SN"
     PS = "PS"
     AS = "AS"


class Assignmentofbenefits(str, Enum):
     """
     135 - Assignment of benefits

     Y  Yes
     N  No
     M  Modified assignment
     """


     Y = "Y"
     N = "N"
     M = "M"


class Yes_noindicator(str, Enum):
     """
     136 - Yes-no indicator

     Y  Yes
     N  No
     """


     Y = "Y"
     N = "N"


class Mailclaimparty(str, Enum):
     """
     137 - Mail claim party

     E  Employer
     G  Guarantor
     I  Insurance company
     O  Other
     P  Patient
     """


     E = "E"
     G = "G"
     I = "I"
     O = "O"
     P = "P"


class Militaryservice(str, Enum):
     """
     140 - Military service

     USA  U.S. Army
     USN  U.S. Navy
     USAF  U.S. Air Force
     USMC  U.S. Marines
     USCG  U.S. Coast Guard
     USPHS  U.S. Public Health Service
     NOAA  National Oceanic and Atmospheric Administration
     NATO  North Atlantic Treaty Organization
     AUSA  Australian Army
     AUSN  Australian Navy
     AUSAF  Australian Air Force
     """


     USA = "USA"
     USN = "USN"
     USAF = "USAF"
     USMC = "USMC"
     USCG = "USCG"
     USPHS = "USPHS"
     NOAA = "NOAA"
     NATO = "NATO"
     AUSA = "AUSA"
     AUSN = "AUSN"
     AUSAF = "AUSAF"


class Militaryrank_grade(str, Enum):
     """
     141 - Military rank-grade

     O2  Officers
     O1  Officers
     O10  Officers
     W4  
     O3  Officers
     O4  Officers
     O5  Officers
     O6  Officers
     O8  Officers
     O9  Officers
     W1  
     W2  
     W3  
     O7  Officers
     E9  Enlisted
     E1 ... E9  Enlisted
     E2  Enlisted
     E3  Enlisted
     E4  Enlisted
     E5  Enlisted
     E6  Enlisted
     E8  Enlisted
     E1  Enlisted
     E7  Enlisted
     O1 ... O10  Officers
     W1 ... W4  Warrant Officers
     """


     O2 = "O2"
     O1 = "O1"
     O10 = "O10"
     W4 = "W4"
     O3 = "O3"
     O4 = "O4"
     O5 = "O5"
     O6 = "O6"
     O8 = "O8"
     O9 = "O9"
     W1 = "W1"
     W2 = "W2"
     W3 = "W3"
     O7 = "O7"
     E9 = "E9"
     E1_____E9 = "E1 ... E9"
     E2 = "E2"
     E3 = "E3"
     E4 = "E4"
     E5 = "E5"
     E6 = "E6"
     E8 = "E8"
     E1 = "E1"
     E7 = "E7"
     O1_____O10 = "O1 ... O10"
     W1_____W4 = "W1 ... W4"


class Militarystatus(str, Enum):
     """
     142 - Military status

     ACT  Active duty
     RET  Retired
     DEC  Deceased
     """


     ACT = "ACT"
     RET = "RET"
     DEC = "DEC"


class Eligibilitysource(str, Enum):
     """
     144 - Eligibility source

     1  Insurance company
     2  Employer
     3  Insured presented policy
     4  Insured presented card
     5  Signed statement on file
     6  Verbal information
     7  None
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"
     _7 = "7"


class Roomtype(str, Enum):
     """
     145 - Room type

     PRI  Private room
     2PRI  Second private room
     SPR  Semi-private room
     2SPR  Second semi-private room
     ICU  Intensive care unit
     2ICU  Second intensive care unit
     """


     PRI = "PRI"
     _2PRI = "2PRI"
     SPR = "SPR"
     _2SPR = "2SPR"
     ICU = "ICU"
     _2ICU = "2ICU"


class Amounttype(str, Enum):
     """
     146 - Amount type

     DF  Differential
     LM  Limit
     PC  Percentage
     RT  Rate
     UL  Unlimited
     """


     DF = "DF"
     LM = "LM"
     PC = "PC"
     RT = "RT"
     UL = "UL"


class Policytype(str, Enum):
     """
     147 - Policy type

     ANC  Ancillary
     2ANC  Second ancillary
     MMD  Major medical
     2MMD  Second major medical
     3MMD  Third major medical
     """


     ANC = "ANC"
     _2ANC = "2ANC"
     MMD = "MMD"
     _2MMD = "2MMD"
     _3MMD = "3MMD"


class Penaltytype(str, Enum):
     """
     148 - Penalty type

     AT  Currency amount
     PC  Percentage
     """


     AT = "AT"
     PC = "PC"


class Daytype(str, Enum):
     """
     149 - Day type

     AP  Approved
     DE  Denied
     PE  Pending
     """


     AP = "AP"
     DE = "DE"
     PE = "PE"


class Pre_certificationpatienttype(str, Enum):
     """
     150 - Pre-certification patient type

     ER  Emergency
     IPE  Inpatient elective
     OPE  Outpatient elective
     UR  Urgent
     """


     ER = "ER"
     IPE = "IPE"
     OPE = "OPE"
     UR = "UR"


class Valuecode(str, Enum):
     """
     153 - Value code

     01  Most common semi-private rate
     02  Hospital has no semi-private rooms
     04  Inpatient professional component charges which are combined billed
     05  Professional component included in charges and also billed separate to carrier
     06  Medicare blood deductible
     08  Medicare life time reserve amount in the first calendar year
     09  Medicare co-insurance amount in the first calendar year
     10  Lifetime reserve amount in the second calendar year
     11  Co-insurance amount in the second calendar year
     12  Working aged beneficiary/spouse with employer group health plan
     13  ESRD beneficiary in a Medicare coordination period with an employer group health plan
     14  No Fault including auto/other
     15  Worker's Compensation
     16  PHS, or other federal agency
     17  Payer code
     21  Catastrophic
     22  Surplus
     23  Recurring monthly incode
     24  Medicaid rate code
     30  Pre-admission testing
     31  Patient liability amount
     37  Pints of blood furnished
     38  Blood deductible pints
     39  Pints of blood replaced
     40  New coverage not implemented by HMO (for inpatient service only)
     41  Black lung
     42  VA
     43  Disabled beneficiary under age 64 with LGHP
     44  Amount provider agreed to accept from primary payer when this amount is less than charges but higher than payment received,, then a Medicare secondary payment is due
     45  Accident hour
     46  Number of grace days
     47  Any liability insurance
     48  Hemoglobin reading
     49  Hematocrit reading
     50  Physical therapy visits
     51  Occupational therapy visits
     52  Speech therapy visits
     53  Cardiac rehab visits
     56  Skilled nurse - home visit hours
     57  Home health aide - home visit hours
     58  Arterial blood gas
     59  Oxygen saturation
     60  HHA branch MSA
     67  Peritoneal dialysis
     68  EPO-drug
     70  Payer codes
     72  Payer codes
     70 ... 72  Payer codes
     71  Payer codes
     75  Payer codes
     75 ... 79  Payer codes
     76  Payer codes
     77  Payer codes
     78  Payer codes
     79  Payer codes
     80  Psychiatric visits
     81  Visits subject to co-payment
     A1  Deductible payer A
     A2  Coinsurance payer A
     A3  Estimated responsibility payer A
     X0  Service excluded on primary policy
     X4  Supplemental coverage
     """


     _01 = "01"
     _02 = "02"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _08 = "08"
     _09 = "09"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _13 = "13"
     _14 = "14"
     _15 = "15"
     _16 = "16"
     _17 = "17"
     _21 = "21"
     _22 = "22"
     _23 = "23"
     _24 = "24"
     _30 = "30"
     _31 = "31"
     _37 = "37"
     _38 = "38"
     _39 = "39"
     _40 = "40"
     _41 = "41"
     _42 = "42"
     _43 = "43"
     _44 = "44"
     _45 = "45"
     _46 = "46"
     _47 = "47"
     _48 = "48"
     _49 = "49"
     _50 = "50"
     _51 = "51"
     _52 = "52"
     _53 = "53"
     _56 = "56"
     _57 = "57"
     _58 = "58"
     _59 = "59"
     _60 = "60"
     _67 = "67"
     _68 = "68"
     _70 = "70"
     _72 = "72"
     _70_____72 = "70 ... 72"
     _71 = "71"
     _75 = "75"
     _75_____79 = "75 ... 79"
     _76 = "76"
     _77 = "77"
     _78 = "78"
     _79 = "79"
     _80 = "80"
     _81 = "81"
     A1 = "A1"
     A2 = "A2"
     A3 = "A3"
     X0 = "X0"
     X4 = "X4"


class Accept_applicationacknowledgmentconditions(str, Enum):
     """
     155 - Accept-application acknowledgment conditions

     AL  Always
     NE  Never
     ER  Error/reject conditions only
     SU  Successful completion only
     """


     AL = "AL"
     NE = "NE"
     ER = "ER"
     SU = "SU"


class Whichdate_timequalifier(str, Enum):
     """
     156 - Which date-time qualifier

     ANY  Any date/time within a range
     COL  Collection date/time, equivalent to film or sample collection date/time
     ORD  Order date/time
     RCT  Specimen receipt date/time, receipt of specimen in filling ancillary (Lab)
     REP  Report date/time, report date/time at filing ancillary (i.e., Lab)
     SCHED  Schedule date/time
     """


     ANY = "ANY"
     COL = "COL"
     ORD = "ORD"
     RCT = "RCT"
     REP = "REP"
     SCHED = "SCHED"


class Whichdate_timestatusqualifier(str, Enum):
     """
     157 - Which date-time status qualifier

     ANY  Any status
     CFN  Current final value, whether final or corrected
     COR  Corrected only (no final with corrections)
     FIN  Final only (no corrections)
     PRE  Preliminary
     REP  Report completion date/time
     """


     ANY = "ANY"
     CFN = "CFN"
     COR = "COR"
     FIN = "FIN"
     PRE = "PRE"
     REP = "REP"


class Date_timeselectionqualifier(str, Enum):
     """
     158 - Date-time selection qualifier

     1ST  First value within range
     ALL  All values within the range
     LST  Last value within the range
     REV  All values within the range returned in reverse chronological order (This is the default if not otherwise specified.)
     """


     _1ST = "1ST"
     ALL = "ALL"
     LST = "LST"
     REV = "REV"


class Dietcodespecificationtype(str, Enum):
     """
     159 - Diet code specification type

     D  Diet
     S  Supplement
     P  Preference
     """


     D = "D"
     S = "S"
     P = "P"


class Traytype(str, Enum):
     """
     160 - Tray type

     EARLY  Early tray
     LATE  Late tray
     GUEST  Guest tray
     NO  No tray
     MSG  Tray message only
     """


     EARLY = "EARLY"
     LATE = "LATE"
     GUEST = "GUEST"
     NO = "NO"
     MSG = "MSG"


class Allowsubstitution(str, Enum):
     """
     161 - Allow substitution

     N  Substitutions are NOT authorized.  (This is the default - null.)
     G  Allow generic substitutions.
     T  Allow therapeutic substitutions
     """


     N = "N"
     G = "G"
     T = "T"


class Routeofadministration(str, Enum):
     """
     162 - Route of administration

     AP  Apply Externally
     B  Buccal
     DT  Dental
     EP  Epidural
     ET  Endotrachial Tube
     GTT  Gastrostomy Tube
     GU  GU Irrigant
     IMR  Immerse (Soak) Body Part
     IA  Intra-arterial
     IB  Intrabursal
     IC  Intracardiac
     ICV  Intracervical (uterus)
     ID  Intradermal
     IH  Inhalation
     IHA  Intrahepatic Artery
     IM  Intramuscular
     IN  Intranasal
     IO  Intraocular
     IP  Intraperitoneal
     IS  Intrasynovial
     IT  Intrathecal
     IU  Intrauterine
     IV  Intravenous
     MTH  Mouth/Throat
     MM  Mucous Membrane
     NS  Nasal
     NG  Nasogastric
     NP  Nasal Prongs
     NT  Nasotrachial Tube
     OP  Ophthalmic
     OT  Otic
     OTH  Other/Miscellaneous
     PF  Perfusion
     PO  Oral
     PR  Rectal
     RM  Rebreather Mask
     SD  Soaked Dressing
     SC  Subcutaneous
     SL  Sublingual
     TP  Topical
     TRA  Tracheostomy
     TD  Transdermal
     TL  Translingual
     UR  Urethral
     VG  Vaginal
     VM  Ventimask
     WND  Wound
     """


     AP = "AP"
     B = "B"
     DT = "DT"
     EP = "EP"
     ET = "ET"
     GTT = "GTT"
     GU = "GU"
     IMR = "IMR"
     IA = "IA"
     IB = "IB"
     IC = "IC"
     ICV = "ICV"
     ID = "ID"
     IH = "IH"
     IHA = "IHA"
     IM = "IM"
     IN = "IN"
     IO = "IO"
     IP = "IP"
     IS = "IS"
     IT = "IT"
     IU = "IU"
     IV = "IV"
     MTH = "MTH"
     MM = "MM"
     NS = "NS"
     NG = "NG"
     NP = "NP"
     NT = "NT"
     OP = "OP"
     OT = "OT"
     OTH = "OTH"
     PF = "PF"
     PO = "PO"
     PR = "PR"
     RM = "RM"
     SD = "SD"
     SC = "SC"
     SL = "SL"
     TP = "TP"
     TRA = "TRA"
     TD = "TD"
     TL = "TL"
     UR = "UR"
     VG = "VG"
     VM = "VM"
     WND = "WND"


class Bodysite(str, Enum):
     """
     163 - Body site

     BE  Bilateral Ears
     OU  Bilateral Eyes
     BN  Bilateral Nares
     BU  Buttock
     CT  Chest Tube
     LA  Left Arm
     LAC  Left Anterior Chest
     LACF  Left Antecubital Fossa
     LD  Left Deltoid
     LE  Left Ear
     LEJ  Left External Jugular
     OS  Left Eye
     LF  Left Foot
     LG  Left Gluteus Medius
     LH  Left Hand
     LIJ  Left Internal Jugular
     LLAQ  Left Lower Abd Quadrant
     LLFA  Left Lower Forearm
     LMFA  Left Mid Forearm
     LN  Left Naris
     LPC  Left Posterior Chest
     LSC  Left Subclavian
     LT  Left Thigh
     LUA  Left Upper Arm
     LUAQ  Left Upper Abd Quadrant
     LUFA  Left Upper Forearm
     LVG  Left Ventragluteal
     LVL  Left Vastus Lateralis
     NB  Nebulized
     PA  Perianal
     PERIN  Perineal
     RA  Right Arm
     RAC  Right Anterior Chest
     RACF  Right Antecubital Fossa
     RD  Right Deltoid
     RE  Right Ear
     REJ  Right External Jugular
     OD  Right Eye
     RF  Right Foot
     RG  Right Gluteus Medius
     RH  Right Hand
     RIJ  Right Internal Jugular
     RLAQ  Rt Lower Abd Quadrant
     RLFA  Right Lower Forearm
     RMFA  Right Mid Forearm
     RN  Right Naris
     RPC  Right Posterior Chest
     RSC  Right Subclavian
     RT  Right Thigh
     RUA  Right Upper Arm
     RUAQ  Right Upper Abd Quadrant
     RUFA  Right Upper Forearm
     RVL  Right Vastus Lateralis
     RVG  Right Ventragluteal
     """


     BE = "BE"
     OU = "OU"
     BN = "BN"
     BU = "BU"
     CT = "CT"
     LA = "LA"
     LAC = "LAC"
     LACF = "LACF"
     LD = "LD"
     LE = "LE"
     LEJ = "LEJ"
     OS = "OS"
     LF = "LF"
     LG = "LG"
     LH = "LH"
     LIJ = "LIJ"
     LLAQ = "LLAQ"
     LLFA = "LLFA"
     LMFA = "LMFA"
     LN = "LN"
     LPC = "LPC"
     LSC = "LSC"
     LT = "LT"
     LUA = "LUA"
     LUAQ = "LUAQ"
     LUFA = "LUFA"
     LVG = "LVG"
     LVL = "LVL"
     NB = "NB"
     PA = "PA"
     PERIN = "PERIN"
     RA = "RA"
     RAC = "RAC"
     RACF = "RACF"
     RD = "RD"
     RE = "RE"
     REJ = "REJ"
     OD = "OD"
     RF = "RF"
     RG = "RG"
     RH = "RH"
     RIJ = "RIJ"
     RLAQ = "RLAQ"
     RLFA = "RLFA"
     RMFA = "RMFA"
     RN = "RN"
     RPC = "RPC"
     RSC = "RSC"
     RT = "RT"
     RUA = "RUA"
     RUAQ = "RUAQ"
     RUFA = "RUFA"
     RVL = "RVL"
     RVG = "RVG"


class Administrationdevice(str, Enum):
     """
     164 - Administration device

     AP  Applicator
     BT  Buretrol
     HL  Heparin Lock
     IPPB  IPPB
     IVP  IV Pump
     IVS  IV Soluset
     MI  Metered Inhaler
     NEB  Nebulizer
     PCA  PCA Pump
     """


     AP = "AP"
     BT = "BT"
     HL = "HL"
     IPPB = "IPPB"
     IVP = "IVP"
     IVS = "IVS"
     MI = "MI"
     NEB = "NEB"
     PCA = "PCA"


class Administrationmethod(str, Enum):
     """
     165 - Administration method

     CH  Chew
     DI  Dissolve
     DU  Dust
     IF  Infiltrate
     IS  Insert
     IR  Irrigate
     IVPB  IV Piggyback
     IVP  IV Push
     NB  Nebulized
     PT  Pain
     PF  Perfuse
     SH  Shampoo
     SO  Soak
     WA  Wash
     WI  Wipe
     """


     CH = "CH"
     DI = "DI"
     DU = "DU"
     IF = "IF"
     IS = "IS"
     IR = "IR"
     IVPB = "IVPB"
     IVP = "IVP"
     NB = "NB"
     PT = "PT"
     PF = "PF"
     SH = "SH"
     SO = "SO"
     WA = "WA"
     WI = "WI"


class RXcomponenttype(str, Enum):
     """
     166 - RX component type

     B  Base
     A  Additive
     """


     B = "B"
     A = "A"


class Substitutionstatus(str, Enum):
     """
     167 - Substitution status

     N  No substitute was dispensed.  This is equivalent to the default (null) value.
     G  A generic substitution was dispensed.
     T  A therapeutic substitution was dispensed.
     0  No product selection indicated
     1  Substitution not allowed by prescriber
     2  Substitution allowed - patient requested product dispensed
     3  Substitution allowed - pharmacist selected product dispensed
     4  Substitution allowed - generic drug not in stock
     5  Substitution allowed - brand drug dispensed as a generic
     7  Substitution not allowed - brand drug mandated by law
     8  Substitution allowed - generic drug not available in marketplace
     """


     N = "N"
     G = "G"
     T = "T"
     _0 = "0"
     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _7 = "7"
     _8 = "8"


class Processingpriority(str, Enum):
     """
     168 - Processing priority

     S  Stat (do immediately)
     A  As soon as possible (a priority lower than stat)
     R  Routine
     P  Preoperative (to be done prior to surgery)
     T  Timing critical (do as near as possible to requested time)
     C  Measure continuously (e.g., arterial line blood pressure)
     B  Do at bedside or portable (may be used with other codes)
     """


     S = "S"
     A = "A"
     R = "R"
     P = "P"
     T = "T"
     C = "C"
     B = "B"


class Reportingpriority(str, Enum):
     """
     169 - Reporting priority

     C  Call back results
     R  Rush reporting
     """


     C = "C"
     R = "R"


class Derivedspecimen(str, Enum):
     """
     170 - Derived specimen

     P  Parent Observation
     C  Child Observation
     N  Not Applicable
     """


     P = "P"
     C = "C"
     N = "N"


class Coordinationofbenefits(str, Enum):
     """
     173 - Coordination of benefits

     CO  Coordination
     IN  Independent
     """


     CO = "CO"
     IN = "IN"


class Natureofservice_test_observation(str, Enum):
     """
     174 - Nature of service-test-observation

     P  Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen
     F  Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatinine clearance), usually done at different times and/or on different specimens
     A  Atomic service/test/observation (test code or treatment code)
     S  Superset--a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes); This set indicates that the code being described is used to order multiple service/test/observation b
     C  Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar--arterial ratio, cardiac output)
     """


     P = "P"
     F = "F"
     A = "A"
     S = "S"
     C = "C"


class Masterfileidentifiercode(str, Enum):
     """
     175 - Master file identifier code

     CDM  Charge description master file
     CMA  Clinical study with phases and scheduled master file
     CMB  Clinical study without phases but with scheduled master file
     LOC  Location master file
     OMA  Numerical observation master file
     OMB  Categorical observation master file
     OMC  Observation batteries master file
     OMD  Calculated observations master file
     PRA  Practitioner master file
     STF  Staff master file
     CLN  Clinic master file
     OME  Other basic observation/service attributes
     """


     CDM = "CDM"
     CMA = "CMA"
     CMB = "CMB"
     LOC = "LOC"
     OMA = "OMA"
     OMB = "OMB"
     OMC = "OMC"
     OMD = "OMD"
     PRA = "PRA"
     STF = "STF"
     CLN = "CLN"
     OME = "OME"


class Confidentialitycode(str, Enum):
     """
     177 - Confidentiality code

     V  Very restricted
     R  Restricted
     U  Usual control
     EMP  Employee
     UWM  Unwed mother
     VIP  Very important person or celebrity
     PSY  Psychiatric patient
     AID  AIDS patient
     HIV  HIV(+) patient
     ETH  Alcohol/drug treatment patient
     """


     V = "V"
     R = "R"
     U = "U"
     EMP = "EMP"
     UWM = "UWM"
     VIP = "VIP"
     PSY = "PSY"
     AID = "AID"
     HIV = "HIV"
     ETH = "ETH"


class Fileleveleventcode(str, Enum):
     """
     178 - File level event code

     REP  Replace current version of this master file with the version contained in this message
     UPD  Change file records as defined in the record-level event codes for each record that follows
     """


     REP = "REP"
     UPD = "UPD"


class Responselevel(str, Enum):
     """
     179 - Response level

     NE  Never.  No application-level response needed
     ER  Error/Reject conditions only.  Only MFA segments denoting errors must be returned via the application-level acknowledgment for this message
     AL  Always. All MFA segments (whether denoting errors or not) must be returned via the application-level acknowledgment message
     SU  Success.  Only MFA segments denoting success must be returned via the application-level acknowledgment for this message
     """


     NE = "NE"
     ER = "ER"
     AL = "AL"
     SU = "SU"


class Record_leveleventcode(str, Enum):
     """
     180 - Record-level event code

     MAD  Add record to master file
     MDL  Delete record from master file
     MUP  Update record for master file
     MDC  Deactivate: discontinue using record in master file, but do not delete from database
     MAC  Reactivate deactivated record
     """


     MAD = "MAD"
     MDL = "MDL"
     MUP = "MUP"
     MDC = "MDC"
     MAC = "MAC"


class MFNrecord_levelerrorreturn(str, Enum):
     """
     181 - MFN record-level error return

     S  Successful posting of the record defined by the MFE segment
     U  Unsuccessful posting of the record defined by the MFE segment
     """


     S = "S"
     U = "U"


class Active_inactive(str, Enum):
     """
     183 - Active-inactive

     A  Active Staff
     I  Inactive Staff
     """


     A = "A"
     I = "I"


class Preferredmethodofcontact(str, Enum):
     """
     185 - Preferred method of contact

     B  Beeper Number
     C  Cellular Phone Number
     E  E-Mail Address (for backward compatibility)
     F  FAX Number
     H  Home Phone Number
     O  Office Phone Number
     """


     B = "B"
     C = "C"
     E = "E"
     F = "F"
     H = "H"
     O = "O"


class Providerbilling(str, Enum):
     """
     187 - Provider billing

     I  Institution bills for provider
     P  Provider does own billing
     """


     I = "I"
     P = "P"


class Ethnicgroup(str, Enum):
     """
     189 - Ethnic group

     H  Hispanic or Latino
     N  Not Hispanic or Latino
     U  Unknown
     """


     H = "H"
     N = "N"
     U = "U"


class Addresstype(str, Enum):
     """
     190 - Address type

     BA  Bad address
     N  Birth (nee) (birth address, not otherwise specified)
     BDL  Birth delivery location (address where birth occurred)
     F  Country Of Origin
     C  Current Or Temporary
     B  Firm/Business
     H  Home
     L  Legal Address
     M  Mailing
     O  Office
     P  Permanent
     RH  Registry home.  Refers to the information system, typically managed by a public health agency, that stores patient information such as immunization histories or cancer data, regardless of where the patient obtains services.
     BR  Residence  at birth (home address at time of birth)
     """


     BA = "BA"
     N = "N"
     BDL = "BDL"
     F = "F"
     C = "C"
     B = "B"
     H = "H"
     L = "L"
     M = "M"
     O = "O"
     P = "P"
     RH = "RH"
     BR = "BR"


class Typeofreferenceddata(str, Enum):
     """
     191 - Type of referenced data

     AP  Other application data, typically uninterpreted binary data  (HL7 V2.3 and later)
     AU  Audio data  (HL7 V2.3 and later)
     FT  Formatted text (HL7 V2.2 only)
     IM  Image data  (HL7 V2.3 and later)
     multipart  MIME multipart package
     NS  Non-scanned image (HL7 V2.2 only)
     SD  Scanned document (HL7 V2.2 only)
     SI  Scanned image (HL7 V2.2 only)
     TEXT  Machine readable text document (HL7 V2.3.1 and later)
     TX  Machine readable text document (HL7 V2.2 only)
     """


     AP = "AP"
     AU = "AU"
     FT = "FT"
     IM = "IM"
     multipart = "multipart"
     NS = "NS"
     SD = "SD"
     SI = "SI"
     TEXT = "TEXT"
     TX = "TX"


class Amountclass(str, Enum):
     """
     193 - Amount class

     AT  Amount
     LM  Limit
     PC  Percentage
     UL  Unlimited
     """


     AT = "AT"
     LM = "LM"
     PC = "PC"
     UL = "UL"


class Nametype(str, Enum):
     """
     200 - Name type

     A  Alias Name
     B  Name at Birth
     C  Adopted Name
     D  Display Name
     I  Licensing Name
     L  Legal Name
     M  Maiden Name
     N  Nickname /"Call me" Name/Street Name
     P  Name of Partner/Spouse (retained for backward compatibility only)
     R  Registered Name (animals only)
     S  Coded Pseudo-Name to ensure anonymity
     T  Indigenous/Tribal/Community Name
     U  Unspecified
     """


     A = "A"
     B = "B"
     C = "C"
     D = "D"
     I = "I"
     L = "L"
     M = "M"
     N = "N"
     P = "P"
     R = "R"
     S = "S"
     T = "T"
     U = "U"


class Telecommunicationusecode(str, Enum):
     """
     201 - Telecommunication use code

     PRN  Primary Residence Number
     ORN  Other Residence Number
     WPN  Work Number
     VHN  Vacation Home Number
     ASN  Answering Service Number
     EMR  Emergency Number
     NET  Network (email) Address
     BPN  Beeper Number
     """


     PRN = "PRN"
     ORN = "ORN"
     WPN = "WPN"
     VHN = "VHN"
     ASN = "ASN"
     EMR = "EMR"
     NET = "NET"
     BPN = "BPN"


class Telecommunicationequipmenttype(str, Enum):
     """
     202 - Telecommunication equipment type

     PH  Telephone
     FX  Fax
     MD  Modem
     CP  Cellular Phone
     BP  Beeper
     Internet  Internet Address: Use Only If Telecommunication Use Code Is NET
     X.400  X.400 email address: Use Only If Telecommunication Use Code Is NET
     """


     PH = "PH"
     FX = "FX"
     MD = "MD"
     CP = "CP"
     BP = "BP"
     Internet = "Internet"
     X_400 = "X.400"


class Identifiertype(str, Enum):
     """
     203 - Identifier type

     AM  American Express
     AN  Account number
     BA  Bank Account Number
     BR  Birth registry number
     BRN  Breed Registry Number
     DI  Diner's Club card
     DL  Driver's license number
     DN  Doctor number
     DR  Donor Registration Number
     DS  Discover Card
     EI  Employee number
     EN  Employer number
     FI  Facility ID
     GI  Guarantor internal identifier
     GN  Guarantor external  identifier
     HC  Health Card Number
     JHN  Jurisdictional health number (Canada)
     LN  License number
     LR  Local Registry ID
     MA  Medicaid number
     MC  Medicare number
     MCN  Microchip Number
     MR  Medical record number
     MS  MasterCard
     NE  National employer identifier
     NH  National Health Plan Identifier
     NI  National unique individual identifier
     NNxxx  National Person Identifier where the xxx is the ISO table 3166  3-character (alphabetic) country code
     NPI  National provider identifier
     PEN  Pension Number
     PI  Patient internal identifier
     PN  Person number
     PRN  Provider number
     PT  Patient external identifier
     RR  Railroad Retirement number
     RRI  Regional registry ID
     SL  State license
     SR  State registry ID
     SS  Social Security number
     U  Unspecified
     UPIN  Medicare/HCFA's Universal Physician Identification numbers
     VN  Visit number
     VS  VISA
     WC  WIC identifier
     WCN  Workers' Comp Number
     XX  Organization identifier
     """


     AM = "AM"
     AN = "AN"
     BA = "BA"
     BR = "BR"
     BRN = "BRN"
     DI = "DI"
     DL = "DL"
     DN = "DN"
     DR = "DR"
     DS = "DS"
     EI = "EI"
     EN = "EN"
     FI = "FI"
     GI = "GI"
     GN = "GN"
     HC = "HC"
     JHN = "JHN"
     LN = "LN"
     LR = "LR"
     MA = "MA"
     MC = "MC"
     MCN = "MCN"
     MR = "MR"
     MS = "MS"
     NE = "NE"
     NH = "NH"
     NI = "NI"
     NNxxx = "NNxxx"
     NPI = "NPI"
     PEN = "PEN"
     PI = "PI"
     PN = "PN"
     PRN = "PRN"
     PT = "PT"
     RR = "RR"
     RRI = "RRI"
     SL = "SL"
     SR = "SR"
     SS = "SS"
     U = "U"
     UPIN = "UPIN"
     VN = "VN"
     VS = "VS"
     WC = "WC"
     WCN = "WCN"
     XX = "XX"


class Organizationalnametype(str, Enum):
     """
     204 - Organizational name type

     A  Alias name
     L  Legal name
     D  Display name
     SL  Stock exchange listing name
     """


     A = "A"
     L = "L"
     D = "D"
     SL = "SL"


class Pricetype(str, Enum):
     """
     205 - Price type

     AP  administrative price or handling fee
     DC  direct unit cost
     IC  indirect unit cost
     PF  professional fee for performing provider
     TF  technology fee for use of equipment
     TP  total price
     UP  unit price, may be based on length of procedure or service
     """


     AP = "AP"
     DC = "DC"
     IC = "IC"
     PF = "PF"
     TF = "TF"
     TP = "TP"
     UP = "UP"


class Segmentactioncode(str, Enum):
     """
     206 - Segment action code

     A  Add/Insert
     D  Delete
     U  Update
     """


     A = "A"
     D = "D"
     U = "U"


class Processingmode(str, Enum):
     """
     207 - Processing mode

     A  Archive
     R  Restore from archive
     I  Initial load
     T  Current processing, transmitted at intervals (scheduled or on demand)
     Not present  Not present (the default, meaning current  processing)
     """


     A = "A"
     R = "R"
     I = "I"
     T = "T"
     Not_present = "Not present"


class Queryresponsestatus(str, Enum):
     """
     208 - Query response status

     OK  Data found, no errors (this is the default)
     NF  No data found, no errors
     AE  Application error
     AR  Application reject
     """


     OK = "OK"
     NF = "NF"
     AE = "AE"
     AR = "AR"


class Relationaloperator(str, Enum):
     """
     209 - Relational operator

     EQ  Equal
     NE  Not Equal
     LT  Less than
     GT  Greater than
     LE  Less than or equal
     GE  Greater than or equal
     CT  Contains
     GN  Generic
     """


     EQ = "EQ"
     NE = "NE"
     LT = "LT"
     GT = "GT"
     LE = "LE"
     GE = "GE"
     CT = "CT"
     GN = "GN"


class Relationalconjunction(str, Enum):
     """
     210 - Relational conjunction

     AND  Default
     OR  
     """


     AND = "AND"
     OR = "OR"


class Alternatecharactersets(str, Enum):
     """
     211 - Alternate character sets

     ASCII  The printable 7-bit ASCII character set. (This is the default if this field is omitted)
     8859/1  The printable characters from the ISO 8859/1 Character set
     8859/2  The printable characters from the ISO 8859/2 Character set
     8859/3  The printable characters from the ISO 8859/3 Character set
     8859/4  The printable characters from the ISO 8859/4 Character set
     8859/5  The printable characters from the ISO 8859/5 Character set
     8859/6  The printable characters from the ISO 8859/6 Character set
     8859/7  The printable characters from the ISO 8859/7 Character set
     8859/8  The printable characters from the ISO 8859/8 Character set
     8859/9  The printable characters from the ISO 8859/9 Character set
     ISO IR14  Code for Information Exchange (one byte)(JIS X 0201-1976).  Note that the code contains a space, i.e. "ISO IR14".
     ISO IR87  Code for the Japanese Graphic Character set for information interchange (JIS X 0208-1990), Note that the code contains a space, i.e. "ISO IR87".
     ISO IR159  Code of the supplementary Japanese Graphic Character set for information interchange (JIS X 0212-1990). Note that the code contains a space, i.e. "ISO IR159".
     UNICODE  The world wide character standard from ISO/IEC 10646-1-19931
     """


     ASCII = "ASCII"
     _8859_1 = "8859/1"
     _8859_2 = "8859/2"
     _8859_3 = "8859/3"
     _8859_4 = "8859/4"
     _8859_5 = "8859/5"
     _8859_6 = "8859/6"
     _8859_7 = "8859/7"
     _8859_8 = "8859/8"
     _8859_9 = "8859/9"
     ISO_IR14 = "ISO IR14"
     ISO_IR87 = "ISO IR87"
     ISO_IR159 = "ISO IR159"
     UNICODE = "UNICODE"


class Purgestatuscode(str, Enum):
     """
     213 - Purge status code

     P  Marked for purge.  User is no longer able to update the visit.
     D  The visit is marked for deletion and the user cannot enter new data against it.
     I  The visit is marked inactive and the user cannot enter new data against it.
     """


     P = "P"
     D = "D"
     I = "I"


class Visitprioritycode(str, Enum):
     """
     217 - Visit priority code

     1  Emergency
     2  Urgent
     3  Elective
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"


class Livingarrangement(str, Enum):
     """
     220 - Living arrangement

     A  Alone
     F  Family
     I  Institution
     R  Relative
     U  Unknown
     S  Spouse Only
     """


     A = "A"
     F = "F"
     I = "I"
     R = "R"
     U = "U"
     S = "S"


class Livingdependency(str, Enum):
     """
     223 - Living dependency

     S  Spouse Dependent
     D  Spouse dependent
     M  Medical Supervision Required
     C  Small Children Dependent
     WU  Walk up
     O  Other
     U  Unknown
     CB  Common Bath
     """


     S = "S"
     D = "D"
     M = "M"
     C = "C"
     WU = "WU"
     O = "O"
     U = "U"
     CB = "CB"


class Transportarranged(str, Enum):
     """
     224 - Transport arranged

     A  Arranged
     N  Not Arranged
     U  Unknown
     """


     A = "A"
     N = "N"
     U = "U"


class Escortrequired(str, Enum):
     """
     225 - Escort required

     R  Required
     N  Not Required
     U  Unknown
     """


     R = "R"
     N = "N"
     U = "U"


class Manufacturersofvaccines(str, Enum):
     """
     227 - Manufacturers of vaccines (code=MVX)

     AB  Abbott Laboratories (includes Ross Products Division)
     AD  Adams Laboratories
     ALP  Alpha Therapeutic Corporation
     AR  Armour [Inactive-use CEN]
     AVI  Aviron
     BA  Baxter Healthcare Corporation
     BAY  Bayer Corporation(includes Miles, Inc. and Cutter Laboratories)
     BP  Berna Products [Inactive-use BPC]
     BPC  Berna Products Corporation (includes Swiss Serum and Vaccine Institute Berne)
     CEN  Centeon L.L.C. (includes Armour Pharmaceutical Company)
     CHI  Chiron Corporation
     CON  Connaught [Inactive-use PMC]
     EVN  Evans Medical Limited (an affiliate of Medeva Pharmaceuticals, Inc.)
     GRE  Greer Laboratories, Inc.
     IAG  Immuno International AG
     IM  Merieux [Inactive-use PMC]
     IUS  Immuno-U.S., Inc.
     JPN  The Research Foundation for Microbial Diseases of Osaka University (BIKEN)
     KGC  Korea Green Cross Corporation
     LED  Lederle [Inactive-use WAL]
     MA  Massachusetts Public Health Biologic Laboratories
     MED  MedImmune, Inc.
     MIL  Miles [Inactive-use BAY]
     MIP  Bioport Corporation (formerly Michigan Biologic Products Institute)
     MSD  Merck & Co., Inc.
     NAB  NABI (formerly North American Biologicals, Inc.)
     NYB  New York Blood Center
     NAV  North American Vaccine, Inc.
     NOV  Novartis Pharmaceutical Corporation (includes Ciba-Geigy Limited and Sandoz Limited)
     OTC  Organon Teknika Corporation
     ORT  Ortho Diagnostic Systems, Inc.
     PD  Parkedale Pharmaceuticals (formerly Parke-Davis)
     PMC  Aventis Pasteur Inc. (formerly Pasteur Merieux Connaught; includes Connaught Laboratories and Pasteur Merieux)
     PRX  Praxis Biologics [Inactive-use WAL]
     SCL  Sclavo, Inc.
     SI  Swiss Serum and Vaccine Inst. [Inactive-use BPC]
     SKB  SmithKline Beecham
     USA  United States Army Medical Research and Materiel Command
     WA  Wyeth-Ayerst [Inactive-use WAL]
     WAL  Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories, Lederle Laboratories, and Praxis Biologics)
     OTH  Other manufacturer
     UNK  Unknown manufacturer
     """


     AB = "AB"
     AD = "AD"
     ALP = "ALP"
     AR = "AR"
     AVI = "AVI"
     BA = "BA"
     BAY = "BAY"
     BP = "BP"
     BPC = "BPC"
     CEN = "CEN"
     CHI = "CHI"
     CON = "CON"
     EVN = "EVN"
     GRE = "GRE"
     IAG = "IAG"
     IM = "IM"
     IUS = "IUS"
     JPN = "JPN"
     KGC = "KGC"
     LED = "LED"
     MA = "MA"
     MED = "MED"
     MIL = "MIL"
     MIP = "MIP"
     MSD = "MSD"
     NAB = "NAB"
     NYB = "NYB"
     NAV = "NAV"
     NOV = "NOV"
     OTC = "OTC"
     ORT = "ORT"
     PD = "PD"
     PMC = "PMC"
     PRX = "PRX"
     SCL = "SCL"
     SI = "SI"
     SKB = "SKB"
     USA = "USA"
     WA = "WA"
     WAL = "WAL"
     OTH = "OTH"
     UNK = "UNK"


class Diagnosisclassification(str, Enum):
     """
     228 - Diagnosis classification

     C  Consultation
     D  Diagnosis
     M  Medication (antibiotic)
     O  Other
     R  Radiological scheduling (not using ICDA codes)
     S  Sign and symptom
     T  Tissue diagnosis
     I  Invasive procedure not classified elsewhere (I.V., catheter, etc.)
     """


     C = "C"
     D = "D"
     M = "M"
     O = "O"
     R = "R"
     S = "S"
     T = "T"
     I = "I"


class DRGpayor(str, Enum):
     """
     229 - DRG payor

     M  Medicare
     C  Champus
     G  Managed Care Organization
     """


     M = "M"
     C = "C"
     G = "G"


class Procedurefunctionaltype(str, Enum):
     """
     230 - Procedure functional type

     A  Anesthesia
     P  Procedure for treatment (therapeutic, including operations)
     I  Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)
     D  Diagnostic procedure
     """


     A = "A"
     P = "P"
     I = "I"
     D = "D"


class Studentstatus(str, Enum):
     """
     231 - Student status

     F  Full-time student
     P  Part-time student
     N  Not a student
     """


     F = "F"
     P = "P"
     N = "N"


class Insurancecompanycontactreason(str, Enum):
     """
     232 - Insurance company contact reason

     01  Medicare claim status
     02  Medicaid claim status
     03  Name/address change
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"


class Reporttiming(str, Enum):
     """
     234 - Report timing

     CO  Correction
     AD  Additional information
     RQ  Requested information
     DE  Device evaluation
     PD  Periodic
     3D  3 day report
     7D  7 day report
     10D  10 day report
     15D  15 day report
     30D  30 day report
     """


     CO = "CO"
     AD = "AD"
     RQ = "RQ"
     DE = "DE"
     PD = "PD"
     _3D = "3D"
     _7D = "7D"
     _10D = "10D"
     _15D = "15D"
     _30D = "30D"


class Reportsource(str, Enum):
     """
     235 - Report source

     C  Clinical trial
     L  Literature
     H  Health professional
     R  Regulatory agency
     D  Database/registry/poison control center
     N  Non-healthcare professional
     P  Patient
     M  Manufacturer/marketing authority holder
     E  Distributor
     O  Other
     """


     C = "C"
     L = "L"
     H = "H"
     R = "R"
     D = "D"
     N = "N"
     P = "P"
     M = "M"
     E = "E"
     O = "O"


class Eventreportedto(str, Enum):
     """
     236 - Event reported to

     M  Manufacturer
     L  Local facility/user facility
     R  Regulatory agency
     D  Distributor
     """


     M = "M"
     L = "L"
     R = "R"
     D = "D"


class Eventqualification(str, Enum):
     """
     237 - Event qualification

     I  Interaction
     O  Overdose
     A  Abuse
     M  Misuse
     D  Dependency
     L  Lack of expect therapeutic effect
     W  Drug withdrawal
     B  Unexpected beneficial effect
     """


     I = "I"
     O = "O"
     A = "A"
     M = "M"
     D = "D"
     L = "L"
     W = "W"
     B = "B"


class Eventseriousness(str, Enum):
     """
     238 - Event seriousness

     Y  Yes
     S  Significant
     N  No
     """


     Y = "Y"
     S = "S"
     N = "N"


class Eventexpected(str, Enum):
     """
     239 - Event expected

     Y  Yes
     N  No
     U  Unknown
     """


     Y = "Y"
     N = "N"
     U = "U"


class Eventconsequence(str, Enum):
     """
     240 - Event consequence

     D  Death
     L  Life threatening
     H  Caused hospitalized
     P  Prolonged hospitalization
     C  Congenital anomaly/birth defect
     I  Incapacity which is significant, persistent or permanent
     J  Disability which is significant, persistent or permanent
     R  Required intervention to prevent permanent impairment/damage
     O  Other
     """


     D = "D"
     L = "L"
     H = "H"
     P = "P"
     C = "C"
     I = "I"
     J = "J"
     R = "R"
     O = "O"


class Patientoutcome(str, Enum):
     """
     241 - Patient outcome

     D  Died
     R  Recovering
     N  Not recovering/unchanged
     W  Worsening
     S  Sequelae
     F  Fully recovered
     U  Unknown
     """


     D = "D"
     R = "R"
     N = "N"
     W = "W"
     S = "S"
     F = "F"
     U = "U"


class Primaryobserversqualification(str, Enum):
     """
     242 - Primary observer s qualification

     P  Physician (osteopath, homeopath)
     R  Pharmacist
     M  Mid-level professional (nurse, nurse practitioner, physician's assistant)
     H  Other health professional
     C  Health care consumer/patient
     L  Lawyer/attorney
     O  Other non-health professional
     """


     P = "P"
     R = "R"
     M = "M"
     H = "H"
     C = "C"
     L = "L"
     O = "O"


class Identitymaybedivulged(str, Enum):
     """
     243 - Identity may be divulged

     Y  Yes
     N  No
     NA  Not applicable
     """


     Y = "Y"
     N = "N"
     NA = "NA"


class Statusofevaluation(str, Enum):
     """
     247 - Status of evaluation

     Y  Evaluation completed
     P  Evaluation in progress
     K  Problem already known, no evaluation necessary
     X  Product not made by company
     A  Evaluation anticipated, but not yet begun
     D  Product discarded -- unable to follow up
     C  Product received in condition which made analysis impossible
     I  Product remains implanted -- unable to follow up
     U  Product unavailable for follow up investigation
     Q  Product under quarantine -- unable to follow up
     R  Product under recall/corrective action
     O  Other
     """


     Y = "Y"
     P = "P"
     K = "K"
     X = "X"
     A = "A"
     D = "D"
     C = "C"
     I = "I"
     U = "U"
     Q = "Q"
     R = "R"
     O = "O"


class Productsource(str, Enum):
     """
     248 - Product source

     A  Actual product involved in incident was evaluated
     L  A product from the same lot as the actual product involved was evaluated
     R  A product from a reserve sample was evaluated
     N  A product from a controlled/non-related inventory was evaluated
     """


     A = "A"
     L = "L"
     R = "R"
     N = "N"


class Relatednessassessment(str, Enum):
     """
     250 - Relatedness assessment

     H  Highly probable
     M  Moderately probable
     S  Somewhat probable
     I  Improbable
     N  Not related
     """


     H = "H"
     M = "M"
     S = "S"
     I = "I"
     N = "N"


class Actiontakeninresponsetotheevent(str, Enum):
     """
     251 - Action taken in response to the event

     WP  Product withdrawn permanently
     WT  Product withdrawn temporarily
     DR  Product dose or frequency of use reduced
     DI  Product dose or frequency of use increased
     OT  Other
     N  None
     """


     WP = "WP"
     WT = "WT"
     DR = "DR"
     DI = "DI"
     OT = "OT"
     N = "N"


class Causalityobservations(str, Enum):
     """
     252 - Causality observations

     AW  Abatement of event after product withdrawn
     BE  Event recurred after product reintroduced
     LI  Literature reports association of product with event
     IN  Event occurred after product introduced
     EX  Alternative explanations for the event available
     PL  Effect observed when patient receives placebo
     TC  Toxic levels of product documented in blood or body fluids
     DR  Dose response observed
     SE  Similar events in past for this patient
     OE  Occurrence of event was confirmed by objective evidence
     OT  Other
     """


     AW = "AW"
     BE = "BE"
     LI = "LI"
     IN = "IN"
     EX = "EX"
     PL = "PL"
     TC = "TC"
     DR = "DR"
     SE = "SE"
     OE = "OE"
     OT = "OT"


class Indirectexposuremechanism(str, Enum):
     """
     253 - Indirect exposure mechanism

     B  Breast milk
     P  Transplacental
     F  Father
     X  Blood product
     O  Other
     """


     B = "B"
     P = "P"
     F = "F"
     X = "X"
     O = "O"


class Kindofquantity(str, Enum):
     """
     254 - Kind of quantity

     CACT  *Catalytic Activity
     CNC  *Catalytic Concentration
     CCRTO  Catalytic Concentration Ratio
     CCNT  *Catalytic Content
     CFR  *Catalytic Fraction
     CRAT  *Catalytic Rate
     CRTO  Catalytic Ratio
     ENT  *Entitic
     ENTSUB  *Entitic Substance of Amount
     ENTCAT  *Entitic Catalytic Activity
     ENTNUM  *Entitic Number
     ENTVOL  *Entitic Volume
     MASS  *Mass
     MCNC  *Mass Concentration
     MCRTO  *Mass Concentration Ratio
     MCNT  Mass Content
     MFR  *Mass Fraction
     MINC  *Mass Increment
     MRAT  *Mass Rate
     MRTO  *Mass Ratio
     NUM  *Number
     NCNC  *Number Concentration
     NCNT  *Number Content
     NFR  *Number Fraction
     NRTO  *Number Ratio
     SUB  *Substance Amount
     SCNC  *Substance Concentration
     SCRTO  *Substance Concentration Ratio
     SCNT  *Substance Content
     SCNTR  *Substance Content Rate
     SFR  *Substance Fraction
     SCNCIN  *Substance Concentration Increment
     SRAT  *Substance Rate
     SRTO  *Substance Ratio
     VOL  *Volume
     VCNT  *Volume Content
     VFR  *Volume Fraction
     VRAT  *Volume Rate
     VRTO  *Volume Ratio
     ACNC  Concentration, Arbitrary Substance
     RLMCNC  *Relative Mass Concentration
     RLSCNC  *Relative Substance Concentration
     THRMCNC  *Threshold Mass Concentration
     THRSCNC  *Threshold Substance Concentration
     TIME  *Time (e.g. seconds)
     TMDF  *Time Difference
     TMSTP  *Time Stamp -- Date and Time
     TRTO  *Time Ratio
     RCRLTM  *Reciprocal Relative Time
     RLTM  *Relative Time
     ABS  Absorbance
     ACT  *Activity
     APER  Appearance
     ARB  *Arbitrary
     AREA  Area
     ASPECT  Aspect
     CLAS  Class
     CNST  *Constant
     COEF  *Coefficient
     COLOR  Color
     CONS  Consistency
     DEN  Density
     DEV  Device
     DIFF  *Difference
     ELAS  Elasticity
     ELPOT  Electrical Potential (Voltage)
     ELRAT  Electrical current (amperage)
     ELRES  Electrical Resistance
     ENGR  Energy
     EQL  Equilibrium
     FORCE  Mechanical force
     FREQ  Frequency
     IMP  Impression/ interpretation of study
     KINV  *Kinematic Viscosity
     LEN  Length
     LINC  *Length Increment
     LIQ  *Liquefaction
     MGFLUX  Magnetic flux
     MORPH  Morphology
     MOTIL  Motility
     OD  Optical density
     OSMOL  *Osmolality
     PRID  Presence/Identity/Existence
     PRES  *Pressure (Partial)
     PWR  Power (wattage)
     RANGE  *Ranges
     RATIO  *Ratios
     RDEN  *Relative Density
     REL  *Relative
     SATFR  *Saturation Fraction
     SHAPE  Shape
     SMELL  Smell
     SUSC  *Susceptibility
     TASTE  Taste
     TEMP  *Temperature
     TEMPDF  *Temperature Difference
     TEMPIN  *Temperature Increment
     TITR  *Dilution Factor (Titer)
     TYPE  *Type
     VEL  *Velocity
     VELRT  *Velocity Ratio
     VISC  *Viscosity
     """


     CACT = "CACT"
     CNC = "CNC"
     CCRTO = "CCRTO"
     CCNT = "CCNT"
     CFR = "CFR"
     CRAT = "CRAT"
     CRTO = "CRTO"
     ENT = "ENT"
     ENTSUB = "ENTSUB"
     ENTCAT = "ENTCAT"
     ENTNUM = "ENTNUM"
     ENTVOL = "ENTVOL"
     MASS = "MASS"
     MCNC = "MCNC"
     MCRTO = "MCRTO"
     MCNT = "MCNT"
     MFR = "MFR"
     MINC = "MINC"
     MRAT = "MRAT"
     MRTO = "MRTO"
     NUM = "NUM"
     NCNC = "NCNC"
     NCNT = "NCNT"
     NFR = "NFR"
     NRTO = "NRTO"
     SUB = "SUB"
     SCNC = "SCNC"
     SCRTO = "SCRTO"
     SCNT = "SCNT"
     SCNTR = "SCNTR"
     SFR = "SFR"
     SCNCIN = "SCNCIN"
     SRAT = "SRAT"
     SRTO = "SRTO"
     VOL = "VOL"
     VCNT = "VCNT"
     VFR = "VFR"
     VRAT = "VRAT"
     VRTO = "VRTO"
     ACNC = "ACNC"
     RLMCNC = "RLMCNC"
     RLSCNC = "RLSCNC"
     THRMCNC = "THRMCNC"
     THRSCNC = "THRSCNC"
     TIME = "TIME"
     TMDF = "TMDF"
     TMSTP = "TMSTP"
     TRTO = "TRTO"
     RCRLTM = "RCRLTM"
     RLTM = "RLTM"
     ABS = "ABS"
     ACT = "ACT"
     APER = "APER"
     ARB = "ARB"
     AREA = "AREA"
     ASPECT = "ASPECT"
     CLAS = "CLAS"
     CNST = "CNST"
     COEF = "COEF"
     COLOR = "COLOR"
     CONS = "CONS"
     DEN = "DEN"
     DEV = "DEV"
     DIFF = "DIFF"
     ELAS = "ELAS"
     ELPOT = "ELPOT"
     ELRAT = "ELRAT"
     ELRES = "ELRES"
     ENGR = "ENGR"
     EQL = "EQL"
     FORCE = "FORCE"
     FREQ = "FREQ"
     IMP = "IMP"
     KINV = "KINV"
     LEN = "LEN"
     LINC = "LINC"
     LIQ = "LIQ"
     MGFLUX = "MGFLUX"
     MORPH = "MORPH"
     MOTIL = "MOTIL"
     OD = "OD"
     OSMOL = "OSMOL"
     PRID = "PRID"
     PRES = "PRES"
     PWR = "PWR"
     RANGE = "RANGE"
     RATIO = "RATIO"
     RDEN = "RDEN"
     REL = "REL"
     SATFR = "SATFR"
     SHAPE = "SHAPE"
     SMELL = "SMELL"
     SUSC = "SUSC"
     TASTE = "TASTE"
     TEMP = "TEMP"
     TEMPDF = "TEMPDF"
     TEMPIN = "TEMPIN"
     TITR = "TITR"
     TYPE = "TYPE"
     VEL = "VEL"
     VELRT = "VELRT"
     VISC = "VISC"


class Durationcategories(str, Enum):
     """
     255 - Duration categories

     PT  To identify measures at a point in time.  This is a synonym for "spot" or "random" as applied to urine measurements.
     *  (asterisk) Life of the "unit."  Used for blood products.
     30M  30 minutes
     1H  1 hour
     2H  2 hours
     2.5H  2 1/2 hours
     3H  3 hours
     4H  4 hours
     5H  5 hours
     6H  6 hours
     7H  7 hours
     8H  8 hours
     12H  12 hours
     24H  24 hours
     2D  2 days
     3D  3 days
     4D  4 days
     5D  5 days
     6D  6 days
     1W  1 week
     2W  2 weeks
     3W  3 weeks
     4W  4 weeks
     1L  1 months (30 days)
     2L  2 months
     3L  3 months
     """


     PT = "PT"
     star = "*"
     _30M = "30M"
     _1H = "1H"
     _2H = "2H"
     _2_5H = "2.5H"
     _3H = "3H"
     _4H = "4H"
     _5H = "5H"
     _6H = "6H"
     _7H = "7H"
     _8H = "8H"
     _12H = "12H"
     _24H = "24H"
     _2D = "2D"
     _3D = "3D"
     _4D = "4D"
     _5D = "5D"
     _6D = "6D"
     _1W = "1W"
     _2W = "2W"
     _3W = "3W"
     _4W = "4W"
     _1L = "1L"
     _2L = "2L"
     _3L = "3L"


class Timedelaypostchallenge(str, Enum):
     """
     256 - Time delay post challenge

     BS  Baseline (time just before the challenge)
     PEAK  The time post drug dose at which the highest drug level is reached (differs by drug)
     TROUGH  The time post drug dose at which the lowest drug level is reached (varies with drug)
     RANDOM  Time from the challenge, or dose not specified. (random)
     1M  1 minute post challenge
     2M  2 minutes post challenge
     3M  3 minutes post challenge
     4M  4 minutes post challenge
     5M  5 minutes post challenge
     6M  6 minutes post challenge
     7M  7 minutes post challenge
     8M  8 minutes post challenge
     9M  9 minutes post challenge
     10M  10 minutes post challenge
     15M  15 minutes post challenge
     20M  20 minutes post challenge
     25M  25 minutes post challenge
     30M  30 minutes post challenge
     1H  1 hour post challenge
     2H  2 hours post challenge
     2.5H  2 1/2 hours post challenge
     3H  3 hours post challenge
     4H  4 hours post challenge
     5H  5  hours post challenge
     6H  6 hours post challenge
     7H  7 hours post challenge
     8H  8 hours post challenge
     8H SHIFT  8 hours aligned on nursing shifts
     12H  12 hours post challenge
     24H  24 hours post challenge
     2D  2 days
     3D  3 days
     4D  4 days
     5D  5 days
     6D  6 days
     7D  7 days
     1W  1 week
     10D  10 days
     2W  2 weeks
     3W  3 weeks
     4W  4 weeks
     1L  1 month (30 days) post challenge
     2L  2 months (60 days) post challenge
     3L  3 months (90 days) post challenge
     """


     BS = "BS"
     PEAK = "PEAK"
     TROUGH = "TROUGH"
     RANDOM = "RANDOM"
     _1M = "1M"
     _2M = "2M"
     _3M = "3M"
     _4M = "4M"
     _5M = "5M"
     _6M = "6M"
     _7M = "7M"
     _8M = "8M"
     _9M = "9M"
     _10M = "10M"
     _15M = "15M"
     _20M = "20M"
     _25M = "25M"
     _30M = "30M"
     _1H = "1H"
     _2H = "2H"
     _2_5H = "2.5H"
     _3H = "3H"
     _4H = "4H"
     _5H = "5H"
     _6H = "6H"
     _7H = "7H"
     _8H = "8H"
     _8H_SHIFT = "8H SHIFT"
     _12H = "12H"
     _24H = "24H"
     _2D = "2D"
     _3D = "3D"
     _4D = "4D"
     _5D = "5D"
     _6D = "6D"
     _7D = "7D"
     _1W = "1W"
     _10D = "10D"
     _2W = "2W"
     _3W = "3W"
     _4W = "4W"
     _1L = "1L"
     _2L = "2L"
     _3L = "3L"


class Natureofchallenge(str, Enum):
     """
     257 - Nature of challenge

     CFST  Fasting (no calorie intake) for the period specified in the time component of the term, e.g., 1H POST CFST
     EXCZ  Exercise undertaken as challenge (can be quantified)
     FFST  No fluid intake for the period specified in the time component of the term
     """


     CFST = "CFST"
     EXCZ = "EXCZ"
     FFST = "FFST"


class Relationshipmodifier(str, Enum):
     """
     258 - Relationship modifier

     CONTROL  Control
     PATIENT  Patient
     DONOR  Donor
     BPU  Blood product unit
     """


     CONTROL = "CONTROL"
     PATIENT = "PATIENT"
     DONOR = "DONOR"
     BPU = "BPU"


class Modality(str, Enum):
     """
     259 - Modality

     AS  Angioscopy
     BS  Biomagnetic imaging
     CD  Color flow Doppler
     CP  Colposcopy
     CR  Computed radiography
     CS  Cystoscopy
     CT  Computed tomography
     DD  Duplex Doppler
     DG  Diapanography
     DM  Digital microscopy
     EC  Echocardiography
     ES  Endoscopy
     FA  Fluorescein angiography
     FS  Fundoscopy
     LP  Laparoscopy
     LS  Laser surface scan
     MA  Magnetic resonance angiography
     MS  Magnetic resonance spectroscopy
     NM  Nuclear Medicine (radioisotope study)
     OT  Other
     PT  Positron emission tomography (PET)
     RF  Radio fluoroscopy
     ST  Single photon emission computed tomography (SPECT)
     TG  Thermography
     US  Ultrasound
     XA  X-ray Angiography
     """


     AS = "AS"
     BS = "BS"
     CD = "CD"
     CP = "CP"
     CR = "CR"
     CS = "CS"
     CT = "CT"
     DD = "DD"
     DG = "DG"
     DM = "DM"
     EC = "EC"
     ES = "ES"
     FA = "FA"
     FS = "FS"
     LP = "LP"
     LS = "LS"
     MA = "MA"
     MS = "MS"
     NM = "NM"
     OT = "OT"
     PT = "PT"
     RF = "RF"
     ST = "ST"
     TG = "TG"
     US = "US"
     XA = "XA"


class Patientlocationtype(str, Enum):
     """
     260 - Patient location type

     N  Nursing Unit
     R  Room
     B  Bed
     E  Exam Room
     O  Operating Room
     C  Clinic
     D  Department
     L  Other Location
     """


     N = "N"
     R = "R"
     B = "B"
     E = "E"
     O = "O"
     C = "C"
     D = "D"
     L = "L"


class Locationequipment(str, Enum):
     """
     261 - Location equipment

     OXY  Oxygen
     SUC  Suction
     VIT  Vital signs monitor
     INF  Infusion pump
     IVP  IV pump
     EEG  Electro-Encephalogram
     EKG  Electro-Cardiogram
     VEN  Ventilator
     """


     OXY = "OXY"
     SUC = "SUC"
     VIT = "VIT"
     INF = "INF"
     IVP = "IVP"
     EEG = "EEG"
     EKG = "EKG"
     VEN = "VEN"


class Privacylevel(str, Enum):
     """
     262 - Privacy level

     F  Isolation
     P  Private room
     J  Private room - medically justified
     Q  Private room - due to overflow
     S  Semi-private room
     W  Ward
     """


     F = "F"
     P = "P"
     J = "J"
     Q = "Q"
     S = "S"
     W = "W"


class Levelofcare(str, Enum):
     """
     263 - Level of care

     A  Ambulatory
     E  Emergency
     F  Isolation
     N  Intensive care
     C  Critical care
     R  Routine
     S  Surgery
     """


     A = "A"
     E = "E"
     F = "F"
     N = "N"
     C = "C"
     R = "R"
     S = "S"


class Specialtytype(str, Enum):
     """
     265 - Specialty type

     AMB  Ambulatory
     PSY  Psychiatric
     PPS  Pediatric psychiatric
     REH  Rehabilitation
     PRE  Pediatric rehabilitation
     ISO  Isolation
     OBG  Obstetrics, gynecology
     PIN  Pediatric/neonatal intensive care
     INT  Intensive care
     SUR  Surgery
     PSI  Psychiatric intensive care
     EDI  Education
     CAR  Coronary/cardiac care
     NBI  Newborn, nursery, infants
     CCR  Critical care
     PED  Pediatrics
     EMR  Emergency
     OBS  Observation
     WIC  Walk-in clinic
     PHY  General/family practice
     ALC  Allergy
     FPC  Family planning
     CHI  Chiropractic
     CAN  Cancer
     NAT  Naturopathic
     OTH  Other specialty
     """


     AMB = "AMB"
     PSY = "PSY"
     PPS = "PPS"
     REH = "REH"
     PRE = "PRE"
     ISO = "ISO"
     OBG = "OBG"
     PIN = "PIN"
     INT = "INT"
     SUR = "SUR"
     PSI = "PSI"
     EDI = "EDI"
     CAR = "CAR"
     NBI = "NBI"
     CCR = "CCR"
     PED = "PED"
     EMR = "EMR"
     OBS = "OBS"
     WIC = "WIC"
     PHY = "PHY"
     ALC = "ALC"
     FPC = "FPC"
     CHI = "CHI"
     CAN = "CAN"
     NAT = "NAT"
     OTH = "OTH"


class Daysoftheweek(str, Enum):
     """
     267 - Days of the week

     SAT  Saturday
     SUN  Sunday
     MON  Monday
     TUE  Tuesday
     WED  Wednesday
     THU  Thursday
     FRI  Friday
     """


     SAT = "SAT"
     SUN = "SUN"
     MON = "MON"
     TUE = "TUE"
     WED = "WED"
     THU = "THU"
     FRI = "FRI"


class Override(str, Enum):
     """
     268 - Override

     X  Override not allowed
     A  Override allowed
     R  Override required
     """


     X = "X"
     A = "A"
     R = "R"


class Chargeonindicator(str, Enum):
     """
     269 - Charge on indicator

     O  Charge on Order
     R  Charge on Result
     """


     O = "O"
     R = "R"


class Documenttype(str, Enum):
     """
     270 - Document type

     AR  Autopsy report
     CD  Cardiodiagnostics
     CN  Consultation
     DI  Diagnostic imaging
     DS  Discharge summary
     ED  Emergency department report
     HP  History and physical examination
     OP  Operative report
     PC  Psychiatric consultation
     PH  Psychiatric history and physical examination
     PN  Procedure note
     PR  Progress note
     SP  Surgical pathology
     TS  Transfer summary
     """


     AR = "AR"
     CD = "CD"
     CN = "CN"
     DI = "DI"
     DS = "DS"
     ED = "ED"
     HP = "HP"
     OP = "OP"
     PC = "PC"
     PH = "PH"
     PN = "PN"
     PR = "PR"
     SP = "SP"
     TS = "TS"


class Documentcompletionstatus(str, Enum):
     """
     271 - Document completion status

     DI  Dictated
     DO  Documented
     IP  In Progress
     IN  Incomplete
     PA  Pre-authenticated
     AU  Authenticated
     LA  Legally authenticated
     """


     DI = "DI"
     DO = "DO"
     IP = "IP"
     IN = "IN"
     PA = "PA"
     AU = "AU"
     LA = "LA"


class Documentconfidentialitystatus(str, Enum):
     """
     272 - Document confidentiality status

     V  Very restricted
     R  Restricted
     U  Usual control
     """


     V = "V"
     R = "R"
     U = "U"


class Documentavailabilitystatus(str, Enum):
     """
     273 - Document availability status

     AV  Available for patient care
     CA  Deleted
     OB  Obsolete
     UN  Unavailable for patient care
     """


     AV = "AV"
     CA = "CA"
     OB = "OB"
     UN = "UN"


class Documentstoragestatus(str, Enum):
     """
     275 - Document storage status

     AC  Active
     AA  Active and archived
     AR  Archived (not active)
     PU  Purged
     """


     AC = "AC"
     AA = "AA"
     AR = "AR"
     PU = "PU"


class Appointmentreasoncodes(str, Enum):
     """
     276 - Appointment reason codes

     ROUTINE  Routine appointment - default if not valued
     WALKIN  A previously unscheduled walk-in visit
     CHECKUP  A routine check-up, such as an annual physical
     FOLLOWUP  A follow up visit from a previous appointment
     EMERGENCY  Emergency appointment
     """


     ROUTINE = "ROUTINE"
     WALKIN = "WALKIN"
     CHECKUP = "CHECKUP"
     FOLLOWUP = "FOLLOWUP"
     EMERGENCY = "EMERGENCY"


class Appointmenttypecodes(str, Enum):
     """
     277 - Appointment type codes

     Normal  Routine schedule request type - default if not valued
     Tentative  A request for a tentative (e.g., "penciled in") appointment
     Complete  A request to add a completed appointment, used to maintain records of completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)
     """


     N_mal = "Normal"
     Tentative = "Tentative"
     Complete = "Complete"


class Fillerstatuscodes(str, Enum):
     """
     278 - Filler status codes

     Pending  Appointment has not yet been confirmed
     Waitlist  Appointment has been placed on a waiting list for a particular slot, or set of slots
     Booked  The indicated appointment is booked
     Started  The indicated appointment has begun and is currently in progress
     Complete  The indicated appointment has completed normally (was not discontinued, canceled, or deleted)
     Cancelled  The indicated appointment was stopped from occurring (canceled prior to starting)
     Discontinued  The indicated appointment was discontinued (DC'ed while in progress, discontinued parent appointment, or discontinued child appointment)
     Deleted  The indicated appointment was deleted from the filler application
     Blocked  The indicated time slot(s) is(are) blocked
     Overbook  The appointment has been confirmed; however it is confirmed in an overbooked state
     """


     Pending = "Pending"
     Waitlist = "Waitlist"
     Booked = "Booked"
     Started = "Started"
     Complete = "Complete"
     Cancelled = "Cancelled"
     Discontinued = "Discontinued"
     Deleted = "Deleted"
     Blocked = "Blocked"
     Overbook = "Overbook"


class Allowsubstitutioncodes(str, Enum):
     """
     279 - Allow substitution codes

     No  Substitution of this resource is not allowed
     Confirm  Contact the Placer Contact Person prior to making any substitutions of this resource
     Notify  Notify the Placer Contact Person, through normal institutional procedures, that a substitution of this resource has been made
     Yes  Substitution of this resource is allowed
     """


     No = "No"
     Confirm = "Confirm"
     Notify = "Notify"
     Yes = "Yes"


class Referralpriority(str, Enum):
     """
     280 - Referral priority

     S  STAT
     A  ASAP
     R  Routine
     """


     S = "S"
     A = "A"
     R = "R"


class Referraltype(str, Enum):
     """
     281 - Referral type

     Lab  Laboratory
     Rad  Radiology
     Med  Medical
     Skn  Skilled Nursing
     Psy  Psychiatric
     Hom  Home Care
     """


     Lab = "Lab"
     Rad = "Rad"
     Med = "Med"
     Skn = "Skn"
     Psy = "Psy"
     Hom = "Hom"


class Referraldisposition(str, Enum):
     """
     282 - Referral disposition

     WR  Send Written Report
     RP  Return Patient After Evaluation
     AM  Assume Management
     SO  Second Opinion
     """


     WR = "WR"
     RP = "RP"
     AM = "AM"
     SO = "SO"


class Referralstatus(str, Enum):
     """
     283 - Referral status

     A  Accepted
     P  Pending
     R  Rejected
     E  Expired
     """


     A = "A"
     P = "P"
     R = "R"
     E = "E"


class Referralcategory(str, Enum):
     """
     284 - Referral category

     I  Inpatient
     O  Outpatient
     A  Ambulatory
     E  Emergency
     """


     I = "I"
     O = "O"
     A = "A"
     E = "E"


class Providerrole(str, Enum):
     """
     286 - Provider role

     RP  Referring Provider
     PP  Primary Care Provider
     CP  Consulting Provider
     RT  Referred to Provider
     """


     RP = "RP"
     PP = "PP"
     CP = "CP"
     RT = "RT"


class Problem_goalactioncode(str, Enum):
     """
     287 - Problem-goal action code

     AD  ADD
     CO  CORRECT
     DE  DELETE
     LI  LINK
     UC  UNCHANGED
     UN  UNLINK
     UP  UPDATE
     """


     AD = "AD"
     CO = "CO"
     DE = "DE"
     LI = "LI"
     UC = "UC"
     UN = "UN"
     UP = "UP"


class MIMEbase64encodingcharacters(str, Enum):
     """
     290 - MIME base64 encoding characters

     0  A
     1  B
     2  C
     3  D
     4  E
     5  F
     6  G
     7  H
     8  I
     9  J
     10  K
     11  L
     12  M
     13  N
     14  O
     15  P
     17  R
     16  Q
     18  S
     19  T
     20  U
     21  V
     22  W
     23  X
     24  Y
     25  Z
     26  a
     27  b
     28  c
     29  d
     30  e
     31  f
     32  g
     33  h
     34  I
     35  j
     36  k
     37  l
     38  m
     39  n
     40  o
     41  p
     42  q
     43  r
     44  s
     45  t
     46  u
     47  v
     48  w
     49  x
     50  y
     51  z
     52  0
     53  1
     54  2
     55  3
     56  4
     57  5
     58  6
     59  7
     60  8
     61  9
     62  +
     63  /
     (pad)  =
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"
     _7 = "7"
     _8 = "8"
     _9 = "9"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _13 = "13"
     _14 = "14"
     _15 = "15"
     _17 = "17"
     _16 = "16"
     _18 = "18"
     _19 = "19"
     _20 = "20"
     _21 = "21"
     _22 = "22"
     _23 = "23"
     _24 = "24"
     _25 = "25"
     _26 = "26"
     _27 = "27"
     _28 = "28"
     _29 = "29"
     _30 = "30"
     _31 = "31"
     _32 = "32"
     _33 = "33"
     _34 = "34"
     _35 = "35"
     _36 = "36"
     _37 = "37"
     _38 = "38"
     _39 = "39"
     _40 = "40"
     _41 = "41"
     _42 = "42"
     _43 = "43"
     _44 = "44"
     _45 = "45"
     _46 = "46"
     _47 = "47"
     _48 = "48"
     _49 = "49"
     _50 = "50"
     _51 = "51"
     _52 = "52"
     _53 = "53"
     _54 = "54"
     _55 = "55"
     _56 = "56"
     _57 = "57"
     _58 = "58"
     _59 = "59"
     _60 = "60"
     _61 = "61"
     _62 = "62"
     _63 = "63"
     (pad) = "(pad)"


class SubtypeofReferencedData(str, Enum):
     """
     291 - Subtype of Referenced Data

     BASIC  ISDN PCM audio data
     DICOM  Digital Imaging and Communications in Medicine
     FAX  Facsimile data
     GIF  Graphics Interchange Format
     HTML  Hypertext Markup Language
     JOT  Electronic ink data (Jot 1.0 standard)
     JPEG  Joint Photographic Experts Group
     Octet-stream  Uninterpreted binary data
     PICT  PICT format image data
     PostScript  PostScript program
     RTF  Rich Text Format
     SGML  Standard Generalized Markup Language (HL7 V2.3.1 and later)
     TIFF  TIFF image data
     x-hl7-cda-level-one  HL7 Clinical Document Architecture Level One document
     XML  Extensible Markup Language (HL7 V2.3.1 and later)
     """


     BASIC = "BASIC"
     DICOM = "DICOM"
     FAX = "FAX"
     GIF = "GIF"
     HTML = "HTML"
     JOT = "JOT"
     JPEG = "JPEG"
     Octet_stream = "Octet-stream"
     PICT = "PICT"
     PostScript = "PostScript"
     RTF = "RTF"
     SGML = "SGML"
     TIFF = "TIFF"
     x_hl7_cda_level_one = "x-hl7-cda-level-one"
     XML = "XML"


class Vaccinesadministered(str, Enum):
     """
     292 - Vaccines administered

     54  adenovirus vaccine, type 4, live, oral
     55  adenovirus vaccine, type 7, live, oral
     82  adenovirus vaccine, NOS
     24  anthrax vaccine
     19  Bacillus Calmette-Guerin vaccine
     27  botulinum antitoxin
     26  cholera vaccine
     29  cytomegalovirus immune globulin, intravenous
     56  dengue fever vaccine
     12  diphtheria antitoxin
     28  diphtheria and tetanus toxoids, adsorbed for pediatric use
     20  diphtheria, tetanus toxoids and acellular pertussis vaccine
     50  DTaP-Haemophilus influenzae type b conjugate vaccine
     01  diphtheria, tetanus toxoids and pertussis vaccine
     22  DTP-Haemophilus influenzae type b conjugate vaccine
     57  hantavirus vaccine
     52  hepatitis A vaccine, adult dosage
     83  hepatitis A vaccine, pediatric/adolescent dosage, 2 dose schedule
     84  hepatitis A vaccine, pediatric/adolescent dosage, 3 dose schedule
     31  hepatitis A vaccine, pediatric dosage, NOS
     85  hepatitis A vaccine, NOS
     30  hepatitis B immune globulin
     08  hepatitis B vaccine, pediatric or pediatric/adolescent dosage
     42  hepatitis B vaccine, adolescent/high risk infant dosage
     43  hepatitis B vaccine, adult dosage
     44  hepatitis B vaccine, dialysis patient dosage
     45  hepatitis B vaccine, NOS
     58  hepatitis C vaccine
     59  hepatitis E vaccine
     60  herpes simplex virus, type 2 vaccine
     46  Haemophilus influenzae type b vaccine, PRP-D conjugate
     47  Haemophilus influenzae type b vaccine, HbOC conjugate
     48  Haemophilus influenzae type b vaccine, PRP-T conjugate
     49  Haemophilus influenzae type b vaccine, PRP-OMP conjugate
     17  Haemophilus influenzae type b vaccine, conjugate NOS
     51  Haemophilus influenzae type b conjugate and Hepatitis B vaccine
     61  human immunodeficiency virus vaccine
     62  human papilloma virus vaccine
     86  immune globulin, intramuscular
     87  immune globulin, intravenous
     14  immune globulin, NOS
     15  influenza virus vaccine, split virus (incl. purified surface antigen)
     16  influenza virus vaccine, whole virus
     88  influenza virus vaccine, NOS
     10  poliovirus vaccine, inactivated
     02  poliovirus vaccine, live, oral
     89  poliovirus vaccine, NOS
     39  Japanese encephalitis vaccine
     63  Junin virus vaccine
     64  leishmaniasis vaccine
     65  leprosy vaccine
     66  Lyme disease vaccine
     03  measles, mumps and rubella virus vaccine
     04  measles and rubella virus vaccine
     94  measles, mumps, rubella, and varicella virus vaccine
     67  malaria vaccine
     05  measles virus vaccine
     68  melanoma vaccine
     32  meningococcal polysaccharide vaccine
     07  mumps virus vaccine
     69  parainfluenza-3 virus vaccine
     11  pertussis vaccine
     23  plague vaccine
     33  pneumococcal  polysaccharide vaccine
     100  pneumococcal conjugate vaccine, polyvalent
     70  Q fever vaccine
     18  rabies vaccine, for intramuscular injection
     40  rabies vaccine, for intradermal injection
     90  rabies vaccine, NOS
     72  rheumatic fever vaccine
     73  Rift Valley fever vaccine
     34  rabies immune globulin
     74  rotavirus vaccine, tetravalent, live, oral
     71  respiratory syncytial virus immune globulin, intravenous
     93  respiratory syncytial virus monoclonal antibody (palivizumab), intramuscular
     06  rubella virus vaccine
     38  rubella and mumps virus vaccine
     75  smallpox vaccine
     76  Staphylococcus bacteriophage lysate
     09  tetanus and diphtheria toxoids, adsorbed for adult use
     35  tetanus toxoid
     77  tick-borne encephalitis vaccine
     13  tetanus immune globulin
     95  tuberculin skin test; old tuberculin, multipuncture device
     96  tuberculin skin test; purified protein derivative solution, intradermal
     97  tuberculin skin test; purified protein derivative, multipuncture device
     98  tuberculin skin test; NOS
     78  tularemia vaccine
     25  typhoid vaccine, live, oral
     41  typhoid vaccine, parenteral, other than acetone-killed, dried
     53  typhoid vaccine, parenteral, acetone-killed, dried (U.S. military)
     101  Typhoid Vi capsular polysaccharide vaccine
     91  typhoid vaccine, NOS
     79  vaccinia immune globulin
     21  varicella virus vaccine
     81  Venezuelan equine encephalitis, inactivated
     80  Venezuelan equine encephalitis, live, attenuated
     92  Venezuelan equine encephalitis vaccine, NOS
     36  varicella zoster immune globulin
     37  yellow fever vaccine
     999  unknown vaccine or immune globulin
     99  RESERVED - do not use
     """


     _54 = "54"
     _55 = "55"
     _82 = "82"
     _24 = "24"
     _19 = "19"
     _27 = "27"
     _26 = "26"
     _29 = "29"
     _56 = "56"
     _12 = "12"
     _28 = "28"
     _20 = "20"
     _50 = "50"
     _01 = "01"
     _22 = "22"
     _57 = "57"
     _52 = "52"
     _83 = "83"
     _84 = "84"
     _31 = "31"
     _85 = "85"
     _30 = "30"
     _08 = "08"
     _42 = "42"
     _43 = "43"
     _44 = "44"
     _45 = "45"
     _58 = "58"
     _59 = "59"
     _60 = "60"
     _46 = "46"
     _47 = "47"
     _48 = "48"
     _49 = "49"
     _17 = "17"
     _51 = "51"
     _61 = "61"
     _62 = "62"
     _86 = "86"
     _87 = "87"
     _14 = "14"
     _15 = "15"
     _16 = "16"
     _88 = "88"
     _10 = "10"
     _02 = "02"
     _89 = "89"
     _39 = "39"
     _63 = "63"
     _64 = "64"
     _65 = "65"
     _66 = "66"
     _03 = "03"
     _04 = "04"
     _94 = "94"
     _67 = "67"
     _05 = "05"
     _68 = "68"
     _32 = "32"
     _07 = "07"
     _69 = "69"
     _11 = "11"
     _23 = "23"
     _33 = "33"
     _100 = "100"
     _70 = "70"
     _18 = "18"
     _40 = "40"
     _90 = "90"
     _72 = "72"
     _73 = "73"
     _34 = "34"
     _74 = "74"
     _71 = "71"
     _93 = "93"
     _06 = "06"
     _38 = "38"
     _75 = "75"
     _76 = "76"
     _09 = "09"
     _35 = "35"
     _77 = "77"
     _13 = "13"
     _95 = "95"
     _96 = "96"
     _97 = "97"
     _98 = "98"
     _78 = "78"
     _25 = "25"
     _41 = "41"
     _53 = "53"
     _101 = "101"
     _91 = "91"
     _79 = "79"
     _21 = "21"
     _81 = "81"
     _80 = "80"
     _92 = "92"
     _36 = "36"
     _37 = "37"
     _999 = "999"
     _99 = "99"


class Timeselectioncriteriaparameterclasscodes(str, Enum):
     """
     294 - Time selection criteria parameter class codes

     Prefstart  The preferred start time for the appointment request, service or resource.   Any legal time specification in the format HHMM, using 24-hour clock notation
     Prefend  The preferred end time for the appointment request, service or resource.  Any legal time specification in the format HHMM, using 24-hour clock notation
     Mon  An indicator that Monday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     Tue  An indicator that Tuesday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     Wed  An indicator that Wednesday is or is not preferred for the day on which the appointment will occur. OK = Preferred appointment day; NO = Day is not preferred
     Thu  An indicator that Thursday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     Fri  An indicator that Friday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     Sat  An indicator that Saturday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     Sun  An indicator that Sunday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day; NO = Day is not preferred
     """


     Prefstart = "Prefstart"
     Prefend = "Prefend"
     Mon = "Mon"
     Tue = "Tue"
     Wed = "Wed"
     Thu = "Thu"
     Fri = "Fri"
     Sat = "Sat"
     Sun = "Sun"


class CPRangeType(str, Enum):
     """
     298 - CP Range Type

     P  Pro-rate.  Apply this price to this interval, pro-rated by whatever portion of the interval has occurred/been consumed
     F  Flat-rate.  Apply the entire price to this interval, do not pro-rate the price if the full interval has not occurred/been consumed
     """


     P = "P"
     F = "F"


class Encoding(str, Enum):
     """
     299 - Encoding

     A  No encoding - data are displayable ASCII characters.
     Hex  Hexadecimal encoding - consecutive pairs of hexadecimal digits represent consecutive single octets.
     Base64  Encoding as defined by MIME (Multipurpose Internet Mail Extensions) standard RFC 1521.  Four consecutive ASCII characters represent three consecutive octets of binary data.  Base64 utilizes a 65-character subset of US-ASCII, consisting of both the upper a
     """


     A = "A"
     Hex = "Hex"
     Base64 = "Base64"


class UniversalIDtype(str, Enum):
     """
     301 - Universal ID type

     DNS  An Internet dotted name. Either in ASCII or as integers
     GUID  Same as UUID.
     HCD  The CEN Healthcare Coding Scheme Designator. (Identifiers used in DICOM follow this assignment scheme.)
     HL7  Reserved for future HL7 registration schemes
     ISO  An International Standards Organization Object Identifier
     N  These are reserved for locally defined coding schemes.
     M  These are reserved for locally defined coding schemes.
     L,M,N  These are reserved for locally defined coding schemes.
     L  These are reserved for locally defined coding schemes.
     Random  Usually a base64 encoded string of random bits.   The uniqueness depends on the length of the bits.  Mail systems often generate ASCII string  "unique names," from a combination of random bits and system names.  Obviously, such identifiers will not be con
     UUID  The DCE Universal Unique Identifier
     x400  An X.400 MHS format identifier
     x500  An X.500 directory name
     """


     DNS = "DNS"
     GUID = "GUID"
     HCD = "HCD"
     HL7 = "HL7"
     ISO = "ISO"
     N = "N"
     M = "M"
     L_M_N = "L,M,N"
     L = "L"
     Random = "Random"
     UUID = "UUID"
     x400 = "x400"
     x500 = "x500"


class Personlocationtype(str, Enum):
     """
     305 - Person location type

     C  Clinic
     D  Department
     H  Home
     N  Nursing Unit
     O  Provider's Office
     P  Phone
     S  SNF
     """


     C = "C"
     D = "D"
     H = "H"
     N = "N"
     O = "O"
     P = "P"
     S = "S"


class Coveragetype(str, Enum):
     """
     309 - Coverage type

     H  Hospital/institutional
     P  Physician/professional
     B  Both hospital and physician
     """


     H = "H"
     P = "P"
     B = "B"


class Jobstatus(str, Enum):
     """
     311 - Job status

     P  Permanent
     T  Temporary
     O  Other
     U  Unknown
     """


     P = "P"
     T = "T"
     O = "O"
     U = "U"


class Livingwillcode(str, Enum):
     """
     315 - Living will code

     Y  Yes, patient has a living will
     F  Yes, patient has a living will but it is not on file
     N  No, patient does not have a living will and no information was provided
     I  No, patient does not have a living will but information was provided
     U  Unknown
     """


     Y = "Y"
     F = "F"
     N = "N"
     I = "I"
     U = "U"


class Organdonorcode(str, Enum):
     """
     316 - Organ donor code

     Y  Yes, patient is a documented donor and documentation is on file
     F  Yes, patient is a documented donor, but documentation is not on file
     N  No, patient has not agreed to be a donor
     I  No, patient is not a documented donor, but information was provided
     R  Patient leaves organ donation decision to relatives
     P  Patient leaves organ donation decision to a specific person
     U  Unknown
     """


     Y = "Y"
     F = "F"
     N = "N"
     I = "I"
     R = "R"
     P = "P"
     U = "U"


class Annotations(str, Enum):
     """
     317 - Annotations

     9900  Pace spike
     9901  SAS marker
     9902  Sense marker
     9903  Beat marker
     9904  etc.
     """


     _9900 = "9900"
     _9901 = "9901"
     _9902 = "9902"
     _9903 = "9903"
     _9904 = "9904"


class Dispensemethod(str, Enum):
     """
     321 - Dispense method

     TR  Traditional
     UD  Unit Dose
     F  Floor Stock
     AD  Automatic Dispensing
     """


     TR = "TR"
     UD = "UD"
     F = "F"
     AD = "AD"


class Completionstatus(str, Enum):
     """
     322 - Completion status

     CP  Complete
     RE  Refused
     NA  Not Administered
     PA  Partially Administered
     """


     CP = "CP"
     RE = "RE"
     NA = "NA"
     PA = "PA"


class Actioncode(str, Enum):
     """
     323 - Action code

     A  Add/Insert
     D  Delete
     U  Update
     """


     A = "A"
     D = "D"
     U = "U"


class LocationcharacteristicID(str, Enum):
     """
     324 - Location characteristic ID

     SMK  Smoking
     LIC  Licensed
     IMP  Implant: can be used for radiation implant patients
     SHA  Shadow: a temporary holding location that does not physically exist
     INF  Infectious disease: this location can be used for isolation
     PRL  Privacy level: indicating the level of private versus non-private room
     LCR  Level of care
     OVR  Overflow
     STF  Bed is staffed
     SET  Bed is set up
     GEN  Gender of patient(s)
     TEA  Teaching location
     """


     SMK = "SMK"
     LIC = "LIC"
     IMP = "IMP"
     SHA = "SHA"
     INF = "INF"
     PRL = "PRL"
     LCR = "LCR"
     OVR = "OVR"
     STF = "STF"
     SET = "SET"
     GEN = "GEN"
     TEA = "TEA"


class LocationrelationshipID(str, Enum):
     """
     325 - Location relationship ID

     RX  Nearest  pharmacy
     RX2  Second nearest pharmacy
     LAB  Nearest  lab
     LB2  Second nearest lab
     DTY  Nearest  dietary location
     ALI  Location Alias(es)
     PAR  Parent location
     """


     RX = "RX"
     RX2 = "RX2"
     LAB = "LAB"
     LB2 = "LB2"
     DTY = "DTY"
     ALI = "ALI"
     PAR = "PAR"


class Visitindicator(str, Enum):
     """
     326 - Visit indicator

     A  Account level (default)
     V  Visit level
     """


     A = "A"
     V = "V"


class Quantitymethod(str, Enum):
     """
     329 - Quantity method

     A  Actual count
     E  Estimated (see comment)
     """


     A = "A"
     E = "E"


class Marketingbasis(str, Enum):
     """
     330 - Marketing basis

     510K  510 (K)
     510E  510 (K) exempt
     PMA  Premarketing authorization
     PRE  Preamendment
     TXN  Transitional
     522S  Post marketing study (522)
     """


     _510K = "510K"
     _510E = "510E"
     PMA = "PMA"
     PRE = "PRE"
     TXN = "TXN"
     _522S = "522S"


class Facilitytype(str, Enum):
     """
     331 - Facility type

     U  User
     M  Manufacturer
     D  Distributor
     A  Agent for a foreign manufacturer
     """


     U = "U"
     M = "M"
     D = "D"
     A = "A"


class Sourcetype(str, Enum):
     """
     332 - Source type

     I  Initiate
     A  Accept
     """


     I = "I"
     A = "A"


class Disabledperson(str, Enum):
     """
     334 - Disabled person

     PT  Patient
     GT  Guarantor
     IN  Insured
     AP  Associated party
     """


     PT = "PT"
     GT = "GT"
     IN = "IN"
     AP = "AP"


class Repeatpattern(str, Enum):
     """
     335 - Repeat pattern

     Q<integer>S  every  seconds
     Q<integer>M  every  minutes
     Q<integer>H  every  hours
     Q<integer>D  every  days
     Q<integer>W  every  weeks
     Q<integer>L  every  months (Lunar cycle)
     Q<integer>J<day#>  repeats on a particular day of the week, from the French jour (day).  If  is missing, the repeat rate is assumed to be 1.  Day numbers are counted from 1=Monday to 7=Sunday.  So Q2J2 means every second Tuesday; Q1J6 means every Saturday.
     BID  twice a day at institution-specified times (e.g., 9AM-4PM)
     TID  three times a day at institution-specified times (e.g., 9AM-4PM-9PM)
     QID  four times a day at institution-specified times (e.g., 9AM-11AM-4PM-9PM)
     xID  "X" times per day at institution-specified times, where X is a numeral 5 or greater.  E.g., 5ID=five times per day; 8ID=8 times per day
     QAM  in the morning at institution-specified time
     QSHIFT  during each of three eight-hour shifts at institution-specified times
     QOD  every other day (same as Q2D)
     QHS  every day before the hour of sleep
     QPM  in the evening at institution-specified time
     C  service is provided continuously between start time and stop time
     U <spec>  for future use, where  is an interval specification as defined by the UNIX cron specification.
     PRN  given as needed
     PRNxxx  where xxx is some frequency code (e.g., PRNQ6H); given as needed over the frequency period.
     Once  one time only.  This is also the default when this component is null.
     Meal Related Timings  C ("cum")
     A  Ante (before)
     P  Post (after)
     I  Inter (e.g., between this meal and the next, between dinner and sleep
     M  Cibus Matutinus (breakfast)
     D  Cibus Diurnus (lunch)
     V  Cibus Vespertinus (dinner)
     """


     Q_integer_S = "Q<integer>S"
     Q_integer_M = "Q<integer>M"
     Q_integer_H = "Q<integer>H"
     Q_integer_D = "Q<integer>D"
     Q_integer_W = "Q<integer>W"
     Q_integer_L = "Q<integer>L"
     Q_integer_J_dayhashtag_ = "Q<integer>J<day#>"
     BID = "BID"
     TID = "TID"
     QID = "QID"
     xID = "xID"
     QAM = "QAM"
     QSHIFT = "QSHIFT"
     QOD = "QOD"
     QHS = "QHS"
     QPM = "QPM"
     C = "C"
     U__spec_ = "U <spec>"
     PRN = "PRN"
     PRNxxx = "PRNxxx"
     Once = "Once"
     Meal_Related_Timings = "Meal Related Timings"
     A = "A"
     P = "P"
     I = "I"
     M = "M"
     D = "D"
     V = "V"


class Referralreason(str, Enum):
     """
     336 - Referral reason

     S  Second Opinion
     P  Patient Preference
     O  Provider Ordered
     W  Work Load
     """


     S = "S"
     P = "P"
     O = "O"
     W = "W"


class Certificationstatus(str, Enum):
     """
     337 - Certification status

     C  Certified
     E  Eligible
     """


     C = "C"
     E = "E"


class PractitionerIDnumbertype(str, Enum):
     """
     338 - Practitioner ID number type

     CY  County number
     DEA  Drug Enforcement Agency no.
     GL  General ledger number
     L&I  Labor and industries number
     MCD  Medicaid number
     MCR  Medicare number
     QA  QA number
     SL  State license number
     TAX  Tax ID number
     TRL  Training license number
     UPIN  Unique physician ID no.
     """


     CY = "CY"
     DEA = "DEA"
     GL = "GL"
     L_I = "L&I"
     MCD = "MCD"
     MCR = "MCR"
     QA = "QA"
     SL = "SL"
     TAX = "TAX"
     TRL = "TRL"
     UPIN = "UPIN"


class Advancedbeneficiarynoticecode(str, Enum):
     """
     339 - Advanced beneficiary notice code

     1  Service is subject to medical necessity procedures
     2  Patient has been informed of responsibility, and agrees to pay for service
     3  Patient has been informed of responsibility, and asks that the payer be billed
     4  Advanced Beneficiary Notice has not been signed
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"


class Patientsrelationshiptoinsured(str, Enum):
     """
     344 - Patient s relationship to insured

     01  Patient is insured
     02  Spouse
     03  Natural child/insured financial responsibility
     04  Natural child/Insured does not have financial responsibility
     05  Step child
     06  Foster child
     07  Ward of the court
     08  Employee
     09  Unknown
     10  Handicapped dependent
     11  Organ donor
     12  Cadaver donor
     13  Grandchild
     14  Niece/nephew
     15  Injured plaintiff
     16  Sponsored dependent
     17  Minor dependent of a minor dependent
     18  Parent
     19  Grandparent
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _07 = "07"
     _08 = "08"
     _09 = "09"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _13 = "13"
     _14 = "14"
     _15 = "15"
     _16 = "16"
     _17 = "17"
     _18 = "18"
     _19 = "19"


class Specialprogramindicator(str, Enum):
     """
     348 - Special program indicator

     01  EPSDT-CHAP
     02  Physically handicapped children's program
     03  Special federal funding
     04  Family planning
     05  Disability
     06  PPV/Medicare 100% payment
     07  Induced abortion-danger to life
     08  Induced abortion victim rape/incest
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _07 = "07"
     _08 = "08"


class PSRO_URapprovalindicator(str, Enum):
     """
     349 - PSRO-UR approval indicator

     1  Approved by the PSRO/UR as billed
     2  Automatic approval as billed based on focused review
     3  Partial approval
     4  Admission denied
     5  Postpayment review applicable
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"


class Occurrencecode(str, Enum):
     """
     350 - Occurrence code

     01  Auto accident
     02  No fault insurance involved-including auto accident/other
     03  Accident/tort liability
     04  Accident/employment related
     05  Other accident
     06  Crime victim
     09  Start of infertility treatment cycle
     10  Last menstrual period
     11  Onset of symptoms/illness
     12  Date of onset for a chronically dependent individual
     17  Date outpatient occupational therapy plan established or last reviewed
     18  Date of retirement patient/beneficiary
     19  Date of retirement spouse
     20  Guarantee of payment began
     21  UR notice received
     22  Date active care ended
     24  Date insurance denied
     25  Date benefits terminated by primary payor
     26  Date SNF bed available
     27  Date home health plan established
     28  Spouse's date of birth
     29  Date outpatient physical therapy plan established or last reviewed
     30  Date outpatient speech pathology plan established or last reviewed
     31  Date beneficiary notified of intent to bill (accommodations)
     32  Date beneficiary notified of intent to bill (procedures or treatments)
     33  First day of the Medicare coordination period for ESRD beneficiaries covered by EGHP
     34  Date of election of extended care facilities
     35  Date treatment started for P.T.
     36  Date of inpatient hospital discharge for covered transplant patients
     37  Date of inpatient hospital discharge for non-covered transplant patient
     40  Scheduled date of admission
     41  Date of first test for pre-admission testing
     42  Date of discharge
     43  Scheduled date of canceled surgery
     44  Date treatment started for O.T.
     45  Date treatment started for S.T.
     46  Date treatment started for cardiac rehab.
     48  Payer codes
     49  Payer codes
     47 ... 49  Payer codes
     47  Payer codes
     50  Date lien released
     51  Date treatment started for psychiatric care
     94  Occurrence span codes and dates
     85  Occurrence span codes and dates
     86  Occurrence span codes and dates
     87  Occurrence span codes and dates
     88  Occurrence span codes and dates
     89  Occurrence span codes and dates
     90  Occurrence span codes and dates
     91  Occurrence span codes and dates
     93  Occurrence span codes and dates
     82  Occurrence span codes and dates
     95  Occurrence span codes and dates
     96  Occurrence span codes and dates
     97  Occurrence span codes and dates
     98  Occurrence span codes and dates
     99  Occurrence span codes and dates
     92  Occurrence span codes and dates
     74  Occurrence span codes and dates
     70  Occurrence span codes and dates
     70 ... 99  Occurrence span codes and dates
     71  Occurrence span codes and dates
     84  Occurrence span codes and dates
     73  Occurrence span codes and dates
     83  Occurrence span codes and dates
     75  Occurrence span codes and dates
     76  Occurrence span codes and dates
     77  Occurrence span codes and dates
     78  Occurrence span codes and dates
     79  Occurrence span codes and dates
     80  Occurrence span codes and dates
     81  Occurrence span codes and dates
     72  Occurrence span codes and dates
     A1  Birthdate - insured A
     A2  Effective date - insured A policy
     A3  Benefits exhausted payer A
     """


     _01 = "01"
     _02 = "02"
     _03 = "03"
     _04 = "04"
     _05 = "05"
     _06 = "06"
     _09 = "09"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _17 = "17"
     _18 = "18"
     _19 = "19"
     _20 = "20"
     _21 = "21"
     _22 = "22"
     _24 = "24"
     _25 = "25"
     _26 = "26"
     _27 = "27"
     _28 = "28"
     _29 = "29"
     _30 = "30"
     _31 = "31"
     _32 = "32"
     _33 = "33"
     _34 = "34"
     _35 = "35"
     _36 = "36"
     _37 = "37"
     _40 = "40"
     _41 = "41"
     _42 = "42"
     _43 = "43"
     _44 = "44"
     _45 = "45"
     _46 = "46"
     _48 = "48"
     _49 = "49"
     _47_____49 = "47 ... 49"
     _47 = "47"
     _50 = "50"
     _51 = "51"
     _94 = "94"
     _85 = "85"
     _86 = "86"
     _87 = "87"
     _88 = "88"
     _89 = "89"
     _90 = "90"
     _91 = "91"
     _93 = "93"
     _82 = "82"
     _95 = "95"
     _96 = "96"
     _97 = "97"
     _98 = "98"
     _99 = "99"
     _92 = "92"
     _74 = "74"
     _70 = "70"
     _70_____99 = "70 ... 99"
     _71 = "71"
     _84 = "84"
     _73 = "73"
     _83 = "83"
     _75 = "75"
     _76 = "76"
     _77 = "77"
     _78 = "78"
     _79 = "79"
     _80 = "80"
     _81 = "81"
     _72 = "72"
     A1 = "A1"
     A2 = "A2"
     A3 = "A3"


class Occurrencespan(str, Enum):
     """
     351 - Occurrence span

     70  Qualifying stay dates for SNF
     71  Prior stay dates
     72  First/last visit
     73  Benefit eligibility period
     74  Non-covered level of care
     75  SNF level of care
     76  Patient liability
     77  Provider liability period
     78  SNF prior stay dates
     79  Payer code
     M0  PSRO/UR approved stay dates
     """


     _70 = "70"
     _71 = "71"
     _72 = "72"
     _73 = "73"
     _74 = "74"
     _75 = "75"
     _76 = "76"
     _77 = "77"
     _78 = "78"
     _79 = "79"
     M0 = "M0"


class CWEstatuses(str, Enum):
     """
     353 - CWE statuses

     U  Unknown
     UASK  Asked but Unknown
     NAV  Not available
     NA  Not applicable
     NASK  Not asked
     """


     U = "U"
     UASK = "UASK"
     NAV = "NAV"
     NA = "NA"
     NASK = "NASK"


class Messagestructure(str, Enum):
     """
     354 - Message structure

     ACK  Varies
     ADT_A01  A01, A04, A08, A13
     ADT_A02  A02
     ADT_A03  A03
     ADT_A05  A05, A14, A28, A31
     ADT_A06  A06, A07
     ADT_A09  A09, A10, A11, A12
     ADT_A15  A15
     ADT_A16  A16
     ADT_A17  A17
     ADT_A18  A18
     ADT_A20  A20
     ADT_A24  A24
     ADT_A30  A30, A34, A35, A36, A46, A47, A48, A49
     ADT_A37  A37
     ADT_A38  A38
     ADT_A39  A39, A40, A41, A42
     ADT_A43  A43, A44
     ADT_A45  A45
     ADT_A50  A50, A51
     ADT_A52  A52, A53, A55
     ADT_A54  A54
     ADT_A60  A60
     ADT_A61  A61, A62
     ADR_A19  A19
     BAR_P01  P01
     BAR_P02  P02
     BAR_P05  P05
     BAR_P06  P06
     BAR_P10  P10
     CRM_C01  C01, C02, C03, C04, C05, C06, C07, C08
     CSU_C09  C09, C10, C11, C12
     DFT_P03  P03
     DOC_T12  T12
     DSR_Q01  Q01
     DSR_Q03  Q03
     EAC_U07  U07
     EAN_U09  U09
     EAR_U08  U08
     EDR_R07  R07
     EQQ_Q04  Q04
     ERP_R09  R09
     ESR_U02  U02
     ESU_U01  U01
     INR_U06  U06
     INU_U05  U05
     LSU_U12  U12, U13
     MDM_T01  T01, T03, T05, T07, T09, T11
     MDM_T02  T02, T04, T06, T08, T10
     MFD_MFA  MFA
     MFK_M01  M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11
     MFN_M01  M01
     MFN_M02  M02
     MFN_M03  M03
     MFN_M04  M04
     MFN_M05  M05
     MFN_M06  M06
     MFN_M07  M07
     MFN_M08  M08
     MFN_M09  M09
     MFN_M10  M10
     MFN_M11  M11
     MFN_M12  M12
     MFQ_M01  M01-M06
     MFR_M01  M01-M06
     NMD_N02  N02
     NMQ_N01  N01
     NMR_N01  N01
     OMD_O03  O03
     OMG_O19  O19
     OML_O21  O21
     OMN_O07  O07
     OMP_O09  O09
     OMS_O05  O05
     ORD_O04  O04
     ORF_R04  R04
     ORG_O20  O20
     ORM_O01  O01
     ORP_O10  O10
     ORR_O02  O02
     ORS_O06  O06
     ORU_R01  R01
     ORU_W01  W01
     OSQ_Q06  Q06
     OSR_Q06  Q06
     PEX_P07  P07, P08
     PGL_PC6  PC6, PC7, PC8
     PMU_B01  B01, B02
     PMU_B03  B03
     PMU_B04  B04, B05
     PPG_PCG  PCG, PCH, PCJ
     PPP_PCB  PCB, PCC, PCD
     PPR_PC1  PC1, PC2, PC3
     PPT_PCL  PCL
     PPV_PCA  PCA
     PRR_PC5  PC5
     PTR_PCF  PCF
     QCK_Q02  Q02
     QCN_J01  J01, J02
     QRY_A19  A19
     QRY_PC4  PC4, PC9, PCE, PCK
     QRY_Q01  Q01
     QRY_Q02  Q02
     QBP_Q21  Q21, Q22, Q23, Q24, Q25
     QRY_R02  R02
     QRY_T12  T12
     QSB_Q16  Q16
     QVR_Q17  Q17
     RAR_RAR  RAR
     RAS_O17  O17
     RCI_I05  I05
     RCL_I06  I06
     RDE_O11  O11
     RDR_RDR  RDR
     RDS_O13  O13
     REF_I12  I12, I13, I14, I15
     RER_RER  RER
     RGR_RGR  RGR
     RGV_O15  O15
     ROR_ROR  ROR
     RPA_I08  I08, I09. I10, 1II
     RPI_I01  I01, I04
     RPL_I02  I02
     RPR_I03  I03
     RQA_I08  I08, I09, I10, I11
     RQC_I05  I05, I06
     RQI_I01  I01, I02, I03, I07
     RQP_I04  I04
     RQQ_Q09  Q09
     RRA_O18  O18
     RRD_O14  O14
     RRE_O12  O12
     RRG_O16  O16
     RRI_I12  I12, I13, I14, I15
     RSP_K21  K21
     RSP_K22  K22
     RSP_K23  K23, K24
     SIU_S12  S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S26
     SPQ_Q08  Q08
     SQM_S25  S25
     SQR_S25  S25
     SRM_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
     SRR_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
     SSR_U04  U04
     SSU_U03  U03
     SUR_P09  P09
     TCU_U10  U10, U11
     UDM_Q05  Q05
     VQQ_Q07  Q07
     VXQ_V01  V01
     VXR_V03  V03
     VXU_V04  V04
     VXX_V02  V02
     ADT_A21  A21, A22, A23, A25, A26, A27, A29, A32, A33
     QBP_Q11  Q11
     QBP_Q13  Q13
     QBP_Q15  Q15
     RDY_K11  K11
     RTB_K13  K13
     RDY_K15  K15
     TBR_R08  R08
     RPI_I04  I04
     RSP_K24  K24
     RSP_K25  K25
     DSR_P04  P04
     OUL_R21  R21
     ORN_O08  O08
     ORL_O22  O22
     """


     ACK = "ACK"
     ADT_A01 = "ADT_A01"
     ADT_A02 = "ADT_A02"
     ADT_A03 = "ADT_A03"
     ADT_A05 = "ADT_A05"
     ADT_A06 = "ADT_A06"
     ADT_A09 = "ADT_A09"
     ADT_A15 = "ADT_A15"
     ADT_A16 = "ADT_A16"
     ADT_A17 = "ADT_A17"
     ADT_A18 = "ADT_A18"
     ADT_A20 = "ADT_A20"
     ADT_A24 = "ADT_A24"
     ADT_A30 = "ADT_A30"
     ADT_A37 = "ADT_A37"
     ADT_A38 = "ADT_A38"
     ADT_A39 = "ADT_A39"
     ADT_A43 = "ADT_A43"
     ADT_A45 = "ADT_A45"
     ADT_A50 = "ADT_A50"
     ADT_A52 = "ADT_A52"
     ADT_A54 = "ADT_A54"
     ADT_A60 = "ADT_A60"
     ADT_A61 = "ADT_A61"
     ADR_A19 = "ADR_A19"
     BAR_P01 = "BAR_P01"
     BAR_P02 = "BAR_P02"
     BAR_P05 = "BAR_P05"
     BAR_P06 = "BAR_P06"
     BAR_P10 = "BAR_P10"
     CRM_C01 = "CRM_C01"
     CSU_C09 = "CSU_C09"
     DFT_P03 = "DFT_P03"
     DOC_T12 = "DOC_T12"
     DSR_Q01 = "DSR_Q01"
     DSR_Q03 = "DSR_Q03"
     EAC_U07 = "EAC_U07"
     EAN_U09 = "EAN_U09"
     EAR_U08 = "EAR_U08"
     EDR_R07 = "EDR_R07"
     EQQ_Q04 = "EQQ_Q04"
     ERP_R09 = "ERP_R09"
     ESR_U02 = "ESR_U02"
     ESU_U01 = "ESU_U01"
     INR_U06 = "INR_U06"
     INU_U05 = "INU_U05"
     LSU_U12 = "LSU_U12"
     MDM_T01 = "MDM_T01"
     MDM_T02 = "MDM_T02"
     MFD_MFA = "MFD_MFA"
     MFK_M01 = "MFK_M01"
     MFN_M01 = "MFN_M01"
     MFN_M02 = "MFN_M02"
     MFN_M03 = "MFN_M03"
     MFN_M04 = "MFN_M04"
     MFN_M05 = "MFN_M05"
     MFN_M06 = "MFN_M06"
     MFN_M07 = "MFN_M07"
     MFN_M08 = "MFN_M08"
     MFN_M09 = "MFN_M09"
     MFN_M10 = "MFN_M10"
     MFN_M11 = "MFN_M11"
     MFN_M12 = "MFN_M12"
     MFQ_M01 = "MFQ_M01"
     MFR_M01 = "MFR_M01"
     NMD_N02 = "NMD_N02"
     NMQ_N01 = "NMQ_N01"
     NMR_N01 = "NMR_N01"
     OMD_O03 = "OMD_O03"
     OMG_O19 = "OMG_O19"
     OML_O21 = "OML_O21"
     OMN_O07 = "OMN_O07"
     OMP_O09 = "OMP_O09"
     OMS_O05 = "OMS_O05"
     ORD_O04 = "ORD_O04"
     ORF_R04 = "ORF_R04"
     ORG_O20 = "ORG_O20"
     ORM_O01 = "ORM_O01"
     ORP_O10 = "ORP_O10"
     ORR_O02 = "ORR_O02"
     ORS_O06 = "ORS_O06"
     ORU_R01 = "ORU_R01"
     ORU_W01 = "ORU_W01"
     OSQ_Q06 = "OSQ_Q06"
     OSR_Q06 = "OSR_Q06"
     PEX_P07 = "PEX_P07"
     PGL_PC6 = "PGL_PC6"
     PMU_B01 = "PMU_B01"
     PMU_B03 = "PMU_B03"
     PMU_B04 = "PMU_B04"
     PPG_PCG = "PPG_PCG"
     PPP_PCB = "PPP_PCB"
     PPR_PC1 = "PPR_PC1"
     PPT_PCL = "PPT_PCL"
     PPV_PCA = "PPV_PCA"
     PRR_PC5 = "PRR_PC5"
     PTR_PCF = "PTR_PCF"
     QCK_Q02 = "QCK_Q02"
     QCN_J01 = "QCN_J01"
     QRY_A19 = "QRY_A19"
     QRY_PC4 = "QRY_PC4"
     QRY_Q01 = "QRY_Q01"
     QRY_Q02 = "QRY_Q02"
     QBP_Q21 = "QBP_Q21"
     QRY_R02 = "QRY_R02"
     QRY_T12 = "QRY_T12"
     QSB_Q16 = "QSB_Q16"
     QVR_Q17 = "QVR_Q17"
     RAR_RAR = "RAR_RAR"
     RAS_O17 = "RAS_O17"
     RCI_I05 = "RCI_I05"
     RCL_I06 = "RCL_I06"
     RDE_O11 = "RDE_O11"
     RDR_RDR = "RDR_RDR"
     RDS_O13 = "RDS_O13"
     REF_I12 = "REF_I12"
     RER_RER = "RER_RER"
     RGR_RGR = "RGR_RGR"
     RGV_O15 = "RGV_O15"
     ROR_ROR = "ROR_ROR"
     RPA_I08 = "RPA_I08"
     RPI_I01 = "RPI_I01"
     RPL_I02 = "RPL_I02"
     RPR_I03 = "RPR_I03"
     RQA_I08 = "RQA_I08"
     RQC_I05 = "RQC_I05"
     RQI_I01 = "RQI_I01"
     RQP_I04 = "RQP_I04"
     RQQ_Q09 = "RQQ_Q09"
     RRA_O18 = "RRA_O18"
     RRD_O14 = "RRD_O14"
     RRE_O12 = "RRE_O12"
     RRG_O16 = "RRG_O16"
     RRI_I12 = "RRI_I12"
     RSP_K21 = "RSP_K21"
     RSP_K22 = "RSP_K22"
     RSP_K23 = "RSP_K23"
     SIU_S12 = "SIU_S12"
     SPQ_Q08 = "SPQ_Q08"
     SQM_S25 = "SQM_S25"
     SQR_S25 = "SQR_S25"
     SRM_S01 = "SRM_S01"
     SRR_S01 = "SRR_S01"
     SSR_U04 = "SSR_U04"
     SSU_U03 = "SSU_U03"
     SUR_P09 = "SUR_P09"
     TCU_U10 = "TCU_U10"
     UDM_Q05 = "UDM_Q05"
     VQQ_Q07 = "VQQ_Q07"
     VXQ_V01 = "VXQ_V01"
     VXR_V03 = "VXR_V03"
     VXU_V04 = "VXU_V04"
     VXX_V02 = "VXX_V02"
     ADT_A21 = "ADT_A21"
     QBP_Q11 = "QBP_Q11"
     QBP_Q13 = "QBP_Q13"
     QBP_Q15 = "QBP_Q15"
     RDY_K11 = "RDY_K11"
     RTB_K13 = "RTB_K13"
     RDY_K15 = "RDY_K15"
     TBR_R08 = "TBR_R08"
     RPI_I04 = "RPI_I04"
     RSP_K24 = "RSP_K24"
     RSP_K25 = "RSP_K25"
     DSR_P04 = "DSR_P04"
     OUL_R21 = "OUL_R21"
     ORN_O08 = "ORN_O08"
     ORL_O22 = "ORL_O22"


class Primarykeyvaluetype(str, Enum):
     """
     355 - Primary key value type

     PL  Person location
     CE  Coded element
     """


     PL = "PL"
     CE = "CE"


class Alternatecharactersethandlingscheme(str, Enum):
     """
     356 - Alternate character set handling scheme

     ISO 2022-1994  This standard is titled "Information Technology - Character Code Structure and Extension Technique". This standard specifies an escape sequence from basic one byte character set to specified other character set, and vice versa.  The escape sequence explic
     2.3  The character set switching mode specified in HL7 2.3, sections 2.8.28.6.1, and 2.9.2.  Note that the escape sequences used in this mode do not use the ASCII "esc" character. They are "HL7 escape sequences" as defined in HL7 2.3, sec.  2.9 as defined in I
     <null>  This is the default, indicating that there is no character set switching occurring in this message.
     """


     ISO_2022_1994 = "ISO 2022-1994"
     _2_3 = "2.3"
     _null_ = "<null>"


class Messageerrorconditioncodes(str, Enum):
     """
     357 - Message error condition codes

     0  Message accepted
     100  Segment sequence error
     101  Required field missing
     102  Data type error
     103  Table value not found
     200  Unsupported message type
     201  Unsupported event code
     202  Unsupported processing id
     203  Unsupported version id
     204  Unknown key identifier
     205  Duplicate key identifier
     206  Application record locked
     207  Application internal error
     """


     _0 = "0"
     _100 = "100"
     _101 = "101"
     _102 = "102"
     _103 = "103"
     _200 = "200"
     _201 = "201"
     _202 = "202"
     _203 = "203"
     _204 = "204"
     _205 = "205"
     _206 = "206"
     _207 = "207"


class Diagnosispriority(str, Enum):
     """
     359 - Diagnosis priority

     0  Not included in diagnosis ranking
     1  The primary diagnosis
     2 ...  For ranked secondary diagnoses
     """


     _0 = "0"
     _1 = "1"
     _2____ = "2 ..."


class Degree(str, Enum):
     """
     360 - Degree

     AAS  Associate of Applied Science
     AA  Associate of Arts
     ABA  Associate of Business Administration
     AE  Associate of Engineering
     AS  Associate of Science
     BA  Bachelor of Arts
     BBA  Bachelor of Business Administration
     BE  Bachelor or Engineering
     BFA  Bachelor of Fine Arts
     BN  Bachelor of Nursing
     BS  Bachelor of Science
     BSL  Bachelor of Science - Law
     BT  Bachelor of Theology
     CER  Certificate
     DIP  Diploma
     DBA  Doctor of Business Administration
     DED  Doctor of Education
     PharmD  Doctor of Pharmacy
     PHE  Doctor of Engineering
     PHD  Doctor of Philosophy
     PHS  Doctor of Science
     MD  Doctor of Medicine
     DO  Doctor of Osteopathy
     HS  High School Graduate
     JD  Juris Doctor
     MA  Master of Arts
     MBA  Master of Business Administration
     MCE  Master of Civil Engineering
     MDI  Master of Divinity
     MED  Master of Education
     MEE  Master of Electrical Engineering
     ME  Master of Engineering
     MFA  Master of Fine Arts
     MME  Master of Mechanical Engineering
     MS  Master of Science
     MSL  Master of Science - Law
     MT  Master of Theology
     NG  Non-Graduate
     SEC  Secretarial Certificate
     TS  Trade School Graduate
     """


     AAS = "AAS"
     AA = "AA"
     ABA = "ABA"
     AE = "AE"
     AS = "AS"
     BA = "BA"
     BBA = "BBA"
     BE = "BE"
     BFA = "BFA"
     BN = "BN"
     BS = "BS"
     BSL = "BSL"
     BT = "BT"
     CER = "CER"
     DIP = "DIP"
     DBA = "DBA"
     DED = "DED"
     PharmD = "PharmD"
     PHE = "PHE"
     PHD = "PHD"
     PHS = "PHS"
     MD = "MD"
     DO = "DO"
     HS = "HS"
     JD = "JD"
     MA = "MA"
     MBA = "MBA"
     MCE = "MCE"
     MDI = "MDI"
     MED = "MED"
     MEE = "MEE"
     ME = "ME"
     MFA = "MFA"
     MME = "MME"
     MS = "MS"
     MSL = "MSL"
     MT = "MT"
     NG = "NG"
     SEC = "SEC"
     TS = "TS"


class Assigningauthority(str, Enum):
     """
     363 - Assigning authority

     AUSDVA  Australia - Dept. of Veterans Affairs
     AUSHIC  Australia - Health Insurance Commission
     CANAB  Canada - Alberta
     CANBC  Canada - British Columbia
     CANMB  Canada - Manitoba
     CANNB  Canada - New Brunswick
     CANNF  Canada - Newfoundland
     CANNS  Canada - Nova Scotia
     CANNT  Canada - Northwest Territories
     CANNU  Canada - Nanavut
     CANON  Canada - Ontario
     CANPE  Canada - Prince Edward Island
     CANQC  Canada - Quebec
     CANSK  Canada - Saskatchewan
     CANYT  Canada - Yukon Territories
     NLVWS  NL - Ministerie van Volksgezondheid, Welzijn en Sport
     USCDC  US Center for Disease Control
     USHCFA  US Healthcare Finance Authority
     USSSA  US Social Security Administration
     """


     AUSDVA = "AUSDVA"
     AUSHIC = "AUSHIC"
     CANAB = "CANAB"
     CANBC = "CANBC"
     CANMB = "CANMB"
     CANNB = "CANNB"
     CANNF = "CANNF"
     CANNS = "CANNS"
     CANNT = "CANNT"
     CANNU = "CANNU"
     CANON = "CANON"
     CANPE = "CANPE"
     CANQC = "CANQC"
     CANSK = "CANSK"
     CANYT = "CANYT"
     NLVWS = "NLVWS"
     USCDC = "USCDC"
     USHCFA = "USHCFA"
     USSSA = "USSSA"


class Commenttype(str, Enum):
     """
     364 - Comment type

     PI  Patient Instructions
     AI  Ancillary Instructions
     GI  General Instructions
     1R  Primary Reason
     2R  Secondary Reason
     GR  General Reason
     RE  Remark
     DR  Duplicate/Interaction Reason
     """


     PI = "PI"
     AI = "AI"
     GI = "GI"
     _1R = "1R"
     _2R = "2R"
     GR = "GR"
     RE = "RE"
     DR = "DR"


class Equipmentstate(str, Enum):
     """
     365 - Equipment state

     PU  Powered Up
     IN  Initializing
     ID  Idle
     CO  Configuring
     OP  Normal Operation
     CL  Clearing
     PA  Pausing
     PD  Paused
     ES  E-stopped
     """


     PU = "PU"
     IN = "IN"
     ID = "ID"
     CO = "CO"
     OP = "OP"
     CL = "CL"
     PA = "PA"
     PD = "PD"
     ES = "ES"


class Local_remotecontrolstate(str, Enum):
     """
     366 - Local-remote control state

     L  Local
     R  Remote
     """


     L = "L"
     R = "R"


class Alertlevel(str, Enum):
     """
     367 - Alert level

     N  Normal
     W  Warning
     S  Serious
     C  Critical
     """


     N = "N"
     W = "W"
     S = "S"
     C = "C"


class Remotecontrolcommand(str, Enum):
     """
     368 - Remote control command

     SA  Sampling
     LO  Load
     UN  Unload
     LK  Lock
     UC  Unlock
     TT  Transport To
     CN  Clear Notification
     IN  Initialize/Initiate
     SU  Setup
     CL  Clear
     PA  Pause
     RE  Resume
     ES  Emergency -stop
     LC  Local Control Request
     RC  Remote Control Request
     AB  Abort
     EN  Enable Sending Events
     DI  Disable Sending Events
     EX  Execute (command specified in field Parameters (ST) 01394)
     """


     SA = "SA"
     LO = "LO"
     UN = "UN"
     LK = "LK"
     UC = "UC"
     TT = "TT"
     CN = "CN"
     IN = "IN"
     SU = "SU"
     CL = "CL"
     PA = "PA"
     RE = "RE"
     ES = "ES"
     LC = "LC"
     RC = "RC"
     AB = "AB"
     EN = "EN"
     DI = "DI"
     EX = "EX"


class Specimenrole(str, Enum):
     """
     369 - Specimen role

     P  Patient (default if blank component value)
     Q  Control specimen
     C  Calibrator
     B  Blind Sample
     R  Replicate (of patient sample as a control)
     """


     P = "P"
     Q = "Q"
     C = "C"
     B = "B"
     R = "R"


class Containerstatus(str, Enum):
     """
     370 - Container status

     I  Identified
     P  In Position
     O  In Process
     R  Process Completed
     L  Left Equipment
     M  Missing
     X  Container Unavailable
     U  Unknown
     """


     I = "I"
     P = "P"
     O = "O"
     R = "R"
     L = "L"
     M = "M"
     X = "X"
     U = "U"


class Additive(str, Enum):
     """
     371 - Additive

     EDTK  Potassium/K EDTA
     EDTN  Sodium/Na EDTA
     HEPL  Lithium/Li  Heparin
     HEPN  Sodium/Na  Heparin
     C32  3.2%  Citrate
     C38  3.8% Citrate
     BOR  Borate
     HCL6  6N HCL
     """


     EDTK = "EDTK"
     EDTN = "EDTN"
     HEPL = "HEPL"
     HEPN = "HEPN"
     C32 = "C32"
     C38 = "C38"
     BOR = "BOR"
     HCL6 = "HCL6"


class Specimencomponent(str, Enum):
     """
     372 - Specimen component

     SUP  Supernatant
     SED  Sediment
     BLD  Whole blood, homogeneous
     BSEP  Whole blood, separated
     PRP  Platelet rich plasma
     PPP  Platelet poor plasma
     SER  Serum, NOS (not otherwise specified)
     PLAS  Plasma, NOS (not otherwise specified)
     """


     SUP = "SUP"
     SED = "SED"
     BLD = "BLD"
     BSEP = "BSEP"
     PRP = "PRP"
     PPP = "PPP"
     SER = "SER"
     PLAS = "PLAS"


class Treatment(str, Enum):
     """
     373 - Treatment

     LDLP  LDL Precipitation
     RECA  Recalification
     DEFB  Defibrination
     ACID  Acidification
     NEUT  Neutralization
     ALK  Alkalization
     FILT  Filtration
     UFIL  Ultrafiltration
     """


     LDLP = "LDLP"
     RECA = "RECA"
     DEFB = "DEFB"
     ACID = "ACID"
     NEUT = "NEUT"
     ALK = "ALK"
     FILT = "FILT"
     UFIL = "UFIL"


class Systeminducedcontaminants(str, Enum):
     """
     374 - System induced contaminants

     CNTM  Present, type of contamination unspecified
     """


     CNTM = "CNTM"


class Artificialblood(str, Enum):
     """
     375 - Artificial blood

     SFHB  Stromal free hemoglobin preparations
     FLUR  Fluorocarbons
     """


     SFHB = "SFHB"
     FLUR = "FLUR"


class Specialhandlingconsiderations(str, Enum):
     """
     376 - Special handling considerations

     PRTL  Protect from light
     CFRZ  Critical Frozen
     CATM  Critical do not expose to atmosphere - Do not uncap
     CREF  Critical refrigerated
     CAMB  Critical ambient temperature
     C37  Critical maintain at 37C (e.g., cryoglobulin specimen
     """


     PRTL = "PRTL"
     CFRZ = "CFRZ"
     CATM = "CATM"
     CREF = "CREF"
     CAMB = "CAMB"
     C37 = "C37"


class Otherenvironmentalfactors(str, Enum):
     """
     377 - Other environmental factors

     ATM  Opened container, atmosphere/duration unspecified
     A60  Opened container, indoor atmosphere, 60 minutes duration
     """


     ATM = "ATM"
     A60 = "A60"


class Substancestatus(str, Enum):
     """
     383 - Substance status

     EW  Expired Warning
     EE  Expired Error
     CW  Calibration Warning
     CE  Calibration Error
     QW  QC Warning
     QE  QC Error
     NW  Not Available Warning
     NE  Not Available Error
     OW  Other Warning
     OE  Other Error
     OK  OK Status
     """


     EW = "EW"
     EE = "EE"
     CW = "CW"
     CE = "CE"
     QW = "QW"
     QE = "QE"
     NW = "NW"
     NE = "NE"
     OW = "OW"
     OE = "OE"
     OK = "OK"


class Substancetype(str, Enum):
     """
     384 - Substance type

     SR  Single Test Reagent
     MR  Multiple Test Reagent (consumption cannot be tied to orders for single test)
     DI  Diluent
     PT  Pretreatment
     RC  Reagent Calibrator
     CO  Control
     PW  Purified Water
     LW  Liquid Waste
     SW  Solid Waste
     SC  Countable Solid Item (e.g., Tip, etc.)
     LI  Measurable Liquid Item
     OT  Other
     """


     SR = "SR"
     MR = "MR"
     DI = "DI"
     PT = "PT"
     RC = "RC"
     CO = "CO"
     PW = "PW"
     LW = "LW"
     SW = "SW"
     SC = "SC"
     LI = "LI"
     OT = "OT"


class Commandresponse(str, Enum):
     """
     387 - Command response

     OK  Command completed successfully
     TI  Command cannot be completed within requested completion time
     ER  Command cannot be completed because of error condition (see response parameters)
     ST  Command cannot be completed because of the status of the requested equipment
     UN  Command cannot be completed for unknown reasons
     """


     OK = "OK"
     TI = "TI"
     ER = "ER"
     ST = "ST"
     UN = "UN"


class Processingtype(str, Enum):
     """
     388 - Processing type

     P  Regular Production
     E  Evaluation
     """


     P = "P"
     E = "E"


class Analyterepeatstatus(str, Enum):
     """
     389 - Analyte repeat status

     O  Original, first run
     R  Repeated without dilution
     D  Repeated with dilution
     F  Reflex test
     """


     O = "O"
     R = "R"
     D = "D"
     F = "F"


class Segmentgroup(str, Enum):
     """
     391 - Segment group

     PIDG  PID group
     OBRG  OBR group
     ORCG  ORC group
     RXAG  RXA group
     RXDG  RXD group
     RXEG  RXE group
     RXOG  RXO group
     etc  
     """


     PIDG = "PIDG"
     OBRG = "OBRG"
     ORCG = "ORCG"
     RXAG = "RXAG"
     RXDG = "RXDG"
     RXEG = "RXEG"
     RXOG = "RXOG"
     etc = "etc"


class Matchreason(str, Enum):
     """
     392 - Match reason

     DB  Match on Date of Birth
     NA  Match on Name (Alpha Match)
     NP  Match on Name (Phonetic Match)
     SS  Match on Social Security Number
     """


     DB = "DB"
     NA = "NA"
     NP = "NP"
     SS = "SS"


class Matchalgorithms(str, Enum):
     """
     393 - Match algorithms

     LINKSOFT_2.01  
     MATCHWARE_1.2  
     """


     LINKSOFT_2_01 = "LINKSOFT_2.01"
     MATCHWARE_1_2 = "MATCHWARE_1.2"


class Responsemodality(str, Enum):
     """
     394 - Response modality

     R  Real Time
     T  Bolus (a series of responses sent at the same time without use of batch formatting)
     B  Batch
     """


     R = "R"
     T = "T"
     B = "B"


class Modifyindicator(str, Enum):
     """
     395 - Modify indicator

     N  New Subscription
     M  Modified Subscription
     """


     N = "N"
     M = "M"


class CodingSystem(str, Enum):
     """
     396 - Coding System

     99zzz or L  Local general code (where z is an alphanumeric character)
     ACR  American College of Radiology finding codes
     ART  WHO Adverse Reaction Terms
     AS4  ASTM E1238/ E1467 Universal
     AS4E  AS4 Neurophysiology Codes
     ATC  American Type Culture Collection
     C4  CPT-4
     C5  CPT-5
     CAS  Chemical abstract codes
     CD2  CDT-2 Codes
     CDCA  CDC Analyte Codes
     CDCM  CDC Methods/Instruments Codes
     CDS  CDC Surveillance
     CE  CEN ECG diagnostic codes
     CLP  CLIP
     CPTM  CPT Modifier Code
     CST  COSTART
     CVX  CDC Vaccine Codes
     DCL  DICOM Class Label
     DCM  DICOM modality codes
     DQL  DICOM Query Label
     E  EUCLIDES
     E5  Euclides  quantity codes
     E6  Euclides Lab method codes
     E7  Euclides Lab equipment codes
     ENZC  Enzyme Codes
     FDDC  First DataBank Drug Codes
     FDDX  First DataBank Diagnostic Codes
     FDK  FDA K10
     HB  HIBCC
     HCPCS  HCFA Common Procedure Coding System
     HHC  Home Health Care
     HI  Health Outcomes
     HL7nnnn  HL7 Defined Codes where nnnn is the HL7 table number
     HPC  HCFA Procedure Codes (HCPCS)
     I10  ICD-10
     I10P  ICD-10  Procedure Codes
     I9  ICD9
     I9C  ICD-9CM
     IBT  ISBT
     IC2  ICHPPC-2
     ICDO  International Classification of Diseases for Oncology
     ICS  ICCS
     ICSD  International Classification of Sleep Disorders
     ISOnnnn  ISO Defined Codes where nnnn is the ISO table number
     IUPP  IUPAC/IFCC Property Codes
     IUPC  IUPAC/IFCC Component Codes
     JC8  Japanese Chemistry
     LB  Local billing code
     LN  Logical Observation Identifier Names and Codes (LOINC(r))
     MCD  Medicaid
     MCR  Medicare
     MDDX  Medispan Diagnostic Codes
     MEDC  Medical Economics Drug Codes
     MEDR  Medical Dictionary for Drug Regulatory Affairs (MEDDRA)
     MEDX  Medical Economics Diagnostic Codes
     MGPI  Medispan GPI
     MVX  CDC Vaccine Manufacturer Codes
     NDA  NANDA
     NDC  National drug codes
     NIC  Nursing Interventions Classification
     NPI  National Provider Identifier
     OHA  Omaha System
     POS  POS Codes
     RC  Read Classification
     SDM  SNOMED- DICOM Microglossary
     SNM  Systemized Nomenclature of Medicine (SNOMED)
     SNM3  SNOMED International
     SNT  SNOMED topology codes (anatomic sites)
     UC  UCDS
     UMD  MDNS
     UML  Unified Medical Language
     UPC  Universal Product Code
     UPIN  UPIN
     W1  WHO record # drug codes (6 digit)
     W2  WHO record # drug codes (8 digit)
     W4  WHO record # code with ASTM extension
     WC  WHO ATC
     """


     _99zzz___L = "99zzz or L"
     ACR = "ACR"
     ART = "ART"
     AS4 = "AS4"
     AS4E = "AS4E"
     ATC = "ATC"
     C4 = "C4"
     C5 = "C5"
     CAS = "CAS"
     CD2 = "CD2"
     CDCA = "CDCA"
     CDCM = "CDCM"
     CDS = "CDS"
     CE = "CE"
     CLP = "CLP"
     CPTM = "CPTM"
     CST = "CST"
     CVX = "CVX"
     DCL = "DCL"
     DCM = "DCM"
     DQL = "DQL"
     E = "E"
     E5 = "E5"
     E6 = "E6"
     E7 = "E7"
     ENZC = "ENZC"
     FDDC = "FDDC"
     FDDX = "FDDX"
     FDK = "FDK"
     HB = "HB"
     HCPCS = "HCPCS"
     HHC = "HHC"
     HI = "HI"
     HL7nnnn = "HL7nnnn"
     HPC = "HPC"
     I10 = "I10"
     I10P = "I10P"
     I9 = "I9"
     I9C = "I9C"
     IBT = "IBT"
     IC2 = "IC2"
     ICDO = "ICDO"
     ICS = "ICS"
     ICSD = "ICSD"
     ISOnnnn = "ISOnnnn"
     IUPP = "IUPP"
     IUPC = "IUPC"
     JC8 = "JC8"
     LB = "LB"
     LN = "LN"
     MCD = "MCD"
     MCR = "MCR"
     MDDX = "MDDX"
     MEDC = "MEDC"
     MEDR = "MEDR"
     MEDX = "MEDX"
     MGPI = "MGPI"
     MVX = "MVX"
     NDA = "NDA"
     NDC = "NDC"
     NIC = "NIC"
     NPI = "NPI"
     OHA = "OHA"
     POS = "POS"
     RC = "RC"
     SDM = "SDM"
     SNM = "SNM"
     SNM3 = "SNM3"
     SNT = "SNT"
     UC = "UC"
     UMD = "UMD"
     UML = "UML"
     UPC = "UPC"
     UPIN = "UPIN"
     W1 = "W1"
     W2 = "W2"
     W4 = "W4"
     WC = "WC"


class Sequencing(str, Enum):
     """
     397 - Sequencing

     A  Ascending
     AN  Ascending, case insensitive
     D  Descending
     DN  Descending, case insensitive
     N  None
     """


     A = "A"
     AN = "AN"
     D = "D"
     DN = "DN"
     N = "N"


class Continuationstylecode(str, Enum):
     """
     398 - Continuation style code

     F  Fragmentation
     I  Interactive Continuation
     """


     F = "F"
     I = "I"


class Countrycode(str, Enum):
     """
     399 - Country code

     ABW  ARUBA
     AFG  AFGHANISTAN
     AFT  FRENCH SOUTHERN TERRITORIES
     AGO  ANGOLA
     AIA  ANGUILLA
     ALB  ALBANIA
     AND  ANDORRA
     ANT  NETHERLANDS ANTILLES
     ARE  UNITED ARAB EMIRATES
     ARG  ARGENTINA
     ARM  ARMENIA
     ASM  AMERICAN SAMOA
     ATA  ANTARCTICA
     ATG  ANTIGUA AND BARBUDA
     AUS  AUSTRALIA
     AUT  AUSTRIA
     AZE  AZERBAIJAN
     BDI  BURUNDI
     BEL  BELGIUM
     BEN  BENIN
     BFA  BURKINA FASO
     BGD  BANGLADESH
     BGR  BULGARIA
     BHR  BAHRAIN
     BHS  BAHAMAS
     BIH  BOSNIA AND HERZEGOVINA
     BLR  BELARUS
     BLZ  BELIZE
     BMU  BERMUDA
     BOL  BOLIVIA
     BRA  BRAZIL
     BRB  BARBADOS
     BRN  BRUNEI DARUSSALAM
     BTN  BHUTAN
     BVT  BOUVET ISLAND
     BWA  BOTSWANA
     CAF  CENTRAL AFRICAN REPUBLIC
     CAN  CANADA
     CCK  COCOS (KEELING) ISLANDS
     CHE  SWITZERLAND
     CHL  CHILE
     CHN  CHINA
     CIV  COTE D'VOIRE
     CMR  CAMEROON
     COD  CONGO, THE DEMOCRATIC REPUBLIC OF THE
     COG  CONGO
     COK  COOK ISLAND
     COL  COLOMBIA
     COM  COMOROS
     CPV  CAPE VERDE
     CRI  COSTA RICA
     CUB  CUBA
     CXR  CHRISTMAS ISLAND
     CYM  CAYMAN ISLANDS
     CYP  CYPRUS
     CZE  CZECH REPUBLIC
     DEU  GERMANY
     DJI  DJIBOUTI
     DMA  DOMINICA
     DNK  DENMARK
     DOM  DOMINICAN REPUBLIC
     DZA  ALGERIA
     ECU  ECUADOR
     EGY  EGYPT
     ERI  ERITREA
     ESH  WESTERN SAHARA
     ESP  SPAIN
     EST  ESTONIA
     ETH  ETHIOPIA
     FIN  FINLAND
     FJI  FIJI
     FLK  FALKLAND ISLANDS (MALVINAS)
     FRA  FRANCE
     FRO  FAROE ISLANDS
     FSM  MICRONESIA, FEDERATED STATES OF
     GAB  GABON
     GBR  UNITED KINGDOM
     GEO  GEORGIA
     GHA  GHANA
     GIB  GIBRALTAR
     GIN  GUINEA
     GLP  GUADELOUPE
     GMB  GAMBIA
     GNB  GUINEA-BISSAU
     GNQ  EQUATORIAL GUINEA
     GRC  GREECE
     GRD  GRENADA
     GRL  GREENLAND
     GTM  GUATEMALA
     GUF  FRENCH GUIANA
     GUM  GUAM
     GUY  GUYANA
     HKG  HONG KONG
     HMD  HEARD ISLAND AND MCDONALD ISLANDS
     HND  HONDURAS
     HRV  CROATIA
     HTI  HAITI
     HUN  HUNGARY
     IDN  INDONESIA
     IND  INDIA
     IOT  BRITISH INDIAN OCEAN TERRITORY
     IRL  IRELAND
     IRN  IRAN, ISLAMIC REPUBLIC OF
     IRQ  IRAQ
     ISL  ICELAND
     ISR  ISRAEL
     ITA  ITALY
     JAM  JAMAICA
     JOR  JORDAN
     JPN  JAPAN
     KAZ  KAZAKSTAN
     KEN  KENYA
     KGZ  KYRGYZSTAN
     KHM  CAMBODIA
     KIR  KIRIBATI
     KNA  SAINT KITTS AND NEVIS
     KOR  KOREA, REPUBLIC OF
     KWT  KUWAIT
     LAO  LAO PEOPLE'S DEMOCRATIC REPUBLIC
     LBN  LEBANNON
     LBR  LIBERIA
     LBY  LIBYAN ARAB JAMAHIRIYA
     LCA  SAINT LUCIA
     LIE  LIECHTENSTEIN
     LKA  SRI LANKA
     LSO  LESOTHO
     LTU  LITHUANIA
     LUX  LUXEMBOURG
     LVA  LATIVA
     MAC  MACAU
     MAR  MOROCCO
     MCO  MONACO
     MDA  MOLDOVA, REPUBLIC OF
     MDG  MADAGASCAR
     MDV  MALDIVES
     MEX  MEXICO
     MHL  MARSHALL ISLANDS
     MKD  MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF
     MLI  MALI
     MLT  MALTA
     MMR  MYANMAR
     MNG  MONGOLIA
     MNP  NORTHERN MARIANA ISLANDS
     MOZ  MOZAMBIQUE
     MRT  MAURITANIA
     MSR  MONTSERRAT
     MTQ  MARTINIQUE
     MUS  MAURITUS
     MWI  MALAWI
     MYS  MALAYSIA
     MYT  MAYOTTE
     NAM  NAMIBIA
     NCL  NEW CALEDONIA
     NER  NIGER
     NFK  NORFOLK ISLAND
     NGA  NIGERIA
     NIC  NICARAGUA
     NIU  NIUE
     NLD  NETHERLANDS
     NOR  NORWAY
     NPL  NEPAL
     NRU  NAURU
     NZL  NEW ZEALAND
     OMN  OMAN
     PAK  PAKISTAN
     PAN  PANAMA
     PCN  PITCAIRN
     PER  PERU
     PHL  PHILIPPINES
     PLW  PALAU
     PNG  PAPUA NEW GUINEA
     POL  POLAND
     PRI  PUERTO RICO
     PRK  KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF
     PRT  PORTUGAL
     PRY  PARAGUAY
     PYF  FRENCH POLYNESIA
     QAT  QATAR
     REU  REUNION
     ROM  ROMANIA
     RUS  RUSSIAN FEDERATION
     RWA  RWANDA
     SAU  SAUDI ARABIA
     SDN  SUDAN
     SEN  SENEGAL
     SGP  SINGAPORE
     SGS  SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS
     SHN  SAINT HELENA
     SJM  SVALBARD AND JAN MAYEN
     SLB  SOLOMON ISLANDS
     SLE  SIERRA LEONE
     SLV  EL SALVADOR
     SMR  SAN MARINO
     SOM  SOMALIA
     SPM  SAINT PIERRE AND MIQUELON
     STP  SAO TOME AND PRINCIPE
     SUR  SURINAME
     SVK  SLOVAKIA
     SVN  SLOVENIA
     SWE  SWEDEN
     SWZ  SWAZILAND
     SYC  SEYCHELLES
     SYR  SYRIAN ARAB REPUBLIC
     TCA  TURKS AND CAICOS ISLANDS
     TCD  CHAD
     TGO  TOGO
     THA  THAILAND
     TJK  TAJIKISTAN
     TKL  TOKELAU
     TKM  TURKMENISTAN
     TMP  EAST TIMOR
     TON  TONGA
     TTO  TRINIDAD AND TOBAGO
     TUN  TUNISIA
     TUR  TURKEY
     TUV  TUVALU
     TWN  TAIWAN, PROVINCE OF CHINA
     TZA  TANZANIA, UNITED REPUBLIC OF
     UGA  UGANDA
     UKR  UKRAINE
     UMI  UNITED STATES MINOR OUTLYING ISLANDS
     URY  URUGUAY
     USA  UNITED STATES
     UZB  UZBEKISTAN
     VAT  HOLY SEE  (VATICAN CITY STATE)
     VCT  SAINT VINCENT AND THE GRENADINES
     VEN  VENEZUELA
     VGB  VIRGIN ISLANDS, BRITISH
     VIR  VIRGIN ISLANDS, U.S.
     VNM  VIET NAM
     VUT  VANUATU
     WLF  WALLIS AND FUTUNA
     WSM  SAMOA
     YEM  YEMEN
     YUG  YUGOSLAVIA
     ZAF  SOUTH AFRICA
     ZMB  ZAMBIA
     ZWE  ZIMBABWE
     """


     ABW = "ABW"
     AFG = "AFG"
     AFT = "AFT"
     AGO = "AGO"
     AIA = "AIA"
     ALB = "ALB"
     AND = "AND"
     ANT = "ANT"
     ARE = "ARE"
     ARG = "ARG"
     ARM = "ARM"
     ASM = "ASM"
     ATA = "ATA"
     ATG = "ATG"
     AUS = "AUS"
     AUT = "AUT"
     AZE = "AZE"
     BDI = "BDI"
     BEL = "BEL"
     BEN = "BEN"
     BFA = "BFA"
     BGD = "BGD"
     BGR = "BGR"
     BHR = "BHR"
     BHS = "BHS"
     BIH = "BIH"
     BLR = "BLR"
     BLZ = "BLZ"
     BMU = "BMU"
     BOL = "BOL"
     BRA = "BRA"
     BRB = "BRB"
     BRN = "BRN"
     BTN = "BTN"
     BVT = "BVT"
     BWA = "BWA"
     CAF = "CAF"
     CAN = "CAN"
     CCK = "CCK"
     CHE = "CHE"
     CHL = "CHL"
     CHN = "CHN"
     CIV = "CIV"
     CMR = "CMR"
     COD = "COD"
     COG = "COG"
     COK = "COK"
     COL = "COL"
     COM = "COM"
     CPV = "CPV"
     CRI = "CRI"
     CUB = "CUB"
     CXR = "CXR"
     CYM = "CYM"
     CYP = "CYP"
     CZE = "CZE"
     DEU = "DEU"
     DJI = "DJI"
     DMA = "DMA"
     DNK = "DNK"
     DOM = "DOM"
     DZA = "DZA"
     ECU = "ECU"
     EGY = "EGY"
     ERI = "ERI"
     ESH = "ESH"
     ESP = "ESP"
     EST = "EST"
     ETH = "ETH"
     FIN = "FIN"
     FJI = "FJI"
     FLK = "FLK"
     FRA = "FRA"
     FRO = "FRO"
     FSM = "FSM"
     GAB = "GAB"
     GBR = "GBR"
     GEO = "GEO"
     GHA = "GHA"
     GIB = "GIB"
     GIN = "GIN"
     GLP = "GLP"
     GMB = "GMB"
     GNB = "GNB"
     GNQ = "GNQ"
     GRC = "GRC"
     GRD = "GRD"
     GRL = "GRL"
     GTM = "GTM"
     GUF = "GUF"
     GUM = "GUM"
     GUY = "GUY"
     HKG = "HKG"
     HMD = "HMD"
     HND = "HND"
     HRV = "HRV"
     HTI = "HTI"
     HUN = "HUN"
     IDN = "IDN"
     IND = "IND"
     IOT = "IOT"
     IRL = "IRL"
     IRN = "IRN"
     IRQ = "IRQ"
     ISL = "ISL"
     ISR = "ISR"
     ITA = "ITA"
     JAM = "JAM"
     JOR = "JOR"
     JPN = "JPN"
     KAZ = "KAZ"
     KEN = "KEN"
     KGZ = "KGZ"
     KHM = "KHM"
     KIR = "KIR"
     KNA = "KNA"
     KOR = "KOR"
     KWT = "KWT"
     LAO = "LAO"
     LBN = "LBN"
     LBR = "LBR"
     LBY = "LBY"
     LCA = "LCA"
     LIE = "LIE"
     LKA = "LKA"
     LSO = "LSO"
     LTU = "LTU"
     LUX = "LUX"
     LVA = "LVA"
     MAC = "MAC"
     MAR = "MAR"
     MCO = "MCO"
     MDA = "MDA"
     MDG = "MDG"
     MDV = "MDV"
     MEX = "MEX"
     MHL = "MHL"
     MKD = "MKD"
     MLI = "MLI"
     MLT = "MLT"
     MMR = "MMR"
     MNG = "MNG"
     MNP = "MNP"
     MOZ = "MOZ"
     MRT = "MRT"
     MSR = "MSR"
     MTQ = "MTQ"
     MUS = "MUS"
     MWI = "MWI"
     MYS = "MYS"
     MYT = "MYT"
     NAM = "NAM"
     NCL = "NCL"
     NER = "NER"
     NFK = "NFK"
     NGA = "NGA"
     NIC = "NIC"
     NIU = "NIU"
     NLD = "NLD"
     NOR = "NOR"
     NPL = "NPL"
     NRU = "NRU"
     NZL = "NZL"
     OMN = "OMN"
     PAK = "PAK"
     PAN = "PAN"
     PCN = "PCN"
     PER = "PER"
     PHL = "PHL"
     PLW = "PLW"
     PNG = "PNG"
     POL = "POL"
     PRI = "PRI"
     PRK = "PRK"
     PRT = "PRT"
     PRY = "PRY"
     PYF = "PYF"
     QAT = "QAT"
     REU = "REU"
     ROM = "ROM"
     RUS = "RUS"
     RWA = "RWA"
     SAU = "SAU"
     SDN = "SDN"
     SEN = "SEN"
     SGP = "SGP"
     SGS = "SGS"
     SHN = "SHN"
     SJM = "SJM"
     SLB = "SLB"
     SLE = "SLE"
     SLV = "SLV"
     SMR = "SMR"
     SOM = "SOM"
     SPM = "SPM"
     STP = "STP"
     SUR = "SUR"
     SVK = "SVK"
     SVN = "SVN"
     SWE = "SWE"
     SWZ = "SWZ"
     SYC = "SYC"
     SYR = "SYR"
     TCA = "TCA"
     TCD = "TCD"
     TGO = "TGO"
     THA = "THA"
     TJK = "TJK"
     TKL = "TKL"
     TKM = "TKM"
     TMP = "TMP"
     TON = "TON"
     TTO = "TTO"
     TUN = "TUN"
     TUR = "TUR"
     TUV = "TUV"
     TWN = "TWN"
     TZA = "TZA"
     UGA = "UGA"
     UKR = "UKR"
     UMI = "UMI"
     URY = "URY"
     USA = "USA"
     UZB = "UZB"
     VAT = "VAT"
     VCT = "VCT"
     VEN = "VEN"
     VGB = "VGB"
     VIR = "VIR"
     VNM = "VNM"
     VUT = "VUT"
     WLF = "WLF"
     WSM = "WSM"
     YEM = "YEM"
     YUG = "YUG"
     ZAF = "ZAF"
     ZMB = "ZMB"
     ZWE = "ZWE"


class Governmentreimbursementprogram(str, Enum):
     """
     401 - Government reimbursement program

     MM  Medicare
     C  Medi-Cal
     """


     MM = "MM"
     C = "C"


class Schooltype(str, Enum):
     """
     402 - School type

     D  Dental
     G  Graduate
     M  Medical
     U  Undergraduate
     """


     D = "D"
     G = "G"
     M = "M"
     U = "U"


class Languageability(str, Enum):
     """
     403 - Language ability

     1  Read
     2  Write
     3  Speak
     4  Understand
     5  Sign
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"


class Languageproficiency(str, Enum):
     """
     404 - Language proficiency

     1  Excellent
     2  Good
     3  Fair
     4  Poor
     5  Some (level unknown)
     6  None
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"


class ParticipantOrganizationUnitType(str, Enum):
     """
     406 - Participant Organization Unit Type

     H  Home
     O  Office
     1  Hospital
     2  Physician Clinic
     3  Long Term Care
     4  Acute Care
     5  Other
     """


     H = "H"
     O = "O"
     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"


class Applicationchangetype(str, Enum):
     """
     409 - Application change type

     SU  Start up
     SD  Shut down
     M  Migrates to different CPU
     """


     SU = "SU"
     SD = "SD"
     M = "M"


class Supplementalserviceinformationvalues(str, Enum):
     """
     411 - Supplemental service information values

     1ST  First
     2ND  Second
     3RD  Third
     4TH  Fourth
     5TH  Fifth
     ANT  Anterior
     A/P  Anterior/Posterior
     BLT  Bilateral
     DEC  Decubitus
     DST  Distal
     LAT  Lateral
     LFT  Left
     LLQ  Left Lower Quadrant
     LOW  Lower
     LUQ  Left Upper Quadrant
     MED  Medial
     OR  Operating Room
     PED  Pediatric
     POS  Posterior
     PRT  Portable
     PRX  Proximal
     REC  Recumbent
     RLQ  Right Lower Quadrant
     RGH  Right
     RUQ  Right Upper Quadrant
     UPP  Upper
     UPR  Upright
     WCT  With Contrast
     WOC  Without Contrast
     WSD  With Sedation
     """


     _1ST = "1ST"
     _2ND = "2ND"
     _3RD = "3RD"
     _4TH = "4TH"
     _5TH = "5TH"
     ANT = "ANT"
     A_P = "A/P"
     BLT = "BLT"
     DEC = "DEC"
     DST = "DST"
     LAT = "LAT"
     LFT = "LFT"
     LLQ = "LLQ"
     LOW = "LOW"
     LUQ = "LUQ"
     MED = "MED"
     OR = "OR"
     PED = "PED"
     POS = "POS"
     PRT = "PRT"
     PRX = "PRX"
     REC = "REC"
     RLQ = "RLQ"
     RGH = "RGH"
     RUQ = "RUQ"
     UPP = "UPP"
     UPR = "UPR"
     WCT = "WCT"
     WOC = "WOC"
     WSD = "WSD"


class DRGtransfertype(str, Enum):
     """
     415 - DRG transfer type

     N  DRG Non Exempt
     E  DRG Exempt
     """


     N = "N"
     E = "E"


class ProcedureDRGtype(str, Enum):
     """
     416 - Procedure DRG type

     1  1st non-Operative
     2  2nd non-Operative
     3  Major Operative
     4  2nd Operative
     5  3rd Operative
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"


class Tissuetypecode(str, Enum):
     """
     417 - Tissue type code

     1  Insufficient Tissue
     2  Not abnormal
     3  Abnormal-not categorized
     4  Mechanical abnormal
     5  Growth alteration
     6  Degeneration & necrosis
     7  Non-acute inflammation
     8  Non-malignant neoplasm
     9  Malignant neoplasm
     0  No tissue expected
     B  Basal cell carcinoma
     C  Carcinoma-unspecified type
     G  Additional tissue required
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"
     _7 = "7"
     _8 = "8"
     _9 = "9"
     _0 = "0"
     B = "B"
     C = "C"
     G = "G"


class Procedurepriority(str, Enum):
     """
     418 - Procedure priority

     0  the admitting procedure
     1  the primary procedure
     2  for ranked secondary procedures
       
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"
     NEL = ""


class Severityofillnesscode(str, Enum):
     """
     421 - Severity of illness code

     MI  Mild
     MO  Moderate
     SE  Severe
     """


     MI = "MI"
     MO = "MO"
     SE = "SE"


class Triagecode(str, Enum):
     """
     422 - Triage code

     1  Non-acute
     2  Acute
     3  Urgent
     4  Severe
     5  Dead on Arrival (DOA)
     99  Other
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _99 = "99"


class Casecategorycode(str, Enum):
     """
     423 - Case category code

     D  Doctor's Office Closed
     """


     D = "D"


class Gestationcategorycode(str, Enum):
     """
     424 - Gestation category code

     1  Premature / Pre-term
     2  Full Term
     3  Overdue / Post-term
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"


class Newborncode(str, Enum):
     """
     425 - Newborn code

     5  Born at home
     3  Born en route
     1  Born in facility
     4  Other
     2  Transfer in
     """


     _5 = "5"
     _3 = "3"
     _1 = "1"
     _4 = "4"
     _2 = "2"


class Bloodproductcode(str, Enum):
     """
     426 - Blood product code

     CRYO  Cryoprecipitated AHF
     CRYOP  Pooled Cryopecipitate
     FFP  Fresh Frozen Plasma
     FFPTH  Fresh Frozen Plasma - Thawed
     PC  Packed Cells
     PCA  Autologous Packed Cells
     PCNEO  Packed Cells - Neonatal
     PCW  Washed Packed Cells
     PLT  Platelet Concentrate
     PLTNEO  Reduced Volume Platelets
     PLTP  Pooled Platelets
     PLTPH  Platelet Pheresis
     PLTPHLR  Leukoreduced Platelet Pheresis
     RWB  Reconstituted Whole Blood
     WBA  Autologous Whole Blood
     """


     CRYO = "CRYO"
     CRYOP = "CRYOP"
     FFP = "FFP"
     FFPTH = "FFPTH"
     PC = "PC"
     PCA = "PCA"
     PCNEO = "PCNEO"
     PCW = "PCW"
     PLT = "PLT"
     PLTNEO = "PLTNEO"
     PLTP = "PLTP"
     PLTPH = "PLTPH"
     PLTPHLR = "PLTPHLR"
     RWB = "RWB"
     WBA = "WBA"


class Riskmanagementincidentcode(str, Enum):
     """
     427 - Risk management incident code

     B  Body fluid exposure
     C  Contaminated Substance
     D  Diet Errors
     E  Equipment problem
     F  Patient fell (not from bed)
     H  Patient fell from bed
     I  Infusion error
     J  Foreign object left during surgery
     K  Sterile precaution violated
     P  Procedure error
     R  Pharmaceutical error
     S  Suicide Attempt
     T  Transfusion error
     O  Other
     """


     B = "B"
     C = "C"
     D = "D"
     E = "E"
     F = "F"
     H = "H"
     I = "I"
     J = "J"
     K = "K"
     P = "P"
     R = "R"
     S = "S"
     T = "T"
     O = "O"


class Incidenttypecode(str, Enum):
     """
     428 - Incident type code

     P  Preventable
     U  User Error
     O  Other
     """


     P = "P"
     U = "U"
     O = "O"


class ProductionclassCode(str, Enum):
     """
     429 - Production class Code

     BR  Breeding/genetic stock
     DA  Dairy
     DR  Draft
     DU  Dual Purpose
     LY  Layer, Includes Multiplier flocks
     MT  Meat
     OT  Other
     PL  Pleasure
     RA  Racing
     SH  Show
     NA  Not Applicable
     U  Unknown
     """


     BR = "BR"
     DA = "DA"
     DR = "DR"
     DU = "DU"
     LY = "LY"
     MT = "MT"
     OT = "OT"
     PL = "PL"
     RA = "RA"
     SH = "SH"
     NA = "NA"
     U = "U"


class Modeofarrivalcode(str, Enum):
     """
     430 - Mode of arrival code

     A  Ambulance
     C  Car
     F  On foot
     H  Helicopter
     P  Public Transport
     O  Other
     U  Unknown
     """


     A = "A"
     C = "C"
     F = "F"
     H = "H"
     P = "P"
     O = "O"
     U = "U"


class Recreationaldrugusecode(str, Enum):
     """
     431 - Recreational drug use code

     A  Alcohol
     K  Kava
     M  Marijuana
     T  Tobacco - smoked
     C  Tobacco - chewed
     O  Other
     U  Unknown
     """


     A = "A"
     K = "K"
     M = "M"
     T = "T"
     C = "C"
     O = "O"
     U = "U"


class Admissionlevelofcarecode(str, Enum):
     """
     432 - Admission level of care code

     AC  Acute
     CH  Chronic
     CO  Comatose
     CR  Critical
     IM  Improved
     MO  Moribund
     """


     AC = "AC"
     CH = "CH"
     CO = "CO"
     CR = "CR"
     IM = "IM"
     MO = "MO"


class Precautioncode(str, Enum):
     """
     433 - Precaution code

     A  Aggressive
     B  Blind
     C  Confused
     D  Deaf
     I  On IV
     N  "No-code" (i.e. Do not resuscitate)
     P  Paraplegic
     O  Other
     U  Unknown
     """


     A = "A"
     B = "B"
     C = "C"
     D = "D"
     I = "I"
     N = "N"
     P = "P"
     O = "O"
     U = "U"


class Patientconditioncode(str, Enum):
     """
     434 - Patient condition code

     A  Satisfactory
     C  Critical
     P  Poor
     S  Stable
     O  Other
     U  Unknown
     """


     A = "A"
     C = "C"
     P = "P"
     S = "S"
     O = "O"
     U = "U"


class Advancedirectivecode(str, Enum):
     """
     435 - Advance directive code

     DNR  Do not resuscitate
     """


     DNR = "DNR"


class SensitivitytoCausativeAgentcode(str, Enum):
     """
     436 - Sensitivity to Causative Agent code

     AD  Adverse Reaction (Not otherwise classified)
     AL  Allergy
     CT  Contraindication
     IN  Intolerance
     """


     AD = "AD"
     AL = "AL"
     CT = "CT"
     IN = "IN"


class Alertdevicecode(str, Enum):
     """
     437 - Alert device code

     B  Bracelet
     N  Necklace
     W  Wallet Card
     """


     B = "B"
     N = "N"
     W = "W"


class Allergyclinicalstatus(str, Enum):
     """
     438 - Allergy clinical status

     U  Unconfirmed
     P  Pending
     S  Suspect
     C  Confirmed or verified
     I  Confirmed but inactive
     E  Erroneous
     D  Doubt raised
     """


     U = "U"
     P = "P"
     S = "S"
     C = "C"
     I = "I"
     E = "E"
     D = "D"


class Datatypes(str, Enum):
     """
     440 - Data types

     AD  Address
     CD  Channel definition
     CE  Coded element
     CF  Coded element with formatted values
     CK  Composite ID with check digit
     CM  Composite
     CN  Composite ID number and name
     CNE  Coded with no exceptions
     CP  Composite price
     CQ  Composite quantity with units
     CWE  Coded with exceptions
     CX  Extended composite ID with check digit
     DLN  Driver's license number
     DR  Date/time range
     DT  Date
     ED  Encapsulated data
     EI  Entity identifier
     FC  Financial class
     FN  Family name
     FT  Formatted text
     HD  Hierarchic designator
     ID  Coded values for HL7 tables
     IS  Coded value for user-defined tables
     JCC  Job code/class
     MA  Multiplexed array
     MO  Money
     NA  Numeric array
     NM  Numeric
     PL  Person location
     PN  Person name
     PPN  Performing person time stamp
     PT  Processing type
     QIP  Query input parameter list
     QSC  Query selection criteria
     RCD  Row column definition
     RI  Repeat interval
     RP  Reference pointer
     SAD  Street Address
     SCV  Scheduling class value pair
     SI  Sequence ID
     SN  Structured numeric
     SRT  Sort order
     ST  String
     TM  Time
     TN  Telephone number
     TQ  Timing/quantity
     TS  Time stamp
     TX  Text data
     VH  Visiting hours
     VID  Version identifier
     XAD  Extended address
     XCN  Extended composite ID number and name
     XON  Extended composite name and ID number for organizations
     XPN  Extended person name
     XTN  Extended telecommunications number
     """


     AD = "AD"
     CD = "CD"
     CE = "CE"
     CF = "CF"
     CK = "CK"
     CM = "CM"
     CN = "CN"
     CNE = "CNE"
     CP = "CP"
     CQ = "CQ"
     CWE = "CWE"
     CX = "CX"
     DLN = "DLN"
     DR = "DR"
     DT = "DT"
     ED = "ED"
     EI = "EI"
     FC = "FC"
     FN = "FN"
     FT = "FT"
     HD = "HD"
     ID = "ID"
     IS = "IS"
     JCC = "JCC"
     MA = "MA"
     MO = "MO"
     NA = "NA"
     NM = "NM"
     PL = "PL"
     PN = "PN"
     PPN = "PPN"
     PT = "PT"
     QIP = "QIP"
     QSC = "QSC"
     RCD = "RCD"
     RI = "RI"
     RP = "RP"
     SAD = "SAD"
     SCV = "SCV"
     SI = "SI"
     SN = "SN"
     SRT = "SRT"
     ST = "ST"
     TM = "TM"
     TN = "TN"
     TQ = "TQ"
     TS = "TS"
     TX = "TX"
     VH = "VH"
     VID = "VID"
     XAD = "XAD"
     XCN = "XCN"
     XON = "XON"
     XPN = "XPN"
     XTN = "XTN"


class Immunizationregistrystatus(str, Enum):
     """
     441 - Immunization registry status

     A  Active
     I  Inactive
     L  Inactive - Lost to follow-up (cancel contract)
     M  Inactive - Moved or gone elsewhere (cancel contract)
     P  Inactive - Permanently inactive (Do not reactivate or add new entries to the record)
     O  Other
     U  Unknown
     """


     A = "A"
     I = "I"
     L = "L"
     M = "M"
     P = "P"
     O = "O"
     U = "U"


class Locationservicecode(str, Enum):
     """
     442 - Location service code

     D  Diagnostic
     T  Therapeutic
     P  Primary Care
     E  Emergency Room Casualty
     """


     D = "D"
     T = "T"
     P = "P"
     E = "E"


class ProviderrRole(str, Enum):
     """
     443 - Provider role

     AD  Admitting
     AT  Attending
     CP  Consulting Provider
     FHCP  Family Health Care Professional
     PP  Primary Care Provider
     RP  Referring Provider
     RT  Referred to Provider
     """


     AD = "AD"
     AT = "AT"
     CP = "CP"
     FHCP = "FHCP"
     PP = "PP"
     RP = "RP"
     RT = "RT"


class Nameassemblyorder(str, Enum):
     """
     444 - Name assembly order

     G  Prefix Given Middle Family Suffix
     F  Prefix Family Middle Given Suffix
     """


     G = "G"
     F = "F"


class IdentityReliabilityCode(str, Enum):
     """
     445 - Identity Reliability Code

     US  Unknown/Default Social Security Number
     UD  Unknown/Default Date of Birth
     UA  Unknown/Default Address
     AL  Patient/Person Name is an Alias
     """


     US = "US"
     UD = "UD"
     UA = "UA"
     AL = "AL"


class EventtType(str, Enum):
     """
     450 - Event type

     LOG  Log Event
     SER  Service Event
     """


     LOG = "LOG"
     SER = "SER"


class Substanceidentifier(str, Enum):
     """
     451 - Substance identifier

     ALL  Used for query of all inventory items
     """


     ALL = "ALL"


class Healthcareprovidertypecode(str, Enum):
     """
     452 - Health care provider type code

     SUGGESTION  ANSI ASC X12 Health Care Provider Taxonomy, Level 1 - Type
     """


     SUGGESTION = "SUGGESTION"


class Healthcareproviderclassification(str, Enum):
     """
     453 - Health care provider classification

     SUGGESTION  ANSI ASC X12 Health Care Provider Taxonomy, Level 2 -  Classification
     """


     SUGGESTION = "SUGGESTION"


class Healthcareproviderareaofspecialization(str, Enum):
     """
     454 - Health care provider area of specialization

     SUGGESTION  ANSI ASC X12 Health Care Provider Taxonomy, Level 3 - specialization
     """


     SUGGESTION = "SUGGESTION"


class Typeofbillcode(str, Enum):
     """
     455 - Type of bill code

     131  Hospital - Outpatient - Admit thru Discharge Claim
     141  Hospital - Other - Admit thru Discharge Claim
1312
     """


     _131 = "131"
     _141 = "141"


class Revenuecode(str, Enum):
     """
     456 - Revenue code

     260  IV Therapy
     280  Oncology
     301  Lab/Chemistry
     991  Cafeteria /Guest Tray
     993  Telephone/Telegraph
     994  TV/Radio
1312
     """


     _260 = "260"
     _280 = "280"
     _301 = "301"
     _991 = "991"
     _993 = "993"
     _994 = "994"


class Overallclaimdispositioncode(str, Enum):
     """
     457 - Overall claim disposition code

     0  No edits present on claim
     1  Only edits present are for line item denial or rejection
     2  Multiple-day claim with one or more days denied or rejected
     3  Claim denied, rejected, suspended or returned to provider with only post payment edits
     4  Claim denied, rejected, suspended or returned to provider with only pre payment edits
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"


class OCEeditcode(str, Enum):
     """
     458 - OCE edit code

     1  Invalid diagnosis code
     2  Diagnosis and age conflict
     3  Diagnosis and sex conflict
     4  Medicare secondary payer alert
     5  E-code as reason for visit
     6  Invalid procedure code
     7  Procedure and age conflict
     8  Procedure and sex conflict
     9  Nov-covered service
     10  Non-covered  service submitted for verification of denial (condition code 21 from header information on claim)
     11  Non-covered service submitted for FI review (condition code 20 from header information on claim)
     12  Questionable covered service
     13  Additional payment for service not provided by Medicare
     14  Code indicates a site of service not included in OPPS
     15  Service unit out of range for procedure
     16  Multiple bilateral procedures without modifier 50 (see Appendix A)
     17  Multiple bilateral procedures with modifier 50 (see Appendix A)
     18  Inpatient procedure
     19  Mutually exclusive procedure that is not allowed even if appropriate modifier present
     20  Component of a comprehensive procedure that is not allowed even if appropriate modifier present
     21  Medical visit on same day as a type "T" or "S" procedure without modifier 25 (see Appendix B)
     22  Invalid modifier
     23  Invalid date
     24  Date out of OCE range
     25  Invalid age
     26  Invalid sex
     27  Only incidental services reported
     28  Code not recognized by Medicare; alternate code for same service available
     29  Partial hospitalization service for non-mental health diagnosis
     30  Insufficient services on day of partial hospitalization
     31  Partial hospitalization on same day as ECT or type "T" procedure
     32  Partial hospitalization claim spans 3 or less days with in-sufficient services, or ECT or significant procedure on at least one of the days
     33  Partial hospitalization claim spans more than 3 days with insufficient number of days having mental health services
     34  Partial hospitalization claim spans more than 3 days with insufficient number of days meeting partial hospitalization criteria
     35  Only activity therapy and/or occupational therapy services provided
     36  Extensive mental health services provided on day of ECT or significant procedure
     37  Terminated bilateral procedure or terminated procedure with units greater than one
     38  Inconsistency between implanted device and implantation procedure
     39  Mutually exclusive procedure that would be allowed if appropriate modifier were present
     40  Component of a comprehensive procedure that would be allowed if appropriate modifier were present
     41  Invalid revenue code
     42  Multiple medical visits on same day with same revenue code without condition code G0 (see Appendix B)
1312
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"
     _6 = "6"
     _7 = "7"
     _8 = "8"
     _9 = "9"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _13 = "13"
     _14 = "14"
     _15 = "15"
     _16 = "16"
     _17 = "17"
     _18 = "18"
     _19 = "19"
     _20 = "20"
     _21 = "21"
     _22 = "22"
     _23 = "23"
     _24 = "24"
     _25 = "25"
     _26 = "26"
     _27 = "27"
     _28 = "28"
     _29 = "29"
     _30 = "30"
     _31 = "31"
     _32 = "32"
     _33 = "33"
     _34 = "34"
     _35 = "35"
     _36 = "36"
     _37 = "37"
     _38 = "38"
     _39 = "39"
     _40 = "40"
     _41 = "41"
     _42 = "42"


class ReimbursementActionCode(str, Enum):
     """
     459 - Reimbursement Action Code

     0  OCE line item denial or rejection is not ignored
     1  OCE line item denial or rejection is ignored
     2  External line item denial. Line item is denied even if no OCE edits
     3  External line item rejection. Line item is rejected even if no OCE edits
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"
     _3 = "3"


class Denialorrejectioncode(str, Enum):
     """
     460 - Denial or rejection code

     0  Line item not denied or rejected
     1  Line item denied or rejected
     2  Line item is on a multiple-day claim. The line item is not denied or rejected, but occurs on a day that has been denied or rejected.
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"


class Name_addressrepresentation(str, Enum):
     """
     465 - Name-address representation

     I  Ideographic (i.e., Kanji)
     A  Alphabetic (i.e., Default or some single-byte)
     P  Phonetic (i.e., ASCII, Katakana, Hiragana, etc.)
     """


     I = "I"
     A = "A"
     P = "P"


class Ambulatorypaymentclassificationcode(str, Enum):
     """
     466 - Ambulatory payment classification code

     031  Dental procedures
     163  Excision/biopsy
     181  Level 1 skin repair.
1312
     """


     _031 = "031"
     _163 = "163"
     _181 = "181"


class Modifiereditcode(str, Enum):
     """
     467 - Modifier edit code

     0  Modifier does NOT exist
     1  Modifier present, no errors
     2  Modifier invalid
     3  Modifier NOT approved for ASC/HOPD use
     4  Modifier approved for ASC/HOPD use, inappropriate for code
     U  Modifer edit code unknown
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     U = "U"


class Paymentadjustmentcode(str, Enum):
     """
     468 - Payment adjustment code

     1  No payment adjustment
     2  Designated current drug or biological payment adjustment applies to APC (status indicator G)
     3  Designated new device payment adjustment applies to APC (status indicator H)
     4  Designated new drug or new biological payment adjustment applies to APC (status indicator J)
     5  Deductible not applicable (specific list of HCPCS codes)
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"
     _5 = "5"


class Packagingstatuscode(str, Enum):
     """
     469 - Packaging status code

     0  Not packaged
     1  Packaged service (status indicator N, or no HCPCS code and certain revenue codes)
     2  Packaged as part of partial hospitalization per diem or daily mental health service per diem
     """


     _0 = "0"
     _1 = "1"
     _2 = "2"


class Reimbursementtypecode(str, Enum):
     """
     470 - Reimbursement type code

     OPPS  Outpatient Prospective Payment System
     Pckg  Packaged APC
     Lab  Clinical Laboratory APC
     Thrpy  Therapy APC
     DME  Durable Medical Equipment
     EPO  Epotein
     Mamm  Screening Mammography APC
     PartH  Partial Hospitalization APC
     Crnl  Corneal Tissue APC
     NoPay  This APC is not paid
     """


     OPPS = "OPPS"
     Pckg = "Pckg"
     Lab = "Lab"
     Thrpy = "Thrpy"
     DME = "DME"
     EPO = "EPO"
     Mamm = "Mamm"
     PartH = "PartH"
     Crnl = "Crnl"
     NoPay = "NoPay"


class TQConjunctionID(str, Enum):
     """
     472 - TQ Conjunction ID

     S  Synchronous. Do the next specification after this one (unless otherwise constrained by the following components: ORC-7^4-start date/time and ORC-7^5-end date/time). An "S" specification implies that the second timing sequence follows the first, e.g., when
     A  Asynchronous: Do the next specification in parallel with this one (unless otherwise constrained by the following components: ORC-7^4-start date/time and ORC-7^5-end date/time).  The conjunction of "A" specifies two parallel instructions, as are sometimes
     C  This is an actuation time.  It will be followed by a completion time for the service.  This code allows one to distinguish between the time and priority at which a service should be actuated (e.g., blood should be drawn) and the time and priority at which
     """


     S = "S"
     A = "A"
     C = "C"


class Formularystatus(str, Enum):
     """
     473 - Formulary status

     G  This observation/service is on the formulary, and has guidelines
     N  This observation/service is not on the formulary
     R  This observation/service is on the formulary, but is restricted
     Y  This observation/service is on the formulary
     """


     G = "G"
     N = "N"
     R = "R"
     Y = "Y"


class PractitionerOrganizationUnitType(str, Enum):
     """
     474 - Practitioner Organization Unit Type

     D  Department
     F  Facility
     L  Local market area
     M  Medical Center Area
     U  Subdepartment
     S  Subdivision
     V  Division
     """


     D = "D"
     F = "F"
     L = "L"
     M = "M"
     U = "U"
     S = "S"
     V = "V"
