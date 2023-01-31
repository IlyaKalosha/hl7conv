from enum import Enum


class Sex(str, Enum):
     """
     001 - Sex

     U  Unknown
     O  Other
     M  Male
     F  Female
     """


     U = "U"
     O = "O"
     M = "M"
     F = "F"


class MaritalStatus(str, Enum):
     """
     002 - Marital Status

     W  Widowed
     S  Single
     M  Married
     D  Divorced
     A  Separated
     """


     W = "W"
     S = "S"
     M = "M"
     D = "D"
     A = "A"


class EventType(str, Enum):
     """
     003 - Event Type

     I01  RQI/RPI - Request for insurance information
     P06  BAR/ACK - End account
     I09  RQA/RPA - Request for modification to an authorization
     I08  RQA/RPA - Request for treatment authorization information
     I07  PIN/ACK - Unsolicited insurance information
     I06  RQC/RCL - Request/receipt of clinical data listing
     I05  RQC/RCI - Request for patient clinical information
     I04  RQD/RPI - Request for patient demographic data
     I11  RQA/RPA - Request for cancellation of an authorization
     I02  RQI/RPL - Request/receipt of patient selection display list
     I12  REF/RRI - Patient referral
     C12  CSU - Update/correction of patient order/result information
     C11  CSU - Patient completes a phase of the clinical trial
     C10  CSU - Patient completes the clinical trial
     C09  CSU - Automated time intervals for reporting, like monthly
     C08  SRM - Patient has gone off phase of clinical trial
     C07  SRM - Correct/update phase information
     C06  SRM - Cancel patient entering a phase (clerical mistake)
     C05  SRM - Patient enters phase of clinical trial
     I03  RQI/RPR - Request/receipt of patient selection list
     M06  MFN/MFK - Charge description master file
     P05  BAR/ACK - Update account
     P04  QRY/DSP - Generate bill and A/R statements
     P03  DFT/ACK - Post detail financial transaction
     P02  BAR/ACK - Purge patient account
     X01  PEX - Product experience
     O02  ORR - Order response (also RRE, RRD, RRG, RRA,
     A01  ADT/ACK - Admit a patient
     I10  RQA/RPA - Request for resubmission of an authorization
     M07  MFN/MFK - Clinical study without phases but with schedules master file
     C02  SRM - Cancel a patient registration on clinical trial (for clerical mistakes only)
     M05  MFN/MFK - Patient location master file
     M04  MFD/ACK - Master files delayed application acknowledgement
     M03  MFN/MFK - Master file - Test/Observation
     M02  MFN/MFK - Master file - Staff Practioner
     M01  MFN/MFK - Master file not otherwise specified (for backward compatibility only)
     I15  REF/RRI - Request patient referral status
     I14  REF/RRI - Cancel patient referral
     I13  REF/RRI - Modify patient referral
     M08  MFN/MFK - Test/Observation (Nurmeric) master file
     A10  ADT/ACK -  Patient arriving
     A19  QRY/ACK -  Patient query
     A18  ADT/ACK -  Merge patient information
     A17  ADT/ACK -  Swap patients
     A16  ADT/ACK -  Pending discharge
     A15  ADT/ACK -  Pending transfer
     A14  ADT/ACK -  Pending admit
     A13  ADT/ACK -  Cancel discharge
     C04  SRM - Patient has gone off a clinical trial
     A11  ADT/ACK -  Cancel admit
     A22  ADT/ACK -  Leave of absence - in (returning)
     A09  ADT/ACK -  Patient departing
     A08  ADT/ACK -  Update patient information
     A07  ADT/ACK -  Transfer an inpatient to outpatient
     A06  ADT/ACK -  Transfer an outpatient to inpatient
     A05  ADT/ACK -  Preadmit a patient
     A04  ADT/ACK -  Register a patient
     A03  ADT/ACK -  Discharge a patient
     A02  ADT/ACK -  Transfer a patient
     A12  ADT/ACK -  Cancel transfer
     A30  ADT/ACK -  Merge person information
     P01  BAR/ACK - Add and update patient account
     C01  SRM - Register a patient on a clinical trial
     A38  ADT/ACK - Cancel pre-admit
     A37  ADT/ACK -  Unlink patient information
     A36  ADT/ACK -  Merge patient information - patient ID and account number
     A35  ADT/ACK -  Merge patient information - account number only
     A34  ADT/ACK -  Merge patient information - patient ID only
     A33  ADT/ACK -  Cancel patient departing
     A20  ADT/ACK -  Bed status update
     A31  ADT/ACK -  Update person information
     A21  ADT/ACK -  Leave of absence - out (leaving)
     A29  ADT/ACK -  Delete person information
     A28  ADT/ACK -  Add person information
     A27  ADT/ACK -  Cancel pending admit
     A26  ADT/ACK -  Cancel pending transfer
     A25  ADT/ACK -  Cancel pending discharge
     A24  ADT/ACK -  Link patient information
     A23  ADT/ACK -  Delete a patient record
     C03  SRM - Correct/update registration information
     A32  ADT/ACK -  Cancel patient arriving
     S04  SRM/SRR - Request appointment cancellation
     R02  QRY - Query for results of observation
     R03  Display-oriented results, query/unsol. update (for backward compatibility only)
     R04  ORF - Response to query; transmission of requested observation
     S19  SIU/ACK - Notification ofmodification of service/resource on appointment
     S18  SIU/ACK - Notification of addition of service/resource on appointment
     RAR  RAR - Pharmacy administration information query response
     S17  SIU/ACK - Notification of appointmentdeletion
     RDR  RDR - Pharmacy dispense information query response
     RER  RER - Pharmacy encoded order information query response
     RGR  RGR - Pharmacy dose information query response
     ROR  ROR - Pharmacy prescription order query response
     S01  SRM/SRR - Request new appointment booking
     S20  SIU/ACK - Notification of cancellation of service/resource on appointment
     S03  SRM/SRR - Request appointment modification
     Q05  UDM/ACK - Unsolicited display update
     S05  SRM/SRR - Request appointment discontinuation
     S06  SRM/SRR - Request appointment deletion
     S07  SRM/SRR - Request addition of service/resource on appointment
     S16  SIU/ACK - Notification of appointment discontinuation
     S15  SIU/ACK - Notification of appointment cancellation
     O01  ORM - Order message (also RDE, RDS, RGV, RAS,
     S14  SIU/ACK - Notification of appointment modification
     S13  SIU/ACK - Notification of appointment rescheduling
     S12  SIU/ACK - Notification of new appointment booking
     S11  SRM/SRR - Request deletion of servic/resource on appointment
     S10  SRM/SRR - Request discontinuation of servic/resource on appointment
     S09  SRM/SRR - Request cancellation of servic/resource on appointment
     S02  SRM/SRR - Request appointment rescheduling
     T05  MDM/ACK - Document addendum notification
     W02  QRF - Waveform result, response to query
     W01  ORU - Waveform result, unsolicited transmission of requested information
     varies  MFQ/MFR - Master files query (use event same as asking for e.g., M05 - location)
     V04  VXU - Unsolicited vaccination record update
     V03  VXR - Vaccination record response
     V02  VXX - Response to vaccination query returning multiple PID matches
     V01  VXQ - Query for vaccination record
     T09  MDM/ACK - Document cancel notification
     T08  MDM/ACK - Document replace notification and content
     R01  ORU/ACK - Unsolicited transmission of an observation
     T06  MDM/ACK - Document addendum notification and content
     S08  SRM/SRR - Request modification of service/resource on appointment
     T04  MDM/ACK - Document status change notification and content
     S23  SIU/ACK - Notification of blocked schedule time slot(s)
     Q03  DSR/ACK - Deferred response to a query
     Q02  QRY/ACK - Query sent for deferred response
     Q01  QRY/DSR - Query sent for immediate response
     S21  SIU/ACK - Notification of discontinuation of service/resource on appointment
     T07  MDM/ACK - Document replace notification
     S22  SIU/ACK - Notification of deletion of service/resource on appointment
     T03  MDM/ACK - Document status change notification
     S24  SIU/ACK - Notification of open (unblocked) schedule time slot(s)
     S25  SQM/SQR - Query schedule information
     T01  MDM/ACK - Original document notification
     T02  MDM/ACK - Original document notification and content
     T11  MDM/ACK - Document cancel notification
     T10  MDM/ACK - Document replacement notification and content
     S26  notification that patient did not show up for schedule appointment
     A40  ADT/ACK - Merge patient - internal ID
     A39  ADT/ACK - Merge person - external ID
     T12  QRY/DOC - Document query
     PC7  PGL - PC/Goal Update
     PCD  PPP - PC/Pathway (Problem Oriented) Delete
     PCC  PPP - PC/Pathway (Problem Oriented) Update
     PCB  PPP - PC/Pathway (Problem Oriented) Add
     PCA  PGL - PC/Goal Response
     M09  MFN/MFK - Test/Observation (Categorical) master file
     M10  MFN/MFK - Test/Observation batteries master file
     M11  MFN/MFK - Test/calculated observation master file
     A50  ADT/ACK - Change visit number
     PC8  PGL - PC/Goal Delete
     PCG  PPP - PC/Pathway (Goal Oriented) Add
     PC6  PGL - PC/Goal Add
     PC5  PPR - PC/Problem Reponse
     PC4  PPR - PC/Problem Query
     PC3  PPR - PC/Problem Delete
     PC2  PPR - PC/Problem Update
     P07  PEX - Unsolicited initial individual product experience report
     P08  PEX - Unsolicited update individual product experience report
     P09  SUR - Summary product experience report
     PC9  PGL - PC/Goal Query
     CNQ  QRY/EQQ/SPQ/VQQ/RQQ - Cancel query
     A42  ADT/ACK - Merge visit - visit number
     A43  ADT/ACK - Move patient information - internal ID
     A44  ADT/ACK - Move account information - internal ID
     A45  ADT/ACK - Move visit information - visit number
     A46  ADT/ACK - Change external ID
     A47  ADT/ACK - Change internal ID
     A48  ADT/ACK - Change alternate patient ID
     A49  ADT/ACK - Change patient account number
     PCE  PPP - PC/Pathway (Problem Oriented) Query
     PC1  PPR - PC/Problem Add
     PCF  PPP - PC/Pathway (Problem Oriented) Query Response
     R06  UDM-unsolicited update/display results
     R05  QRY/DSR- query für display results
     Q06  OSQ/OSR - Query for order status
     PCL  PPP - PC/Pathway (Goal Oriented) Query Response
     PCK  PPP - PC/Pathway (Goal Oriented) Query
     PCJ  PPP - PC/Pathway (Goal Oriented) Delete
     PCH  PPP - PC/Pathway (Goal Oriented) Update
     A41  ADT/ACK - Merge account - patient account number
     A51  ADT/ACK - Change alternate visit ID
     """


     I01 = "I01"
     P06 = "P06"
     I09 = "I09"
     I08 = "I08"
     I07 = "I07"
     I06 = "I06"
     I05 = "I05"
     I04 = "I04"
     I11 = "I11"
     I02 = "I02"
     I12 = "I12"
     C12 = "C12"
     C11 = "C11"
     C10 = "C10"
     C09 = "C09"
     C08 = "C08"
     C07 = "C07"
     C06 = "C06"
     C05 = "C05"
     I03 = "I03"
     M06 = "M06"
     P05 = "P05"
     P04 = "P04"
     P03 = "P03"
     P02 = "P02"
     X01 = "X01"
     O02 = "O02"
     A01 = "A01"
     I10 = "I10"
     M07 = "M07"
     C02 = "C02"
     M05 = "M05"
     M04 = "M04"
     M03 = "M03"
     M02 = "M02"
     M01 = "M01"
     I15 = "I15"
     I14 = "I14"
     I13 = "I13"
     M08 = "M08"
     A10 = "A10"
     A19 = "A19"
     A18 = "A18"
     A17 = "A17"
     A16 = "A16"
     A15 = "A15"
     A14 = "A14"
     A13 = "A13"
     C04 = "C04"
     A11 = "A11"
     A22 = "A22"
     A09 = "A09"
     A08 = "A08"
     A07 = "A07"
     A06 = "A06"
     A05 = "A05"
     A04 = "A04"
     A03 = "A03"
     A02 = "A02"
     A12 = "A12"
     A30 = "A30"
     P01 = "P01"
     C01 = "C01"
     A38 = "A38"
     A37 = "A37"
     A36 = "A36"
     A35 = "A35"
     A34 = "A34"
     A33 = "A33"
     A20 = "A20"
     A31 = "A31"
     A21 = "A21"
     A29 = "A29"
     A28 = "A28"
     A27 = "A27"
     A26 = "A26"
     A25 = "A25"
     A24 = "A24"
     A23 = "A23"
     C03 = "C03"
     A32 = "A32"
     S04 = "S04"
     R02 = "R02"
     R03 = "R03"
     R04 = "R04"
     S19 = "S19"
     S18 = "S18"
     RAR = "RAR"
     S17 = "S17"
     RDR = "RDR"
     RER = "RER"
     RGR = "RGR"
     ROR = "ROR"
     S01 = "S01"
     S20 = "S20"
     S03 = "S03"
     Q05 = "Q05"
     S05 = "S05"
     S06 = "S06"
     S07 = "S07"
     S16 = "S16"
     S15 = "S15"
     O01 = "O01"
     S14 = "S14"
     S13 = "S13"
     S12 = "S12"
     S11 = "S11"
     S10 = "S10"
     S09 = "S09"
     S02 = "S02"
     T05 = "T05"
     W02 = "W02"
     W01 = "W01"
     varies = "varies"
     V04 = "V04"
     V03 = "V03"
     V02 = "V02"
     V01 = "V01"
     T09 = "T09"
     T08 = "T08"
     R01 = "R01"
     T06 = "T06"
     S08 = "S08"
     T04 = "T04"
     S23 = "S23"
     Q03 = "Q03"
     Q02 = "Q02"
     Q01 = "Q01"
     S21 = "S21"
     T07 = "T07"
     S22 = "S22"
     T03 = "T03"
     S24 = "S24"
     S25 = "S25"
     T01 = "T01"
     T02 = "T02"
     T11 = "T11"
     T10 = "T10"
     S26 = "S26"
     A40 = "A40"
     A39 = "A39"
     T12 = "T12"
     PC7 = "PC7"
     PCD = "PCD"
     PCC = "PCC"
     PCB = "PCB"
     PCA = "PCA"
     M09 = "M09"
     M10 = "M10"
     M11 = "M11"
     A50 = "A50"
     PC8 = "PC8"
     PCG = "PCG"
     PC6 = "PC6"
     PC5 = "PC5"
     PC4 = "PC4"
     PC3 = "PC3"
     PC2 = "PC2"
     P07 = "P07"
     P08 = "P08"
     P09 = "P09"
     PC9 = "PC9"
     CNQ = "CNQ"
     A42 = "A42"
     A43 = "A43"
     A44 = "A44"
     A45 = "A45"
     A46 = "A46"
     A47 = "A47"
     A48 = "A48"
     A49 = "A49"
     PCE = "PCE"
     PC1 = "PC1"
     PCF = "PCF"
     R06 = "R06"
     R05 = "R05"
     Q06 = "Q06"
     PCL = "PCL"
     PCK = "PCK"
     PCJ = "PCJ"
     PCH = "PCH"
     A41 = "A41"
     A51 = "A51"


class PatientClass(str, Enum):
     """
     004 - Patient Class

     R  Recurring Patient
     P  Preadmit
     O  Outpatient
     I  Inpatient
     E  Emergency
     B  Obstetrics
     """


     R = "R"
     P = "P"
     O = "O"
     I = "I"
     E = "E"
     B = "B"


class AdmissionType(str, Enum):
     """
     007 - Admission Type

     A  Accident
     E  Emergency
     L  Labor and Delivery
     R  Routine
     """


     A = "A"
     E = "E"
     L = "L"
     R = "R"


class AcknowledgementCode(str, Enum):
     """
     008 - Acknowledgement Code

     AA  Original mode:  Application Accept / Enhanced mode:  Application acknowledgement:  Accept
     AE  Original mode:  Application Error / Enhanced mode:  Application acknowledgement:  Error
     AR  Original mode:  Application Reject / Enhanced mode:  Application acknowledgement:  Reject
     CA  Enhanced mode:  Application acknowledgement:  Commit Accept
     CE  Enhanced mode:  Application acknowledgement:  Commit Error
     CR  Enhanced mode:  Application acknowledgement:  Commit Reject
     """


     AA = "AA"
     AE = "AE"
     AR = "AR"
     CA = "CA"
     CE = "CE"
     CR = "CR"


class AmbulatoryStatus(str, Enum):
     """
     009 - Ambulatory Status

     A0  No functional limitations
     A1  Ambulates with assistive device
     A2  Wheelchair/stretcher bound
     A3  Comatose; non-responsive
     A4  Disoriented
     A5  Vision Impaired
     A6  Hearing Impaired
     A7  Speech Impaired
     A8  Nonenglish Speaking
     A9  Functional level unknown
     B1  Oxygen Therapy
     B2  Special Equipment (tubes, IV's, catheters)
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


class TransactionType(str, Enum):
     """
     017 - Transaction Type

     PY  Payment
     CG  Charge
     CD  Credit
     AJ  Adjustment
     """


     PY = "PY"
     CG = "CG"
     CD = "CD"
     AJ = "AJ"


class Priority(str, Enum):
     """
     027 - Priority

     T  Timing critical (do as near as possible to requested time)
     S  Stat (do immediately)
     R  Routine
     P  Preoperative (to be done prior to surgery)
     A  As soon as possible (a priority lower than stat)
     """


     T = "T"
     S = "S"
     R = "R"
     P = "P"
     A = "A"


class OrderStatus(str, Enum):
     """
     038 - Order Status

     SC  In process, scheduled
     RP  Order has been replaced
     IP  In process, unspecified
     HD  Order is on hold
     ER  Error, order not found
     DC  Order was discontinued
     CM  Order is completed
     CA  Order was canceled
     A  Some, but not all, results available
     """


     SC = "SC"
     RP = "RP"
     IP = "IP"
     HD = "HD"
     ER = "ER"
     DC = "DC"
     CM = "CM"
     CA = "CA"
     A = "A"


class WhatSubjectFilter(str, Enum):
     """
     048 - What Subject Filter

     NSC  Network status change
     ANU  Nursing unit lookup (returns patients in beds, excluding empty beds)
     APA  Account number query, return matching visit
     APM  Medical record number query, returns visits for a medical record number
     APN  Patient name lookup
     APP  Physician lookup
     ARN  Nursing unit lookup (returns patients in beds, including empty beds)
     CAN  Cancel.  Used to cancel a query
     DEM  Demographics
     FIN  Financial
     GOL  Goals
     MRI  Most recent inpatient
     ADV  Advice/diagnosis
     NCK  Network clock
     VXI  Vaccine Information
     NST  Network statistic
     ORD  Order
     OTH  Other
     PRB  Problems
     PRO  Procedure
     RAR  Pharmacy administration information
     RDR  Pharmacy dispense information
     RER  Pharmacy encoded order information
     RES  Result
     RGR  Pharmacy give information
     ROR  Pharmacy prescription information
     STA  Status
     MRO  Most recent outpatient
     """


     NSC = "NSC"
     ANU = "ANU"
     APA = "APA"
     APM = "APM"
     APN = "APN"
     APP = "APP"
     ARN = "ARN"
     CAN = "CAN"
     DEM = "DEM"
     FIN = "FIN"
     GOL = "GOL"
     MRI = "MRI"
     ADV = "ADV"
     NCK = "NCK"
     VXI = "VXI"
     NST = "NST"
     ORD = "ORD"
     OTH = "OTH"
     PRB = "PRB"
     PRO = "PRO"
     RAR = "RAR"
     RDR = "RDR"
     RER = "RER"
     RES = "RES"
     RGR = "RGR"
     ROR = "ROR"
     STA = "STA"
     MRO = "MRO"


class DiagnosisType(str, Enum):
     """
     052 - Diagnosis Type

     W  Working
     F  Final
     A  Admitting
     """


     W = "W"
     F = "F"
     A = "A"


class CheckDigitScheme(str, Enum):
     """
     061 - Check Digit Scheme

     M11  Mod 11 algorithm
     M10  Mod 10 algorithm
     """


     M11 = "M11"
     M10 = "M10"


class EventReason(str, Enum):
     """
     062 - Event Reason

     03  Census management
     02  Physician order
     01  Patient request
     """


     _03 = "03"
     _02 = "02"
     _01 = "01"


class SpecimenActionCode(str, Enum):
     """
     065 - Specimen Action Code

     S  Schedule the tests specified below
     R  Revised order
     P  Pending specimen; Order sent prior to delivery
     O  Specimen obtained by service other than Lab
     L  Lab to obtain specimen from patient
     G  Generated order; reflex order
     A  Add ordered tests to the existing specimen
     """


     S = "S"
     R = "R"
     P = "P"
     O = "O"
     L = "L"
     G = "G"
     A = "A"


class SpecimenSourceCodes(str, Enum):
     """
     070 - Specimen Source Codes

     GENC  Genital cervix
     MAR  Marrow
     EARW  Ear wax (cerumen)
     ELT  Electrode
     ENDC  Endocardium
     ENDM  Endometrium
     EOS  Eosinophils
     EXHLD  Exhaled gas (=breath)
     EYE  Eye
     FIB  Fibroblasts
     FIST  Fistula
     FLT  Filter
     FLU  Body fluid, unsp
     GAS  Gas
     DUFL  Duodenal fluid
     IT  Intubation tube
     ABS  Abcess
     LYM  Lymphocytes
     LNV  Line venous
     LNA  Line arterial
     LN  Line
     GAST  Gastric fluid/contents
     LAM  Lamella
     GEN  Genital
     ISLT  Isolate
     IHG  Inhaled Gas
     HAR  Hair
     GENV  Genital vaginal
     GENL  Genital lochia
     DRN  Drain
     LIQ  Liquid NOS
     CALC  Calculus (=Stone)
     AMN  Amniotic fluid
     ASP  Aspirate
     BBL  Blood bag
     BDY  Whole body
     BIFL  Bile fluid
     BLD  Whole blood
     BLDA  Blood  arterial
     BLDC  Blood  capillary
     BLDV  Blood  venous
     BON  Bone
     BPH  Basophils
     BPU  Blood product unit
     BRN  Burn
     EAR  Ear
     CSF  Cerebral spinal fluid
     DOSE  Dose med or substance
     DIAF  Dialysis fluid
     CYST  Cyst
     CVX  Cervix
     CVM  Cervical mucus
     BRO  Bronchial
     CTP  Catheter tip
     BRTH  Breath (use EXHLD)
     COL  Colostrum
     CNL  Cannula
     CNJT  Conjunctiva
     CDM  Cardiac muscle
     CBLD  Cord blood
     MBLD  Menstrual blood
     CUR  Curettage
     UR  Urine
     MAC  Macrophages
     TEAR  Tears
     THRB  Thrombocyte (platelet)
     THRT  Throat
     TISG  Tissue gall bladder
     TISPL  Tissue placenta
     TISS  Tissue
     TISU  Tissue ulcer
     TLGI  Tissue large intestine
     TLNG  Tissue lung
     TSMI  Tissue small intestine
     TUB  Tube NOS
     ULC  Ulcer
     STON  Stone (use CALC)
     VOM  Vomitus
     WNDE  Wound exudate
     WNDD  Wound drainage
     WNDA  Wound abscess
     WND  Wound
     WICK  Wick
     UMB  Umbilical blood
     WAT  Water
     UMED  Unknown medicine
     USUB  Unknown substance
     URTH  Urethra
     URT  Urine catheter
     URNS  Urine sediment
     URC  Urine clean catch
     STL  Stool = Fecal
     WBC  Leukocytes
     PRT  Peritoneal fluid /ascites
     MEC  Meconium
     MILK  Breast milk
     MLK  Milk
     NAIL  Nail
     NOS  Nose (nasal passage)
     ORH  Other
     PAFL  Pancreatic fluid
     PAT  Patient
     PLAS  Plasma
     PLB  Plasma bag
     PLC  Placenta
     PLR  Pleural fluid (thoracentesis fld)
     PMN  Polymorphonuclear neutrophils
     SWT  Sweat
     SER  Serum
     SPTT  Sputum - tracheal aspirate
     SPTC  Sputum - coughed
     SPT  Sputum
     SPRM  Spermatozoa
     SNV  Synovial fluid (Joint fluid)
     PPP  Patelet poor plasma
     SKM  Skeletal muscle
     PRP  Platelet rich plasma
     SEM  Seminal fluid
     SAL  Saliva
     RT  Route of medicine
     RBC  Erythrocytes
     PUS  Pus
     XXX  To be specified in another part of the message
     SKN  Skin
     """


     GENC = "GENC"
     MAR = "MAR"
     EARW = "EARW"
     ELT = "ELT"
     ENDC = "ENDC"
     ENDM = "ENDM"
     EOS = "EOS"
     EXHLD = "EXHLD"
     EYE = "EYE"
     FIB = "FIB"
     FIST = "FIST"
     FLT = "FLT"
     FLU = "FLU"
     GAS = "GAS"
     DUFL = "DUFL"
     IT = "IT"
     ABS = "ABS"
     LYM = "LYM"
     LNV = "LNV"
     LNA = "LNA"
     LN = "LN"
     GAST = "GAST"
     LAM = "LAM"
     GEN = "GEN"
     ISLT = "ISLT"
     IHG = "IHG"
     HAR = "HAR"
     GENV = "GENV"
     GENL = "GENL"
     DRN = "DRN"
     LIQ = "LIQ"
     CALC = "CALC"
     AMN = "AMN"
     ASP = "ASP"
     BBL = "BBL"
     BDY = "BDY"
     BIFL = "BIFL"
     BLD = "BLD"
     BLDA = "BLDA"
     BLDC = "BLDC"
     BLDV = "BLDV"
     BON = "BON"
     BPH = "BPH"
     BPU = "BPU"
     BRN = "BRN"
     EAR = "EAR"
     CSF = "CSF"
     DOSE = "DOSE"
     DIAF = "DIAF"
     CYST = "CYST"
     CVX = "CVX"
     CVM = "CVM"
     BRO = "BRO"
     CTP = "CTP"
     BRTH = "BRTH"
     COL = "COL"
     CNL = "CNL"
     CNJT = "CNJT"
     CDM = "CDM"
     CBLD = "CBLD"
     MBLD = "MBLD"
     CUR = "CUR"
     UR = "UR"
     MAC = "MAC"
     TEAR = "TEAR"
     THRB = "THRB"
     THRT = "THRT"
     TISG = "TISG"
     TISPL = "TISPL"
     TISS = "TISS"
     TISU = "TISU"
     TLGI = "TLGI"
     TLNG = "TLNG"
     TSMI = "TSMI"
     TUB = "TUB"
     ULC = "ULC"
     STON = "STON"
     VOM = "VOM"
     WNDE = "WNDE"
     WNDD = "WNDD"
     WNDA = "WNDA"
     WND = "WND"
     WICK = "WICK"
     UMB = "UMB"
     WAT = "WAT"
     UMED = "UMED"
     USUB = "USUB"
     URTH = "URTH"
     URT = "URT"
     URNS = "URNS"
     URC = "URC"
     STL = "STL"
     WBC = "WBC"
     PRT = "PRT"
     MEC = "MEC"
     MILK = "MILK"
     MLK = "MLK"
     NAIL = "NAIL"
     NOS = "NOS"
     ORH = "ORH"
     PAFL = "PAFL"
     PAT = "PAT"
     PLAS = "PLAS"
     PLB = "PLB"
     PLC = "PLC"
     PLR = "PLR"
     PMN = "PMN"
     SWT = "SWT"
     SER = "SER"
     SPTT = "SPTT"
     SPTC = "SPTC"
     SPT = "SPT"
     SPRM = "SPRM"
     SNV = "SNV"
     PPP = "PPP"
     SKM = "SKM"
     PRP = "PRP"
     SEM = "SEM"
     SAL = "SAL"
     RT = "RT"
     RBC = "RBC"
     PUS = "PUS"
     XXX = "XXX"
     SKN = "SKN"


class DiagnosticServiceSectionID(str, Enum):
     """
     074 - Diagnostic Service Section ID

     EC  Electrocardiac (e.g., EKG,  EEC, Holter)
     NMR  Nuclear magnetic resonance
     MYC  Mycology
     MCB  Mycobacteriology
     MB  Microbiology
     LAB  Laboratory
     IMM  Immunology
     ICU  Bedside ICU Monitoring
     AU  Audiology
     EN  Electroneuro (EEG, EMG,EP,PSG)
     OSL  Outside Lab
     CUS  Cardiac Ultrasound
     CTH  Cardiac catheterization
     CT  CAT scan
     CP  Cytopathology
     CH  Chemistry
     BLB  Blood bank
     BG  Blood gases
     HM  Hematology
     RAD  Radiology
     VUS  Vascular Ultrasound
     VR  Virology
     TX  Toxicology
     SR  Serology
     SP  Surgidal Pathology
     RX  Radiograph
     RUS  Radiology ultrasound
     NMS  Nuclear medicine scan
     RC  Respiratory Care (therapy)
     NRS  Nursing service measures
     PT  Physical Therapy
     PHY  Physician (Hx. Dx, admission note, etc.l)
     PHR  Pharmacy
     PF  Pulmonary function
     OUS  OB Ultrasound
     OTH  Other
     OT  Occupational Therapy
     XRC  Cineradiograph
     RT  Radiation therapy
     """


     EC = "EC"
     NMR = "NMR"
     MYC = "MYC"
     MCB = "MCB"
     MB = "MB"
     LAB = "LAB"
     IMM = "IMM"
     ICU = "ICU"
     AU = "AU"
     EN = "EN"
     OSL = "OSL"
     CUS = "CUS"
     CTH = "CTH"
     CT = "CT"
     CP = "CP"
     CH = "CH"
     BLB = "BLB"
     BG = "BG"
     HM = "HM"
     RAD = "RAD"
     VUS = "VUS"
     VR = "VR"
     TX = "TX"
     SR = "SR"
     SP = "SP"
     RX = "RX"
     RUS = "RUS"
     NMS = "NMS"
     RC = "RC"
     NRS = "NRS"
     PT = "PT"
     PHY = "PHY"
     PHR = "PHR"
     PF = "PF"
     OUS = "OUS"
     OTH = "OTH"
     OT = "OT"
     XRC = "XRC"
     RT = "RT"


class MessageType(str, Enum):
     """
     076 - Message Type

     ACK  General acknowledgment message
     ADT  ADT message
     ADR  ADT response
     ARD  Ancillary RPT (display)
     BAR  Add/change billing account
     CNQ  Cancel query
     CSU  Unsolicited clinical study data
     DFT  Detail financial transaction
     DSR  Display response
     DOC  Document Response
     EQQ  Embedded query language query
     ERP  Event replay response
     ERQ  Event replay query
     EDR  Enhanced display response
     MCF  Delayed acknowledgment
     MFD  Master files delayed application ack
     MDM  Documentation message
     MFN  Master files notification
     MFQ  Master files query
     MFR  Master files query response
     MFK  Master files application ack
     ORF  Observ. result/record response
     ORM  Order message
     ORR  Order acknowledgment message
     ORU  Observ result/unsolicited
     OSR  Order status response
     OSQ  Order status query
     PEX  Product experience
     PIN  Patient information
     PPG  Patient Pathway (goal-oriented) message
     PPT  Patient Pathway (goal oriented) response
     PGL  Patient goal
     PPR  Patient problem
     PPV  Patient Goal Response
     PRR  Patient Problem Response
     PTR  Patient Pathway (problem-oriented) response
     QCK  Query General  Acknowledgment
     QRY  Query, original Mode
     RAS  Pharmacy administration message
     RCL  Return clinical list
     RDS  Pharmacy dispense message
     RDE  Pharmacy encoded order message
     RER  Pharmacy encoded order information
     RGR  Pharmacy dose information
     RDR  Pharmacy dispense information
     RAR  Pharmacy administration information
     RCI  Return clinical information
     RGV  Pharmacy give message
     ROR  Pharmacy prescription order response
     REF  Patient referral
     ROC  Request clinical information
     ROD  Request pateint demographics
     RPI  Return patient information
     RPA  Return patient authorization
     RRI  Return patient referral
     RPL  Return patient display list
     RPR  Return patient list
     RQA  Request patient authorization
     RQC  Request Clinical Information
     RQI  Request patient information
     RQP  Request Patient Demographics
     RRA  Pharmacy administration acknowledgment
     RRD  Pharmacy dispense acknowledgment
     RRE  Pharmacy encoded order acknowledgment
     RRG  Pharmacy give acknowledgment
     SRM  Schedule request
     SQR  Schedule query response
     SIU  Schedule information unsolicited
     SPQ  Stored procedure request
     SQM  Schedule query
     SRR  Scheduled request response
     TBR  Tabular response
     UDM  Unsolicited display message
     VQQ  Virtual table query
     VXQ  Query for vaccination record
     VXR  Vaccination query record response
     VXU  Unsolicited vaccinnation record update
     VXX  Vaccination query response with multiple PID matches
     """


     ACK = "ACK"
     ADT = "ADT"
     ADR = "ADR"
     ARD = "ARD"
     BAR = "BAR"
     CNQ = "CNQ"
     CSU = "CSU"
     DFT = "DFT"
     DSR = "DSR"
     DOC = "DOC"
     EQQ = "EQQ"
     ERP = "ERP"
     ERQ = "ERQ"
     EDR = "EDR"
     MCF = "MCF"
     MFD = "MFD"
     MDM = "MDM"
     MFN = "MFN"
     MFQ = "MFQ"
     MFR = "MFR"
     MFK = "MFK"
     ORF = "ORF"
     ORM = "ORM"
     ORR = "ORR"
     ORU = "ORU"
     OSR = "OSR"
     OSQ = "OSQ"
     PEX = "PEX"
     PIN = "PIN"
     PPG = "PPG"
     PPT = "PPT"
     PGL = "PGL"
     PPR = "PPR"
     PPV = "PPV"
     PRR = "PRR"
     PTR = "PTR"
     QCK = "QCK"
     QRY = "QRY"
     RAS = "RAS"
     RCL = "RCL"
     RDS = "RDS"
     RDE = "RDE"
     RER = "RER"
     RGR = "RGR"
     RDR = "RDR"
     RAR = "RAR"
     RCI = "RCI"
     RGV = "RGV"
     ROR = "ROR"
     REF = "REF"
     ROC = "ROC"
     ROD = "ROD"
     RPI = "RPI"
     RPA = "RPA"
     RRI = "RRI"
     RPL = "RPL"
     RPR = "RPR"
     RQA = "RQA"
     RQC = "RQC"
     RQI = "RQI"
     RQP = "RQP"
     RRA = "RRA"
     RRD = "RRD"
     RRE = "RRE"
     RRG = "RRG"
     SRM = "SRM"
     SQR = "SQR"
     SIU = "SIU"
     SPQ = "SPQ"
     SQM = "SQM"
     SRR = "SRR"
     TBR = "TBR"
     UDM = "UDM"
     VQQ = "VQQ"
     VXQ = "VXQ"
     VXR = "VXR"
     VXU = "VXU"
     VXX = "VXX"


class AbnormalFlags(str, Enum):
     """
     078 - Abnormal Flags

     LL  Below lower panic limits
     >  Above absolute high-off instrument scale
     A  Abnormal (applies to non-numeric results)
     AA  Very abnormal (applies to non-numeric units, analagous to panic limits for numeric units)
     B  Better--use when direction not relevant
     D  Significant change down
     H  Above high normal
     HH  Above upper panic limits
     <  Below absolute low-off instrument scale
     L  Below low normal
     W  Worse--use when direction not relevant
     MS  Moderately sensitive (microbiology sensitivies only)
     N  Normal (applies to non-numeric results)
     null  No range defined, or normal ranges don't apply
     R  Resistant (microbiology sensitivies only)
     S  Sensitive (microbiology sensitivies only)
     U  Significant change up
     VS  Very sensitive (microbiology sensitivies only)
     I  Intermediate (microbiology sensitivies only)
     """


     LL = "LL"
     _ = ">"
     A = "A"
     AA = "AA"
     B = "B"
     D = "D"
     H = "H"
     HH = "HH"
     _ = "<"
     L = "L"
     W = "W"
     MS = "MS"
     N = "N"
     null = "null"
     R = "R"
     S = "S"
     U = "U"
     VS = "VS"
     I = "I"


class NatureofAbnormalTesting(str, Enum):
     """
     080 - Nature of Abnormal Testing

     S  A sex-based population
     R  A race-based population
     N  None - generic normal range
     A  An age-based population
     """


     S = "S"
     R = "R"
     N = "N"
     A = "A"


class ObservationResultStatusCodesInterpretation(str, Enum):
     """
     085 - Observation Result Status Codes Interpretation

     X  Results cannot be obtained for this observation
     U  Results status change to Final.  Results did not change (don't transmit test).  E.g., radiology changes status from preliminary to final
     S  Partial results
     R  Results entered -- not verified
     P  Preliminary results
     I  Specimen in lab; results pending
     F  Final results;  Can only be changed with a corrected result.
     D  Deletes the OBX record
     C  Record coming over is a correction and thus replaces a final result
     """


     X = "X"
     U = "U"
     S = "S"
     R = "R"
     P = "P"
     I = "I"
     F = "F"
     D = "D"
     C = "C"


class QueryPriority(str, Enum):
     """
     091 - Query Priority

     I  Immediate
     D  Deferred
     """


     I = "I"
     D = "D"


class Re_admissionIndicator(str, Enum):
     """
     092 - Re-admission Indicator

     R  Readmission
     """


     R = "R"


class ReleaseInformation(str, Enum):
     """
     093 - Release Information

     Y  Yes
     N  No
     """


     Y = "Y"
     N = "N"


class TypeofAgreement(str, Enum):
     """
     098 - Type of Agreement

     U  unified
     S  Standard
     M  Maternity
     """


     U = "U"
     S = "S"
     M = "M"


class WhentoCharge(str, Enum):
     """
     100 - When to Charge

     T  At a designated date/time
     S  At time service is started
     R  At time service is completed
     O  On receipt of order
     D  On discharge
     """


     T = "T"
     S = "S"
     R = "R"
     O = "O"
     D = "D"


class DelayedAcknowledgementType(str, Enum):
     """
     102 - Delayed Acknowledgement Type

     F  Acknowledgement after processing
     D  Message received, stored for later processing
     """


     F = "F"
     D = "D"


class ProcessingID(str, Enum):
     """
     103 - Processing ID

     T  Training
     P  Production
     D  Debugging
     """


     T = "T"
     P = "P"
     D = "D"


class VersionID(str, Enum):
     """
     104 - Version ID

     2.3  Release 2.3 ?? 1996
     2.2  Release 2.2  December 1994
     2.1  Release 2.1  March 1990
     2.0D  Demo 2.0  October 1988
     2.0  Release 2.0  September 1988
     """


     _2_3 = "2.3"
     _2_2 = "2.2"
     _2_1 = "2.1"
     _2_0D = "2.0D"
     _2_0 = "2.0"


class SourceofComment(str, Enum):
     """
     105 - Source of Comment

     P  Orderer (placer) is source of comment
     O  Other system is source of comment
     L  Ancillary (filler) department is source of comment
     """


     P = "P"
     O = "O"
     L = "L"


class Query_ResponseFormatCode(str, Enum):
     """
     106 - Query-Response Format Code

     T  Response is in tabular format
     R  Response is in record-oriented format
     D  Response is in display format
     """


     T = "T"
     R = "R"
     D = "D"


class DeferredResponseType(str, Enum):
     """
     107 - Deferred Response Type

     L  Later than the date/time specified
     B  Before the date/time specified
     """


     L = "L"
     B = "B"


class QueryResultsLevel(str, Enum):
     """
     108 - Query Results Level

     T  Full results (default)
     S  Status only
     R  Results without bulk text
     O  Order plus order status
     """


     T = "T"
     S = "S"
     R = "R"
     O = "O"


class ReportPriority(str, Enum):
     """
     109 - Report Priority

     S  STAT
     R  Routine
     """


     S = "S"
     R = "R"


class BedStatus(str, Enum):
     """
     116 - Bed Status

     U  Unoccupied
     O  Occupied
     K  Contaminated
     I  Isolated
     H  Housekeeping
     C  Closed
     """


     U = "U"
     O = "O"
     K = "K"
     I = "I"
     H = "H"
     C = "C"


class OrderControlCode(str, Enum):
     """
     119 - Order Control Code

     HR  On hold as requested
     XX  Order changed, unsolicited
     PA  Parent order
     OR  Released as requested
     OK  Order accepted and OK
     OH  Order held
     OD  Order discontinued
     OC  Order canceled
     RL  Release previous hold
     NA  Number assigned
     RE  Observations to follow
     HD  Hold order request
     DR  Discontinued as requested
     DE  Data Errors
     DC  Discontinue order request
     CR  Canceled as requested
     CN  Combined result
     CH  Child order
     CA  Cancel order request
     NW  New Order
     SS  Send order status request
     XR  Changed as requested
     XO  Change order request
     UX  Unable to change
     UR  Unable to release
     UM  Unable to replace
     UH  Unable to put on hold
     UD  Unable to discontinue
     UC  Unable to cancel
     RO  Replacement order
     SR  Response to send order status request
     SN  Send order number
     SC  Status changed
     RU  Replaced unsolicited
     RR  Request received
     RQ  Replaced as requested
     RP  Order replace request
     OE  Order released
     RF  Refill order request
     OF  Order refilled as requested
     FU  Order refilled, unsolicited
     UF  Unable to refill
     DF  Order refill request denied
     AF  Order refille request approval
     UA  Unable to accept order
     """


     HR = "HR"
     XX = "XX"
     PA = "PA"
     OR = "OR"
     OK = "OK"
     OH = "OH"
     OD = "OD"
     OC = "OC"
     RL = "RL"
     NA = "NA"
     RE = "RE"
     HD = "HD"
     DR = "DR"
     DE = "DE"
     DC = "DC"
     CR = "CR"
     CN = "CN"
     CH = "CH"
     CA = "CA"
     NW = "NW"
     SS = "SS"
     XR = "XR"
     XO = "XO"
     UX = "UX"
     UR = "UR"
     UM = "UM"
     UH = "UH"
     UD = "UD"
     UC = "UC"
     RO = "RO"
     SR = "SR"
     SN = "SN"
     SC = "SC"
     RU = "RU"
     RR = "RR"
     RQ = "RQ"
     RP = "RP"
     OE = "OE"
     RF = "RF"
     OF = "OF"
     FU = "FU"
     UF = "UF"
     DF = "DF"
     AF = "AF"
     UA = "UA"


class ResponseFlag(str, Enum):
     """
     121 - Response Flag

     R  Same as E, also Replacement and Parent-Child
     N  Only the MSA segment is returned
     F  Same as D, plus confirmations explicitly
     E  Report exceptions only
     D  Same as R, also other associated segments
     """


     R = "R"
     N = "N"
     F = "F"
     E = "E"
     D = "D"


class ChargeType(str, Enum):
     """
     122 - Charge Type

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


class ResultStatus(str, Enum):
     """
     123 - Result Status

     Z  No record of this patient. (Used only on queries)
     Y  No order on record for this test.  (Used only on queries)
     X  No results available; Order canceled.
     S  No results available; procedure scheduled, but not done
     R  Results stored; not yet verified
     P  Preliminary: A verified early result is available, final results not yet obtained
     O  Order received; specimen not yet received
     I  No results available; specimen received, procedure incomplete
     F  Final results; results stored and verified.  Can only be changed with a corrected result.
     C  Correction to results
     A  Some, but not all, results available
     """


     Z = "Z"
     Y = "Y"
     X = "X"
     S = "S"
     R = "R"
     P = "P"
     O = "O"
     I = "I"
     F = "F"
     C = "C"
     A = "A"


class TransportationMode(str, Enum):
     """
     124 - Transportation Mode

     WHLC  Wheelchair
     WALK  Patient walks to diagnostic service
     PORT  The examining device goes to patient's location
     CART  Cart - patient travels on cart or gurney
     """


     WHLC = "WHLC"
     WALK = "WALK"
     PORT = "PORT"
     CART = "CART"


class ValueType(str, Enum):
     """
     125 - Value Type

     PN  Person Name
     CE  Coded Entry
     CF  Coded Element With Formatted Values
     CK  Composite ID With Check Digit
     CN  Composite ID And Name
     CP  Composite Price
     CX  Extended Composite ID With Check Digit
     DT  Date
     ED  Encapsulated Data
     FT  Formatted Text (Display)
     ID  Coded Value
     AD  Address
     NM  Numeric
     XTN  Extended Telecommunications Number
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
     MO  Money
     """


     PN = "PN"
     CE = "CE"
     CF = "CF"
     CK = "CK"
     CN = "CN"
     CP = "CP"
     CX = "CX"
     DT = "DT"
     ED = "ED"
     FT = "FT"
     ID = "ID"
     AD = "AD"
     NM = "NM"
     XTN = "XTN"
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
     MO = "MO"


class QuantityLimitedRequest(str, Enum):
     """
     126 - Quantity Limited Request

     ZO  Locally defined
     RD  Records
     PG  Pages
     LI  Lines
     CH  Characters
     """


     ZO = "ZO"
     RD = "RD"
     PG = "PG"
     LI = "LI"
     CH = "CH"


class AllergyType(str, Enum):
     """
     127 - Allergy Type

     MC  Miscellaneous Contraindication
     MA  Miscellaneous Allergy
     FA  Food Allergy
     DA  Drug Allergy
     """


     MC = "MC"
     MA = "MA"
     FA = "FA"
     DA = "DA"


class AllergySeverity(str, Enum):
     """
     128 - Allergy Severity

     SV  Severe
     MO  Moderate
     MI  Mild
     """


     SV = "SV"
     MO = "MO"
     MI = "MI"


class ContactRole(str, Enum):
     """
     131 - Contact Role

     PR  Person preparing referral
     EP  Emergency contact person
     CP  Contact person
     BP  Billing contact person
     """


     PR = "PR"
     EP = "EP"
     CP = "CP"
     BP = "BP"


class ProcedurePractitionerIdentifierCodeType(str, Enum):
     """
     133 - Procedure Practitioner Identifier Code Type

     SN  Scrub Nurse
     RS  Resident
     RD  Radiologist
     PS  Primary Surgeon
     PR  Procedure MD (surgeon)
     NP  Nurse Practitioner
     CM  Certified Nurse Midwife
     AS  Assistant Surgeon
     AN  Anesthesiologist
     """


     SN = "SN"
     RS = "RS"
     RD = "RD"
     PS = "PS"
     PR = "PR"
     NP = "NP"
     CM = "CM"
     AS = "AS"
     AN = "AN"


class AssignmentofBenefits(str, Enum):
     """
     135 - Assignment of Benefits

     Y  Yes
     N  No
     M  Modified assignment
     """


     Y = "Y"
     N = "N"
     M = "M"


class Yes_NoIndicator(str, Enum):
     """
     136 - Yes-No Indicator

     Y  Yes
     N  No
     """


     Y = "Y"
     N = "N"


class MailClaimParty(str, Enum):
     """
     137 - Mail Claim Party

     P  Patient
     O  Other
     I  Insurance Company
     G  Guarantor
     E  Employer
     """


     P = "P"
     O = "O"
     I = "I"
     G = "G"
     E = "E"


class EligibilitySource(str, Enum):
     """
     144 - Eligibility Source

     7  None
     6  Verbal Information
     5  Signed statement on file
     4  Insured presented card
     3  Insured presented policy
     2  Employer
     1  Insurance company
     """


     _7 = "7"
     _6 = "6"
     _5 = "5"
     _4 = "4"
     _3 = "3"
     _2 = "2"
     _1 = "1"


class RoomType(str, Enum):
     """
     145 - Room Type

     SPR  Semi-private room
     PRI  Private room
     ICU  Intensive care unit
     2SPR  Second semi-private room
     2PRI  Second private room
     2ICU  Second intensive care unit
     """


     SPR = "SPR"
     PRI = "PRI"
     ICU = "ICU"
     _2SPR = "2SPR"
     _2PRI = "2PRI"
     _2ICU = "2ICU"


class AmountType(str, Enum):
     """
     146 - Amount Type

     UL  Unlimited
     RT  Rate
     PC  Percentage
     LM  Limit
     DF  Differential
     """


     UL = "UL"
     RT = "RT"
     PC = "PC"
     LM = "LM"
     DF = "DF"


class PolicyType(str, Enum):
     """
     147 - Policy Type

     MMD  Major medical
     ANC  Ancillary
     3MMD  Third major medical
     2MMD  Second major medical
     2ANC  Second ancillary
     """


     MMD = "MMD"
     ANC = "ANC"
     _3MMD = "3MMD"
     _2MMD = "2MMD"
     _2ANC = "2ANC"


class PenaltyType(str, Enum):
     """
     148 - Penalty Type

     PC  Percentage
     AT  Currency Amount
     """


     PC = "PC"
     AT = "AT"


class DayType(str, Enum):
     """
     149 - Day Type

     PE  Pending
     DE  Denied
     AP  Approved
     """


     PE = "PE"
     DE = "DE"
     AP = "AP"


class Pre_certificationPatientType(str, Enum):
     """
     150 - Pre-certification Patient Type

     UR  Urgent
     OPE  Outpatient elective
     IPE  Inpatient elective
     ER  Emergency
     """


     UR = "UR"
     OPE = "OPE"
     IPE = "IPE"
     ER = "ER"


class Accept_ApplicationAcknowledgementConditions(str, Enum):
     """
     155 - Accept-Application Acknowledgement Conditions

     SU  Successful completion only
     NE  Never
     ER  Error/reject conditions only
     AL  Always
     """


     SU = "SU"
     NE = "NE"
     ER = "ER"
     AL = "AL"


class WhichDate_TimeQualifier(str, Enum):
     """
     156 - Which Date-Time Qualifier

     SCHED  Schedule date/time
     REP  Report date/time, report date/time at filiing ancillary (i.e., Lab)
     RCT  Specimen receipt date/time, receipt of specimen in filling ancillary (Lab)
     ORD  Order date/time
     COL  Collection date/time, equivalent to film or sample collection date/time
     CAN  Cancellation date/time
     ANY  Any date/time within a range
     """


     SCHED = "SCHED"
     REP = "REP"
     RCT = "RCT"
     ORD = "ORD"
     COL = "COL"
     CAN = "CAN"
     ANY = "ANY"


class WhichDate_TimeStatusQualifier(str, Enum):
     """
     157 - Which Date-Time Status Qualifier

     REP  Report completion date/time
     PRE  Preliminary
     FIN  Final only (no corrections)
     COR  Corrected only (no final with corrections)
     CFN  Current final value, whether final or corrected
     ANY  Any status
     """


     REP = "REP"
     PRE = "PRE"
     FIN = "FIN"
     COR = "COR"
     CFN = "CFN"
     ANY = "ANY"


class Date_TimeSelectionQualifier(str, Enum):
     """
     158 - Date-Time Selection Qualifier

     REV  All values within the range returned in reverse chronological order (Default if not otherwise specified.)
     LST  Last value within the range
     ALL  All values within the range
     1ST  First value within range
     """


     REV = "REV"
     LST = "LST"
     ALL = "ALL"
     _1ST = "1ST"


class DietType(str, Enum):
     """
     159 - Diet Type

     S  Supplement
     P  Preference
     D  Diet
     """


     S = "S"
     P = "P"
     D = "D"


class TrayType(str, Enum):
     """
     160 - Tray Type

     NO  No tray
     MSG  Tray message only
     LATE  Late tray
     GUEST  Guest tray
     EARLY  Early tray
     """


     NO = "NO"
     MSG = "MSG"
     LATE = "LATE"
     GUEST = "GUEST"
     EARLY = "EARLY"


class AllowSubstitution(str, Enum):
     """
     161 - Allow Substitution

     T  Allow therapeutic substitutions
     N  Substitutions are NOT authorized.  (This is the default - null.)
     G  Allow generic substitutions
     """


     T = "T"
     N = "N"
     G = "G"


class RouteofAdministration(str, Enum):
     """
     162 - Route of Administration

     IB  Intrabursal
     NP  Nasal Prongs (Used primarily for respiratory therapy and anesthesia delivery)
     NG  Nasogastric
     MM  Mucous Membrane
     IMR  Immerse (Soak) Body Part
     IH  Inhalation
     ID  Intradermal
     AP  Apply Externally
     IC  Intracardiac
     OP  Ophthalmic
     IA  Intra-arterial
     GU  GU Irrigant
     GTT  Gastronomy Tube
     ET  Endotrachial Tube (Used primarily for respiratory therapy and anesthesia delivery)
     EP  Epidural
     DT  Dental
     B  Buccal
     ICV  Intracervical (uterus)
     SC  Subcutaneous
     VM  Ventimask
     VG  Vaginal
     UR  Urethral
     TRA  Tracheostomy (Used primarily for respiratory therapy and anesthesia delivery)
     TP  Topical
     TL  Translingual
     TD  Transdermal
     NS  Nasal
     SD  Soaked Dressing
     NT  Nasotrachial Tube
     RM  Rebreather Mask (Used primarily for respiratory therapy and anesthesia delivery)
     PR  Rectal
     PO  Oral
     PF  Perfusion
     OTH  Other/Miscellaneous
     OT  Otic
     WND  Wound
     SL  Sublingual
     """


     IB = "IB"
     NP = "NP"
     NG = "NG"
     MM = "MM"
     IMR = "IMR"
     IH = "IH"
     ID = "ID"
     AP = "AP"
     IC = "IC"
     OP = "OP"
     IA = "IA"
     GU = "GU"
     GTT = "GTT"
     ET = "ET"
     EP = "EP"
     DT = "DT"
     B = "B"
     ICV = "ICV"
     SC = "SC"
     VM = "VM"
     VG = "VG"
     UR = "UR"
     TRA = "TRA"
     TP = "TP"
     TL = "TL"
     TD = "TD"
     NS = "NS"
     SD = "SD"
     NT = "NT"
     RM = "RM"
     PR = "PR"
     PO = "PO"
     PF = "PF"
     OTH = "OTH"
     OT = "OT"
     WND = "WND"
     SL = "SL"


class AdministrativeSite(str, Enum):
     """
     163 - Administrative Site

     LLAQ  Left Lower Abd Quadrant
     BU  Buttock
     BE  Bilateral Ears
     LV  Left Vastus Lateralis
     LUFA  Left Upper Forearm
     LUAQ  Left Upper Abd Quadrant
     LUA  Left Upper Arm
     LT  Left Thigh
     LSC  Left Subclavian
     LPC  Left Posterior Chest
     LNB  Nebulized
     LN  Left Naris
     RVL  Right Vastus Lateralis
     LLFA  Left Lower Forearm
     OD  Right Eye
     LIJ  Left Internal Jugular
     LH  Left Hand
     LG  Left Gluteus Medius
     LF  Left Foot
     LEJ  Left External Jugular
     LE  Left Ear
     LD  Left Deltoid
     LACF  Left Antecubital Fossa
     LAC  Left Anterior Chest
     LA  Left Arm
     CT  Chest Tube
     LMFA  Left Mid Forearm
     RG  Right Gluteus Medius
     RVG  Right Ventragluteal
     RUFA  Right Upper Forearm
     RUAQ  Right Upper Abd Quadrant
     RUA  Right Upper Arm
     RT  Right Thigh
     RSC  Right Subclavian
     RPC  Right Posterior Chest
     RN  Right Naris
     RMFA  Right Mid Forearm
     RLFA  Right Lower Forearm
     RLAQ  Rt Lower Abd Quadrant
     BN  Bilateral Nares
     RH  Right Hand
     LVG  Left Ventragluteal
     RF  Right Foot
     REJ  Right External Jugular
     RE  Right Ear
     RD  Right Deltoid
     RACF  Right Antecubital Fossa
     RAC  Right Anterior Chest
     RA  Right Arm
     PERIN  Perineal
     PA  Perianal
     OU  Bilateral Eyes
     OS  Left Eye
     RIJ  Right Internal Jugular
     NB  Nebulized
     LVL  Left Vastus Lateralis
     """


     LLAQ = "LLAQ"
     BU = "BU"
     BE = "BE"
     LV = "LV"
     LUFA = "LUFA"
     LUAQ = "LUAQ"
     LUA = "LUA"
     LT = "LT"
     LSC = "LSC"
     LPC = "LPC"
     LNB = "LNB"
     LN = "LN"
     RVL = "RVL"
     LLFA = "LLFA"
     OD = "OD"
     LIJ = "LIJ"
     LH = "LH"
     LG = "LG"
     LF = "LF"
     LEJ = "LEJ"
     LE = "LE"
     LD = "LD"
     LACF = "LACF"
     LAC = "LAC"
     LA = "LA"
     CT = "CT"
     LMFA = "LMFA"
     RG = "RG"
     RVG = "RVG"
     RUFA = "RUFA"
     RUAQ = "RUAQ"
     RUA = "RUA"
     RT = "RT"
     RSC = "RSC"
     RPC = "RPC"
     RN = "RN"
     RMFA = "RMFA"
     RLFA = "RLFA"
     RLAQ = "RLAQ"
     BN = "BN"
     RH = "RH"
     LVG = "LVG"
     RF = "RF"
     REJ = "REJ"
     RE = "RE"
     RD = "RD"
     RACF = "RACF"
     RAC = "RAC"
     RA = "RA"
     PERIN = "PERIN"
     PA = "PA"
     OU = "OU"
     OS = "OS"
     RIJ = "RIJ"
     NB = "NB"
     LVL = "LVL"


class AdminstrationDevice(str, Enum):
     """
     164 - Adminstration Device

     PCA  PCA Pump
     NEB  Nebulizer
     MI  Metered Inhaler
     IVS  IV Soluset
     IVP  IV Pump
     IPPB  IPPB
     HL  Heparin Lock
     BT  Buretrol
     AP  Applicator
     """


     PCA = "PCA"
     NEB = "NEB"
     MI = "MI"
     IVS = "IVS"
     IVP = "IVP"
     IPPB = "IPPB"
     HL = "HL"
     BT = "BT"
     AP = "AP"


class AdministrationMethod(str, Enum):
     """
     165 - Administration Method

     WI  Wipe
     WA  Wash
     SO  Soak
     SH  Shampoo
     PT  Pain
     PF  Perfuse
     NB  Nebulized
     IVPB  IV Piggyback
     IVP  IV Push
     IS  Insert
     IR  Irrigate
     IF  Inflitrate
     DU  Dust
     DI  Dissolve
     CH  Chew
     """


     WI = "WI"
     WA = "WA"
     SO = "SO"
     SH = "SH"
     PT = "PT"
     PF = "PF"
     NB = "NB"
     IVPB = "IVPB"
     IVP = "IVP"
     IS = "IS"
     IR = "IR"
     IF = "IF"
     DU = "DU"
     DI = "DI"
     CH = "CH"


class RXComponentType(str, Enum):
     """
     166 - RX Component Type

     B  Base
     A  Additive
     """


     B = "B"
     A = "A"


class SubstitutionStatus(str, Enum):
     """
     167 - Substitution Status

     T  A therapeutic substitution was dispensed
     N  No substitute was dispensed.  This is equivalent to the default (null) value.
     G  A generic substitution was dispensed
     """


     T = "T"
     N = "N"
     G = "G"


class ProcessingPriority(str, Enum):
     """
     168 - Processing Priority

     T  Timing critical (do as near as possible to requested time)
     S  Stat (do immediately)
     R  Routine
     P  Preoperative (to be done prior to surgery)
     C  Measure continuously (e.g., arterial line blood pressure)
     B  Do at bedside or portable (may be used with other codes)
     A  As soon as possible (a priority lower than stat)
     """


     T = "T"
     S = "S"
     R = "R"
     P = "P"
     C = "C"
     B = "B"
     A = "A"


class ReportingPriority(str, Enum):
     """
     169 - Reporting Priority

     R  Rush reporting
     C  Call back results
     """


     R = "R"
     C = "C"


class DerivedSpecimen(str, Enum):
     """
     170 - Derived Specimen

     P  Parent Observation
     N  Not Applicable
     C  Child Observation
     """


     P = "P"
     N = "N"
     C = "C"


class CoordinationofBenefits(str, Enum):
     """
     173 - Coordination of Benefits

     IN  Independent
     CO  Coordination
     """


     IN = "IN"
     CO = "CO"


class NatureofTest_Observation(str, Enum):
     """
     174 - Nature of Test-Observation

     S  Superset--a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes)
     P  Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen
     F  Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatine clearance), usually done at different times and/or on different specimens
     C  Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar--arterial ratio, cardiac output)
     A  Atomic test/observation (test code or treatment code)
     """


     S = "S"
     P = "P"
     F = "F"
     C = "C"
     A = "A"


class MasterFileIdentifierCode(str, Enum):
     """
     175 - Master File Identifier Code

     STF  Staff Master File (see Chapter 8, Appendix)
     PRA  Practitioner master file (see Chapter 8, Appendix)
     OM6  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM5  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM4  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM3  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM2  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM1-OM6  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     OM1  Observation text master file segments (e.g., Lab) (see Chapter 87, Appendix B):
     LOC  Location master file (see Chapter 3, Appendix)
     CM2  Clinical study Data Schedule Master
     CM1  Clinical study phase master
     CM0  Clinical study master
     CDM  Charge description master file (see Chapter 6, Appendix)
     """


     STF = "STF"
     PRA = "PRA"
     OM6 = "OM6"
     OM5 = "OM5"
     OM4 = "OM4"
     OM3 = "OM3"
     OM2 = "OM2"
     OM1_OM6 = "OM1-OM6"
     OM1 = "OM1"
     LOC = "LOC"
     CM2 = "CM2"
     CM1 = "CM1"
     CM0 = "CM0"
     CDM = "CDM"


class Confidentialitycode(str, Enum):
     """
     177 - Confidentiality code

     VIP  Very important person or celebrity
     V  Very restricted
     UWM  Unwed mother
     U  Usual control
     R  Restricted
     PSY  Psychiatric patient
     HIV  HIV(+) patient
     ETH  Alcohol/drug treatment patient
     EMP  Employee
     AID  AIDS patient
     """


     VIP = "VIP"
     V = "V"
     UWM = "UWM"
     U = "U"
     R = "R"
     PSY = "PSY"
     HIV = "HIV"
     ETH = "ETH"
     EMP = "EMP"
     AID = "AID"


class FileLevelEventCode(str, Enum):
     """
     178 - File Level Event Code

     UPD  Change file records as defined in the record level event codes for each record that follows
     REP  Replace current version of this master file with the version contained in this message
     """


     UPD = "UPD"
     REP = "REP"


class ResponseLevel(str, Enum):
     """
     179 - Response Level

     SU  Success.  Only MFA segments denoting success must be returned via the application level acknowledgement for this message
     NE  Never.  no application level response needed
     ER  Error/Reject conditions only.  Only MFA segments denoting errors must be returned via the application level acknowledgement for this message
     AL  Always. All MFA segments (whether denoting errors or not) must be returned via the application level acknowledgement message
     """


     SU = "SU"
     NE = "NE"
     ER = "ER"
     AL = "AL"


class RecordLevelEventCode(str, Enum):
     """
     180 - Record Level Event Code

     MUP  Update record for master file
     MDL  Delete record from master file
     MDC  Deactivate: discontinue using record in master file, but do not delete from database
     MAD  Add record to master file
     MAC  Reactivate deactivated record
     """


     MUP = "MUP"
     MDL = "MDL"
     MDC = "MDC"
     MAD = "MAD"
     MAC = "MAC"


class MFNRecordLevelErrorReturn(str, Enum):
     """
     181 - MFN Record Level Error Return

     U  Unsuccessful posting of the record defined by the MFE segment
     S  Successful posting of the record defined by the MFE segment
     """


     U = "U"
     S = "S"


class Active_Inactive(str, Enum):
     """
     183 - Active-Inactive

     I  Inactive staff
     A  Active staff
     """


     I = "I"
     A = "A"


class PreferredMethodofContact(str, Enum):
     """
     185 - Preferred Method of Contact

     O  Office Phone Number
     H  Home Phone Number
     F  FAX Number
     E  E-Mail Address (Not In TN Format)
     C  Cellular Phone Number
     B  Beeper Number
     """


     O = "O"
     H = "H"
     F = "F"
     E = "E"
     C = "C"
     B = "B"


class ProviderBilling(str, Enum):
     """
     187 - Provider Billing

     P  Provider does own billing
     I  Institution bills for provider
     """


     P = "P"
     I = "I"


class AddressType(str, Enum):
     """
     190 - Address Type

     P  Permanent
     O  Office
     M  Mailing
     H  Home
     F  County of Origin
     C  Current or Temporary
     B  Business
     """


     P = "P"
     O = "O"
     M = "M"
     H = "H"
     F = "F"
     C = "C"
     B = "B"


class MaintypeofreferencedData(str, Enum):
     """
     191 - Main type of referenced Data

     TX  Machine Readable Text Document
     SI  Scanned Image
     SD  Scanned Document
     NS  Non-scanned Image
     IM  Image Data
     FT  Formatted Text
     AU  Audio Data
     AP  Other application data, typically uninterpreted binary data
     """


     TX = "TX"
     SI = "SI"
     SD = "SD"
     NS = "NS"
     IM = "IM"
     FT = "FT"
     AU = "AU"
     AP = "AP"


class AmountClass(str, Enum):
     """
     193 - Amount Class

     UL  Unlimited
     PC  Percentage
     LM  Limit
     AT  Amount
     """


     UL = "UL"
     PC = "PC"
     LM = "LM"
     AT = "AT"


class NameType(str, Enum):
     """
     200 - Name Type

     O  Other
     M  Maiden Name
     L  Legal Name
     D  Display Name
     C  Adopted Name
     A  Alias Name
     """


     O = "O"
     M = "M"
     L = "L"
     D = "D"
     C = "C"
     A = "A"


class TelecommunicationUseCode(str, Enum):
     """
     201 - Telecommunication Use Code

     WPN  Work Number
     VHN  Vacation Home Number
     PRN  Primary Residence Number
     ORN  Other Residence Number
     NET  Network (email) Address
     EMR  Emergency Number
     ASN  Answering Service Number
     """


     WPN = "WPN"
     VHN = "VHN"
     PRN = "PRN"
     ORN = "ORN"
     NET = "NET"
     EMR = "EMR"
     ASN = "ASN"


class TelecommunicationEquipmentType(str, Enum):
     """
     202 - Telecommunication Equipment Type

     X.400  X.400 email address:  use only if telecommunication use code is NET
     PH  Telephone
     MD  Modem
     Internet  Internet Address:  Use only if telecommunication use code is NET
     FX  Fax
     CP  Cellular Phone
     BP  Beeper/Pager
     """


     X_400 = "X.400"
     PH = "PH"
     MD = "MD"
     Internet = "Internet"
     FX = "FX"
     CP = "CP"
     BP = "BP"


class IdentifierType(str, Enum):
     """
     203 - Identifier Type

     MA  Medicaid Number
     AN  Account Number
     BR  Birth Registry Number
     DI  Diner's Club Card
     DL  Driver's License Number
     DN  Doctor Number
     DS  Discover Card
     EI  Employee Number
     EN  Employer Number
     AM  American Express
     GN  Guarantor External Identifier
     XX  Organizaiton Indentifier
     MC  Medicare Number
     MR  Medical Record Number
     MS  Master Card
     PI  Patient Internal Identifier
     PT  Patient External Identifier
     RR  Railroad Retirement Number
     SS  Social Security Number
     VN  Visit Number
     VS  VISA
     GI  Guarantor Internal Identifier
     """


     MA = "MA"
     AN = "AN"
     BR = "BR"
     DI = "DI"
     DL = "DL"
     DN = "DN"
     DS = "DS"
     EI = "EI"
     EN = "EN"
     AM = "AM"
     GN = "GN"
     XX = "XX"
     MC = "MC"
     MR = "MR"
     MS = "MS"
     PI = "PI"
     PT = "PT"
     RR = "RR"
     SS = "SS"
     VN = "VN"
     VS = "VS"
     GI = "GI"


class OrganizationalNameType(str, Enum):
     """
     204 - Organizational Name Type

     SL  Stock Exchange Listing Name
     L  Legal Name
     D  Display Name
     A  Alias Name
     """


     SL = "SL"
     L = "L"
     D = "D"
     A = "A"


class PriceType(str, Enum):
     """
     205 - Price Type

     UP  Unit Price, may be based on length of procedure or service
     TP  Total Price
     TF  Technology Fee for Use of Equipment
     PF  Professional Fee for Performing Provider
     IC  Indirect Unit Cost
     DC  Direct Unit Cost
     AP  Administrative Price or Handling Fee
     """


     UP = "UP"
     TP = "TP"
     TF = "TF"
     PF = "PF"
     IC = "IC"
     DC = "DC"
     AP = "AP"


class SegmentActionCode(str, Enum):
     """
     206 - Segment Action Code

     U  Update
     D  Delete
     A  Add/Insert
     """


     U = "U"
     D = "D"
     A = "A"


class ProcessingMode(str, Enum):
     """
     207 - Processing Mode

     R  Restore from Archive
     I  Initial Load
     A  Archive
     Not present  Not Present (the default, meaning current processing)
     """


     R = "R"
     I = "I"
     A = "A"
     Not_present = "Not present"


class QueryResponseStatus(str, Enum):
     """
     208 - Query Response Status

     OK  Data found, no errors (this is the default)
     NF  No data found, no errors
     """


     OK = "OK"
     NF = "NF"


class RelationalOperator(str, Enum):
     """
     209 - Relational Operator

     NE  Not equal
     LT  Less than
     LE  Less than or equal
     GT  Greater than
     GN  Generic
     GE  Greater than or equal
     EQ  Equal
     CT  Contains
     """


     NE = "NE"
     LT = "LT"
     LE = "LE"
     GT = "GT"
     GN = "GN"
     GE = "GE"
     EQ = "EQ"
     CT = "CT"


class RelationalConjunction(str, Enum):
     """
     210 - Relational Conjunction

     OR  
     AND  Default
     """


     OR = "OR"
     AND = "AND"


class AlternateCharacterSets(str, Enum):
     """
     211 - Alternate Character Sets

     UNICODE  
     JIS X 0202  ISO 2022 with escape sequences for Kanjii
     JAS2020  A subset of ISO2020 used for most Kanjii transmissions
     ASCII  The printable 7-bit ASCII character set . (This is the default if this field is omitted)
     8859/9  The printable characters from the ISO 8859/9 Character set
     8859/8  The printable characters from the ISO 8859/8 Character set
     8859/7  The printable characters from the ISO 8859/7 Character set
     8859/6  The printable characters from the ISO 8859/6 Character set
     8859/5  The printable characters from the ISO 8859/5 Character set
     8859/4  The printable characters from the ISO 8859/4 Character set
     8859/3  The printable characters from the ISO 8859/3 Character set
     8859/2  The printable characters from the ISO 8859/2 Character set
     8859/1  The printable characters from the ISO 8859/1 Character set
     """


     UNICODE = "UNICODE"
     JIS_X_0202 = "JIS X 0202"
     JAS2020 = "JAS2020"
     ASCII = "ASCII"
     _8859_9 = "8859/9"
     _8859_8 = "8859/8"
     _8859_7 = "8859/7"
     _8859_6 = "8859/6"
     _8859_5 = "8859/5"
     _8859_4 = "8859/4"
     _8859_3 = "8859/3"
     _8859_2 = "8859/2"
     _8859_1 = "8859/1"


class PurgeStatus(str, Enum):
     """
     213 - Purge Status

     P  Marked for purge.  User is no longer able to update the visit.
     I  The visit is marked inactive and the user cannot enter new data against it
     D  The visit is marked for deletion and the user cannot enter new data against it
     """


     P = "P"
     I = "I"
     D = "D"


class LivingArrangements(str, Enum):
     """
     220 - Living Arrangements

     U  Unknown
     S  Spouse
     R  Relative
     I  Institution
     F  Family
     A  Alone
     """


     U = "U"
     S = "S"
     R = "R"
     I = "I"
     F = "F"
     A = "A"


class LivingDependency(str, Enum):
     """
     223 - Living Dependency

     WU  Walk up
     S  Small children
     M  Medical supervision required
     D  Spouse dependent
     CB  Common bath
     """


     WU = "WU"
     S = "S"
     M = "M"
     D = "D"
     CB = "CB"


class TransportArranged(str, Enum):
     """
     224 - Transport Arranged

     U  Unknown
     N  Not Arranged
     A  Arranged
     """


     U = "U"
     N = "N"
     A = "A"


class EscortRequired(str, Enum):
     """
     225 - Escort Required

     U  Unknown
     R  Required
     N  Not Required
     """


     U = "U"
     R = "R"
     N = "N"


class ManufacturersofVaccines(str, Enum):
     """
     227 - Manufacturers of Vaccines

     MA  Massachusetts Public Health
     AD  Adams
     ALP  Alpha
     AR  Armour
     BA  Baxter
     BAY  Bayer
     BP  Berna
     CON  Connaught
     EVN  Evans
     GRE  Greer
     IM  Merieux
     IUS  Immuno-US
     JPN  Microbial Dis/Osaka U
     AB  Abbott
     LED  Lederle
     WA  Wyeth-Ayerst
     MIL  Miles
     MIP  Michigan Dept Public Health
     MSD  Merck
     NAB  North American Biologicals, Inc.
     NYB  New York Blood Center
     OTC  Organon Teknika
     OTH  Other
     PD  Parke Davis
     PRX  Praxis Biologics
     SCL  Sclavo
     SI  Swiss Serum and Vaccine Inst.
     SKB  SmithKline
     UNK  Unknown manufacturer
     KGC  Korea Green Cross
     """


     MA = "MA"
     AD = "AD"
     ALP = "ALP"
     AR = "AR"
     BA = "BA"
     BAY = "BAY"
     BP = "BP"
     CON = "CON"
     EVN = "EVN"
     GRE = "GRE"
     IM = "IM"
     IUS = "IUS"
     JPN = "JPN"
     AB = "AB"
     LED = "LED"
     WA = "WA"
     MIL = "MIL"
     MIP = "MIP"
     MSD = "MSD"
     NAB = "NAB"
     NYB = "NYB"
     OTC = "OTC"
     OTH = "OTH"
     PD = "PD"
     PRX = "PRX"
     SCL = "SCL"
     SI = "SI"
     SKB = "SKB"
     UNK = "UNK"
     KGC = "KGC"


class DiagnosisClassification(str, Enum):
     """
     228 - Diagnosis Classification

     T  Tissue diagnosis
     S  Sign and symptom
     R  Radiological scheduling (not using ICDA codes)
     O  Other
     M  Medication (antibiotic)
     I  Invasive procedure not classified elsewhere (I.V., catheter, etc.)
     D  Diagnosis
     C  Consultation
     """


     T = "T"
     S = "S"
     R = "R"
     O = "O"
     M = "M"
     I = "I"
     D = "D"
     C = "C"


class OutlierType(str, Enum):
     """
     229 - Outlier Type

     M  Medicare
     G  Managed Care Organization
     C  Champus
     """


     M = "M"
     G = "G"
     C = "C"


class ProcedureFunctionalType(str, Enum):
     """
     230 - Procedure Functional Type

     P  Procedure for treatment (therapeutic includes operations)
     I  Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)
     D  Diagnostic Procedure
     A  Anesthesia
     """


     P = "P"
     I = "I"
     D = "D"
     A = "A"


class StudentStatus(str, Enum):
     """
     231 - Student Status

     P  Part-time student
     N  Not a student
     F  Full-time student
     """


     P = "P"
     N = "N"
     F = "F"


class InsuranceCompanyContactReason(str, Enum):
     """
     232 - Insurance Company Contact Reason

     03  Name/address change
     02  Medicaid claim status
     01  Medicare claim status
     """


     _03 = "03"
     _02 = "02"
     _01 = "01"


class ReportTiming(str, Enum):
     """
     234 - Report Timing

     RQ  Requested information
     PD  Periodic
     DE  Device evaluation
     CO  Correction
     AD  Additional information
     7D  7 day report
     3D  3 day report
     30D  30 day report
     15D  15 day report
     10D  10 day report
     """


     RQ = "RQ"
     PD = "PD"
     DE = "DE"
     CO = "CO"
     AD = "AD"
     _7D = "7D"
     _3D = "3D"
     _30D = "30D"
     _15D = "15D"
     _10D = "10D"


class ReportSource(str, Enum):
     """
     235 - Report Source

     R  Regulatory agency
     P  Patient
     O  Other
     N  Non-healthcare professional
     M  Manufacturer/marketing authority holder
     L  Literature
     H  Health professional
     E  Distributor
     D  Database/registry/poison control center
     C  Clinical trial
     """


     R = "R"
     P = "P"
     O = "O"
     N = "N"
     M = "M"
     L = "L"
     H = "H"
     E = "E"
     D = "D"
     C = "C"


class ReportedTo(str, Enum):
     """
     236 - Reported To

     R  Regulatory agency
     M  Manufacturer
     L  Local facility/user facility
     D  Distributor
     """


     R = "R"
     M = "M"
     L = "L"
     D = "D"


class EventQualification(str, Enum):
     """
     237 - Event Qualification

     W  Drug withdrawal
     O  Overdose
     M  Misuse
     L  Lack of expect therapeutic effect
     I  Interaction
     D  Dependency
     B  Unexpected beneficial effect
     A  Abuse
     """


     W = "W"
     O = "O"
     M = "M"
     L = "L"
     I = "I"
     D = "D"
     B = "B"
     A = "A"


class EventSeriousness(str, Enum):
     """
     238 - Event Seriousness

     Y  Yes
     S  Significant
     N  No
     """


     Y = "Y"
     S = "S"
     N = "N"


class EventExpected(str, Enum):
     """
     239 - Event Expected

     Y  Yes
     U  Unknown
     N  No
     """


     Y = "Y"
     U = "U"
     N = "N"


class EventConsequence(str, Enum):
     """
     240 - Event Consequence

     R  Required intervention to prevent permanent impairment/damage
     P  Prolonged hospitalization
     O  Other
     L  Life threatening
     J  Disability which is significant, persistent or permanent
     I  Incapacity which is significant, persistent or permanent
     H  Caused hospitalized
     D  Death
     C  Congenital anomaly/birth defect
     """


     R = "R"
     P = "P"
     O = "O"
     L = "L"
     J = "J"
     I = "I"
     H = "H"
     D = "D"
     C = "C"


class PatientOutcome(str, Enum):
     """
     241 - Patient Outcome

     W  Worsening
     U  Unknown
     S  Sequelae
     R  Recovering
     N  Not recovering/unchanged
     F  Fully recovered
     D  Died
     """


     W = "W"
     U = "U"
     S = "S"
     R = "R"
     N = "N"
     F = "F"
     D = "D"


class PrimaryObserversQualification(str, Enum):
     """
     242 - Primary Observer s Qualification

     R  Pharmacist
     P  Physician (osteopath, homeopath)
     O  Other non-health professional
     M  Mid-level professional (nurse, nurse practitioner, physician's assistant)
     L  Lawyer/attorney
     H  Other health professional
     C  Health care consumer/patient
     """


     R = "R"
     P = "P"
     O = "O"
     M = "M"
     L = "L"
     H = "H"
     C = "C"


class IdentitymaybeDivulged(str, Enum):
     """
     243 - Identity may be Divulged

     Y  Yes
     NA  Not applicable
     N  No
     """


     Y = "Y"
     NA = "NA"
     N = "N"


class StartofEvaluation(str, Enum):
     """
     247 - Start of Evaluation

     Y  Evaluation completed
     X  Product not made by company
     U  Product unavailable for follow up investigation
     R  Product under recall/corrective action
     Q  Product under quarantine -- unable to follow up
     P  Evaluation in progress
     O  Other
     K  Problem already known, no evaluation necessary
     I  Product remains implanted -- unable to follow up
     D  Product discarded -- unable to follow up
     C  Product received in condition which made analysis impossible
     A  Evaluation anticipated, but not yet begun
     """


     Y = "Y"
     X = "X"
     U = "U"
     R = "R"
     Q = "Q"
     P = "P"
     O = "O"
     K = "K"
     I = "I"
     D = "D"
     C = "C"
     A = "A"


class ProductSource(str, Enum):
     """
     248 - Product Source

     R  A product from a reserve sample was evaluated
     N  A product from a controlled/non-related inventory was evaluated
     L  A product from the same lot as the actual product involved was evaluated
     A  Actual product involved in incident was evaluated
     """


     R = "R"
     N = "N"
     L = "L"
     A = "A"


class RelatednessAssessment(str, Enum):
     """
     250 - Relatedness Assessment

     S  Somewhat probable
     N  Not related
     M  Moderately probable
     I  Improbable
     H  Highly probable
     """


     S = "S"
     N = "N"
     M = "M"
     I = "I"
     H = "H"


class ActionTakeninResponsetotheEvent(str, Enum):
     """
     251 - Action Taken in Response to the Event

     WT  Product withdrawn temporarily
     WP  Product withdrawn permanently
     OT  Other
     N  None
     DR  Product dose or frequency of use reduced
     DI  Product dose or frequency of use increased
     """


     WT = "WT"
     WP = "WP"
     OT = "OT"
     N = "N"
     DR = "DR"
     DI = "DI"


class CausalityObservations(str, Enum):
     """
     252 - Causality Observations

     TC  Toxic levels of product documented in blood or body fluids
     SE  Similar events in past for this patient
     PL  Effect observed when patient receives placebo
     OT  Other
     OE  Occurrence of event was confirmed by objective evidence
     LI  Literature reports association of product with event
     IN  Event occurred after product introduced
     EX  Alternative explanations for the event available
     DR  Dose response observed
     BE  Event recurred after product reintroduced
     AW  Abatement of event after product withdrawn
     """


     TC = "TC"
     SE = "SE"
     PL = "PL"
     OT = "OT"
     OE = "OE"
     LI = "LI"
     IN = "IN"
     EX = "EX"
     DR = "DR"
     BE = "BE"
     AW = "AW"


class IndirectExposureMechanism(str, Enum):
     """
     253 - Indirect Exposure Mechanism

     X  Blood product
     P  Transplacental
     O  Other
     F  Father
     B  Breast milk
     """


     X = "X"
     P = "P"
     O = "O"
     F = "F"
     B = "B"


class KindofQuantity(str, Enum):
     """
     254 - Kind of Quantity

     CACT  Catalytic Activity
     CNC  Catalytic Concentration
     CCRTO  Catalytic Concentration Ratio
     CCNT  Catalytic Content
     CFR  Catalytic Fraction
     CRAT  Catalytic Rate
     CRTO  Catalytic Ratio
     ENT  Entitic
     ENTSUB  Entitic Substance of Amount
     ENTCAT  Entitic Catalytic Activity
     ENTNUM  Entitic Number
     ENTVOL  Entitic Volume
     MASS  Mass
     MCNC  Mass Concentration
     MCRTO  Mass Concentration Ratio
     MCNT  Mass Content
     MFR  Mass Fraction
     MINC  Mass Increment
     MRAT  Mass Rate
     MRTO  Mass Ratio
     NUM  Number
     NCNC  Number Concentration
     NCNT  Number Content
     NFR  Number Fraction
     NRTO  Number Ratio
     SUB  Substance Amount
     SCNC  Substance Concentration
     SCRTO  Substance Concentration Ratio
     SCNT  Substance Content
     SCNTR  Substance Content Rate
     SFR  Substance Fraction
     SCNCIN  Substance Concentration Increment
     SRAT  Substance Rate
     SRTO  Substance Ratio
     VOL  Volume
     VCNT  Volume Content
     VFR  Volume Fraction
     VRAT  Volume Rate
     VRTO  Volume Ratio
     ACNC  Concentration, Arbitrary Substance
     RLMCNC  Relative Mass Concentration
     RLSCNC  Relative Substance Concentration
     THRMCNC  Threshold Mass Concentration
     THRSCNC  Threshold Substance Concentration
     TIME  Time (e.g. seconds)
     TMDF  Time Difference
     TMSTP  Time Stamp -- Date and Time
     TRTO  Time Ratio
     RCRLTM  Reciprocal Relative Time
     RLTM  Relative Time
     ABS  Absorbance
     ACT  Activity
     APER  Appearance
     ARB  Arbitrary
     AREA  Area
     ASPECT  Aspect
     CLAS  Class
     CNST  Constant
     COEF  Coefficient
     COLOR  Color
     CONS  Consistency
     DEN  Density
     DEV  Device
     DIFF  Difference
     ELAS  Elasticity
     ELPOT  Electrical Potential (Voltage)
     ELRAT  Electrical current (amperage)
     ELRES  Electrical Resistance
     ENGR  Energy
     EQL  Equilibrium
     FORCE  Mechanical force
     FREQ  Frequency
     IMP  Impression/ interpretation of study
     KINV  Kinematic Viscosity
     LEN  Length
     LINC  Length Increment
     LIQ  Liquifaction
     MGFLUX  Magnetic flux
     MORPH  Morphology
     MOTIL  Motility
     OD  Optical density
     OSMOL  Osmolality
     PRID  Presence/Identity/Existence
     PRES  Pressure (Partial)
     PWR  Power (wattage)
     RANGE  Ranges
     RATIO  Ratios
     RDEN  Relative Density
     REL  Relative
     SATFR  Saturation Fraction
     SHAPE  Shape
     SMELL  Smell
     SUSC  Susceptibility
     TASTE  Taste
     TEMP  Temperature
     TEMPDF  Temperature Difference
     TEMPIN  Temperature Increment
     TITR  Dilution Factor (Titer)
     TYPE  Type
     VEL  Velocity
     VELRT  Velocity Ratio
     VISC  Viscosity
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


class DurationCategories(str, Enum):
     """
     255 - Duration Categories

     PT  To identify measures at a point in time.
     *  Life of the "unit."
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


class TimeDelayPostChallenge(str, Enum):
     """
     256 - Time Delay Post Challenge

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
     5H  5 hours post challenge
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


class NatureofChallenge(str, Enum):
     """
     257 - Nature of Challenge

     FFST  No fluid intake for the period specified in the time component of the term
     EXCZ  Exercise undertaken as challenge (can be quantified)
     CFST  Fasting (no calorie intake) for the period specified in the time component of the term, e.g., 1H POST CFST
     """


     FFST = "FFST"
     EXCZ = "EXCZ"
     CFST = "CFST"


class RelationshipModifier(str, Enum):
     """
     258 - Relationship Modifier

     PATIENT  Patient
     DONOR  Donor
     CONTROL  Control
     BPU  Blood product unit
     """


     PATIENT = "PATIENT"
     DONOR = "DONOR"
     CONTROL = "CONTROL"
     BPU = "BPU"


class Modality(str, Enum):
     """
     259 - Modality

     FS  Fundoscopy
     BS  Biomagnetic imaging
     CD  Color Flow Doppler
     CP  Colposcopy
     CR  Computed Radiography
     CS  Cystoscopy
     CT  Computed Tomography
     DD  Duplex Doppler
     DG  Diapanography
     DM  Digital microscopy
     EC  Echocardiography
     AS  Angioscopy
     FA  Fluorescein Angiography
     XA  X-Ray Angiography
     LP  Laparoscopy
     LS  Laser surface scan
     MA  Magnetic Resonance Angiography
     MS  Magnetic Resonance Spectroscopy
     NM  Nuclear medicine (radioisotope study)
     OT  Other
     PT  Positron Emission Tomography (PET)
     RF  RadioFluoroscopy
     ST  Single Photon Emission Computed Tomography (SPECT)
     TG  Thermography
     US  Ultrasound
     ES  Endoscopy
     """


     FS = "FS"
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
     AS = "AS"
     FA = "FA"
     XA = "XA"
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
     ES = "ES"


class PatientLocationType(str, Enum):
     """
     260 - Patient Location Type

     R  Room
     O  Operating Room
     N  Nursing Unit
     L  Other Location
     E  Exam Room
     D  Department
     C  Clinic
     B  Bed
     """


     R = "R"
     O = "O"
     N = "N"
     L = "L"
     E = "E"
     D = "D"
     C = "C"
     B = "B"


class LocationEquipment(str, Enum):
     """
     261 - Location Equipment

     VIT  Vital signs monitor
     VEN  Ventilator
     SUC  Suction
     OXY  Oxygen
     IVP  IV pump
     INF  Infusion pump
     EKG  Electro-Cardiogram
     EEG  Electro-Encephalogram
     """


     VIT = "VIT"
     VEN = "VEN"
     SUC = "SUC"
     OXY = "OXY"
     IVP = "IVP"
     INF = "INF"
     EKG = "EKG"
     EEG = "EEG"


class PrivacyLevel(str, Enum):
     """
     262 - Privacy Level

     W  Ward
     S  Semi-Private Room
     Q  Private Room - Due To Overflow
     P  Private Room
     J  Private Room - Medically Justified
     F  Isolation
     """


     W = "W"
     S = "S"
     Q = "Q"
     P = "P"
     J = "J"
     F = "F"


class LevelofCare(str, Enum):
     """
     263 - Level of Care

     S  Surgery
     R  Routine
     N  Intensive Care
     F  Isolation
     E  Emergency
     C  Critical Care
     A  Ambulatory
     """


     S = "S"
     R = "R"
     N = "N"
     F = "F"
     E = "E"
     C = "C"
     A = "A"


class SpecialtyType(str, Enum):
     """
     265 - Specialty Type

     OBG  Obstetrics, Gynecology
     AMB  Ambulatory
     CAN  Cancer
     CAR  Coronary/Cardiac Care
     CCR  Critical Care
     CHI  Chiropractic
     EDI  Education
     EMR  Emergency
     FPC  Family Planning
     INT  Intensive Care
     ISO  Isolation
     ALC  Allergy
     NBI  Newborn, Nursery, Infants
     WIC  Walk-In Clinic
     OBS  Observation
     OTH  Other Specialty
     PED  Pediatrics
     PHY  General/Family Practice
     PIN  Pediatric/Neonatal Intensive Care
     PPS  Pediatric Psychiatric
     PRE  Pediatric Rehabilitation
     PSI  Psychiatric Intensive Care
     PSY  Psychiatric
     REH  Rehabilitation
     SUR  Surgery
     NAT  Naturopathic
     """


     OBG = "OBG"
     AMB = "AMB"
     CAN = "CAN"
     CAR = "CAR"
     CCR = "CCR"
     CHI = "CHI"
     EDI = "EDI"
     EMR = "EMR"
     FPC = "FPC"
     INT = "INT"
     ISO = "ISO"
     ALC = "ALC"
     NBI = "NBI"
     WIC = "WIC"
     OBS = "OBS"
     OTH = "OTH"
     PED = "PED"
     PHY = "PHY"
     PIN = "PIN"
     PPS = "PPS"
     PRE = "PRE"
     PSI = "PSI"
     PSY = "PSY"
     REH = "REH"
     SUR = "SUR"
     NAT = "NAT"


class DaysoftheWeek(str, Enum):
     """
     267 - Days of the Week

     WED  Wednesday
     TUE  Tuesday
     THU  Thursday
     SUN  Sunday
     SAT  Saturday
     MON  Monday
     FRI  Friday
     """


     WED = "WED"
     TUE = "TUE"
     THU = "THU"
     SUN = "SUN"
     SAT = "SAT"
     MON = "MON"
     FRI = "FRI"


class Override(str, Enum):
     """
     268 - Override

     X  Override not allowed
     R  Override Required
     A  Override Allowed
     """


     X = "X"
     R = "R"
     A = "A"


class ChargeonIndicator(str, Enum):
     """
     269 - Charge on Indicator

     R  Charge on result
     O  Charge on order
     """


     R = "R"
     O = "O"


class ReportTypeCode(str, Enum):
     """
     270 - Report Type Code

     TS  Transfer summary
     SP  Surgical pathology
     PR  Progress note
     PN  Procedure note
     PH  Psychiatric history and physical examination
     PC  Psychiatric consultation
     OP  Operative report
     HP  History and physical examination
     DS  Discharge summary
     DI  Diagnostic imaging
     CN  Consult
     AR  Autopsy report
     ED  Emergency department report
     CD  Cardiodiagnostics
     """


     TS = "TS"
     SP = "SP"
     PR = "PR"
     PN = "PN"
     PH = "PH"
     PC = "PC"
     OP = "OP"
     HP = "HP"
     DS = "DS"
     DI = "DI"
     CN = "CN"
     AR = "AR"
     ED = "ED"
     CD = "CD"


class DocumentCompletionStatus(str, Enum):
     """
     271 - Document Completion Status

     LA  Legally authenticated
     IN  Incomplete
     DO  Documented
     DI  Dictated
     AU  Authenticated
     PA  Pre-authenticated
     IP  In progress
     """


     LA = "LA"
     IN = "IN"
     DO = "DO"
     DI = "DI"
     AU = "AU"
     PA = "PA"
     IP = "IP"


class DocumentConfidentialityStatus(str, Enum):
     """
     272 - Document Confidentiality Status

     3  ASTM Level 3
     2  ASTM Level 2
     1  ASTM Level 1
     VR  Very restricted
     UC  Usual control
     RE  Restricted
     """


     _3 = "3"
     _2 = "2"
     _1 = "1"
     VR = "VR"
     UC = "UC"
     RE = "RE"


class DocumentAvailabilityStatus(str, Enum):
     """
     273 - Document Availability Status

     UN  Unavailable for patient care
     AV  Available for patient care
     """


     UN = "UN"
     AV = "AV"


class DocumentStorageStatus(str, Enum):
     """
     275 - Document Storage Status

     PU  Purged
     AR  Archived (not active)
     AC  Active
     AA  Active and archived
     """


     PU = "PU"
     AR = "AR"
     AC = "AC"
     AA = "AA"


class AppointmentReasonCodes(str, Enum):
     """
     276 - Appointment Reason Codes

     WALKIN  A previously unscheduled walk-in visit
     ROUTINE  Routine appointment - default if not valued
     FOLLOWUP  A follow up visit from a previous appointment.
     EMERGENCY  Emergency appointment
     CHECKUP  A routine check-up, such as an annual physical.
     """


     WALKIN = "WALKIN"
     ROUTINE = "ROUTINE"
     FOLLOWUP = "FOLLOWUP"
     EMERGENCY = "EMERGENCY"
     CHECKUP = "CHECKUP"


class AppointmentTypeCodes(str, Enum):
     """
     277 - Appointment Type Codes

     TENTATIVE  A request for a tentative (e.g., penciled in) appointment
     NORMAL  Routine schedule request type - default if not valued
     COMPLETE  A request to add a completed appointment, used to maintain records of completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)
     """


     TENTATIVE = "TENTATIVE"
     NORMAL = "NORMAL"
     COMPLETE = "COMPLETE"


class FillerStatusCodes(str, Enum):
     """
     278 - Filler Status Codes

     WAITLIST  Appointment has been placed on a waiting list for a paricular slot, or set of slots
     STARTED  The indicated appointment has begun and is currently in progress
     PENDING  Appointment has not yet been confirmed
     OVERBOOK  The appointment has been confirmed; however it is confirmed in an overbooked state
     Discontinued  The indicated appointment was discontinued (DCed while in progress, discontinued parent appointment, or discontinued child appointment)
     DELETED  The indicated appointment was deleted from the filler application
     COMPLETE  The indicated appointment has completed normally (was not discontinued, canceled, or deleted)
     CANCELLED  The indicated appointment was stopped from occurring (cancelled prior to starting)
     BOOKED  The indicated appointment is booked
     BLOCKED  The indicated time slot(s) is(are) blocked.
     """


     WAITLIST = "WAITLIST"
     STARTED = "STARTED"
     PENDING = "PENDING"
     OVERBOOK = "OVERBOOK"
     Discontinued = "Discontinued"
     DELETED = "DELETED"
     COMPLETE = "COMPLETE"
     CANCELLED = "CANCELLED"
     BOOKED = "BOOKED"
     BLOCKED = "BLOCKED"


class AllowSubstitutionCodes(str, Enum):
     """
     279 - Allow Substitution Codes

     YES  Substitution of this resource is allowed
     NOTIFY  Notify the Placer Contact Person, through normal institutional procedures, that a substitution of this resource has been made
     NO  Substitution of this resource is not allowed
     CONFIRM  Contact the Placer Contact Person prior to making any substitutions of this resource
     """


     YES = "YES"
     NOTIFY = "NOTIFY"
     NO = "NO"
     CONFIRM = "CONFIRM"


class ReferralPriority(str, Enum):
     """
     280 - Referral Priority

     S  STAT
     R  Routine
     A  ASAP
     """


     S = "S"
     R = "R"
     A = "A"


class ReferralType(str, Enum):
     """
     281 - Referral Type

     SKN  Skilled Nursing
     RAD  Radiology
     PSY  Psychiatric
     MED  Medical
     LAB  Laboratory
     HOM  Home Care
     """


     SKN = "SKN"
     RAD = "RAD"
     PSY = "PSY"
     MED = "MED"
     LAB = "LAB"
     HOM = "HOM"


class ReferralDisposition(str, Enum):
     """
     282 - Referral Disposition

     WR  Send Written Report
     SO  Second Opinion
     RP  Return Patient After Evaluation
     AM  Assume Management
     """


     WR = "WR"
     SO = "SO"
     RP = "RP"
     AM = "AM"


class ReferralStatus(str, Enum):
     """
     283 - Referral Status

     R  Rejected
     P  Pending
     E  Expired
     A  Accepted
     """


     R = "R"
     P = "P"
     E = "E"
     A = "A"


class ReferralCategory(str, Enum):
     """
     284 - Referral Category

     O  Outpatient
     I  Inpatient
     E  Emergency
     A  Ambulatory
     """


     O = "O"
     I = "I"
     E = "E"
     A = "A"


class ProviderRole(str, Enum):
     """
     286 - Provider Role

     RT  Referred to Provider
     RP  Referring Provider
     PP  Primary Care Provider
     CP  Consulting Provider
     """


     RT = "RT"
     RP = "RP"
     PP = "PP"
     CP = "CP"


class ActionCode(str, Enum):
     """
     287 - Action Code

     UP  UPDATE
     UN  UNLINK
     UC  UNCHANGED
     LI  LINK
     DE  DELETE
     CO  CORRECT
     AD  ADD
     """


     UP = "UP"
     UN = "UN"
     UC = "UC"
     LI = "LI"
     DE = "DE"
     CO = "CO"
     AD = "AD"


class MIMEbase64encodingCharacters(str, Enum):
     """
     290 - MIME base64 encoding Characters

     3  D
     (pad)  =
     24  Y
     25  Z
     26  a
     27  b
     22  W
     29  d
     21  V
     30  e
     31  f
     32  g
     33  h
     34  I
     35  j
     28  c
     15  P
     0  A
     1  B
     10  K
     11  L
     12  M
     23  X
     14  O
     38  m
     16  Q
     17  R
     18  S
     19  T
     2  C
     20  U
     13  N
     6  G
     53  1
     54  2
     55  3
     56  4
     57  5
     36  k
     59  7
     50  y
     60  8
     61  9
     62  +
     63  /
     7  H
     8  I
     58  6
     45  t
     9  J
     39  n
     4  E
     40  o
     41  p
     42  q
     52  0
     44  s
     51  z
     46  u
     47  v
     48  w
     49  x
     5  F
     37  l
     43  r
     """


     _3 = "3"
     (pad) = "(pad)"
     _24 = "24"
     _25 = "25"
     _26 = "26"
     _27 = "27"
     _22 = "22"
     _29 = "29"
     _21 = "21"
     _30 = "30"
     _31 = "31"
     _32 = "32"
     _33 = "33"
     _34 = "34"
     _35 = "35"
     _28 = "28"
     _15 = "15"
     _0 = "0"
     _1 = "1"
     _10 = "10"
     _11 = "11"
     _12 = "12"
     _23 = "23"
     _14 = "14"
     _38 = "38"
     _16 = "16"
     _17 = "17"
     _18 = "18"
     _19 = "19"
     _2 = "2"
     _20 = "20"
     _13 = "13"
     _6 = "6"
     _53 = "53"
     _54 = "54"
     _55 = "55"
     _56 = "56"
     _57 = "57"
     _36 = "36"
     _59 = "59"
     _50 = "50"
     _60 = "60"
     _61 = "61"
     _62 = "62"
     _63 = "63"
     _7 = "7"
     _8 = "8"
     _58 = "58"
     _45 = "45"
     _9 = "9"
     _39 = "39"
     _4 = "4"
     _40 = "40"
     _41 = "41"
     _42 = "42"
     _52 = "52"
     _44 = "44"
     _51 = "51"
     _46 = "46"
     _47 = "47"
     _48 = "48"
     _49 = "49"
     _5 = "5"
     _37 = "37"
     _43 = "43"


class SubtypeofReferencedData(str, Enum):
     """
     291 - Subtype of Referenced Data

     TIFF  TIFF image data
     PostScript  PostScript program
     PICT  PICT format image data
     JPEG  Needs formal description
     JOT  Electronic ink data (Jot 1.0 standard)
     GIF  Needs formal description
     FAX  Facsimile data
     DICOM  Digital Imaging and Communications in Medicine
     BASIC  ISDN PCM audio data
     RTF  Rich Text Format
     Octet-stream  Uninterpreted binary data
     HTML  Hypertext Markup Language
     """


     TIFF = "TIFF"
     PostScript = "PostScript"
     PICT = "PICT"
     JPEG = "JPEG"
     JOT = "JOT"
     GIF = "GIF"
     FAX = "FAX"
     DICOM = "DICOM"
     BASIC = "BASIC"
     RTF = "RTF"
     Octet_stream = "Octet-stream"
     HTML = "HTML"


class VaccinesAdministered(str, Enum):
     """
     292 - Vaccines Administered

     13  TIG
     01  DTP
     24  Anthrax
     23  Plague
     22  DTP-Hib
     21  Varicella
     20  DTaP
     19  BCG
     18  Rabiesintramuscular injection
     17  Hib-unspecified
     16  Influenzawhole
     26  Cholera
     14  IG
     27  Botulinum antitoxin
     12  Diphtheria antitoxin
     11  Pertussis
     10  IPV
     09  Td (Adult)
     08  Hep B - adolescent or pediatric
     07  Mumps
     06  Rubella
     05  Measles
     04  M/R
     03  MMR
     02  OPV
     15  Influenzasplit (incl. purified surface antigen)
     39  Japanese encephalitis
     51  Hib-Hep B
     50  Dtap-Hib
     49  Hib-PRP-OMP
     48  Hib-PRP-T
     47  Hib-HbOC
     46  Hib-PRP-D
     45  Hep B-other or unspecified
     44  Hep B-dialysis
     43  Hep B-adult
     42  Hep B- adolescent/high risk infant
     25  Typhoidoral
     40  Rabiesintradermal injection
     52  Hep A - adult
     38  Rubella/Mumps
     37  Yellow fever
     36  VZIG
     35  Tetanus toxoid
     34  RIG
     33  Pneumococcal
     32  Meningococcal
     31  Hep A - pediatric
     30  HBIG
     29  CMVIG
     28  DT(pediatric)
     41  Typhoidparenteral
     """


     _13 = "13"
     _01 = "01"
     _24 = "24"
     _23 = "23"
     _22 = "22"
     _21 = "21"
     _20 = "20"
     _19 = "19"
     _18 = "18"
     _17 = "17"
     _16 = "16"
     _26 = "26"
     _14 = "14"
     _27 = "27"
     _12 = "12"
     _11 = "11"
     _10 = "10"
     _09 = "09"
     _08 = "08"
     _07 = "07"
     _06 = "06"
     _05 = "05"
     _04 = "04"
     _03 = "03"
     _02 = "02"
     _15 = "15"
     _39 = "39"
     _51 = "51"
     _50 = "50"
     _49 = "49"
     _48 = "48"
     _47 = "47"
     _46 = "46"
     _45 = "45"
     _44 = "44"
     _43 = "43"
     _42 = "42"
     _25 = "25"
     _40 = "40"
     _52 = "52"
     _38 = "38"
     _37 = "37"
     _36 = "36"
     _35 = "35"
     _34 = "34"
     _33 = "33"
     _32 = "32"
     _31 = "31"
     _30 = "30"
     _29 = "29"
     _28 = "28"
     _41 = "41"


class TimeSelectionCriteriaParameterClassCodes(str, Enum):
     """
     294 - Time Selection Criteria Parameter Class Codes

     WED  An indicator that Wednesday is or is not preferred for the day on which the appointment will occur. OK = Preferred appointment dayNO = Day is not preferred
     TUE  An indicator that Tuesday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     THU  An indicator that Thursday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     SUN  An indicator that Sunday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     SAT  An indicator that Saturday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     PREFSTART  The preferred start time for the appointment request, service or resource.   Any legal time specification in the format HHMM, using 24-hour clock notation
     PREFEND  The preferred start time for the appointment request, service or resource.  Any legal time specification in the format HHMM, using 24-hour clock notation
     MON  An indicator that Monday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     FRI  An indicator that Friday is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment dayNO = Day is not preferred
     """


     WED = "WED"
     TUE = "TUE"
     THU = "THU"
     SUN = "SUN"
     SAT = "SAT"
     PREFSTART = "PREFSTART"
     PREFEND = "PREFEND"
     MON = "MON"
     FRI = "FRI"


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

     A  no encoding - data are displayable ASCII characters.
     Hex  hexadecimal encoding - consecutive pairs of hexadecimal digits represent consecutive single octets.
     Base64  encoding as defined by MIME (Multipurpose Internet Mail Extensions) standard RFC 1521.  Four consecutive ASCII characters represent three consecutive octets of binary data.
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
     Random  Usually a base64 encoded string of random bits.
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


class CoverageType(str, Enum):
     """
     309 - Coverage Type

     P  Physician/professional
     H  Hospital/institutional
     B  Both hospital and physician
     """


     P = "P"
     H = "H"
     B = "B"


class LivingWill(str, Enum):
     """
     315 - Living Will

     Y  Yes, patient has a living will
     U  Unknown
     N  No, patient does not have a living will and no information was provided
     I  No, patient does not have a living will but information was provided
     F  Yes, patient has a living will but it is not on file
     """


     Y = "Y"
     U = "U"
     N = "N"
     I = "I"
     F = "F"


class OrganDonor(str, Enum):
     """
     316 - Organ Donor

     Y  Yes, patient is a donor and card is on file
     F  Yes, patient is a donor, but card is not on file
     N  No, patient is not a donor
     U  Unknown
     """


     Y = "Y"
     F = "F"
     N = "N"
     U = "U"


class Annotations(str, Enum):
     """
     317 - Annotations

     9904  etc.
     9903  Beat marker
     9902  Sense marker
     9901  SAS marker
     9900  Pace spike
     """


     _9904 = "9904"
     _9903 = "9903"
     _9902 = "9902"
     _9901 = "9901"
     _9900 = "9900"


class DispenseMethod(str, Enum):
     """
     321 - Dispense Method

     UD  Unit Dose
     TR  Traditional
     F  Floor Stock
     AD  Automatic Dispensing
     """


     UD = "UD"
     TR = "TR"
     F = "F"
     AD = "AD"


class CompletionStatus(str, Enum):
     """
     322 - Completion Status

     RE  Refused
     PA  Partially Administered
     NA  Not Administered
     CP  Complete
     """


     RE = "RE"
     PA = "PA"
     NA = "NA"
     CP = "CP"


class Actioncode(str, Enum):
     """
     323 - Action Code

     U  Update
     D  Delete
     A  Add/Insert
     """


     U = "U"
     D = "D"
     A = "A"


class LocationCharacteristicID(str, Enum):
     """
     324 - Location Characteristic ID

     TEA  Teaching location
     STF  Bed is staffed
     SMK  Smoking
     SHA  Shadow: a temporary holding location that does not physically exist
     SET  Bed is set up
     PRL  Private Level: indicating a level of private versus non-private room
     OVR  Overflow
     LIC  Licensed
     LCR  Level of care
     INF  Infectious disease: this location can be used for isolation
     IMP  Implant: can be used for radiation implant patients
     GEN  Gender of patient(s)
     """


     TEA = "TEA"
     STF = "STF"
     SMK = "SMK"
     SHA = "SHA"
     SET = "SET"
     PRL = "PRL"
     OVR = "OVR"
     LIC = "LIC"
     LCR = "LCR"
     INF = "INF"
     IMP = "IMP"
     GEN = "GEN"


class LocationRelationshipID(str, Enum):
     """
     325 - Location Relationship ID

     RX2  Second Pharmacy
     RX  Nearest Pharmacy
     PAR  Parent location
     LB2  Second Lab
     LAB  Nearest Lab
     DTY  Nearest Dietary
     ALI  Location alias(es)
     """


     RX2 = "RX2"
     RX = "RX"
     PAR = "PAR"
     LB2 = "LB2"
     LAB = "LAB"
     DTY = "DTY"
     ALI = "ALI"


class VisitIndicator(str, Enum):
     """
     326 - Visit Indicator

     A  Account level (default)
     V  Visit Level
     """


     A = "A"
     V = "V"


class QuantityMethod(str, Enum):
     """
     329 - Quantity Method

     E  Estimated (see comment)
     A  Acutal Count
     """


     E = "E"
     A = "A"


class MarketingBasis(str, Enum):
     """
     330 - Marketing Basis

     TXN  Transitional
     PRE  Preamendment
     PMA  Premarketing authorization
     522S  Post marketing study (522)
     510K  510 (K)
     510E  510 (K) exempt
     """


     TXN = "TXN"
     PRE = "PRE"
     PMA = "PMA"
     _522S = "522S"
     _510K = "510K"
     _510E = "510E"


class FacilityType(str, Enum):
     """
     331 - Facility Type

     U  User
     M  Manufacturer
     D  Distributor
     A  Agent for a foreign manufacturer
     """


     U = "U"
     M = "M"
     D = "D"
     A = "A"


class NetworkSourceType(str, Enum):
     """
     332 - Network Source Type

     I  Initiate
     A  Accept
     """


     I = "I"
     A = "A"


class DisabledPerson(str, Enum):
     """
     334 - Disabled Person

     PT  Patient
     GT  Guarantor
     AP  Associated Party
     IN  Insured
     """


     PT = "PT"
     GT = "GT"
     AP = "AP"
     IN = "IN"


class ReferralReason(str, Enum):
     """
     336 - Referral Reason

     W  Work Load
     S  Second Opinion
     P  Patient Preference
     O  Provider Ordered
     """


     W = "W"
     S = "S"
     P = "P"
     O = "O"


class CertificationStatus(str, Enum):
     """
     337 - Certification Status

     E  Eligible
     C  Certified
     """


     E = "E"
     C = "C"


class PractitionerIDnumbertype(str, Enum):
     """
     338 - Practitioner ID number type

     UPIN  Unique Physician ID. No.
     SL  State License Number
     MCD  Medicaid Number
     GL  General Ledger Number
     CY  County Number
     TAX  Tax ID Number
     DEA  Drug Enforcement Agency No.
     MCR  Medicare Number
     L&I  Labor and Industries Number
     QA  QA Number
     TRL  Training License Number
     """


     UPIN = "UPIN"
     SL = "SL"
     MCD = "MCD"
     GL = "GL"
     CY = "CY"
     TAX = "TAX"
     DEA = "DEA"
     MCR = "MCR"
     L_I = "L&I"
     QA = "QA"
     TRL = "TRL"
