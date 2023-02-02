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

    A01  Admit a patient
    A02  Transfer a patient
    A03  Discharge a patient
    A04  Register a patient
    A05  Pre-admit a Patient
    A06  Transfer an outpatient to inpatient
    A07  Transfer an inpatient to outpatient
    A08  Update patient information
    A09  Patient departing
    A10  Patient arriving
    A11  Cancel admit
    A12  Cancel transfer
    A13  Cancel discharge
    A14  Pending admit
    A15  Pending transfer
    A16  Pending discharge
    A17  Swap patients
    A18  Merge patient information
    A19  Patient query
    A20  Bed Status Update
    A21  Leave of absence - out (leaving)
    A22  Leave of absence - in (returning)
    A23  Delete a patient record
    A24  Link patient information
    A25  Cancel pending discharge
    A26  Cancel pending transfer
    A27  Cancel pending admit
    A28  Add person information
    A29  Delete person information
    A30  Merge Patient information
    A31  Update person information
    A32  Cancel patient arriving
    A33  Cancel patient departing
    A34  Merge patient information - patient ID only
    A35  Merge patient information - account number only
    A36  Merge patient information - patient ID and account number
    A37  Unlink patient information
    M01  Master file not otherwise specified (for backwards compatibility only)
    M02  Master file - Staff Practioner
    M03  Master file - test / observation
    O01  Order message
    O02  Order response
    P01  Add and Update Patient Accounts
    P02  Purge Patient Accounts
    P03  Post detail financial transaction
    P04  Generate bill and accounts receivable statements
    Q01  Immediate access
    Q02  Deferred access
    Q03  Deferred response to query
    Q05  Unsolicited display update
    R01  Unsolicited transmission of requested observation
    R02  Query for results of observation
    R03  Display-oriented results (query / unsolicited update)
    R04  Response to query / transmission of requested observation
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
    M01 = "M01"
    M02 = "M02"
    M03 = "M03"
    O01 = "O01"
    O02 = "O02"
    P01 = "P01"
    P02 = "P02"
    P03 = "P03"
    P04 = "P04"
    Q01 = "Q01"
    Q02 = "Q02"
    Q03 = "Q03"
    Q05 = "Q05"
    R01 = "R01"
    R02 = "R02"
    R03 = "R03"
    R04 = "R04"


class PATIENTCLASS(str, Enum):
    """
    004 - PATIENT CLASS

    E  Emergency
    I  Inpatient
    O  Outpatient
    P  Preadmit
    R  Recurring Patient
    B  Obstetrics
    """

    E = "E"
    I = "I"
    O = "O"
    P = "P"
    R = "R"
    B = "B"


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

    AA  Application accept (original mode) / Application acknowledgement: accept (enhanced mode)
    AE  Application error (original mode) / Application acknowledgement: error (enhanced mode)
    AR  Application reject (original mode) / Application acknowledgement: reject (enhanced mode)
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


class AMBULATORYSTATUS(str, Enum):
    """
    009 - AMBULATORY STATUS

    A0  No functional limitations
    A1  Ambulates with assistive device
    A2  Wheelchair / stretcher bound
    A3  Comatose; non-responsive
    A4  Disoriented
    A5  Vision impaired
    A6  Hearing impaired
    A7  Speech impaired
    A8  Nonenglish speaking
    A9  Functional level unknown
    B1  Oxygen Therapy
    B2  Special equipment (tubes, Ivs, catheters)
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
    6  Secretion / Excretion Precautions
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

    S  Stat (do immediately)
    A  As soon as possible (a priority lower than stat)
    R  Routine (default)
    P  Preoperative (to be done prior to surgery)
    T  Timing critical (do as near as possible to requested time)
    """

    S = "S"
    A = "A"
    R = "R"
    P = "P"
    T = "T"


class UNITSOFMEASURE_ISO5281977(str, Enum):
    """
    036 - UNITS OF MEASURE - ISO528 1977

    BT  Bottle
    EA  Each
    GM  Grams
    KG  Kilograms
    LB  Pounds
    MG  Milligrams
    ML  Milliliters
    OZ  Ounces
    SC  Square centimeters
    TB  Tablet
    VL  Vial
    MEQ  Milliequivalent
    """

    BT = "BT"
    EA = "EA"
    GM = "GM"
    KG = "KG"
    LB = "LB"
    MG = "MG"
    ML = "ML"
    OZ = "OZ"
    SC = "SC"
    TB = "TB"
    VL = "VL"
    MEQ = "MEQ"


class ORDERSTATUS(str, Enum):
    """
    038 - ORDER STATUS

    CA  Order was canceled
    CM  Order is completed
    DC  Order was discontinued
    ER  Error - order not found
    HD  Order is on hold
    IP  In process - unspecified
    RP  Order has been replaced
    SC  In process - scheduled
    """

    CA = "CA"
    CM = "CM"
    DC = "DC"
    ER = "ER"
    HD = "HD"
    IP = "IP"
    RP = "RP"
    SC = "SC"


class WHATSUBJECTFILTER(str, Enum):
    """
    048 - WHAT SUBJECT FILTER

    ADV  Advice / diagnosis
    ANU  Nursing unit lookup (returns patients in beds, excluding empty beds)
    APN  Patient name lookup
    APP  Physician lookup
    ARN  Nursing unit lookup (returns patients in beds, including empty beds)
    APM  Medical record number query, returns visits for a medical record number
    APA  Account number query, return matching visit
    CAN  Cancel (used to cancel a query)
    DEM  Demographics
    FIN  Financial
    MRI  Most recent inpatient
    MRO  Most recent outpatient
    NCK  Network clock
    NSC  Network status change
    NST  Network statistic
    ORD  Order
    OTH  Other
    PRO  Procedure
    RES  Result
    RAR  Pharmacy administration information
    RER  Pharmacy encoded order information
    RDR  Pharmacy dispense information
    RGR  Pharmacy give information
    ROR  Pharmacy prescription information
    STA  Status
    MFQ  Master file query
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
    MRI = "MRI"
    MRO = "MRO"
    NCK = "NCK"
    NSC = "NSC"
    NST = "NST"
    ORD = "ORD"
    OTH = "OTH"
    PRO = "PRO"
    RES = "RES"
    RAR = "RAR"
    RER = "RER"
    RDR = "RDR"
    RGR = "RGR"
    ROR = "ROR"
    STA = "STA"
    MFQ = "MFQ"


class DIAGNOSISCODINGMETHOD(str, Enum):
    """
    053 - DIAGNOSIS CODING METHOD

    I9  ICD9
    """

    I9 = "I9"


class CHECKDIGITSCHEME(str, Enum):
    """
    061 - CHECK DIGIT SCHEME

    M10  Mod 10 algorithm
    M11  Mod 11 algorithm
    """

    M10 = "M10"
    M11 = "M11"


class EVENTREASON(str, Enum):
    """
    062 - EVENT REASON

    01  Patient request
    02  Physician order
    03  Census management
    """

    _01 = "01"
    _02 = "02"
    _03 = "03"


class ACTIONCODE(str, Enum):
    """
    065 - ACTION CODE

    A  Add ordered tests to the existing specimen
    G  Generated order / reflex order
    L  Lab to obtain specimen from patient
    O  Specimen obtained by service other than Lab
    P  Pending specimen - order sent prior to delivery
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


class SOURCEOFSPECIMEN(str, Enum):
    """
    070 - SOURCE OF SPECIMEN

    ABS  Abcess
    AMN  Amniotic fluid
    ASP  Aspirate
    BPH  Basophils
    ABLD  Arterial blood
    BBL  Blood bag
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
    DRN  Drain
    EAR  Ear
    ELT  Electrode
    ENDC  Endocardium
    ENDM  Endometrium
    EOS  Eosinophils
    RBC  Erythrocytes
    FIB  Fibroblasts
    FLT  Filter
    FIST  Fistula
    FLU  Body fluid, unsp
    GAST  Gastric fluid/contents
    GEN  Genital
    GENC  Genital cervix
    GENL  Genital lochia
    GENV  Genital vaginal
    HAR  Hair
    IT  Intubation tube
    LAM  Lamella
    WBC  Leukocytes
    LN  Line
    LNA  Line arterial
    LNV  Line venous
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
    PRT  Peritoneal fluid / ascites
    PER  Peritoneum
    PLC  Placenta
    PLAS  Plasma
    PLB  Plasma bag
    PLR  Pleural fluid (thoracentesis fld)
    PMN  Polymorphonuclear neutrophils
    PUS  Pus
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
    STL  Stool
    SWT  Sweat
    SNV  Synovial fluid (Joint fluid)
    TEAR  Tears
    THRT  Throat
    THRB  Thrombocyte (platelet)
    TISS  Tissue
    TISB  Tissue bone marrow
    TISG  Tissue gall bladder
    TISL  Tissue lung
    TISP  Tissue peritoneum
    TISU  Tissue ulcer
    TISC  Tissue curettage
    TISPL  Tissue placenta
    ULC  Ulcer
    UMB  Umbilical Blood
    URTH  Urethra
    UR  Urine
    URC  Urine clean catch
    URT  Urine catheter
    VOM  Vomitus
    BLD  Whole blood
    BDY  Whole body
    WICK  Wick
    WND  Wound
    WNDA  Wound abscess
    WNDE  Wound exudate
    WNDD  Wound drainage
    """

    ABS = "ABS"
    AMN = "AMN"
    ASP = "ASP"
    BPH = "BPH"
    ABLD = "ABLD"
    BBL = "BBL"
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
    DRN = "DRN"
    EAR = "EAR"
    ELT = "ELT"
    ENDC = "ENDC"
    ENDM = "ENDM"
    EOS = "EOS"
    RBC = "RBC"
    FIB = "FIB"
    FLT = "FLT"
    FIST = "FIST"
    FLU = "FLU"
    GAST = "GAST"
    GEN = "GEN"
    GENC = "GENC"
    GENL = "GENL"
    GENV = "GENV"
    HAR = "HAR"
    IT = "IT"
    LAM = "LAM"
    WBC = "WBC"
    LN = "LN"
    LNA = "LNA"
    LNV = "LNV"
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
    PRT = "PRT"
    PER = "PER"
    PLC = "PLC"
    PLAS = "PLAS"
    PLB = "PLB"
    PLR = "PLR"
    PMN = "PMN"
    PUS = "PUS"
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
    TISB = "TISB"
    TISG = "TISG"
    TISL = "TISL"
    TISP = "TISP"
    TISU = "TISU"
    TISC = "TISC"
    TISPL = "TISPL"
    ULC = "ULC"
    UMB = "UMB"
    URTH = "URTH"
    UR = "UR"
    URC = "URC"
    URT = "URT"
    VOM = "VOM"
    BLD = "BLD"
    BDY = "BDY"
    WICK = "WICK"
    WND = "WND"
    WNDA = "WNDA"
    WNDE = "WNDE"
    WNDD = "WNDD"


class DIAGNOSTICSERVICESECTIONID(str, Enum):
    """
    074 - DIAGNOSTIC SERVICE SECTION ID

    AU  Audiology
    BG  Blood gases
    BLB  Blood bank
    CUS  Cardiac Ultrasound
    CTH  Cardiac catheterization
    CT  CAT scan
    CH  Chemistry
    CP  Cytopathology
    EC  Electrocardiac (e.g., EKG, EEC, Holter)
    EN  Electroneuro (EEG, EMG)
    HM  Hematology
    IMM  Immunology
    MB  Microbiology
    MCB  Mycobacteriology
    MYC  Mycology
    NMS  Nuclear medicine scan
    NMR  Nuclear magnetic resonance
    NRS  Nursing service measures
    OUS  OB Ultrasound
    OT  Occupational therapy
    OTH  Other
    OSL  Outside Lab
    PHR  Pharmacy
    PT  Physical therapy
    PHY  Physician (Hx, Dx, admission note, etc.)
    PF  Pulmonary function
    RX  Radiograph
    RUS  Radiology ultrasound
    RC  Respiratory care (therapy)
    RT  Radiation therapy
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
    IMM = "IMM"
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


class MESSAGETYPE(str, Enum):
    """
    076 - MESSAGE TYPE

    ACK  General acknowledgement message
    ADT  ADT message
    ARD  Ancillary report (display)
    BAR  Add / change billing account
    DFT  Detail financial transaction
    DSR  Display response
    MCF  Delayed acknowledgement
    ORF  Observational result (record response)
    ORM  Order message
    ORR  Order acknowledgement message
    ORU  Observational result (unsolicited)
    OSQ  Order status query
    RAR  Pharmacy administration information
    RAS  Pharmacy administration message
    RDE  Pharmacy encoded order message
    RDR  Pharmacy dispense information
    RDS  Pharmacy dispense message
    RGV  Pharmacy give message
    RGR  Pharmacy dose information
    RER  Pharmacy encoded order information
    ROR  Pharmacy prescription order response
    RRA  Pharmacy administration acknowledgment
    RRD  Pharmacy dispense acknowledgment
    RRE  Pharmacy encoded order acknowledgment
    RRG  Pharmacy give acknowledgment
    QRY  Query
    UDM  Unsolicited display message
    ADR  ADT response
    MFN  Master files notification
    MFK  Master file application acknowledgement
    MFD  Master files delayed application acknowledgement
    MFR  Master files response
    NMQ  Network management query
    NMR  Network management response
    NMD  Network management data
    """

    ACK = "ACK"
    ADT = "ADT"
    ARD = "ARD"
    BAR = "BAR"
    DFT = "DFT"
    DSR = "DSR"
    MCF = "MCF"
    ORF = "ORF"
    ORM = "ORM"
    ORR = "ORR"
    ORU = "ORU"
    OSQ = "OSQ"
    RAR = "RAR"
    RAS = "RAS"
    RDE = "RDE"
    RDR = "RDR"
    RDS = "RDS"
    RGV = "RGV"
    RGR = "RGR"
    RER = "RER"
    ROR = "ROR"
    RRA = "RRA"
    RRD = "RRD"
    RRE = "RRE"
    RRG = "RRG"
    QRY = "QRY"
    UDM = "UDM"
    ADR = "ADR"
    MFN = "MFN"
    MFK = "MFK"
    MFD = "MFD"
    MFR = "MFR"
    NMQ = "NMQ"
    NMR = "NMR"
    NMD = "NMD"


class ABNORMALFLAGS(str, Enum):
    """
    078 - ABNORMAL FLAGS

    L  Below low normal
    H  Above high normal
    LL  Below lower panic limits
    HH  Above upper panic limits
    <  Below absolute low-off instrument scale
    >  Above absolute high-off instrument scale
    N  Normal (applies to non-numeric results)
    A  Abnormal (applies to non-numeric results)
    AA  Very abnormal (applies to non-numeric units, analogous to panic limits for numerics limits)
    null  No range defined, or normal ranges don't apply
    U  Significant change up
    D  Significant change down
    B  Better (use when direction not relevant)
    W  Worse (use when direction not relevant)
    S  Sensitive
    R  Resistant
    I  Intermediate
    MS  Moderately sensitive
    VS  Very sensitive
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


class NATUREOFABNORMALTESTING(str, Enum):
    """
    080 - NATURE OF ABNORMAL TESTING

    A  An age-based population
    N  None - generic normal range
    R  A race-based population
    S  A sex-based population
    """

    A = "A"
    N = "N"
    R = "R"
    S = "S"


class OBSERVATIONRESULTSTATUSCODESINTERPRETATION(str, Enum):
    """
    085 - OBSERVATION RESULT STATUS CODES INTERPRETATION

    C  Record coming over is a correction and thus replaces a result
    D  Deletes the OBX record
    F  Final results (can only be changed with a corrected result)
    I  Specimen in lab - results pending
    P  Preliminary results
    R  Results entered - not verified
    S  Partial results
    X  Results cannot be obtained for this observation
    U  Results status change to Final - results did not change ( don't transmit test)
    """

    C = "C"
    D = "D"
    F = "F"
    I = "I"
    P = "P"
    R = "R"
    S = "S"
    X = "X"
    U = "U"


class QUERYPRIORITY(str, Enum):
    """
    091 - QUERY PRIORITY

    D  Deferred
    I  Immediate
    """

    D = "D"
    I = "I"


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

    D  On discharge
    O  On receipt of order
    R  At time service is completed
    S  At time service is started
    T  At a designated date / time
    """

    D = "D"
    O = "O"
    R = "R"
    S = "S"
    T = "T"


class DELAYEDACKNOWLEDGMENTTYPE(str, Enum):
    """
    102 - DELAYED ACKNOWLEDGMENT TYPE

    D  Message Received, stored for later processing
    F  Acknowledgement after processing
    """

    D = "D"
    F = "F"


class PROCESSINGID(str, Enum):
    """
    103 - PROCESSING ID

    D  Debugging
    P  Production
    T  Training
    """

    D = "D"
    P = "P"
    T = "T"


class VERSIONID(str, Enum):
    """
    104 - VERSION ID

    2.0  Version 2.0, September 1988
    2.0D  Demo    2.0  October 1988
    2.1  Release 2.1  March 1990
    2.2  Release 2.2  December 1994
    """

    _2_0 = "2.0"
    _2_0D = "2.0D"
    _2_1 = "2.1"
    _2_2 = "2.2"


class SOURCEOFCOMMENT(str, Enum):
    """
    105 - SOURCE OF COMMENT

    L  Ancillary (filler) department is source of comment
    P  Orderer (placer) is source of comment
    O  Other system is source of comment
    """

    L = "L"
    P = "P"
    O = "O"


class QUERYFORMATCODE(str, Enum):
    """
    106 - QUERY FORMAT CODE

    D  Response is in display format
    R  Response is in record-oriented format
    """

    D = "D"
    R = "R"


class DEFERREDRESPONSETYPE(str, Enum):
    """
    107 - DEFERRED RESPONSE TYPE

    B  Before the date / time specified
    L  Later than the date / time specified
    """

    B = "B"
    L = "L"


class QUERYRESULTSLEVEL(str, Enum):
    """
    108 - QUERY RESULTS LEVEL

    O  Order plus order status
    R  Results without bulk text
    S  Status only
    T  Full results
    """

    O = "O"
    R = "R"
    S = "S"
    T = "T"


class REPORTPRIORITY(str, Enum):
    """
    109 - REPORT PRIORITY

    R  Routine
    S  Stat
    """

    R = "R"
    S = "S"


class BEDSTATUS(str, Enum):
    """
    116 - BED STATUS

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


class ORDERCONTROL(str, Enum):
    """
    119 - ORDER CONTROL

    NW  New Order
    OK  Order accepted and OK
    CA  Cancel order request
    OC  Order canceled
    CR  Canceled as requested
    UC  Unable to cancel
    DC  Discontinue order request
    OD  Order discontinued
    DR  Discontinued as requested
    UD  Unable to discontinue
    HD  Hold order request
    OH  Order held
    UH  Unable to put on hold
    HR  On hold as requested
    RL  Release previous hold
    OR  Released as requested
    UR  Unable to release
    RP  Order replace request
    RU  Replaced unsolicited
    RO  Replacement order
    RQ  Replaced as requested
    UM  Unable to replace
    PA  Parent order
    CH  Child order
    XO  Change order request
    XX  Order changed, unsolicited
    UX  Unable to change
    XR  Changed as requested
    DE  Data Errors
    RE  Observations to follow
    RR  Request received
    SR  Response to send order status request
    SS  Send order status request
    SC  Status changed
    SN  Send order number
    NA  Number assigned
    CN  Combined result
    """

    NW = "NW"
    OK = "OK"
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


class RESPONSEFLAG(str, Enum):
    """
    121 - RESPONSE FLAG

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


class CHARGETYPE(str, Enum):
    """
    122 - CHARGE TYPE

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


class RESULTSTATUS_OBR(str, Enum):
    """
    123 - RESULT STATUS - OBR

    O  Order received; specimen not yet received
    I  Specimen in lab, not yet processed.
    S  No results available; procedure scheduled, but not done
    P  Preliminary: A verified early result is available, final results not yet obtained
    C  Correction to results
    R  Results stored; not yet verified
    F  Final results - results stored & verified
    X  No results available; Order canceled.
    Y  No order on record for this test.  (Used only on queries)
    Z  No record of this patient. (Used only on queries)
    """

    O = "O"
    I = "I"
    S = "S"
    P = "P"
    C = "C"
    R = "R"
    F = "F"
    X = "X"
    Y = "Y"
    Z = "Z"


class TRANSPORTATIONMODE(str, Enum):
    """
    124 - TRANSPORTATION MODE

    CART  Cart - patient travels on cart or gurney
    PORT  The examining device goes to patient's location
    WALK  Patient walks to diagnostic service
    WHLC  Wheelchair
    """

    CART = "CART"
    PORT = "PORT"
    WALK = "WALK"
    WHLC = "WHLC"


class VALUETYPE(str, Enum):
    """
    125 - VALUE TYPE

    ST  String data
    TX  Text data (display)
    FT  Formatted text (display)
    DT  Date
    TM  Time
    TS  Time stamp ( date & time)
    PN  Person name
    TN  Telephone number
    AD  Address
    CK  Composite ID with check digit
    CN  Composite ID and name
    CE  Coded element
    RP  Reference pointer
    NM  Numeric
    TQ  Timing / quantity
    ID  Coded value
    SI  Sequence ID
    CM  Composite
    CQ  Composite quantity with units
    CF  Coded element with formatted values
    MO  Money
    """

    ST = "ST"
    TX = "TX"
    FT = "FT"
    DT = "DT"
    TM = "TM"
    TS = "TS"
    PN = "PN"
    TN = "TN"
    AD = "AD"
    CK = "CK"
    CN = "CN"
    CE = "CE"
    RP = "RP"
    NM = "NM"
    TQ = "TQ"
    ID = "ID"
    SI = "SI"
    CM = "CM"
    CQ = "CQ"
    CF = "CF"
    MO = "MO"


class QUANTITYLIMITEDREQUEST(str, Enum):
    """
    126 - QUANTITY LIMITED REQUEST

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


class ALLERGYTYPE(str, Enum):
    """
    127 - ALLERGY TYPE

    DA  Drug Allergy
    FA  Food Allergy
    MA  Miscellaneous Allergy
    MC  Miscellaneous Contraindication
    """

    DA = "DA"
    FA = "FA"
    MA = "MA"
    MC = "MC"


class ALLERGYSEVERITY(str, Enum):
    """
    128 - ALLERGY SEVERITY

    SV  Severe
    MO  Moderate
    MI  Mild
    """

    SV = "SV"
    MO = "MO"
    MI = "MI"


class PROCEDUREPRACTITIONERTYPE(str, Enum):
    """
    133 - PROCEDURE PRACTITIONER TYPE

    AN  Anesthesiologist
    PR  Procedure MD (surgeon)
    RD  Radiologist
    RS  Resident
    NP  Nurse Practitioner
    CM  Certified Nurse Midwife
    """

    AN = "AN"
    PR = "PR"
    RD = "RD"
    RS = "RS"
    NP = "NP"
    CM = "CM"


class ASSIGNMENTOFBENEFITS(str, Enum):
    """
    135 - ASSIGNMENT OF BENEFITS

    Y  Yes
    N  No
    M  Modified assignment
    """

    Y = "Y"
    N = "N"
    M = "M"


class Y_NIndicator(str, Enum):
    """
    136 - Y-N Indicator

    Y  Yes
    N  No
    """

    Y = "Y"
    N = "N"


class MAILCLAIMPARTY(str, Enum):
    """
    137 - MAIL CLAIM PARTY

    E  Employer
    G  Guarantor
    I  Insurance Company
    O  Other
    P  Patient
    """

    E = "E"
    G = "G"
    I = "I"
    O = "O"
    P = "P"


class ELIGIBILITYSOURCE(str, Enum):
    """
    144 - ELIGIBILITY SOURCE

    1  Insurance Company
    2  Employer
    3  Insured Presented Policy
    4  Insured Presented Card
    5  Signed Statement on File
    6  Verbal Information
    7  None
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"


class RoomType(str, Enum):
    """
    145 - Room Type

    PRI  Private Room
    2PRI  Second Private Room
    SPR  Semi-private Room
    2SPR  Second Semi-private Room
    ICU  Intensive Care Unit
    2ICU  Second Intensive Care Unit
    """

    PRI = "PRI"
    _2PRI = "2PRI"
    SPR = "SPR"
    _2SPR = "2SPR"
    ICU = "ICU"
    _2ICU = "2ICU"


class AMOUNTTYPE(str, Enum):
    """
    146 - AMOUNT TYPE

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


class POLICYTYPE(str, Enum):
    """
    147 - POLICY TYPE

    ANC  Ancillary
    2ANC  Second Ancillary
    MMD  Major Medical
    2MMD  Second Major Medical
    3MMD  Third Major Medical
    """

    ANC = "ANC"
    _2ANC = "2ANC"
    MMD = "MMD"
    _2MMD = "2MMD"
    _3MMD = "3MMD"


class PENALTYTYPE(str, Enum):
    """
    148 - PENALTY TYPE

    AT  Currency Amount
    PC  Percentage
    """

    AT = "AT"
    PC = "PC"


class DAYTYPE(str, Enum):
    """
    149 - DAY TYPE

    AP  Approved
    DE  Denied
    PE  Pending
    """

    AP = "AP"
    DE = "DE"
    PE = "PE"


class PRECERTIFICATIONPATIENTTYPE(str, Enum):
    """
    150 - PRECERTIFICATION PATIENT TYPE

    ER  Emergency
    IPE  Inpatient elective
    OPE  Outpatient elective
    UR  Urgent
    """

    ER = "ER"
    IPE = "IPE"
    OPE = "OPE"
    UR = "UR"


class ACCEPT_APPLICATIONACKNOWLEDGEMENTCONDITIONS(str, Enum):
    """
    155 - ACCEPT-APPLICATION ACKNOWLEDGEMENT CONDITIONS

    AL  Always
    NE  Never
    ER  Error / reject conditions only
    SU  Successful completion only
    """

    AL = "AL"
    NE = "NE"
    ER = "ER"
    SU = "SU"


class DATE_TIMEQUALIFIER(str, Enum):
    """
    156 - DATE-TIME QUALIFIER

    ORD  Order date / time
    CAN  Cancellation date / time
    SCHED  Schedule date / time
    COL  Collection date / time (equivalent to film or sample collection date / time)
    RCT  Specimen receipt date / time (receipt of specimen in filling ancillary (lab))
    REP  Report date / time (report date / time at filling ancillary (i.e., lab))
    ANY  Any date / time within a range
    """

    ORD = "ORD"
    CAN = "CAN"
    SCHED = "SCHED"
    COL = "COL"
    RCT = "RCT"
    REP = "REP"
    ANY = "ANY"


class WHIHCDATE_TIMESTATUSQUALIFIER(str, Enum):
    """
    157 - WHIHC DATE-TIME STATUS QUALIFIER

    PRE  Preliminary
    REP  Report completion date / time
    CFN  Current final value (whether final or corrected)
    FIN  Final only (no corrections)
    COR  Corrected only (no final with corrections)
    ANY  Any status
    """

    PRE = "PRE"
    REP = "REP"
    CFN = "CFN"
    FIN = "FIN"
    COR = "COR"
    ANY = "ANY"


class DATE_TIMESELECTIONQUALIFIER(str, Enum):
    """
    158 - DATE-TIME SELECTION QUALIFIER

    1ST  First value within range
    ALL  All values within the range
    LST  Last value within the range
    REV  All values within the range returned in reverse chronological order
    """

    _1ST = "1ST"
    ALL = "ALL"
    LST = "LST"
    REV = "REV"


class DIETTYPE(str, Enum):
    """
    159 - DIET TYPE

    D  Diet
    S  Supplement
    P  Preference
    """

    D = "D"
    S = "S"
    P = "P"


class TRAYTYPE(str, Enum):
    """
    160 - TRAY TYPE

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


class ALLOWSUBSTITUTION(str, Enum):
    """
    161 - ALLOW SUBSTITUTION

    N  Substitutions are not authorized
    G  Allow generic substitutions
    T  Allow therapeutic substitutions
    """

    N = "N"
    G = "G"
    T = "T"


class ROUTEOFADMINISTRATION(str, Enum):
    """
    162 - ROUTE OF ADMINISTRATION

    AP  Apply Externally
    B  Buccal
    DT  Dental
    GTT  Gastronomy Tube
    GU  GU Irrigant
    IA  Intra-arterial
    IC  Intracardiac
    ID  Intradermal
    IH  Inhalation
    IM  Intramuscular
    IN  Intranasal
    IO  Intraocular
    IP  Intraperitoneal
    IS  Intrasynovial
    IT  Intrathecal
    IV  Intravenous
    NS  Nasal
    NG  Nasogastric
    OP  Ophthalmic
    OT  Otic
    PO  Oral
    PR  Rectal
    SC  Subcutaneous
    SL  Sublingual
    TP  Topical
    TD  Transdermal
    TL  Translingual
    UR  Urethral
    VG  Vaginal
    """

    AP = "AP"
    B = "B"
    DT = "DT"
    GTT = "GTT"
    GU = "GU"
    IA = "IA"
    IC = "IC"
    ID = "ID"
    IH = "IH"
    IM = "IM"
    IN = "IN"
    IO = "IO"
    IP = "IP"
    IS = "IS"
    IT = "IT"
    IV = "IV"
    NS = "NS"
    NG = "NG"
    OP = "OP"
    OT = "OT"
    PO = "PO"
    PR = "PR"
    SC = "SC"
    SL = "SL"
    TP = "TP"
    TD = "TD"
    TL = "TL"
    UR = "UR"
    VG = "VG"


class ADMINISTRIVESITE(str, Enum):
    """
    163 - ADMINISTRIVE SITE

    BE  Bilateral Ears
    OU  Bilateral Eyes
    BN  Bilateral Nares
    BU  Buttock
    CT  Tubus
    LA  Left arm
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


class ADMINISTRATIONDEVICE(str, Enum):
    """
    164 - ADMINISTRATION DEVICE

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


class ADMINISTRATIONMETHOD(str, Enum):
    """
    165 - ADMINISTRATION METHOD

    CH  Chew
    DI  Dissolve
    DU  Dust
    IF  Inflitrate
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


class RXCOMPONENTTYPE(str, Enum):
    """
    166 - RX COMPONENT TYPE

    B  Base
    A  Additive
    """

    B = "B"
    A = "A"


class SUBSTITUTIONSTATUS(str, Enum):
    """
    167 - SUBSTITUTION STATUS

    N  No substitute was dispensed
    G  A generic substitution was dispensed
    T  A therapeutic substitution was dispensed
    """

    N = "N"
    G = "G"
    T = "T"


class PROCESSINGPRIORITY(str, Enum):
    """
    168 - PROCESSING PRIORITY

    S  Stat (do immediately)
    A  As soon as possible (a priority lower than stat)
    R  Routine
    P  Preoperative (to be done prior to surgery)
    T  Timing critical (do as near as possible to requested time)
    C  Measure continously (e.g., arterial line blood pressure)
    B  Do at bedside or portable (may be used with other codes)
    """

    S = "S"
    A = "A"
    R = "R"
    P = "P"
    T = "T"
    C = "C"
    B = "B"


class REPORTINPRIORITY(str, Enum):
    """
    169 - REPORTIN PRIORITY

    C  Call back results
    R  Rush reporting
    """

    C = "C"
    R = "R"


class DERIVEDSPECIMEN(str, Enum):
    """
    170 - DERIVED SPECIMEN

    P  Parent observation
    C  Child observation
    N  Not applicable
    """

    P = "P"
    C = "C"
    N = "N"


class COORDINATIONOFBENEFITS(str, Enum):
    """
    173 - COORDINATION OF BENEFITS

    CO  Coordination
    IN  Independent
    """

    CO = "CO"
    IN = "IN"


class NATUREOFTEST_OBSERVATION(str, Enum):
    """
    174 - NATURE OF TEST-OBSERVATION

    P  Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen
    F  Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatine clearance), usually done at different times and/or on different specimens
    A  Atomic test/observation (test code or treatment code)
    S  Superset--a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes)
    C  Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar--arterial ratio, cardiac output)
    """

    P = "P"
    F = "F"
    A = "A"
    S = "S"
    C = "C"


class MASTERFILEIDENTIFIERCODE(str, Enum):
    """
    175 - MASTER FILE IDENTIFIER CODE

    CDM  Charge description master file (see chapter 6, appendix)
    STF  Staff master file (see chapter 8, Appendix)
    PRA  Practitioner master file (see chapter 8, appendix)
    OM1  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    OM2  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    OM3  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    OM4  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    OM5  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    OM6  Observation text master file (i.e., Lab) (see Chapter 7, Appendix)
    """

    CDM = "CDM"
    STF = "STF"
    PRA = "PRA"
    OM1 = "OM1"
    OM2 = "OM2"
    OM3 = "OM3"
    OM4 = "OM4"
    OM5 = "OM5"
    OM6 = "OM6"


class CONFIDENTIALITYCODE(str, Enum):
    """
    177 - CONFIDENTIALITY CODE

    V  Very restricted
    R  Restricted
    U  Usual control
    EMP  Employee
    UWM  Unwed mother
    VIP  Very important person or celebrity
    PSY  Psychiatric patient
    AID  AIDS patient
    HIV  HIV(+) patient
    ETH  Alcohol / drug treatment patient
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


class FILE_LEVELEVENTCODE(str, Enum):
    """
    178 - FILE-LEVEL EVENT CODE

    REP  Replace current version of this master file with the version contained in this message
    UPD  Change file records as defined in the record level event codes for each record that follows
    """

    REP = "REP"
    UPD = "UPD"


class ResponseLevel(str, Enum):
    """
    179 - Response Level

    NE  Never. no application level response needed
    ER  Error/Reject conditions only. Only MFA segments denoting errors must be returned via the application level acknowledgement for this message
    AL  Always. All MFA segments (whether denoting errors or not) must be returned via the application level acknowledgement message
    SU  Success. Only MFA segments denoting success must be returned via the application level acknowledgement for this message
    """

    NE = "NE"
    ER = "ER"
    AL = "AL"
    SU = "SU"


class REcordLevelEventCode(str, Enum):
    """
    180 - REcord Level Event Code

    MAD  Add record to master file
    MDL  Delete record from master file
    MUP  Update record for master file
    MDC  Deactivate - discontinue using record in master file, but do not delete from database
    MAC  Reactivate deactivated record
    """

    MAD = "MAD"
    MDL = "MDL"
    MUP = "MUP"
    MDC = "MDC"
    MAC = "MAC"


class MFNRecode_LevelErrorReturn(str, Enum):
    """
    181 - MFN Recode-Level Error Return

    S  Successful posting of the record defined by the MFE segment
    U  Unsuccessful posting of the record defined by the MFE segment
    """

    S = "S"
    U = "U"


class Active_Inactive(str, Enum):
    """
    183 - Active-Inactive

    A  Active staff
    I  Inactive staff
    """

    A = "A"
    I = "I"


class PreferredMethodOfContrct(str, Enum):
    """
    185 - Preferred Method Of Contrct

    H  Home phone number
    O  Office phone number
    F  Fax number
    C  Cellular phone number
    B  Beeper number
    E  E-mail address (not in TN format)
    """

    H = "H"
    O = "O"
    F = "F"
    C = "C"
    B = "B"
    E = "E"


class Providerbilling(str, Enum):
    """
    187 - Provider billing

    P  Provider does own billing
    I  Institution bills for provider
    """

    P = "P"
    I = "I"


class AdressType(str, Enum):
    """
    190 - Adress Type

    C  Current or Temporary
    P  Permanent
    M  Mailing
    B  Business
    O  Office
    H  Home
    """

    C = "C"
    P = "P"
    M = "M"
    B = "B"
    O = "O"
    H = "H"


class TypeOfData(str, Enum):
    """
    191 - Type Of Data

    SI  Scanned Image
    NS  Non-scanned Image
    SD  Scanned Document
    TX  Machine Readable Text Document
    FT  Formatted Text
    """

    SI = "SI"
    NS = "NS"
    SD = "SD"
    TX = "TX"
    FT = "FT"


class AmountClass(str, Enum):
    """
    193 - Amount Class

    AT  Amount
    LM  Limit
    PC  Percentage
    UL  Unlimited
    """

    AT = "AT"
    LM = "LM"
    PC = "PC"
    UL = "UL"
