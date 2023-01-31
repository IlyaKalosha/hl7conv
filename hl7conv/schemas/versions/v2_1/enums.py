from enum import Enum


class SEX(str, Enum):
     """
     001 - SEX

     F  Female
     M  Male
     O  Other
     U  Unknown
     """


     F = "F"
     M = "M"
     O = "O"
     U = "U"


class MARITALSTATUS(str, Enum):
     """
     002 - MARITAL STATUS

     A  Separated
     D  Divorced
     M  Married
     S  Single
     W  Widowed
     """


     A = "A"
     D = "D"
     M = "M"
     S = "S"
     W = "W"


class EVENTTYPECODE(str, Enum):
     """
     003 - EVENT TYPE CODE

     O01  Order message
     Q01  Immediate access
     P02  Purge Patient Accounts
     A19  Patient query
     A15  Pending transfer
     A01  Admit a patient
     A02  Transfer a Patient
     A03  Discharge a Patient
     A04  Register a Patient
     A05  Pre-admit a Patient
     A06  Transfer an outpatient to inpatient
     A07  Transfer an Inpatient to Outpatient
     A08  Update patient information
     A09  Patient departing
     A10  Patient arriving
     A11  Cancel admit
     A12  Cancel transfer
     A13  Cancel discharge
     A14  Pending admit
     A16  Pending discharge
     A17  Swap Patients
     A18  Merge patient information
     A20  Bed status updates
     A21  Leave of Absence - Out (leaving)
     A22  Leave of Absence - In (returning)
     A23  Delete a Patient Record
     A24  Link Patient Records
     O02  Order response
     P01  Add and update patient account
     P03  Post detail financial transaction
     P04  Generate bills and A/R statements
     Q02  Deferred Access
     R01  Unsolicited transmission of requested Observ.
     R03  Display oriented results, query/unsol. update
     """


     O01 = "O01"
     Q01 = "Q01"
     P02 = "P02"
     A19 = "A19"
     A15 = "A15"
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
     A16 = "A16"
     A17 = "A17"
     A18 = "A18"
     A20 = "A20"
     A21 = "A21"
     A22 = "A22"
     A23 = "A23"
     A24 = "A24"
     O02 = "O02"
     P01 = "P01"
     P03 = "P03"
     P04 = "P04"
     Q02 = "Q02"
     R01 = "R01"
     R03 = "R03"


class PATIENTCLASS(str, Enum):
     """
     004 - PATIENT CLASS

     E  Emergency
     I  Inpatient
     O  Outpatient
     P  Preadmit
     """


     E = "E"
     I = "I"
     O = "O"
     P = "P"


class ETHNICGROUP(str, Enum):
     """
     005 - ETHNIC GROUP

     R  Oriental
     H  Hispanic
     C  Caucasian
     B  Black
     """


     R = "R"
     H = "H"
     C = "C"
     B = "B"


class RELIGION(str, Enum):
     """
     006 - RELIGION

     P  Protestant
     N  Hindu
     M  Church of Latter Day Saints (Mormon)
     L  Lutheran
     J  Judaism
     E  Episcopalian
     C  Catholic
     B  Baptist
     A  Atheist
     """


     P = "P"
     N = "N"
     M = "M"
     L = "L"
     J = "J"
     E = "E"
     C = "C"
     B = "B"
     A = "A"


class ADMISSIONTYPE(str, Enum):
     """
     007 - ADMISSION TYPE

     A  Accident
     E  Emergency
     L  Labor and Delivery
     R  Routine
     """


     A = "A"
     E = "E"
     L = "L"
     R = "R"


class ACKNOWLEDGMENTCODE(str, Enum):
     """
     008 - ACKNOWLEDGMENT CODE

     AA  Application Accept
     AE  Application Error
     AR  Application Reject
     """


     AA = "AA"
     AE = "AE"
     AR = "AR"


class AMBULATORYSTATUS(str, Enum):
     """
     009 - AMBULATORY STATUS

     A0  No functional limitations
     A1  Ambulates with assistive device
     A2  Wheelchair/stretcher bound
     A3  Comatose; non-responsive
     A4  Disoriented
     A5  Vision impaired
     A6  Hearing impaired
     A7  Speech impaired
     A8  Non-English Speaking
     A9  Functional level unknown
     B1  Oxygen Therapy
     B2  Special Equipment (tunes, IV's, Catheters)
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


class CHARGINGSYSTEM(str, Enum):
     """
     011 - CHARGING SYSTEM

     R  System that received and processed the order
     S  System that sent the order
     """


     R = "R"
     S = "S"


class STOCKLOCATION(str, Enum):
     """
     012 - STOCK LOCATION

     AN  Filled from ancillary department stock
     FL  Filled from floor stock
     """


     AN = "AN"
     FL = "FL"


class ISOLATION(str, Enum):
     """
     016 - ISOLATION

     0  Antibiotic Resistance Precautions
     1  Blood and Needle Precautions
     2  Enteric Precautions
     3  Neutropenic Precautions
     4  Pregnant Women Precautions
     5  Respiratory Isolation
     6  Secretion/Excretion Precautions
     7  Strict Isolation
     8  Wound and skin Precautions
     9  Precautions
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


class UNUSEDTABLE(str, Enum):
     """
     020 - UNUSED TABLE

     1  Asymptomatic Manifestation
     2  Moderate Manifestation
     3  Major Manifestation
     4  Catastrophic Manifestation
     """


     _1 = "1"
     _2 = "2"
     _3 = "3"
     _4 = "4"


class PRIORITY(str, Enum):
     """
     027 - PRIORITY (COMPONENT 6 QTY-TIMING[735])

     T  Timed collection
     A  ASAP. Fill after STAT orders.
     S  Stat. Required immediately.
     """


     T = "T"
     A = "A"
     S = "S"


class ROUTE(str, Enum):
     """
     033 - ROUTE

     IV  Intravenous
     CH  Chew
     DU  Dust
     EA  Ear
     EY  Eye
     IA  Intro-arterial
     ID  Intra-dermal
     IF  Infiltrate
     IH  Inhalation
     IM  Intra-muscular
     IN  Intra-nasal
     IR  Irrigate
     AP  Apply externally
     IT  Intrathecal
     WI  Wipe
     NB  Nebulized
     NG  Nathogasic
     PA  Peri-anally
     PT  Paint
     PU  IV push
     RC  Rectally
     SH  Shampoo
     SL  Sublingual
     SO  Soak
     SS  IV soluset
     TP  Topically
     WA  Wash
     IS  Inserted
     """


     IV = "IV"
     CH = "CH"
     DU = "DU"
     EA = "EA"
     EY = "EY"
     IA = "IA"
     ID = "ID"
     IF = "IF"
     IH = "IH"
     IM = "IM"
     IN = "IN"
     IR = "IR"
     AP = "AP"
     IT = "IT"
     WI = "WI"
     NB = "NB"
     NG = "NG"
     PA = "PA"
     PT = "PT"
     PU = "PU"
     RC = "RC"
     SH = "SH"
     SL = "SL"
     SO = "SO"
     SS = "SS"
     TP = "TP"
     WA = "WA"
     IS = "IS"


class SITEADMINISTERED(str, Enum):
     """
     034 - SITE ADMINISTERED

     L  Left arm
     B  Buttock
     """


     L = "L"
     B = "B"


class UNITSOFMEASURE_ISO5281977(str, Enum):
     """
     036 - UNITS OF MEASURE - ISO528 1977

     VL  Vial
     TB  Tablet
     SC  Square centimeters
     OZ  Ounces
     MG  Milligrams
     MEQ  Milliequivalent
     KG  Kilograms
     GM  Grams
     EA  Each
     BT  Bottle
     """


     VL = "VL"
     TB = "TB"
     SC = "SC"
     OZ = "OZ"
     MG = "MG"
     MEQ = "MEQ"
     KG = "KG"
     GM = "GM"
     EA = "EA"
     BT = "BT"


class ORDERSTATUS(str, Enum):
     """
     038 - ORDER STATUS

     SC  In process, scheduled
     IP  In process, unspecified
     HD  Order is on hold
     ER  Error, order not found
     DC  Order was discontinued
     CM  Order is completed
     CA  Order was canceled
     """


     SC = "SC"
     IP = "IP"
     HD = "HD"
     ER = "ER"
     DC = "DC"
     CM = "CM"
     CA = "CA"


class WHATSUBJECTFILTER(str, Enum):
     """
     048 - WHAT SUBJECT FILTER

     STA  Status
     RES  Result
     PRO  Procedure
     OTH  Other
     MRO  Most recent outpatient
     MRI  Most recent inpatient
     DEM  Demographics
     CAN  Cancel. Used to cancel a query
     APN  Patient name look up
     ANU  Nursing Unit Look up
     ADV  Advice/Diagnosis
     """


     STA = "STA"
     RES = "RES"
     PRO = "PRO"
     OTH = "OTH"
     MRO = "MRO"
     MRI = "MRI"
     DEM = "DEM"
     CAN = "CAN"
     APN = "APN"
     ANU = "ANU"
     ADV = "ADV"


class DIAGNOSISCODINGMETHOD(str, Enum):
     """
     053 - DIAGNOSIS CODING METHOD

     I9  ICD9
     """


     I9 = "I9"


class CHECKDIGITSCHEME(str, Enum):
     """
     061 - CHECK DIGIT SCHEME

     M11  Mod 11 check digit scheme
     """


     M11 = "M11"


class EVENTREASON(str, Enum):
     """
     062 - EVENT REASON

     02  Physician Order
     01  Patient Request
     """


     _02 = "02"
     _01 = "01"


class ACTIONCODE(str, Enum):
     """
     065 - ACTION CODE

     S  Schedule the tests specified below
     P  Pending specimen-Order sent prior to delivery
     O  Specimen obtained by service other than Lab
     L  Lab to obtain specimen from patient.
     G  Generated order
     C  Cancel order for battery or tests named
     A  Add ordered tests to the existing specimen
     """


     S = "S"
     P = "P"
     O = "O"
     L = "L"
     G = "G"
     C = "C"
     A = "A"


class SOURCEOFSPECIMEN(str, Enum):
     """
     070 - SOURCE OF SPECIMEN

     SAL  Saliva
     BON  Bone
     BRN  Burn
     CNJT  Conjunctiva
     CSF  Cerebral spinal fluid
     CVX  Cervix
     EAR  Ear
     FIB  Fibroblood
     HAR  Hair
     MN  Amniotic Fluid
     NOS  Nose
     OTH  Other
     PLAS  Plasma
     BLD  Blood
     RBC  Erythrocytes
     WND  Wound
     SEM  Seminal Fluid
     SER  Serum
     SKN  Skin
     SNV  Synovial Fluid
     STL  Stool
     SWT  Sweat
     THRT  Throat
     TIS  Tissue
     UMB  Umbilical Blood
     UR  Urine
     URTH  Urethra
     WBC  Leukocytes
     PRT  Peritoneal Fluid
     """


     SAL = "SAL"
     BON = "BON"
     BRN = "BRN"
     CNJT = "CNJT"
     CSF = "CSF"
     CVX = "CVX"
     EAR = "EAR"
     FIB = "FIB"
     HAR = "HAR"
     MN = "MN"
     NOS = "NOS"
     OTH = "OTH"
     PLAS = "PLAS"
     BLD = "BLD"
     RBC = "RBC"
     WND = "WND"
     SEM = "SEM"
     SER = "SER"
     SKN = "SKN"
     SNV = "SNV"
     STL = "STL"
     SWT = "SWT"
     THRT = "THRT"
     TIS = "TIS"
     UMB = "UMB"
     UR = "UR"
     URTH = "URTH"
     WBC = "WBC"
     PRT = "PRT"


class DIAGNOSTICSERVICESECTIONID(str, Enum):
     """
     074 - DIAGNOSTIC SERVICE SECTION ID

     OT  Occupational Therapy
     CH  Chemistry
     CP  Cytopathology
     CT  CAT scan
     CUS  Cardiac Ultrasound
     EC  Electrocardiac (e.g., EKG, EEC, Holter)
     HM  Hematology
     IMM  Immunology
     MB  Microbiology
     MCB  Mycobacteriology
     MYC  Mycology
     NMR  Nuclear magnetic resonance
     BG  Blood gases
     NRS  Nursing service measures
     XRC  Cineradiography
     OTH  Other
     OUS  OB Ultrasound
     PHR  Pharmacy
     PT  Physical Therapy
     RC  Respiratory Care
     RT  Radiation Therapy
     RUS  Radiology ultrasound
     SP  Surgical Pathology
     SR  Serology
     TX  Toxicology
     VUS  Vascular Ultrasound
     NMS  Nuclear medicine scan
     """


     OT = "OT"
     CH = "CH"
     CP = "CP"
     CT = "CT"
     CUS = "CUS"
     EC = "EC"
     HM = "HM"
     IMM = "IMM"
     MB = "MB"
     MCB = "MCB"
     MYC = "MYC"
     NMR = "NMR"
     BG = "BG"
     NRS = "NRS"
     XRC = "XRC"
     OTH = "OTH"
     OUS = "OUS"
     PHR = "PHR"
     PT = "PT"
     RC = "RC"
     RT = "RT"
     RUS = "RUS"
     SP = "SP"
     SR = "SR"
     TX = "TX"
     VUS = "VUS"
     NMS = "NMS"


class MESSAGETYPE(str, Enum):
     """
     076 - MESSAGE TYPE

     UDM  Unsolicited display          QRY       V
     OSQ  Order status query           ORD       IV
     ORU  Observ. result/unsolicited   ANR       VII
     ORR  Order response message       ORD       IV
     ORM  Order                        ORD       IV
     ORF  Observ. Result/record resp.  ANR       VII
     MCF  Delayed acknowledgment       CNT       II
     DSR  Display response             QRY       V
     BAR  Add/change billing account   BLN       VI
     ARD  Ancillary RPT (display)      ANR       VII
     ACK  General Acknowledgment       CNT       II
     """


     UDM = "UDM"
     OSQ = "OSQ"
     ORU = "ORU"
     ORR = "ORR"
     ORM = "ORM"
     ORF = "ORF"
     MCF = "MCF"
     DSR = "DSR"
     BAR = "BAR"
     ARD = "ARD"
     ACK = "ACK"


class ABNORMALFLAGS(str, Enum):
     """
     078 - ABNORMAL FLAGS

     VS  Very sensitive
     U  Significant change up
     S  Sensitive
     R  Resists
     null  No range defined,or normal ranges don't apply
     MS  Moderately sensitive
     LL  Below lower panic limits
     I  Interval
     HH  Above upper panic limits
     H  Above high normal
     D  Significant change down
     AA  Very abnormal
     A  Abnormal (applies to non-numeric results)
     <  Below absolute low-off instrument scale
     """


     VS = "VS"
     U = "U"
     S = "S"
     R = "R"
     null = "null"
     MS = "MS"
     LL = "LL"
     I = "I"
     HH = "HH"
     H = "H"
     D = "D"
     AA = "AA"
     A = "A"
     _ = "<"


class NATUREOFABNORMALTESTING(str, Enum):
     """
     080 - NATURE OF ABNORMAL TESTING

     S  A sexed based population
     R  A race based population
     N  None - generic normal range
     A  An aged based population
     """


     S = "S"
     R = "R"
     N = "N"
     A = "A"


class OBSERVATIONRESULTSTATUS(str, Enum):
     """
     085 - OBSERVATION RESULT STATUS

     S  Partial results
     R  Results entered - not verified
     I  Specimen in lab--results pending
     F  Complete/final results (entered and verified)
     D  Delete previously transmitted observation
     """


     S = "S"
     R = "R"
     I = "I"
     F = "F"
     D = "D"


class QUERYPRIORITY(str, Enum):
     """
     091 - QUERY PRIORITY

     I  Immediate
     D  Deferred
     """


     I = "I"
     D = "D"


class RE_ADMISSIONINDICATOR(str, Enum):
     """
     092 - RE-ADMISSION INDICATOR

     R  Readmission
     """


     R = "R"


class RELEASEOFINFORMATION(str, Enum):
     """
     093 - RELEASE OF INFORMATION

     Y  Yes
     N  No
     """


     Y = "Y"
     N = "N"


class WHENTOCHARGE(str, Enum):
     """
     100 - WHEN TO CHARGE

     S  At time service is started
     R  At time service is completed
     O  On receipt of order
     D  On discharge
     T  At a designated date / time
     """


     S = "S"
     R = "R"
     O = "O"
     D = "D"
     T = "T"


class DELAYEDACKNOWLEDGMENTTYPE(str, Enum):
     """
     102 - DELAYED ACKNOWLEDGMENT TYPE

     D  Message Received, stored for later processing
     """


     D = "D"


class PROCESSINGID(str, Enum):
     """
     103 - PROCESSING ID

     T  Training
     P  Production
     D  Debugging
     """


     T = "T"
     P = "P"
     D = "D"


class VERSIONCONTROLTABLE(str, Enum):
     """
     104 - VERSION CONTROL TABLE

     2.1  Release 2.1  March 1990
     2.0D  Demo    2.0  October 1988
     2.0  Release 2.0  September 1988
     """


     _2_1 = "2.1"
     _2_0D = "2.0D"
     _2_0 = "2.0"


class SOURCEOFCOMMENT(str, Enum):
     """
     105 - SOURCE OF COMMENT

     P  Orderer is source of comment
     L  Ancillary department is source of comment
     """


     P = "P"
     L = "L"


class QUERYFORMATCODE(str, Enum):
     """
     106 - QUERY FORMAT CODE

     R  Response in Record-oriented format
     """


     R = "R"


class DEFERREDRESPONSETYPE(str, Enum):
     """
     107 - DEFERRED RESPONSE TYPE

     L  Later than the DATE/TIME specified
     B  Before the date / time specified
     """


     L = "L"
     B = "B"


class QUERYRESULTSLEVEL(str, Enum):
     """
     108 - QUERY RESULTS LEVEL

     T  Full Results
     S  Status only
     O  Order plus order status
     R  Results without bulk text
     """


     T = "T"
     S = "S"
     O = "O"
     R = "R"


class REPORTPRIORITY(str, Enum):
     """
     109 - REPORT PRIORITY

     S  Stat
     R  Routine
     """


     S = "S"
     R = "R"


class BEDSTATUS(str, Enum):
     """
     116 - BED STATUS

     O  Occupied
     H  Housekeeping
     C  Closed
     U  Unoccupied
     """


     O = "O"
     H = "H"
     C = "C"
     U = "U"


class ORDERCONTROL(str, Enum):
     """
     119 - ORDER CONTROL

     RE  Observations to follow
     CH  Child order
     CN  Combined result
     DC  Discontinue order request
     DE  Data Errors
     DR  Discontinued as requested
     HD  Hold order request
     HR  On hold as requested
     NA  Number assigned            T
     NW  New order                  T
     OD  Order discontinued
     OK  Order accepted and OK
     CA  Cancel order request
     PA  Parent order
     XX  Order changed, unsolicited
     RO  Replacement order
     RP  Order replace request
     RR  Request received
     RU  Replaced unsolicited
     SN  Send filler number            F         I
     SS  Send order status request
     UD  Unable to discontinue
     UH  Unable to put on hold
     UR  Unable to release
     UX  Unable to change
     XR  Changed as requested
     OR  Released as requested
     """


     RE = "RE"
     CH = "CH"
     CN = "CN"
     DC = "DC"
     DE = "DE"
     DR = "DR"
     HD = "HD"
     HR = "HR"
     NA = "NA"
     NW = "NW"
     OD = "OD"
     OK = "OK"
     CA = "CA"
     PA = "PA"
     XX = "XX"
     RO = "RO"
     RP = "RP"
     RR = "RR"
     RU = "RU"
     SN = "SN"
     SS = "SS"
     UD = "UD"
     UH = "UH"
     UR = "UR"
     UX = "UX"
     XR = "XR"
     OR = "OR"


class RESPONSEFLAG(str, Enum):
     """
     121 - RESPONSE FLAG

     D  Same as R, also other associated segments.
     E  Report exceptions only.
     F  Same as D, plus confirmations explicitly.
     N  Only the MSA segment is returned.
     R  Same as E, also Replacement & Parent-child
     """


     D = "D"
     E = "E"
     F = "F"
     N = "N"
     R = "R"


class CHARGETYPE(str, Enum):
     """
     122 - CHARGE TYPE

     RS  Research
     PC  Professional
     NC  No Charge
     GR  Grant
     DP  Department
     CR  Credit
     CO  Contract
     CH  Charge
     """


     RS = "RS"
     PC = "PC"
     NC = "NC"
     GR = "GR"
     DP = "DP"
     CR = "CR"
     CO = "CO"
     CH = "CH"


class RESULTSTATUS_OBR(str, Enum):
     """
     123 - RESULT STATUS - OBR

     Z  No record of this patient
     Y  No order on record for this test
     S  Procedure scheduled, not done
     R  Results stored - not yet verified
     P  Preliminary results
     I  Specimen in lab, not yet processed.
     F  Final results - results stored & verified
     C  Correction of previously transmitted results
     """


     Z = "Z"
     Y = "Y"
     S = "S"
     R = "R"
     P = "P"
     I = "I"
     F = "F"
     C = "C"


class TRANSPORTATIONMODE(str, Enum):
     """
     124 - TRANSPORTATION MODE

     WHLC  Wheelchair
     WALK  Patient walks to diagnostic service
     PORT  The examining device goes to Patient's Loc.
     CART  Cart - patient travels on cart or gurney
     """


     WHLC = "WHLC"
     WALK = "WALK"
     PORT = "PORT"
     CART = "CART"


class VALUETYPE(str, Enum):
     """
     125 - VALUE TYPE

     TX  Text
     TS  Time stamp
     TM  Time
     ST  String data. Used to transmit numerics.
     PN  Person name
     FT  Formatted Text
     CK  Composite ID with check digit
     AD  Address
     """


     TX = "TX"
     TS = "TS"
     TM = "TM"
     ST = "ST"
     PN = "PN"
     FT = "FT"
     CK = "CK"
     AD = "AD"


class QUANTITYLIMITEDREQUEST(str, Enum):
     """
     126 - QUANTITY LIMITED REQUEST

     ZO  Locally defined
     PG  Pages
     LI  Lines
     CH  Characters
     """


     ZO = "ZO"
     PG = "PG"
     LI = "LI"
     CH = "CH"
