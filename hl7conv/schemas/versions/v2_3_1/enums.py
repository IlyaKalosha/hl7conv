from enum import Enum


class Sex(str, Enum):
    """
    0001 - Sex

    F  Female
    M  Male
    O  Other
    U  Unknown
    """

    F = "F"
    M = "M"
    O = "O"
    U = "U"


class Maritalstatus(str, Enum):
    """
    0002 - Marital status

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


class Eventtype(str, Enum):
    """
    0003 - Event type

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
    A18  ADT/ACK -  Merge patient information
    A19  QRY/ADR -  Patient query
    A20  ADT/ACK -  Bed status update
    A21  ADT/ACK -  Patient goes on a leave of absence
    A22  ADT/ACK -  Patient returns from a leave of absence
    A23  ADT/ACK -  Delete a patient record
    A24  ADT/ACK -  Link patient information
    A25  ADT/ACK -  Cancel pending discharge
    A26  ADT/ACK -  Cancel pending transfer
    A27  ADT/ACK -  Cancel pending admit
    A28  ADT/ACK -  Add person information
    A29  ADT/ACK -  Delete person information
    A30  ADT/ACK -  Merge person information
    A31  ADT/ACK -  Update person information
    A32  ADT/ACK -  Cancel patient arriving - tracking
    A33  ADT/ACK -  Cancel patient departing - tracking
    A34  ADT/ACK -  Merge patient information - patient ID only
    A35  ADT/ACK -  Merge patient information - account number only
    A36  ADT/ACK -  Merge patient information - patient ID and account number
    A37  ADT/ACK -  Unlink patient information
    A38  ADT/ACK - Cancel pre-admit
    A39  ADT/ACK - Merge person  patient ID
    A40  ADT/ACK - Merge patient - patient identifier list
    A41  ADT/ACK - Merge account - patient account number
    A42  ADT/ACK - Merge visit - visit number
    A43  ADT/ACK - Move patient information  patient identifier list
    A44  ADT/ACK - Move account information - patient account number
    A45  ADT/ACK - Move visit information - visit number
    A46  ADT/ACK - Change patient ID
    A47  ADT/ACK - Change patient identifier list
    A48  ADT/ACK - Change alternate patient ID
    A49  ADT/ACK - Change patient account number
    A50  ADT/ACK - Change visit number
    A51  ADT/ACK - Change alternate visit ID
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
    CNQ  QRY/EQQ/SPQ/VQQ/RQQ - Cancel query
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
    M01  MFN/MFK - Master file not otherwise specified (for backward compatibility only)
    M02  MFN/MFK - Master file - staff practitioner
    M03  MFN/MFK - Master file - test/observation (for backward compatibility only)
    varies  MFQ/MFR - Master files query (use event same as asking for e.g., M05 - location)
    M04  MFN/MFK - Master files charge description
    M05  MFN/MFK - Patient location master file
    M06  MFN/MFK - Clinical study with phases and schedules master file
    M07  MFN/MFK - Clinical study without phases but with schedules master file
    M08  MFN/MFK - Test/observation (numeric) master file
    M09  MFN/MFK - Test/observation (categorical) master file
    M10  MFN/MFK - Test /observation batteries master file
    M11  MFN/MFK - Test/calculated observations master file
    O01  ORM - Order message (also RDE, RDS, RGV, RAS)
    O02  ORR - Order response (also RRE, RRD, RRG, RRA)
    P01  BAR/ACK - Add patient accounts
    P02  BAR/ACK - Purge patient accounts
    P03  DFT/ACK - Post detail financial transaction
    P04  QRY/DSP  Generate bill and A/R statements
    P05  BAR/ACK  Update account
    P06  BAR/ACK - End account
    P07  PEX - Unsolicited initial individual product experience report
    P08  PEX - Unsolicited update individual product experience report
    P09  SUR - Summary product experience report
    PC1  PPR - PC/ Problem Add
    PC2  PPR - PC/ Problem Update
    PC3  PPR - PC/ Problem Delete
    PC4  QRY - PC/ Problem Query
    PC5  PRR - PC/ Problem Response
    PC6  PGL - PC/ Goal Add
    PC7  PGL - PC/ Goal Update
    PC8  PGL - PC/ Goal Delete
    PC9  QRY - PC/ Goal Query
    PCA  PPV - PC/ Goal Response
    PCB  PPP - PC/ Pathway (Problem-Oriented) Add
    PCC  PPP - PC/ Pathway (Problem-Oriented) Update
    PCD  PPP - PC/ Pathway (Problem-Oriented) Delete
    PCE  QRY - PC/ Pathway (Problem-Oriented) Query
    PCF  PTR - PC/ Pathway (Problem-Oriented) Query Response
    PCG  PPG - PC/ Pathway (Goal-Oriented) Add
    PCH  PPG - PC/ Pathway (Goal-Oriented) Update
    PCJ  PPG - PC/ Pathway (Goal-Oriented) Delete
    PCK  QRY - PC/ Pathway (Goal-Oriented) Query
    PCL  PPT - PC/ Pathway (Goal-Oriented) Query Response
    Q01  QRY/DSR - Query sent for immediate response
    Q02  QRY/QCK - Query sent for deferred response
    Q03  DSR/ACK - Deferred response to a query
    Q04  EQQ  Embedded query language query
    Q05  UDM/ACK - Unsolicited display update message
    Q06  OSQ/OSR - Query for order status
    Q07  VQQ  Virtual table query
    Q08  SPQ  Stored procedure request
    Q09  RQQ  event replay query
    R01  ORU/ACK - Unsolicited transmission of an observation message
    R02  QRY - Query for results of observation
    R03  QRY/DSR Display-oriented results, query/unsol. update (for backward compatibility only)
    R04  ORF - Response to query; transmission of requested observation
    R05  QRY/DSR - query for display results
    R06  UDM - unsolicited update/display results
    R07  EDR  enhanced display response
    R08  TBR  tabular data response
    R09  ERP  event replay response
    RAR  RAR - Pharmacy administration information query response
    RDR  RDR - Pharmacy dispense information query response
    RER  RER - Pharmacy encoded order information query response
    RGR  RGR - Pharmacy dose information query response
    ROR  R0R - Pharmacy prescription order query response
    R0R  R0R - Pharmacy prescription order query response
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
    S24  SIU/ACK - Notification of opened (unblocked) schedule time slot(s)
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
    V01  VXQ - Query for vaccination record
    V02  VXX - Response to vaccination query returning multiple PID matches
    V03  VXR - Vaccination record response
    V04  VXU - Unsolicited vaccination record update
    W01  ORU - Waveform result, unsolicited transmission of requested information
    W02  QRF - Waveform result, response to query
    """

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
    CNQ = "CNQ"
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
    M01 = "M01"
    M02 = "M02"
    M03 = "M03"
    varies = "varies"
    M04 = "M04"
    M05 = "M05"
    M06 = "M06"
    M07 = "M07"
    M08 = "M08"
    M09 = "M09"
    M10 = "M10"
    M11 = "M11"
    O01 = "O01"
    O02 = "O02"
    P01 = "P01"
    P02 = "P02"
    P03 = "P03"
    P04 = "P04"
    P05 = "P05"
    P06 = "P06"
    P07 = "P07"
    P08 = "P08"
    P09 = "P09"
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
    R01 = "R01"
    R02 = "R02"
    R03 = "R03"
    R04 = "R04"
    R05 = "R05"
    R06 = "R06"
    R07 = "R07"
    R08 = "R08"
    R09 = "R09"
    RAR = "RAR"
    RDR = "RDR"
    RER = "RER"
    RGR = "RGR"
    ROR = "ROR"
    R0R = "R0R"
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
    V01 = "V01"
    V02 = "V02"
    V03 = "V03"
    V04 = "V04"
    W01 = "W01"
    W02 = "W02"


class Patientclass(str, Enum):
    """
    0004 - Patient class

    E  Emergency
    I  Inpatient
    O  Outpatient
    P  Preadmit
    R  Recurring patient
    B  Obstetrics
    """

    E = "E"
    I = "I"
    O = "O"
    P = "P"
    R = "R"
    B = "B"


class Admissiontype(str, Enum):
    """
    0007 - Admission type

    A  Accident
    E  Emergency
    L  Labor and Delivery
    R  Routine
    """

    A = "A"
    E = "E"
    L = "L"
    R = "R"


class Acknowledgmentcode(str, Enum):
    """
    0008 - Acknowledgment code

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
    0009 - Ambulatory status

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


class TransactionType(str, Enum):
    """
    0017 - Transaction Type

    CG  Charge
    CD  Credit
    PY  Payment
    AJ  Adjustment
    """

    CG = "CG"
    CD = "CD"
    PY = "PY"
    AJ = "AJ"


class Admitsource(str, Enum):
    """
    0023 - Admit source

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
    0027 - Priority

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
    0038 - Order status

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
    0043 - Condition code

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
    16  Payer codes.
    12  Payer codes.
    12 ... 16  Payer codes.
    13  Payer codes.
    15  Payer codes.
    14  Payer codes.
    18  Maiden name retained
    19  Child retains mothers name
    20  Beneficiary requested billing
    21  Billing for Denial Notice
    26  VA eligible patient chooses to receive services in a medicare certified facility
    27  Patient referred to a sole community hospital for a diagnostic laboratory test
    28  Patient and/or spouses EGHP is secondary to Medicare
    29  Disabled beneficiary and/or family members LGHP is secondary to Medicare
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
    77  Provider accepts or is obligated/required due to a contractual arrangement or
    law to accept payment by a primary payer as payment in full
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
    _16 = "16"
    _12 = "12"
    _12_____16 = "12 ... 16"
    _13 = "13"
    _15 = "15"
    _14 = "14"
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
    0048 - What subject filter

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


class DiagnosisType(str, Enum):
    """
    0052 - Diagnosis Type

    A  Admitting
    W  Working
    F  Final
    """

    A = "A"
    W = "W"
    F = "F"


class Checkdigitscheme(str, Enum):
    """
    0061 - Check digit scheme

    M10  Mod 10 algorithm
    M11  Mod 11 algorithm
    ISO  ISO 7064: 1983
    NPI  Check digit algorithm in the US National Provider Identifier
    """

    M10 = "M10"
    M11 = "M11"
    ISO = "ISO"
    NPI = "NPI"


class Eventreason(str, Enum):
    """
    0062 - Event reason

    01  Patient request
    02  Physician order
    03  Census management
    """

    _01 = "01"
    _02 = "02"
    _03 = "03"


class Specimenactioncode(str, Enum):
    """
    0065 - Specimen action code

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


class Specimensourcecodes(str, Enum):
    """
    0070 - Specimen source codes

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
    PPP  Patelet poor plasma
    PRP  Platelet rich plasma
    PUS  Pus
    RT  Route of medicine
    SAL  Saliva
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
    0074 - Diagnostic service section ID

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
    PT  Physical Therapy
    PHY  Physician (Hx. Dx, admission note, etc.l)
    PF  Pulmonary Function
    RAD  Radiology
    RX  Radiograph
    RUS  Radiology Ultrasound
    RC  Respiratory Care (therapy)
    RT  Radiation Therapy
    SR  Serology
    SP  Surgical Pathology
    TX  Toxicology
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
    VUS = "VUS"
    VR = "VR"
    XRC = "XRC"


class Messagetype(str, Enum):
    """
    0076 - Message type

    ACK  General acknowledgment message
    ADR  ADT response
    ARD  Ancillary RPT (display) (for backward compatibility only)
    ADT  ADT message
    BAR  Add/change billing account
    CRM  Clinical study registration
    CSU  Unsolicited clinical study data
    DFT  Detail financial transaction
    DOC  Document query
    DSR  Display response
    EDR  Enhanced display response
    EQQ  Embedded query language query
    ERP  Event replay response
    MCF  Delayed acknowledgment
    MDM  Documentation message
    MFN  Master files notification
    MFK  Master files application acknowledgment
    MFD  Master files delayed application acknowledgment
    MFQ  Master files query
    MFR  Master files query response
    NMD  Network management data
    NMQ  Network management query
    NMR  Network management response
    ORF  Observ. result/record response
    ORM  Order message
    ORR  Order acknowledgment message
    ORU  Observ result/unsolicited
    OSQ  Order status query
    OSR  Order status response
    PEX  Product experience
    PGL  Patient goal
    PIN  Patient insurance information
    PPG  Patient pathway (goal-oriented) message
    PPP  Patient pathway (problem-oriented) message
    PPR  Patient problem
    PPT  Patient pathway (goal oriented) response
    PPV  Patient goal response
    PRR  Patient problem response
    PTR  Patient pathway (problem-oriented) response
    QCK  Query general acknowledgment
    QRY  Query, original mode
    RAR  Pharmacy administration information
    RAS  Pharmacy administration message
    RCI  Return clinical information
    RCL  Return clinical list
    RDE  Pharmacy encoded order message
    RDR  Pharmacy dispense information
    RDS  Pharmacy dispense message
    REF  Patient referral
    RER  Pharmacy encoded order information
    RGV  Pharmacy give message
    RGR  Pharmacy dose information
    ROR  Pharmacy prescription order response
    RPA  Return patient authorization
    RPI  Return patient information
    RPL  Return patient display list
    RPR  Return patient list
    RQA  Request patient authorization
    RQC  Request clinical information
    RQI  Request patient information
    RQP  Request patient demographics
    RQQ  Event replay query
    RRA  Pharmacy administration acknowledgment
    RRD  Pharmacy dispense acknowledgment
    RRE  Pharmacy encoded order acknowledgment
    RRG  Pharmacy give acknowledgment
    RRI  Return patient referral
    SIU  Schedule information unsolicited
    SPQ  Stored procedure request
    SQM  Schedule query
    SQR  Schedule query response
    SRM  Schedule request
    SRR  Scheduled request response
    SUR  Summary product experience report
    TBR  Tabular data response
    UDM  Unsolicited display message
    VQQ  Virtual table query
    VXQ  Query for vaccination record
    VXX  Vaccination query response with multiple PID matches
    VXR  Vaccination query record response
    VXU  Unsolicited vaccination record update
    """

    ACK = "ACK"
    ADR = "ADR"
    ARD = "ARD"
    ADT = "ADT"
    BAR = "BAR"
    CRM = "CRM"
    CSU = "CSU"
    DFT = "DFT"
    DOC = "DOC"
    DSR = "DSR"
    EDR = "EDR"
    EQQ = "EQQ"
    ERP = "ERP"
    MCF = "MCF"
    MDM = "MDM"
    MFN = "MFN"
    MFK = "MFK"
    MFD = "MFD"
    MFQ = "MFQ"
    MFR = "MFR"
    NMD = "NMD"
    NMQ = "NMQ"
    NMR = "NMR"
    ORF = "ORF"
    ORM = "ORM"
    ORR = "ORR"
    ORU = "ORU"
    OSQ = "OSQ"
    OSR = "OSR"
    PEX = "PEX"
    PGL = "PGL"
    PIN = "PIN"
    PPG = "PPG"
    PPP = "PPP"
    PPR = "PPR"
    PPT = "PPT"
    PPV = "PPV"
    PRR = "PRR"
    PTR = "PTR"
    QCK = "QCK"
    QRY = "QRY"
    RAR = "RAR"
    RAS = "RAS"
    RCI = "RCI"
    RCL = "RCL"
    RDE = "RDE"
    RDR = "RDR"
    RDS = "RDS"
    REF = "REF"
    RER = "RER"
    RGV = "RGV"
    RGR = "RGR"
    ROR = "ROR"
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
    SIU = "SIU"
    SPQ = "SPQ"
    SQM = "SQM"
    SQR = "SQR"
    SRM = "SRM"
    SRR = "SRR"
    SUR = "SUR"
    TBR = "TBR"
    UDM = "UDM"
    VQQ = "VQQ"
    VXQ = "VXQ"
    VXX = "VXX"
    VXR = "VXR"
    VXU = "VXU"


class Abnormalflags(str, Enum):
    """
    0078 - Abnormal flags

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
    0080 - Nature of abnormal testing

    A  An age-based population
    N  None - generic normal range
    R  A race-based population
    S  A sex-based population
    """

    A = "A"
    N = "N"
    R = "R"
    S = "S"


class OutlierType(str, Enum):
    """
    0083 - Outlier Type

    D  Outlier days
    C  Outlier cost
    """

    D = "D"
    C = "C"


class Observationresultstatuscodesinterpretation(str, Enum):
    """
    0085 - Observation result status codes interpretation

    C  Record coming over is a correction and thus replaces a final result D  Deletes the OBX record F  Final
    results; Can only be changed with a corrected result. I  Specimen in lab; results pending N  Not asked; used to
    affirmatively document that the observation identified in the OBX was not sought when the universal service ID in
    OBR-4 implies that it would be sought. O  Order detail description only (no result) P  Preliminary results R
    Results entered -- not verified S  Partial results X  Results cannot be obtained for this observation U  Results
    status change to final without retransmitting results already sent as preliminary.  E.g., radiology changes
    status from preliminary to final W  Post original as wrong, e.g., transmitted for wrong patient
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
    0091 - Query priority

    D  Deferred
    I  Immediate
    """

    D = "D"
    I = "I"


class Re_admissionIndicator(str, Enum):
    """
    0092 - Re-admission Indicator

    R  Readmission
    """

    R = "R"


class Releaseinformation(str, Enum):
    """
    0093 - Release information

    Y  Yes
    N  No
    """

    Y = "Y"
    N = "N"


class Typeofagreement(str, Enum):
    """
    0098 - Type of agreement

    S  Standard
    U  Unified
    M  Maternity
    """

    S = "S"
    U = "U"
    M = "M"


class Whentocharge(str, Enum):
    """
    0100 - When to charge

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
    0102 - Delayed acknowledgment type

    D  Message received, stored for later processing
    F  Acknowledgment after processing
    """

    D = "D"
    F = "F"


class ProcessingID(str, Enum):
    """
    0103 - Processing ID

    D  Debugging
    P  Production
    T  Training
    """

    D = "D"
    P = "P"
    T = "T"


class VersionID(str, Enum):
    """
    0104 - Version ID

    2.0  Release 2.0
    2.0D  Demo 2.0
    2.1  Release 2. 1
    2.2  Release 2.2
    2.3  Release 2.3
    2.3.1  Release 2.3.1
    2.3.2  Release 2.3.2
    """

    _2_0 = "2.0"
    _2_0D = "2.0D"
    _2_1 = "2.1"
    _2_2 = "2.2"
    _2_3 = "2.3"
    _2_3_1 = "2.3.1"
    _2_3_2 = "2.3.2"


class Sourceofcomment(str, Enum):
    """
    0105 - Source of comment

    L  Ancillary (filler) department is source of comment
    P  Orderer (placer) is source of comment
    O  Other system is source of comment
    """

    L = "L"
    P = "P"
    O = "O"


class Query_responseformatcode(str, Enum):
    """
    0106 - Query-response format code

    D  Response is in display format
    R  Response is in record-oriented format
    T  Response is in tabular format
    """

    D = "D"
    R = "R"
    T = "T"


class Deferredresponsetype(str, Enum):
    """
    0107 - Deferred response type

    B  Before the Date/Time specified
    L  Later than the Date/Time specified
    """

    B = "B"
    L = "L"


class Queryresultslevel(str, Enum):
    """
    0108 - Query results level

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
    0109 - Report priority

    R  Routine
    S  Stat
    """

    R = "R"
    S = "S"


class Dischargedisposition(str, Enum):
    """
    0112 - Discharge disposition

    01  Discharged to home or self care (routine discharge) 02  Discharged/transferred to another short term general
    hospital for inpatient care 03  Discharged/transferred to skilled nursing facility (SNF) 04
    Discharged/transferred to an intermediate care facility (ICF) 05  Discharged/transferred to another type of
    institution for inpatient care or referred for outpatient services to another institution 06
    Discharged/transferred to home under care of organized home health service organization 07  Left against medical
    advice or discontinued care 08  Discharged/transferred to home under care of Home IV provider 09  Admitted as an
    inpatient to this hospital 10  Discharge to be defined at state level, if necessary 11  Discharge to be defined
    at state level, if necessary 12  Discharge to be defined at state level, if necessary 13  Discharge to be defined
    at state level, if necessary 14  Discharge to be defined at state level, if necessary 15  Discharge to be defined
    at state level, if necessary 16  Discharge to be defined at state level, if necessary 17  Discharge to be defined
    at state level, if necessary 18  Discharge to be defined at state level, if necessary 19  Discharge to be defined
    at state level, if necessary 20  Expired 21  Expired to be defined at state level, if necessary 22  Expired to be
    defined at state level, if necessary 23  Expired to be defined at state level, if necessary 24  Expired to be
    defined at state level, if necessary 25  Expired to be defined at state level, if necessary 26  Expired to be
    defined at state level, if necessary 27  Expired to be defined at state level, if necessary 28  Expired to be
    defined at state level, if necessary 29  Expired to be defined at state level, if necessary 30  Still patient or
    expected to return for outpatient services 31  Still patient to be defined at state level, if necessary 32  Still
    patient to be defined at state level, if necessary 33  Still patient to be defined at state level, if necessary
    34  Still patient to be defined at state level, if necessary 35  Still patient to be defined at state level,
    if necessary 36  Still patient to be defined at state level, if necessary 37  Still patient to be defined at
    state level, if necessary 38  Still patient to be defined at state level, if necessary 39  Still patient to be
    defined at state level, if necessary 40  Expired at home 41  Expired in a medical facility; e.g., hospital, SNF,
    ICF, or free standing hospice 42  Expired - place unknown
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


class Bedstatus(str, Enum):
    """
    0116 - Bed status

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


class Ordercontrolcodes(str, Enum):
    """
    0119 - Order control codes

    NW  New order (O01)
    OK  Order accepted & OK (O02)
    UA  Unable to accept order (O02/ORR)
    CA  Cancel order request (O01)
    OC  Order canceled (O01)
    CR  Canceled as requested (O02)
    UC  Unable to cancel (O02)
    DC  Discontinue order request (O01)
    OD  Order discontinued (O01)
    DR  Discontinued as requested (O02)
    UD  Unable to discontinue (O02)
    HD  Hold order request (O01)
    OH  Order held (O01)
    UH  Unable to put on hold (O02)
    HR  On hold as requested (O02)
    RL  Release previous hold (O01)
    OE  Order released (O01)
    OR  Released as requested
    UR  Unable to release (O02)
    RP  Order replace request (O01)
    RU  Replaced unsolicited (O01)
    RO  Replacement order (O01)
    RQ  Replaced as requested (O02)
    UM  Unable to replace (O02)
    PA  Parent order (O01/ORU)
    CH  Child order (O01/ORU)
    XO  Change order request (O01)
    XX  Order changed, unsol. (O01)
    UX  Unable to change (O02)
    XR  Changed as requested (O02)
    DE  Data errors (O01/O02)
    RE  Observations to follow (O01/R01)
    RR  Request received (O02)
    SR  Response to send order status request (O02(Q06)
    SS  Send order status request (O01)
    SC  Status changed (O01)
    SN  Send order number (O01)
    NA  Number assigned (O02)
    CN  Combined result (R01)
    RF  Refill order request (O01)
    AF  Order refill request approval (O02)
    DF  Order refill request denied (O02)
    FU  Order refilled, unsolicited (O01)
    OF  Order refilled as requested (O02)
    UF  Unable to refill (O02)
    LI  Link order to patient care problem or goal
    UN  Unlink order from patient care problem or goal
    """

    NW = "NW"
    OK = "OK"
    UA = "UA"
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
    0121 - Response flag

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
    0122 - Charge type

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
    0123 - Result status

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
    0124 - Transportation mode

    CART  Cart - patient travels on cart or gurney
    PORT  The examining device goes to patients location
    WALK  Patient walks to diagnostic service
    WHLC  Wheelchair
    """

    CART = "CART"
    PORT = "PORT"
    WALK = "WALK"
    WHLC = "WHLC"


class Valuetype(str, Enum):
    """
    0125 - Value type

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
    0126 - Quantity limited request

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


class Allergytype(str, Enum):
    """
    0127 - Allergy type

    DA  Drug allergy
    FA  Food allergy
    MA  Miscellaneous allergy
    MC  Miscellaneous contraindication
    """

    DA = "DA"
    FA = "FA"
    MA = "MA"
    MC = "MC"


class Allergyseverity(str, Enum):
    """
    0128 - Allergy severity

    SV  Severe
    MO  Moderate
    MI  Mild
    """

    SV = "SV"
    MO = "MO"
    MI = "MI"


class Procedurepractitioneridentifiercodetype(str, Enum):
    """
    0133 - Procedure practitioner identifier code type

    AN  Anesthesiologist
    PR  Procedure MD (surgeon)
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
    0135 - Assignment of benefits

    Y  Yes
    N  No
    M  Modified assignment
    """

    Y = "Y"
    N = "N"
    M = "M"


class Yes_noindicator(str, Enum):
    """
    0136 - Yes-no indicator

    Y  Yes
    N  No
    """

    Y = "Y"
    N = "N"


class Mailclaimparty(str, Enum):
    """
    0137 - Mail claim party

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
    0140 - Military service

    USA  U.S. Army
    USN  U.S. Navy
    USAF  U.S. Air Force
    USMC  U.S. Marines
    USCG  U.S. Coast Guard
    USPHS  U.S. Public Health Service
    NOAA  National Oceanic and Atmospheric Administration
    NATO  North Atlantic Treaty Organization
    """

    USA = "USA"
    USN = "USN"
    USAF = "USAF"
    USMC = "USMC"
    USCG = "USCG"
    USPHS = "USPHS"
    NOAA = "NOAA"
    NATO = "NATO"


class Militaryrank_grade(str, Enum):
    """
    0141 - Military rank-grade

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
    0142 - Military status

    ACT  Active duty
    RET  Retired
    DEC  Deceased
    """

    ACT = "ACT"
    RET = "RET"
    DEC = "DEC"


class Eligibilitysource(str, Enum):
    """
    0144 - Eligibility source

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
    0145 - Room type

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
    0146 - Amount type

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
    0147 - Policy type

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
    0148 - Penalty type

    AT  Currency amount
    PC  Percentage
    """

    AT = "AT"
    PC = "PC"


class Daytype(str, Enum):
    """
    0149 - Day type

    AP  Approved
    DE  Denied
    PE  Pending
    """

    AP = "AP"
    DE = "DE"
    PE = "PE"


class Pre_certificationpatienttype(str, Enum):
    """
    0150 - Pre-certification patient type

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
    0153 - Value code

    01  Most common semi-private rate 02  Hospital has no semi-private rooms 04  Inpatient professional component
    charges which are combined billed 05  Professional component included in charges and also billed separate to
    carrier 06  Medicare blood deductible 08  Medicare life time reserve amount in the first calendar year 09
    Medicare co-insurance amount in the first calendar year 10  Lifetime reserve amount in the second calendar year
    11  Co-insurance amount in the second calendar year 12  Working aged beneficiary/spouse with employer group
    health plan 13  ESRD beneficiary in a Medicare coordination period with an employer group health plan 14  No
    Fault including auto/other 15  Workers Compensation 16  PHS, or other federal agency 17  Payer code 21
    Catastrophic 22  Surplus 23  Recurring monthly incode 24  Medicaid rate code 30  Pre-admission testing 31
    Patient liability amount 37  Pints of blood furnished 38  Blood deductible pints 39  Pints of blood replaced 40
    New coverage not implemented by HMO (for inpatient service only) 41  Black lung 42  VA 43  Disabled beneficiary
    under age 64 with LGHP 44  Amount provider agreed to accept from primary payer when this amount is less than
    charges but higher than payment received,, then a Medicare secondary payment is due 45  Accident hour 46  Number
    of grace days 47  Any liability insurance 48  Hemoglobin reading 49  Hematocrit reading 50  Physical therapy
    visits 51  Occupational therapy visits 52  Speech therapy visits 53  Cardiac rehab visits 56  Skilled nurse -
    home visit hours 57  Home health aide - home visit hours 58  Arterial blood gas 59  Oxygen saturation 60  HHA
    branch MSA 67  Peritoneal dialysis 68  EPO-drug 70  Payer codes 72  Payer codes 70 ... 72  Payer codes 71  Payer
    codes 75  Payer codes 75 ... 79  Payer codes 76  Payer codes 77  Payer codes 78  Payer codes 79  Payer codes 80
    Psychiatric visits 81  Visits subject to co-payment A1  Deductible payer A A2  Coinsurance payer A A3  Estimated
    responsibility payer A X0  Service excluded on primary policy X4  Supplemental coverage
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
    0155 - Accept-application acknowledgment conditions

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
    0156 - Which date-time qualifier

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
    0157 - Which date-time status qualifier

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
    0158 - Date-time selection qualifier

    1ST  First value within range ALL  All values within the range LST  Last value within the range REV  All values
    within the range returned in reverse chronological order (This is the default if not otherwise specified.)
    """

    _1ST = "1ST"
    ALL = "ALL"
    LST = "LST"
    REV = "REV"


class Dietcodespecificationtype(str, Enum):
    """
    0159 - Diet code specification type

    D  Diet
    S  Supplement
    P  Preference
    """

    D = "D"
    S = "S"
    P = "P"


class Traytype(str, Enum):
    """
    0160 - Tray type

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
    0161 - Allow substitution

    N  Substitutions are NOT authorized.  (This is the default - null.)
    G  Allow generic substitutions.
    T  Allow therapeutic substitutions
    """

    N = "N"
    G = "G"
    T = "T"


class Routeofadministration(str, Enum):
    """
    0162 - Route of administration

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


class Administrativesite(str, Enum):
    """
    0163 - Administrative site

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
    0164 - Administration device

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
    0165 - Administration method

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
    0166 - RX component type

    B  Base
    A  Additive
    """

    B = "B"
    A = "A"


class Substitutionstatus(str, Enum):
    """
    0167 - Substitution status

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
    0168 - Processing priority

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
    0169 - Reporting priority

    C  Call back results
    R  Rush reporting
    """

    C = "C"
    R = "R"


class Derivedspecimen(str, Enum):
    """
    0170 - Derived specimen

    P  Parent Observation
    C  Child Observation
    N  Not Applicable
    """

    P = "P"
    C = "C"
    N = "N"


class Coordinationofbenefits(str, Enum):
    """
    0173 - Coordination of benefits

    CO  Coordination
    IN  Independent
    """

    CO = "CO"
    IN = "IN"


class Natureoftest_observation(str, Enum):
    """
    0174 - Nature of test-observation

    P  Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes),
    usually done at one instrument on one specimen F  Functional procedure that may consist of one or more
    interrelated measures (e.g., glucose tolerance test, creatine clearance), usually done at different times and/or
    on different specimens A  Atomic test/observation (test code or treatment code) S  Superset--a set of batteries
    or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA,
    electrolytes) C  Single observation calculated via a rule or formula from other independent observations (e.g.,
    Alveolar--arterial ratio, cardiac output)
    """

    P = "P"
    F = "F"
    A = "A"
    S = "S"
    C = "C"


class Masterfileidentifiercode(str, Enum):
    """
    0175 - Master file identifier code

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


class Confidentialitycode(str, Enum):
    """
    0177 - Confidentiality code

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
    0178 - File level event code

    REP  Replace current version of this master file with the version contained in this message
    UPD  Change file records as defined in the record-level event codes for each record that follows
    """

    REP = "REP"
    UPD = "UPD"


class Responselevel(str, Enum):
    """
    0179 - Response level

    NE  Never.  No application-level response needed ER  Error/Reject conditions only.  Only MFA segments denoting
    errors must be returned via the application-level acknowledgment for this message AL  Always. All MFA segments (
    whether denoting errors or not) must be returned via the application-level acknowledgment message SU  Success.
    Only MFA segments denoting success must be returned via the application-level acknowledgment for this message
    """

    NE = "NE"
    ER = "ER"
    AL = "AL"
    SU = "SU"


class Record_leveleventcode(str, Enum):
    """
    0180 - Record-level event code

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
    0181 - MFN record-level error return

    S  Successful posting of the record defined by the MFE segment
    U  Unsuccessful posting of the record defined by the MFE segment
    """

    S = "S"
    U = "U"


class Active_inactive(str, Enum):
    """
    0183 - Active-inactive

    A  Active Staff
    I  Inactive Staff
    """

    A = "A"
    I = "I"


class Preferredmethodofcontact(str, Enum):
    """
    0185 - Preferred method of contact

    H  Home Phone Number
    O  Office Phone Number
    F  FAX Number
    C  Cellular Phone Number
    B  Beeper Number
    E  E-Mail Address (for backward compatibility)
    """

    H = "H"
    O = "O"
    F = "F"
    C = "C"
    B = "B"
    E = "E"


class Providerbilling(str, Enum):
    """
    0187 - Provider billing

    P  Provider does own billing
    I  Institution bills for provider
    """

    P = "P"
    I = "I"


class Addresstype(str, Enum):
    """
    0190 - Address type

    C  Current Or Temporary P  Permanent M  Mailing B  Firm/Business O  Office H  Home N  Birth (nee) (birth address,
    not otherwise specified) BDL  Birth delivery location (address where birth occurred) BR  Residence  at birth (
    home address at time of birth) F  Country Of Origin L  Legal Address RH  Registry home.  Refers to the
    information system, typically managed by a public health agency, that  stores patient information such as
    immunization histories or cancer data, regardless of where the patient obtains services. BA  Bad address
    """

    C = "C"
    P = "P"
    M = "M"
    B = "B"
    O = "O"
    H = "H"
    N = "N"
    BDL = "BDL"
    BR = "BR"
    F = "F"
    L = "L"
    RH = "RH"
    BA = "BA"


class Typeofreferenceddata(str, Enum):
    """
    0191 - Type of referenced data

    SI  Scanned image (HL7 V2.2 only)
    NS  Non-scanned image (HL7 V2.2 only)
    SD  Scanned document (HL7 V2.2 only)
    TX  Machine readable text document (HL7 V2.2 only)
    FT  Formatted text (HL7 V2.2 only)
    TEXT  Machine readable text document (HL7 V2.3.1 and later)
    IM  Image data  (new  with HL7 v 2.3)
    AU  Audio data  (new with HL7 v 2.3)
    Image  Image data  (HL7 V2.3 and later)
    AP  Other application data, typically uninterpreted binary data  (new with HL7 v 2.3)
    Audio  Audio data  (HL7 V2.3 and later)
    Application  Other application data, typically uninterpreted binary data  (HL7 V2.3 and later)
    """

    SI = "SI"
    NS = "NS"
    SD = "SD"
    TX = "TX"
    FT = "FT"
    TEXT = "TEXT"
    IM = "IM"
    AU = "AU"
    Image = "Image"
    AP = "AP"
    Audio = "Audio"
    Application = "Application"


class Amountclass(str, Enum):
    """
    0193 - Amount class

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
    0200 - Name type

    A  Alias Name
    L  Legal Name
    D  Display Name
    M  Maiden Name
    C  Adopted Name
    B  Name at Birth
    P  Name of Partner/Spouse
    S  Coded Pseudo-Name to ensure anonymity
    T  Tribal/Community Name
    U  Unspecified
    """

    A = "A"
    L = "L"
    D = "D"
    M = "M"
    C = "C"
    B = "B"
    P = "P"
    S = "S"
    T = "T"
    U = "U"


class Telecommunicationusecode(str, Enum):
    """
    0201 - Telecommunication use code

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
    0202 - Telecommunication equipment type

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
    0203 - Identifier type

    AM  American Express
    AN  Account number
    BR  Birth registry number
    DI  Diners Club card
    DL  Drivers license number
    DN  Doctor number
    DS  Discover Card
    EI  Employee number
    EN  Employer number
    FI  Facility ID
    GI  Guarantor internal identifier
    GN  Guarantor external  identifier
    LN  License number
    LR  Local Registry ID
    MS  MasterCard
    MA  Medicaid number
    MC  Medicare number
    MR  Medical record number
    NE  National employer identifier
    NI  National unique individual identifier
    NH  National Health Plan Identifier
    NNxxx  National Person Identifier where the xxx is the ISO table 3166  3-character (alphabetic) country  code
    NPI  National provider identifier
    PI  Patient internal identifier
    PN  Person number
    PRN  Provider number
    PT  Patient external identifier
    RRI  Regional registry ID
    RR  Railroad Retirement number
    SL  State license
    SR  State registry ID
    SS  Social Security number
    U  Unspecified
    UPIN  Medicare/HCFAs Universal Physician Identification numbers
    VS  VISA
    VN  Visit number
    WC  WIC identifier
    XX  Organization identifier
    """

    AM = "AM"
    AN = "AN"
    BR = "BR"
    DI = "DI"
    DL = "DL"
    DN = "DN"
    DS = "DS"
    EI = "EI"
    EN = "EN"
    FI = "FI"
    GI = "GI"
    GN = "GN"
    LN = "LN"
    LR = "LR"
    MS = "MS"
    MA = "MA"
    MC = "MC"
    MR = "MR"
    NE = "NE"
    NI = "NI"
    NH = "NH"
    NNxxx = "NNxxx"
    NPI = "NPI"
    PI = "PI"
    PN = "PN"
    PRN = "PRN"
    PT = "PT"
    RRI = "RRI"
    RR = "RR"
    SL = "SL"
    SR = "SR"
    SS = "SS"
    U = "U"
    UPIN = "UPIN"
    VS = "VS"
    VN = "VN"
    WC = "WC"
    XX = "XX"


class Organizationalnametype(str, Enum):
    """
    0204 - Organizational name type

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
    0205 - Price type

    AP  administrative price or handling fee
    PF  professional fee for performing provider
    UP  unit price, may be based on length of procedure or service
    TF  technology fee for use of equipment
    DC  direct unit cost
    IC  indirect unit cost
    TP  total price
    """

    AP = "AP"
    PF = "PF"
    UP = "UP"
    TF = "TF"
    DC = "DC"
    IC = "IC"
    TP = "TP"


class Segmentactioncode(str, Enum):
    """
    0206 - Segment action code

    A  Add/Insert
    D  Delete
    U  Update
    """

    A = "A"
    D = "D"
    U = "U"


class Processingmode(str, Enum):
    """
    0207 - Processing mode

    A  Archive
    R  Restore from archive
    I  Initial load
    T  Current processing, transmitted at intervals (scheduled or on demand)
    not present  Not present (the default, meaning current  processing)
    """

    A = "A"
    R = "R"
    I = "I"
    T = "T"
    not_present = "not present"


class Queryresponsestatus(str, Enum):
    """
    0208 - Query response status

    OK  Data found, no errors (this is the default)
    NF  No data found, no errors
    AE  Application error
    AR  Application reject
    """

    OK = "OK"
    NF = "NF"
    AE = "AE"
    AR = "AR"


class RelationalOperator(str, Enum):
    """
    0209 - Relational Operator

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


class RelationalConjunction(str, Enum):
    """
    0210 - Relational Conjunction

    AND  Default
    OR
    """

    AND = "AND"
    OR = "OR"


class Alternatecharactersets(str, Enum):
    """
    0211 - Alternate character sets

    ASCII  The printable 7-bit ASCII character set . (This is the default if this field is omitted) 8859/1  The
    printable characters from the ISO 8859/1 Character set 8859/2  The printable characters from the ISO 8859/2
    Character set 8859/3  The printable characters from the ISO 8859/3 Character set 8859/4  The printable characters
    from the ISO 8859/4 Character set 8859/5  The printable characters from the ISO 8859/5 Character set 8859/6  The
    printable characters from the ISO 8859/6 Character set 8859/7  The printable characters from the ISO 8859/7
    Character set 8859/8  The printable characters from the ISO 8859/8 Character set 8859/9  The printable characters
    from the ISO 8859/9 Character set ISO IR14  Code for Information Exchange (one byte)(JIS X 0201-1976),
    Note that the code contains a  space, i.e. "ISO IR14". ISO IR87  Code for the Japanese Graphic Character set for
    information interchange (JIS X 0208-1990), Note that the code contains a space, i.e. "ISO IR87". ISO IR159  Code
    of the supplementary Japanese Graphic Character set for information interchange (JIS X  0212-1990), Note that the
    code contains a space, i.e. "ISO IR159". UNICODE  The world wide character standard from ISO/IEC 10646-1-1993
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


class Purgestatus(str, Enum):
    """
    0213 - Purge status

    P  Marked for purge.  User is no longer able to update the visit.
    D  The visit is marked for deletion and the user cannot enter new data against it.
    I  The visit is marked inactive and the user cannot enter new data against it.
    """

    P = "P"
    D = "D"
    I = "I"


class Livingarrangement(str, Enum):
    """
    0220 - Living arrangement

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
    0223 - Living dependency

    D  Spouse dependent
    M  Medical Supervision Required
    S  Small children
    WU  Walk up
    CB  Common Bath
    """

    D = "D"
    M = "M"
    S = "S"
    WU = "WU"
    CB = "CB"


class Transportarranged(str, Enum):
    """
    0224 - Transport arranged

    A  Arranged
    N  Not Arranged
    U  Unknown
    """

    A = "A"
    N = "N"
    U = "U"


class Escortrequired(str, Enum):
    """
    0225 - Escort required

    R  Required
    N  Not Required
    U  Unknown
    """

    R = "R"
    N = "N"
    U = "U"


class Manufacturersofvaccines(str, Enum):
    """
    0227 - Manufacturers of vaccines (code=MVX)

    AB  Abbott Laboratories AD  Adams Laboratories ALP  Alpha Therapeutic Corporation AR  Armour (Inactive  use CEN)
    AVI  Aviron BA  Baxter Healthcare Corporation BAY  Bayer Corporation (includes Miles, Inc. and Cutter
    Laboratories) BP  Berna Products (Inactive  use BPC) BPC  Berna Products Corporation (includes Swiss Serum and
    Vaccine Institute Berna) CEN  Centeon L.L.C. (includes Armour Pharmaceutical Company) CHI  Chiron Corporation CON
     Connaught (inactive  use PMC) EVN  Evans Medical Limited GRE  Greer Laboratories, Inc. IAG  Immuno
     International AG IM  Merieux (inactive  Use PMC) IUS  Immuno-US, Inc. JPN  The Research Foundation for
     Microbial Diseases of Osaka University (BIKEN) KGC  Korea Green Cross Corporation LED  Lederle (inactive  use
     WAL) MA  Massachusetts Public Health Biologic Laboratories) MED  Medimmune, Inc. MIL  Miles (inactive  use BAY)
     MIP  Michigan Biologic Products Institute MSD  Merck & Co., Inc. NAB  NABI (formerly North American Biologicals,
     Inc.) NYB  New York Blood Center NAV  North American Vaccine, Inc. NOV  Novartis Pharmaceutical Corporation OTC
     Organon Teknika Corporation ORT  Ortho Diagnostic Systems, Inc. PD  Parkdale Pharmaceuticals (formerly
     Parke-Davis) PMC  Pasteur Merieux Connaught (includes Connaught Laboratories and Pasteur Merieux) PRX  Praxis
     Biologics (inactive  use WAL) SCL  Sclavo, Inc. SI  Swiss Serum and Vaccine Inst. (inactive  use BPC) SKB
     SmithKline Beecham USA  United States Army Medical Research and Materiel Command WA  Wyeth-Ayerst (inactive 
     use WAL) WAL  Wyeth-Ayerst (includes Wyeth-Lederle Vaccines and Pediatrics, Wyeth Laboratories,
     Lederle Laboratories, and Praxis Biologics) OTH  Other UNK  Unknown manufacturer
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
    0228 - Diagnosis classification

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
    0229 - DRG payor

    M  Medicare
    C  Champus
    G  Managed Care Organization
    """

    M = "M"
    C = "C"
    G = "G"


class Procedurefunctionaltype(str, Enum):
    """
    0230 - Procedure functional type

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
    0231 - Student status

    F  Full-time student
    P  Part-time student
    N  Not a student
    """

    F = "F"
    P = "P"
    N = "N"


class Insurancecompanycontactreason(str, Enum):
    """
    0232 - Insurance company contact reason

    01  Medicare claim status
    02  Medicaid claim status
    03  Name/address change
    """

    _01 = "01"
    _02 = "02"
    _03 = "03"


class Reporttiming(str, Enum):
    """
    0234 - Report timing

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
    0235 - Report source

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
    0236 - Event reported to

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
    0237 - Event qualification

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
    0238 - Event seriousness

    Y  Yes
    S  Significant
    N  No
    """

    Y = "Y"
    S = "S"
    N = "N"


class Eventexpected(str, Enum):
    """
    0239 - Event expected

    Y  Yes
    N  No
    U  Unknown
    """

    Y = "Y"
    N = "N"
    U = "U"


class Eventconsequence(str, Enum):
    """
    0240 - Event consequence

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
    0241 - Patient outcome

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


class PrimaryObserver(str, Enum):
    """
    0242 - Primary observerВ’s qualification

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
    0243 - Identity may be divulged

    Y  Yes
    N  No
    NA  Not applicable
    """

    Y = "Y"
    N = "N"
    NA = "NA"


class Statusofevaluation(str, Enum):
    """
    0247 - Status of evaluation

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
    0248 - Product source

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
    0250 - Relatedness assessment

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
    0251 - Action taken in response to the event

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
    0252 - Causality observations

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
    0253 - Indirect exposure mechanism

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
    0254 - Kind of quantity

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
    LIQ  *Liquifaction
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
    0255 - Duration categories

    PT  To identify measures at a point in time.  This is a synonym for "spot" or "random" as applied to urine
    measurements. *  Life of the "unit."  Used for blood products. 30M  30 minutes 1H  1 hour 2H  2 hours 2.5H  2 1/2
    hours 3H  3 hours 4H  4 hours 5H  5 hours 6H  6 hours 7H  7 hours 8H  8 hours 12H  12 hours 24H  24 hours 2D  2
    days 3D  3 days 4D  4 days 5D  5 days 6D  6 days 1W  1 week 2W  2 weeks 3W  3 weeks 4W  4 weeks 1L  1 months (30
    days) 2L  2 months 3L  3 months
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
    0256 - Time delay post challenge

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
    0257 - Nature of challenge

    CFST  Fasting (no calorie intake) for the period specified in the time component of the term, e.g., 1H POST CFST
    EXCZ  Exercise undertaken as challenge (can be quantified)
    FFST  No fluid intake for the period specified in the time component of the term
    """

    CFST = "CFST"
    EXCZ = "EXCZ"
    FFST = "FFST"


class Relationshipmodifier(str, Enum):
    """
    0258 - Relationship modifier

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
    0259 - Modality

    AS  Angioscopy
    BS  Biomagnetic imaging
    CD  Color flow doppler
    CP  Colposcopy
    CR  Computed radiography
    CS  Cystoscopy
    CT  Computed tomography
    DD  Duplex doppler
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
    0260 - Patient location type

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
    0261 - Location equipment

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
    0262 - Privacy level

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
    0263 - Level of care

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
    0265 - Specialty type

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


class DaysoftheWeek(str, Enum):
    """
    0267 - Days of the Week

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
    0268 - Override

    X  Override not allowed
    A  Override allowed
    R  Override required
    """

    X = "X"
    A = "A"
    R = "R"


class Chargeonindicator(str, Enum):
    """
    0269 - Charge on indicator

    O  Charge on Order
    R  Charge on Result
    """

    O = "O"
    R = "R"


class Documenttype(str, Enum):
    """
    0270 - Document type

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
    0271 - Document completion status

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
    0272 - Document confidentiality status

    V  Very restricted
    R  Restricted
    U  Usual control
    """

    V = "V"
    R = "R"
    U = "U"


class Documentavailabilitystatus(str, Enum):
    """
    0273 - Document availability status

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
    0275 - Document storage status

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
    0276 - Appointment reason codes

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
    0277 - Appointment type codes

    Normal  Routine schedule request type - default if not valued Tentative  A request for a tentative (e.g.,
    penciled in) appointment Complete  A request to add a completed appointment, used to maintain records of
    completed appointments that did not appear in the schedule (e.g., STAT, walk-in, etc.)
    """

    N_mal = "Normal"
    Tentative = "Tentative"
    Complete = "Complete"


class Fillerstatuscodes(str, Enum):
    """
    0278 - Filler status codes

    Pending  Appointment has not yet been confirmed Waitlist  Appointment has been placed on a waiting list for a
    particular slot, or set of slots Booked  The indicated appointment is booked Started  The indicated appointment
    has begun and is currently in progress Complete  The indicated appointment has completed normally (was not
    discontinued, canceled, or deleted) Cancelled  T7he indicated appointment was stopped from occurring (canceled
    prior to starting) Discontinued  The indicated appointment was discontinued (DCed while in progress,
    discontinued parent appointment, or discontinued child appointment) Deleted  The indicated appointment was
    deleted from the filler application Blocked  The indicated time slot(s) is(are) blocked Overbook  The appointment
    has been confirmed; however it is confirmed in an overbooked state
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
    0279 - Allow substitution codes

    No  Substitution of this resource is not allowed Confirm  Contact the Placer Contact Person prior to making any
    substitutions of this resource Notify  Notify the Placer Contact Person, through normal institutional procedures,
    that a substitution of this resource has been made Yes  Substitution of this resource is allowed
    """

    No = "No"
    Confirm = "Confirm"
    Notify = "Notify"
    Yes = "Yes"


class Referralpriority(str, Enum):
    """
    0280 - Referral priority

    S  STAT
    A  ASAP
    R  Routine
    """

    S = "S"
    A = "A"
    R = "R"


class Referraltype(str, Enum):
    """
    0281 - Referral type

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
    0282 - Referral disposition

    WR  Send Written Report
    RP  Return Patient After Evaluation
    AM  Assume Management
    SO  Second Opinion
    """

    WR = "WR"
    RP = "RP"
    AM = "AM"
    SO = "SO"


class ReferralStatus(str, Enum):
    """
    0283 - Referral Status

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
    0284 - Referral category

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
    0286 - Provider role

    RP  Referring Provider
    PP  Primary Care Provider
    CP  Consulting Provider
    RT  Referred to Provider
    """

    RP = "RP"
    PP = "PP"
    CP = "CP"
    RT = "RT"


class Problem_GoalActioncode(str, Enum):
    """
    0287 - Problem-Goal Action code

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
    0290 - MIME base64 encoding characters

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
    0291 - Subtype of Referenced Data

    TIFF  TIFF image data
    PICT  PICT format image data
    DICOM  Digital Imaging and Communications in Medicine
    FAX  Facsimile data
    JOT  Electronic ink data (Jot 1.0 standard)
    BASIC  ISDN PCM audio data
    Octet-stream  Uninterpreted binary data
    PostScript  PostScript program
    JPEG  Joint Photographic Experts Group
    GIF  Graphics Interchange Format
    HTML  Hypertext Markup Language
    SGML  Structured General Markup Language (HL7 V2.3.1 and later)
    XML  Extensible Markup Language (HL7 V2.3.1 and later)
    RTF  Rich Text Format
    """

    TIFF = "TIFF"
    PICT = "PICT"
    DICOM = "DICOM"
    FAX = "FAX"
    JOT = "JOT"
    BASIC = "BASIC"
    Octet_stream = "Octet-stream"
    PostScript = "PostScript"
    JPEG = "JPEG"
    GIF = "GIF"
    HTML = "HTML"
    SGML = "SGML"
    XML = "XML"
    RTF = "RTF"


class Vaccinesadministered(str, Enum):
    """
    0292 - Vaccines administered

    54  Adenovirus, type 4
    55  Adenovirus, type 7
    82  Adenovirus, NOS
    24  Anthrax
    19  BCG
    27  Botulinum antitoxin
    26  Cholera
    29  CMVIG
    56  Dengue fever
    12  Diphtheria antitoxin
    28  DT(pediatric)
    20  DTaP
    50  DtaP-Hib
    01  DTP
    22  DTP-Hib
    57  Hantavirus
    52  Hep A - adult
    83  Hep A, ped/adol, 2 dose
    84  Hep A, ped/adol, 3 dose
    31  Hep A, pediatric, NOS
    85  Hep A, NOS
    30  HBIG
    08  Hep B, adolescent or pediatric
    42  Hep B, adolescent/high risk infant
    43  Hep B, adult
    44  Hep B, dialysis
    45  Hep B,  NOS
    58  Hep C
    59  Hep E
    60  Herpes simplex 2
    46  Hib (PRP-D)
    47  Hib (HbOC)
    48  Hib (PRP-T)
    49  Hib (PRP-OMP)
    17  Hib,  NOS
    51  Hib-Hep B
    61  HIV
    62  HPV
    86  IG
    87  IGIV
    14  IG, NOS
    15  Influenzasplit (incl. purified surface antigen)
    16  Influenzawhole
    88  Influenza, NOS
    10  IPV
    02  OPV
    89  Polio, NOS
    39  Japanese encephalitis
    63  Junin virus
    64  Leishmaniasis
    65  Leprosy
    66  Lyme disease
    03  MMR
    04  M/R
    67  Malaria
    05  Measles
    68  Melanoma
    32  Meningococcal
    07  Mumps
    69  Parainfluenza-3
    11  Pertussis
    23  Plague
    33  Pneumococcal
    70  Q fever
    18  Rabies, intramuscular injection
    40  Rabies, intradermal injection
    90  Rabies, NOS
    72  Rheumatic fever
    73  Rift Valley fever
    34  RIG
    74  Rotavirus
    71  RSV-IGIV
    06  Rubella
    38  Rubella/Mumps
    75  Smallpox
    76  Staphylococcus bacterio lysate
    09  Td (Adult)
    35  Tetanus toxoid
    77  Tick-borne encephalitis
    13  TIG
    78  Tularemia vaccine
    25  Typhoidoral
    41  Typhoidparenteral
    53  Typhoid, parenteral, AKD (U.S. military)
    91  Typhoid, NOS
    79  Vaccinia immune globulin
    21  Varicella
    81  VEE, inactivated
    80  VEE, live
    92  VEE, NOS
    36  VZIG
    37  Yellow fever
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
    _67 = "67"
    _05 = "05"
    _68 = "68"
    _32 = "32"
    _07 = "07"
    _69 = "69"
    _11 = "11"
    _23 = "23"
    _33 = "33"
    _70 = "70"
    _18 = "18"
    _40 = "40"
    _90 = "90"
    _72 = "72"
    _73 = "73"
    _34 = "34"
    _74 = "74"
    _71 = "71"
    _06 = "06"
    _38 = "38"
    _75 = "75"
    _76 = "76"
    _09 = "09"
    _35 = "35"
    _77 = "77"
    _13 = "13"
    _78 = "78"
    _25 = "25"
    _41 = "41"
    _53 = "53"
    _91 = "91"
    _79 = "79"
    _21 = "21"
    _81 = "81"
    _80 = "80"
    _92 = "92"
    _36 = "36"
    _37 = "37"


class Timeselectioncriteriaparameterclasscodes(str, Enum):
    """
    0294 - Time selection criteria parameter class codes

    PREFSTART  The preferred start time for the appointment request, service or resource.   Any legal time
    specification in the format HHMM, using 24-hour clock notation PREFEND  The preferred end time for the
    appointment request, service or resource.  Any legal time specification in the format HHMM, using 24-hour clock
    notation MON  An indicator that Monday is or is not preferred for the day on which the appointment will occur. OK
    = Preferred appointment day NO = Day is not preferred TUE  An indicator that Tuesday is or is not preferred for
    the day on which the appointment will occur.  OK = Preferred appointment day NO = Day is not preferred WED An
    indicator that Wednesday is or is not preferred for the day on which the appointment will occur. OK = Preferred
    appointment day NO = Day is not preferred THU  An indicator that Thursday is or is not preferred for the day on
    which the appointment will occur.  OK = Preferred appointment day NO = Day is not preferred FRI  An indicator
    that Friday is or is not preferred for the day on which the appointment will occur.  OK =  Preferred appointment
    day NO = Day is not preferred SAT  An indicator that Saturday is or is not preferred for the day on which the
    appointment will occur.  OK =  Preferred appointment day NO = Day is not preferred SUN  An indicator that Sunday
    is or is not preferred for the day on which the appointment will occur.  OK = Preferred appointment day NO = Day
    is not preferred
    """

    PREFSTART = "PREFSTART"
    PREFEND = "PREFEND"
    MON = "MON"
    TUE = "TUE"
    WED = "WED"
    THU = "THU"
    FRI = "FRI"
    SAT = "SAT"
    SUN = "SUN"


class CPRangeType(str, Enum):
    """
    0298 - CP Range Type

    P  Pro-rate.  Apply this price to this interval, pro-rated by whatever portion of the interval has occurred/been
    consumed F  Flat-rate.  Apply the entire price to this interval, do not pro-rate the price if the full interval
    has not occurred/been consumed
    """

    P = "P"
    F = "F"


class Encoding(str, Enum):
    """
    0299 - Encoding

    A  no encoding - data are displayable ASCII characters. Hex  hexadecimal encoding - consecutive pairs of
    hexadecimal digits represent consecutive single octets. Base64  encoding as defined by MIME (Multipurpose
    Internet Mail Extensions) standard RFC 1521.  Four consecutive ASCII characters represent three consecutive
    octets of binary data.  Base64 utilizes a 65-character subset of US-ASCII, consisting of both the upper a
    """

    A = "A"
    Hex = "Hex"
    Base64 = "Base64"


class UniversalIDtype(str, Enum):
    """
    0301 - Universal ID type

    DNS  An Internet dotted name. Either in ASCII or as integers GUID  Same as UUID. HCD  The CEN Healthcare Coding
    Scheme Designator. (Identifiers used in DICOM follow this assignment scheme.) HL7  Reserved for future HL7
    registration schemes ISO  An International Standards Organization Object Identifier N  These are reserved for
    locally defined coding schemes. M  These are reserved for locally defined coding schemes. L,M,N  These are
    reserved for locally defined coding schemes. L  These are reserved for locally defined coding schemes. Random
    Usually a base64 encoded string of random bits.  The uniqueness depends on the length of the bits.  Mail systems
    often generate ASCII string  "unique names," from a  combination of random bits and system names.  Obviously,
    such identifiers will not be con UUID  The DCE Universal Unique Identifier x400  An X.400 MHS format identifier
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


class Coveragetype(str, Enum):
    """
    0309 - Coverage type

    H  Hospital/institutional
    P  Physician/professional
    B  Both hospital and physician
    """

    H = "H"
    P = "P"
    B = "B"


class Livingwill(str, Enum):
    """
    0315 - Living will

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


class Organdonor(str, Enum):
    """
    0316 - Organ donor

    Y  Yes, patient is a donor and card is on file
    F  Yes, patient is a donor, but card is not on file
    I  No, patient does not have a living will but information was provided
    U  Unknown
    """

    Y = "Y"
    F = "F"
    I = "I"
    U = "U"


class Annotations(str, Enum):
    """
    0317 - Annotations

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
    0321 - Dispense method

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
    0322 - Completion status

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
    0323 - Action code

    A  Add/Insert
    D  Delete
    U  Update
    """

    A = "A"
    D = "D"
    U = "U"


class LocationcharacteristicID(str, Enum):
    """
    0324 - Location characteristic ID

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
    0325 - Location relationship ID

    RX  Nearest  pharmacy
    RX2  Second pharmacy
    LAB  Nearest  lab
    LB2  Second lab
    DTY  Nearest  dietary
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
    0326 - Visit indicator

    A  Account level (default)
    V  Visit level
    """

    A = "A"
    V = "V"


class Quantitymethod(str, Enum):
    """
    0329 - Quantity method

    A  Actual count
    E  Estimated (see comment)
    """

    A = "A"
    E = "E"


class Marketingbasis(str, Enum):
    """
    0330 - Marketing basis

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
    0331 - Facility type

    U  User
    M  Manufacturer
    D  Distributor
    A  Agent for a foreign manufacturer
    """

    U = "U"
    M = "M"
    D = "D"
    A = "A"


class Networksourcetype(str, Enum):
    """
    0332 - Network source type

    I  Initiate
    A  Accept
    """

    I = "I"
    A = "A"


class Disabledperson(str, Enum):
    """
    0334 - Disabled person

    PT  Patient
    GT  Guarantor
    IN  Insured
    AP  Associated party
    """

    PT = "PT"
    GT = "GT"
    IN = "IN"
    AP = "AP"


class Referralreason(str, Enum):
    """
    0336 - Referral reason

    S  Second Opinion
    P  Patient Preference
    O  Provider Ordered
    W  Work Load
    """

    S = "S"
    P = "P"
    O = "O"
    W = "W"


class CertificationStatus(str, Enum):
    """
    0337 - Certification Status

    E  Eligible
    C  Certified
    """

    E = "E"
    C = "C"


class PractitionerIDnumbertype(str, Enum):
    """
    0338 - Practitioner ID number type

    UPIN  Unique physician ID no.
    SL  State license number
    MCD  Medicaid number
    GL  General ledger number
    CY  County number
    TAX  Tax ID number
    DEA  Drug Enforcement Agency no.
    MCR  Medicare number
    L&I  Labor and industries number
    QA  QA number
    TRL  Training license number
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


class AdvancedBeneficiaryNoticeCode(str, Enum):
    """
    0339 - Advanced Beneficiary Notice Code

    1  Service is subject to medical necessity procedures
    2  Patient has been informed of responsibility, and agrees to pay for service
    3  Patient has been informed of responsibility, and asks that the payer be billed
    4  Advanced Beneficiary Notice has not been signed
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"


class PatientRelationshipToInsured(str, Enum):
    """
    0344 - PatientВ’s relationship to insured

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
    0348 - Special program indicator

    01  EPSDT-CHAP
    02  Physically handicapped childrens program
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
    0349 - PSRO-UR approval indicator

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
    0350 - Occurrence code

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
    28  Spouses date of birth
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
    0351 - Occurrence span

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
    M0  PRO/UR approved stay dates
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
    0353 - CWE statuses

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
    0354 - Message structure

    OMS_O01
    ORD_O02
    ORS_O02
    ACK
    ORN_O02
    OMN_O01
    RDO_O01
    RRO_O02
    OMD_O01
    ADT_A01  A01, A04, A05, A08, A13, A14, A28, A31
    ADT_A02  A02, A21, A22, A23, A25, A26, A27, A29, A32, A33
    ADT_A03  A03
    ADT_A06  A06, A07
    ADT_A09  A09, A10, A11, A15
    ADT_A12  A12
    ADT_A16  A16
    ADT_A17  A17
    ADT_A18  A18
    ADT_A20  A20
    ADT_A24  A24
    ADT_A28  A28, A31
    ADT_A30  A30, A34, A35, 136, A46, A47, A48, A49
    ADT_A37  A37
    ADT_A38  A38
    ADT_A39  A39, A40, A41, A42
    ADT_A43  A43, A44
    ADT_A45  A45
    ADT_A50  A50, A51
    ARD_A19  A19
    ADR_A19  A19
    BAR_P01  P01, P05
    BAR_P02  P02
    BAR_P06  P06
    CRM_C01  C01, C02, C03, C04, C05, C06, C07, C08
    CSU_C09  C09, C10, C11, C12
    DFT_P03  P03
    DOC_T12  T12
    DSR_Q01  Q01
    DSR_Q03  Q03
    EDR_R07  R07
    EQQ_Q04  Q04
    ERP_R09  R09
    MDM_T01  T01, T03, T05, T07, T09, T11
    MDM_T02  T02, T04, T06, T08, T10
    MFD_P09  P09
    MFK_M01  M01, M03, M05, M06, M07, M08, M09, M10, M11
    MFN_M01  M01
    MFN_M02  M02
    MFN_M03  M03
    MFN_M05  M05
    MFN_M06  M06
    MFN_M07  M07
    MFN_M08  M08
    MFN_M09  M09
    MFN_M10  M10
    MFN_M11  M11
    ORF_R02  R02, R04
    ORM_O01  O01
    ORM_Q06  Q06
    ORR_O02  O02
    ORR_Q06  Q06
    ORU_R01  R01
    ORU_W01  W01
    OSQ_Q06  Q06
    OSR_Q06  Q06
    PEX_P07  P07, P08
    PGL_PC6  PC6, PC7, PC8
    PIN_I07  I07
    PPG_PCG  PCC, PCH, PCJ
    PPP_PCB  PCB, PCD
    PPR_PC1  PC1, PC2, PC3
    PPT_PCL  PCL
    PPV_PCA  PCA
    PRR_PC5  PC5
    PTR_PCF  PCF
    QCK_Q02  Q02
    QRY_A19  A19
    QRY_PC4  PC4, PC9, PCE, PCK
    QRY_Q01  Q01
    QRY_Q02  Q02
    QRY_R02  R02, R04
    QRY_T12  T12
    RAR_RAR  RAR
    RAS_O01  O01
    RAS_O02  O022
    RCI_I05  I05
    RCL_I06  I06
    RDE_O01  O01
    RDR_RDR  RDR
    RDS_O01  O01
    REF_I12  I12, I13, I14, I15
    RER_RER  RER
    RGR_RGR  RGR
    RGV_O01  O01
    ROR_ROR  ROR
    RPA_I08  I08, I09. I10, 1II
    RPI_I0I  I01, I04
    RPL_I02  I02
    RPR_I03  I03
    RQA_I08  I08, I09, I10, I11
    RQC_I05  I05
    RQC_I06  I06
    RQI_I0I  I01, I02, I03
    RQP_I04  I04
    RQQ_Q09  Q09
    RRA_O02  O02
    RRD_O02  O02
    RRE_O02  O02
    RRG_O02  O02
    RRI_I12  I12, I13, I14, I15
    SIU_S12  S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S26
    SPQ_Q08  Q08
    SQM_S25  S25
    SQR_S25  S25
    SRM_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
    SRM_T12  T12
    SRR_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
    SRR_T12  T12
    SUR_P09  P09
    TBR_R09  R09
    UDM_Q05  Q05
    VQQ_Q07  Q07
    VXQ_V01  V01
    VXR_V03  V03
    VXU_V04  V04
    VXX_V02  V02
    """

    OMS_O01 = "OMS_O01"
    ORD_O02 = "ORD_O02"
    ORS_O02 = "ORS_O02"
    ACK = "ACK"
    ORN_O02 = "ORN_O02"
    OMN_O01 = "OMN_O01"
    RDO_O01 = "RDO_O01"
    RRO_O02 = "RRO_O02"
    OMD_O01 = "OMD_O01"
    ADT_A01 = "ADT_A01"
    ADT_A02 = "ADT_A02"
    ADT_A03 = "ADT_A03"
    ADT_A06 = "ADT_A06"
    ADT_A09 = "ADT_A09"
    ADT_A12 = "ADT_A12"
    ADT_A16 = "ADT_A16"
    ADT_A17 = "ADT_A17"
    ADT_A18 = "ADT_A18"
    ADT_A20 = "ADT_A20"
    ADT_A24 = "ADT_A24"
    ADT_A28 = "ADT_A28"
    ADT_A30 = "ADT_A30"
    ADT_A37 = "ADT_A37"
    ADT_A38 = "ADT_A38"
    ADT_A39 = "ADT_A39"
    ADT_A43 = "ADT_A43"
    ADT_A45 = "ADT_A45"
    ADT_A50 = "ADT_A50"
    ARD_A19 = "ARD_A19"
    ADR_A19 = "ADR_A19"
    BAR_P01 = "BAR_P01"
    BAR_P02 = "BAR_P02"
    BAR_P06 = "BAR_P06"
    CRM_C01 = "CRM_C01"
    CSU_C09 = "CSU_C09"
    DFT_P03 = "DFT_P03"
    DOC_T12 = "DOC_T12"
    DSR_Q01 = "DSR_Q01"
    DSR_Q03 = "DSR_Q03"
    EDR_R07 = "EDR_R07"
    EQQ_Q04 = "EQQ_Q04"
    ERP_R09 = "ERP_R09"
    MDM_T01 = "MDM_T01"
    MDM_T02 = "MDM_T02"
    MFD_P09 = "MFD_P09"
    MFK_M01 = "MFK_M01"
    MFN_M01 = "MFN_M01"
    MFN_M02 = "MFN_M02"
    MFN_M03 = "MFN_M03"
    MFN_M05 = "MFN_M05"
    MFN_M06 = "MFN_M06"
    MFN_M07 = "MFN_M07"
    MFN_M08 = "MFN_M08"
    MFN_M09 = "MFN_M09"
    MFN_M10 = "MFN_M10"
    MFN_M11 = "MFN_M11"
    ORF_R02 = "ORF_R02"
    ORM_O01 = "ORM_O01"
    ORM_Q06 = "ORM_Q06"
    ORR_O02 = "ORR_O02"
    ORR_Q06 = "ORR_Q06"
    ORU_R01 = "ORU_R01"
    ORU_W01 = "ORU_W01"
    OSQ_Q06 = "OSQ_Q06"
    OSR_Q06 = "OSR_Q06"
    PEX_P07 = "PEX_P07"
    PGL_PC6 = "PGL_PC6"
    PIN_I07 = "PIN_I07"
    PPG_PCG = "PPG_PCG"
    PPP_PCB = "PPP_PCB"
    PPR_PC1 = "PPR_PC1"
    PPT_PCL = "PPT_PCL"
    PPV_PCA = "PPV_PCA"
    PRR_PC5 = "PRR_PC5"
    PTR_PCF = "PTR_PCF"
    QCK_Q02 = "QCK_Q02"
    QRY_A19 = "QRY_A19"
    QRY_PC4 = "QRY_PC4"
    QRY_Q01 = "QRY_Q01"
    QRY_Q02 = "QRY_Q02"
    QRY_R02 = "QRY_R02"
    QRY_T12 = "QRY_T12"
    RAR_RAR = "RAR_RAR"
    RAS_O01 = "RAS_O01"
    RAS_O02 = "RAS_O02"
    RCI_I05 = "RCI_I05"
    RCL_I06 = "RCL_I06"
    RDE_O01 = "RDE_O01"
    RDR_RDR = "RDR_RDR"
    RDS_O01 = "RDS_O01"
    REF_I12 = "REF_I12"
    RER_RER = "RER_RER"
    RGR_RGR = "RGR_RGR"
    RGV_O01 = "RGV_O01"
    ROR_ROR = "ROR_ROR"
    RPA_I08 = "RPA_I08"
    RPI_I0I = "RPI_I0I"
    RPL_I02 = "RPL_I02"
    RPR_I03 = "RPR_I03"
    RQA_I08 = "RQA_I08"
    RQC_I05 = "RQC_I05"
    RQC_I06 = "RQC_I06"
    RQI_I0I = "RQI_I0I"
    RQP_I04 = "RQP_I04"
    RQQ_Q09 = "RQQ_Q09"
    RRA_O02 = "RRA_O02"
    RRD_O02 = "RRD_O02"
    RRE_O02 = "RRE_O02"
    RRG_O02 = "RRG_O02"
    RRI_I12 = "RRI_I12"
    SIU_S12 = "SIU_S12"
    SPQ_Q08 = "SPQ_Q08"
    SQM_S25 = "SQM_S25"
    SQR_S25 = "SQR_S25"
    SRM_S01 = "SRM_S01"
    SRM_T12 = "SRM_T12"
    SRR_S01 = "SRR_S01"
    SRR_T12 = "SRR_T12"
    SUR_P09 = "SUR_P09"
    TBR_R09 = "TBR_R09"
    UDM_Q05 = "UDM_Q05"
    VQQ_Q07 = "VQQ_Q07"
    VXQ_V01 = "VXQ_V01"
    VXR_V03 = "VXR_V03"
    VXU_V04 = "VXU_V04"
    VXX_V02 = "VXX_V02"


class Primarykeyvaluetype(str, Enum):
    """
    0355 - Primary key value type

    PL  Person location
    CE  Coded element
    """

    PL = "PL"
    CE = "CE"


class Alternatecharactersethandlingscheme(str, Enum):
    """
    0356 - Alternate character set handling scheme

    2.3  The character set switching mode specified in HL7 2.3, sections 2.8.28.6.1, and 2.9.2.  Note that the escape
    sequences used in this mode are "HL7 escapes sequences" as defined in HL7 2.3, sec.  2.9, and do not use the
    ASCII "esc" character, ISO 2022-1994  This standard is titled "Information Technology - Character Code Structure
    and Extension Technique". This standard specifies an escape sequence from basic one byte character set to
    specified other character set, and  vice versa.  The escape sequence expl <null>  This is the default,
    indicating that there is no character set switching occurring in this message.
    """

    _2_3 = "2.3"
    ISO_2022_1994 = "ISO 2022-1994"
    _null_ = "<null>"


class Messageerrorconditioncodes(str, Enum):
    """
    0357 - Message error condition  codes

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
    0359 - Diagnosis priority

    0  not included in diagnosis ranking
    1  the primary diagnosis
    2 and higher  for ranked secondary diagnoses
    """

    _0 = "0"
    _1 = "1"
    _2_and_higher = "2 and higher"


class Degree(str, Enum):
    """
    0360 - Degree

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
    BSL  Bachelor of Science  Law
    BT  Bachelor of Theology
    CER  Certificate
    DIP  Diploma
    DBA  Doctor of Business Administration
    DED  Doctor of Education
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
    MSL  Master of Science  Law
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


class Commenttype(str, Enum):
    """
    0364 - Comment type

    PI  Patient Instructions
    AI  Ancillary Instructions,
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


class Applicationchangetype(str, Enum):
    """
    0409 - Application change type

    SU  Start up
    SD  Shut down
    M  Migrates to different CPU
    """

    SU = "SU"
    SD = "SD"
    M = "M"


class Name_addressrepresentation(str, Enum):
    """
    4000 - Name-address representation

    I  Ideographic (i.e., Kanji)
    A  Alphabetic (i.e., Default or some single-byte)
    P  Phonetic (i.e., ASCII, Katakana, Hiragana, etc.)
    """

    I = "I"
    A = "A"
    P = "P"
