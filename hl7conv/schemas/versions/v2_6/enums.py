from enum import Enum


class AdministrativeSex(str, Enum):
    """
    001 - Administrative Sex

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


class MaritalStatus(str, Enum):
    """
    002 - Marital Status

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
    A60  ADT/ACK - Update allergy information
    A61  ADT/ACK - Change consulting doctor
    A62  ADT/ACK - Cancel change consulting doctor
    B01  PMU/ACK - Add personnel record
    B02  PMU/ACK - Update personnel record
    B03  PMU/ACK - Delete personnel re cord
    B04  PMU/ACK - Active practicing person
    B05  PMU/ACK - Deactivate practicing person
    B06  PMU/ACK - Terminate practicing person
    B07  PMU/ACK - Grant Certificate/Permission
    B08  PMU/ACK - Revoke Certificate/Permission
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
    CNQ  Cancel Query
    E01  Submit HealthCare Services Invoice
    E02  Cancel HealthCare Services Invoice
    E03  HealthCare Services Invoice Status
    E04  Re-Assess HealthCare Services Invoice Request
    E10  Edit/Adjudication Results
    E12  Request Additional Information
    E13  Additional Information Response
    E15  Payment/Remittance Advice
    E20  Submit Authorization Request
    E21  Cancel Authorization Request
    E22  Authorization Request Status
    E24  Authorization Response
    E30  Submit Health Document related to Authorization Request
    E31  Cancel Health Document related to Authorization Request
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
    K11  RSP - Segment pattern response in response to QBP^Q11
    K13  RTB - Tabular response in response to QBP^Q13
    K15  RDY - Display response in response to QBP^Q15
    K21  RSP - Get person demographics response
    K22  RSP - Find candidates response
    K23  RSP - Get corresponding identifiers response
    K24  RSP - Allocate identifiers response
    K25  RSP - Personnel Information by Segment Response
    K31  RSP -Dispense History Response
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
    M13  MFN/MFK - Master file notification - general
    M14  MFN/MFK - Master file notification - site defined
    M15  MFN/MFK - Inventory item master file notification
    M16  MFN/MFK - Master File Notification Inventory Item Enhanced
    M17  DRG Master File Message
    N01  NMQ/NMR - Application management query message
    N02  NMD/ACK - Application management data message (unsolicited)
    O01  ORM - Order message (also RDE, RDS, RGV, RAS)
    O02  ORR - Order response (also RRE, RRD, RRG, RRA)
    O03  OMD - Diet order
    O04  ORD - Diet order acknowledgment
    O05  OMS - Stock requisition order
    O06  ORS - Stock requisition acknowledgment
    O07  OMN - Non-stock requisition order
    O08  ORN - Non-stock requisition acknowledgment
    O09  OMP - Pharmacy/treatment order
    O10  ORP - Pharmacy/treatment order acknowledgment
    O11  RDE - Pharmacy/treatment encoded order
    O12  RRE - Pharmacy/treatment encoded order acknowledgment
    O13  RDS - Pharmacy/treatment dispense
    O14  RRD - Pharmacy/treatment dispense acknowledgment
    O15  RGV - Pharmacy/treatment give
    O16  RRG - Pharmacy/treatment give acknowledgment
    O17  RAS - Pharmacy/treatment administration
    O18  RRA - Pharmacy/treatment administration acknowledgment
    O19  OMG - General clinical order
    O20  ORG/ORL - General clinical order response
    O21  OML - Laboratory order
    O22  ORL - General laboratory order response message to any OML
    O23  OMI - Imaging order
    O24  ORI - Imaging order response message to any OMI
    O25  RDE - Pharmacy/treatment refill authorization request
    O26  RRE - Pharmacy/Treatment Refill Authorization Acknowledgement
    O27  OMB - Blood product order
    O28  ORB - Blood product order acknowledgment
    O29  BPS - Blood product dispense status
    O30  BRP - Blood product dispense status acknowledgment
    O31  BTS - Blood product transfusion/disposition
    O32  BRT - Blood product transfusion/disposition acknowledgment
    O33  OML - Laboratory order for multiple orders related to a single specimen
    O34  ORL - Laboratory order response message to a multiple order related to single specimen OML
    O35  OML - Laboratory order for multiple orders related to a single container of a specimen
    O36  ORL - Laboratory order response message to a single container of a specimen OML
    O37  OPL - Population/Location-Based Laboratory Order Message
    O38  OPR - Population/Location-Based Laboratory Order Acknowledgment Message
    P01  BAR/ACK - Add patient accounts
    P02  BAR/ACK - Purge patient accounts
    P03  DFT/ACK - Post detail financial transaction
    P04  QRY/DSP - Generate bill and A/R statements
    P05  BAR/ACK - Update account
    P06  BAR/ACK - End account
    P07  PEX - Unsolicited initial individual product experience report
    P08  PEX - Unsolicited update individual product experience report
    P09  SUR - Summary product experience report
    P10  BAR/ACK -Transmit Ambulatory Payment  Classification(APC)
    P11  DFT/ACK - Post Detail Financial Transactions - New
    P12  BAR/ACK - Update Diagnosis/Procedure
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
    Q05  UDM/ACK - Unsolicited display update message
    Q06  OSQ/OSR - Query for order status
    Q11  QBP - Query by parameter requesting an RSP segment pattern response
    Q13  QBP - Query by parameter requesting an  RTB - tabular response
    Q15  QBP - Query by parameter requesting an RDY display response
    Q16  QSB - Create subscription
    Q17  QVR - Query for previous events
    Q21  QBP - Get person demographics
    Q22  QBP - Find candidates
    Q23  QBP - Get corresponding identifiers
    Q24  QBP - Allocate identifiers
    Q25  QBP - Personnel Information by Segment Query
    Q26  ROR - Pharmacy/treatment order response
    Q27  RAR - Pharmacy/treatment administration information
    Q28  RDR - Pharmacy/treatment dispense information
    Q29  RER - Pharmacy/treatment encoded order information
    Q30  RGR - Pharmacy/treatment dose information
    Q31  QBP Query Dispense history
    R01  ORU/ACK - Unsolicited transmission of an observation message
    R02  QRY - Query for results of observation
    R04  ORF - Response to query; transmission of requested observation
    ROR  ROR - Pharmacy prescription order query response
    R21  OUL - Unsolicited laboratory observation
    R22  OUL - Unsolicited Specimen Oriented Observation Message
    R23  OUL - Unsolicited Specimen Container Oriented Observation Message
    R24  OUL - Unsolicited Order Oriented Observation Message
    R25  OPU - Unsolicited Population/Location-Based Laboratory Observation Message
    R30  ORU - Unsolicited Point-Of-Care Observation Message Without Existing Order - Place An Order
    R31  ORU - Unsolicited New Point-Of-Care Observation Message - Search For An Order
    R32  ORU - Unsolicited Pre-Ordered Point-Of-Care Observation
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
    S28  SLR/SLS - Request new sterilization lot
    S29  SLR/SLS - Request Sterilization lot deletion
    S30  STI/STS - Request item
    S31  SDR/SDS - Request anti-microbial device data
    S32  SMD/SMS - Request anti-microbial device cycle data
    S33  STC/ACK - Notification of sterilization configuration
    S34  SLN/ACK - Notification of sterilization lot
    S35  SLN/ACK - Notification of sterilization lot deletion
    S36  SDN/ACK - Notification of anti-microbial device data
    S37  SCN/ACK - Notification of anti-microbial device cycle data
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
    B07 = "B07"
    B08 = "B08"
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
    E01 = "E01"
    E02 = "E02"
    E03 = "E03"
    E04 = "E04"
    E10 = "E10"
    E12 = "E12"
    E13 = "E13"
    E15 = "E15"
    E20 = "E20"
    E21 = "E21"
    E22 = "E22"
    E24 = "E24"
    E30 = "E30"
    E31 = "E31"
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
    K11 = "K11"
    K13 = "K13"
    K15 = "K15"
    K21 = "K21"
    K22 = "K22"
    K23 = "K23"
    K24 = "K24"
    K25 = "K25"
    K31 = "K31"
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
    M13 = "M13"
    M14 = "M14"
    M15 = "M15"
    M16 = "M16"
    M17 = "M17"
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
    O22 = "O22"
    O23 = "O23"
    O24 = "O24"
    O25 = "O25"
    O26 = "O26"
    O27 = "O27"
    O28 = "O28"
    O29 = "O29"
    O30 = "O30"
    O31 = "O31"
    O32 = "O32"
    O33 = "O33"
    O34 = "O34"
    O35 = "O35"
    O36 = "O36"
    O37 = "O37"
    O38 = "O38"
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
    P11 = "P11"
    P12 = "P12"
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
    Q05 = "Q05"
    Q06 = "Q06"
    Q11 = "Q11"
    Q13 = "Q13"
    Q15 = "Q15"
    Q16 = "Q16"
    Q17 = "Q17"
    Q21 = "Q21"
    Q22 = "Q22"
    Q23 = "Q23"
    Q24 = "Q24"
    Q25 = "Q25"
    Q26 = "Q26"
    Q27 = "Q27"
    Q28 = "Q28"
    Q29 = "Q29"
    Q30 = "Q30"
    Q31 = "Q31"
    R01 = "R01"
    R02 = "R02"
    R04 = "R04"
    ROR = "ROR"
    R21 = "R21"
    R22 = "R22"
    R23 = "R23"
    R24 = "R24"
    R25 = "R25"
    R30 = "R30"
    R31 = "R31"
    R32 = "R32"
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
    S28 = "S28"
    S29 = "S29"
    S30 = "S30"
    S31 = "S31"
    S32 = "S32"
    S33 = "S33"
    S34 = "S34"
    S35 = "S35"
    S36 = "S36"
    S37 = "S37"
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


class PatientClass(str, Enum):
    """
    004 - Patient Class

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
    BRE  Brethren
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
    FUL  Christian: Full Gospel
    GRE  Christian: Greek Orthodox
    JWN  Christian: Jehovah's Witness
    MOM  Christian: Latter-day Saints
    LUT  Christian: Lutheran
    LMS  Christian: Lutheran Missouri Synod
    MEN  Christian: Mennonite
    MET  Christian: Methodist
    NAZ  Christian: Church of the Nazarene
    ORT  Christian: Orthodox
    PEN  Christian: Pentecostal
    COP  Christian: Other Pentecostal
    PRE  Christian: Presbyterian
    PRO  Christian: Protestant
    PRC  Christian: Other Protestant
    REC  Christian: Reformed Church
    REO  Christian: Reorganized Church of Jesus Christ-LDS
    CAT  Christian: Roman Catholic
    SAA  Christian: Salvation Army
    SEV  Christian: Seventh Day Adventist
    SOU  Christian: Southern Baptist
    UCC  Christian: United Church of Christ
    UMD  Christian: United Methodist
    UNI  Christian: Unitarian
    UNU  Christian: Unitarian Universalist
    WES  Christian: Wesleyan
    WMC  Christian: Wesleyan Methodist
    COT  Christian: Other
    CNF  Confucian
    DOC  Disciples of Christ
    ERL  Ethnic Religionist
    HIN  Hindu
    HSH  Hindu: Shaivites
    HVA  Hindu: Vaishnavites
    HOT  Hindu: Other
    JAI  Jain
    JEW  Jewish
    JCO  Jewish: Conservative
    JOR  Jewish: Orthodox
    JRC  Jewish: Reconstructionist
    JRF  Jewish: Reform
    JRN  Jewish: Renewal
    JOT  Jewish: Other
    MOS  Muslim
    MSH  Muslim: Shiite
    MSU  Muslim: Sunni
    MOT  Muslim: Other
    NAM  Native American
    NRL  New Religionist
    NOE  Nonreligious
    SHN  Shintoist
    SIK  Sikh
    SPI  Spiritist
    OTH  Other
    VAR  Unknown
    """

    AGN = "AGN"
    ATH = "ATH"
    BAH = "BAH"
    BRE = "BRE"
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
    FUL = "FUL"
    GRE = "GRE"
    JWN = "JWN"
    MOM = "MOM"
    LUT = "LUT"
    LMS = "LMS"
    MEN = "MEN"
    MET = "MET"
    NAZ = "NAZ"
    ORT = "ORT"
    PEN = "PEN"
    COP = "COP"
    PRE = "PRE"
    PRO = "PRO"
    PRC = "PRC"
    REC = "REC"
    REO = "REO"
    CAT = "CAT"
    SAA = "SAA"
    SEV = "SEV"
    SOU = "SOU"
    UCC = "UCC"
    UMD = "UMD"
    UNI = "UNI"
    UNU = "UNU"
    WES = "WES"
    WMC = "WMC"
    COT = "COT"
    CNF = "CNF"
    DOC = "DOC"
    ERL = "ERL"
    HIN = "HIN"
    HSH = "HSH"
    HVA = "HVA"
    HOT = "HOT"
    JAI = "JAI"
    JEW = "JEW"
    JCO = "JCO"
    JOR = "JOR"
    JRC = "JRC"
    JRF = "JRF"
    JRN = "JRN"
    JOT = "JOT"
    MOS = "MOS"
    MSH = "MSH"
    MSU = "MSU"
    MOT = "MOT"
    NAM = "NAM"
    NRL = "NRL"
    NOE = "NOE"
    SHN = "SHN"
    SIK = "SIK"
    SPI = "SPI"
    OTH = "OTH"
    VAR = "VAR"


class AdmissionType(str, Enum):
    """
    007 - Admission Type

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


class AmbulatoryStatus(str, Enum):
    """
    009 - Ambulatory Status

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
    017 - Transaction Type

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


class AdmitSource(str, Enum):
    """
    023 - Admit Source

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
    SOF  First open slot on the identified schedule after the start date/tiem
    SOP  Open slots on the identified schedule between the begin and end of the start date/time range
    SSA  Time slots available for a single appointment
    SSR  Time slots available for a recurring appointment
    STA  Status
    VXI  Vaccine Information
    XID  Get cross-referenced identifiers
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
    SOF = "SOF"
    SOP = "SOP"
    SSA = "SSA"
    SSR = "SSR"
    STA = "STA"
    VXI = "VXI"
    XID = "XID"


class DiagnosisType(str, Enum):
    """
    052 - Diagnosis Type

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

    BCV  Bank Card Validation Number
    NPI  Check digit algorithm in the US National Provider Identifier
    ISO  ISO 7064: 1983
    M10  Mod 10 algorithm
    M11  Mod 11 algorithm
    """

    BCV = "BCV"
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
    O  Other
    U  Unknown
    """

    _01 = "01"
    _02 = "02"
    _03 = "03"
    O = "O"
    U = "U"


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


class SpecimenActionCode(str, Enum):
    """
    065 - Specimen Action Code

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


class EmploymentStatus(str, Enum):
    """
         066 - Employment Status

         1  Full time employed
    1312
         2  Part time employed
         4  Self-employed,
         C  Contract, per diem
         L  Leave of absence (e.g., family leave, sabbatical, etc.)
         T  Temporarily unemployed
         3  Unemployed
         5  Retired
         6  On active military duty
         O  Other
         9  Unknown
    """

    _1 = "1"
    _2 = "2"
    _4 = "4"
    C = "C"
    L = "L"
    T = "T"
    _3 = "3"
    _5 = "5"
    _6 = "6"
    O = "O"
    _9 = "9"


class HospitalService(str, Enum):
    """
    069 - Hospital Service

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


class SpecimenSourceCodes(str, Enum):
    """
    070 - Specimen Source Codes

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
    VITF  Vitreous Fluid
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
    BLDCO = "BLDCO"
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
    VITF = "VITF"
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


class DiagnosticServiceSectionID(str, Enum):
    """
    074 - Diagnostic Service Section ID

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
    PHY  Physician (Hx. Dx, admission note, etc.)
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
    076 - Message type

    ACK  General acknowledgment message
    ADR  ADT response
    ADT  ADT message
    BAR  Add/change billing account
    BPS  Blood product dispense status message
    BRP  Blood product dispense status acknowledgement message
    BRT  Blood product transfusion/disposition acknowledgement message
    BTS  Blood product transfusion/disposition message
    CRM  Clinical study registration message
    CSU  Unsolicited study data message
    DFT  Detail financial transactions
    DOC  Document response
    DSR  Display response
    EAC  Automated equipment command message
    EAN  Automated equipment notification message
    EAR  Automated equipment response message
    EHC  Health Care Invoice
    ESR  Automated equipment status update acknowledgment message
    ESU  Automated equipment status update message
    INR  Automated equipment inventory request message
    INU  Automated equipment inventory update message
    LSR  Automated equipment log/service request message
    LSU  Automated equipment log/service update message
    MDM  Medical document management
    MFD  Master files delayed application acknowledgment
    MFK  Master files application acknowledgment
    MFN  Master files notification
    MFQ  Master files query
    MFR  Master files response
    NMD  Application management data message
    NMQ  Application management query message
    NMR  Application management response message
    OMB  Blood product order message
    OMD  Dietary order
    OMG  General clinical order message
    OMI  Imaging order
    OML  Laboratory order message
    OMN  Non-stock requisition order message
    OMP  Pharmacy/treatment order message
    OMS  Stock requisition order message
    OPL  Population/Location-Based Laboratory Order Message
    OPR  Population/Location-Based Laboratory Order Acknowledgment Message
    OPU  Unsolicited Population/Location-Based Laboratory Observation Message
    ORB  Blood product order acknowledgement message
    ORD  Dietary order acknowledgment message
    ORF  Query for results of observation
    ORG  General clinical order acknowledgment message
    ORI  Imaging order acknowledgement message
    ORL  Laboratory acknowledgment message (unsolicited)
    ORM  Pharmacy/treatment order message
    ORN  Non-stock requisition - General order acknowledgment message
    ORP  Pharmacy/treatment order acknowledgment message
    ORR  General order response message response to any ORM
    ORS  Stock requisition - Order acknowledgment message
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
    ROR  Pharmacy/treatment order response
    RPA  Return patient authorization
    RPI  Return patient information
    RPL  Return patient display list
    RPR  Return patient list
    RQA  Request patient authorization
    RQC  Request clinical information
    RQI  Request patient information
    RQP  Request patient demographics
    RRA  Pharmacy/treatment administration acknowledgment message
    RRD  Pharmacy/treatment dispense acknowledgment message
    RRE  Pharmacy/treatment encoded order acknowledgment message
    RRG  Pharmacy/treatment give acknowledgment message
    RRI  Return referral information
    RSP  Segment pattern response
    RTB  Tabular response
    SCN  Notification of Anti-Microbial Device Cycle Data
    SDN  Notification of Anti-Microbial Device Data
    SDR  Sterilization anti-microbial device data request
    SIU  Schedule information unsolicited
    SLN  Notification of New Sterilization Lot
    SLR  Sterilization lot request
    SMD  Sterilization anti-microbial device cycle data request
    SQM  Schedule query message
    SQR  Schedule query response
    SRM  Schedule request message
    SRR  Scheduled request response
    SSR  Specimen status request message
    SSU  Specimen status update message
    STC  Notification of Sterilization Configuration
    STI  Sterilization item request
    SUR  Summary product experience report
    TBR  Tabular data response
    TCR  Automated equipment test code settings request message
    TCU  Automated equipment test code settings update message
    UDM  Unsolicited display update message
    VXQ  Query for vaccination record
    VXR  Vaccination record response
    VXU  Unsolicited vaccination record update
    VXX  Response for vaccination query with multiple PID matches
    """

    ACK = "ACK"
    ADR = "ADR"
    ADT = "ADT"
    BAR = "BAR"
    BPS = "BPS"
    BRP = "BRP"
    BRT = "BRT"
    BTS = "BTS"
    CRM = "CRM"
    CSU = "CSU"
    DFT = "DFT"
    DOC = "DOC"
    DSR = "DSR"
    EAC = "EAC"
    EAN = "EAN"
    EAR = "EAR"
    EHC = "EHC"
    ESR = "ESR"
    ESU = "ESU"
    INR = "INR"
    INU = "INU"
    LSR = "LSR"
    LSU = "LSU"
    MDM = "MDM"
    MFD = "MFD"
    MFK = "MFK"
    MFN = "MFN"
    MFQ = "MFQ"
    MFR = "MFR"
    NMD = "NMD"
    NMQ = "NMQ"
    NMR = "NMR"
    OMB = "OMB"
    OMD = "OMD"
    OMG = "OMG"
    OMI = "OMI"
    OML = "OML"
    OMN = "OMN"
    OMP = "OMP"
    OMS = "OMS"
    OPL = "OPL"
    OPR = "OPR"
    OPU = "OPU"
    ORB = "ORB"
    ORD = "ORD"
    ORF = "ORF"
    ORG = "ORG"
    ORI = "ORI"
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
    ROR = "ROR"
    RPA = "RPA"
    RPI = "RPI"
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
    RRI = "RRI"
    RSP = "RSP"
    RTB = "RTB"
    SCN = "SCN"
    SDN = "SDN"
    SDR = "SDR"
    SIU = "SIU"
    SLN = "SLN"
    SLR = "SLR"
    SMD = "SMD"
    SQM = "SQM"
    SQR = "SQR"
    SRM = "SRM"
    SRR = "SRR"
    SSR = "SSR"
    SSU = "SSU"
    STC = "STC"
    STI = "STI"
    SUR = "SUR"
    TBR = "TBR"
    TCR = "TCR"
    TCU = "TCU"
    UDM = "UDM"
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
    S  Susceptible. Indicates for microbiology susceptibilities only.
    R  Resistant. Indicates for microbiology susceptibilities only.
    I  Intermediate. Indicates for microbiology susceptibilities only.
    MS  Moderately susceptible. Indicates for microbiology susceptibilities only.
    VS  Very susceptible. Indicates for microbiology susceptibilities only.
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


class NatureofAbnormalTesting(str, Enum):
    """
    080 - Nature of Abnormal Testing

    A  An age-based population
    N  None - generic normal range
    R  A race-based population
    S  A sex-based population
    SP  Species
    B  Breed
    ST  Strain
    """

    A = "A"
    N = "N"
    R = "R"
    S = "S"
    SP = "SP"
    B = "B"
    ST = "ST"


class OutlierType(str, Enum):
    """
    083 - Outlier Type

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
    S  Partial results.   Deprecated. Retained only for backward compatibility as of V2.6.
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


class Re_AdmissionIndicator(str, Enum):
    """
    092 - Re-Admission Indicator

    R  Re-admission
    """

    R = "R"


class ReleaseInformation(str, Enum):
    """
         093 - Release Information

         Y  Yes
         N  No
    1312
    """

    Y = "Y"
    N = "N"


class TypeofAgreement(str, Enum):
    """
    098 - Type of Agreement

    S  Standard
    U  Unified
    M  Maternity
    """

    S = "S"
    U = "U"
    M = "M"


class Invocationevent(str, Enum):
    """
    100 - Invocation event

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
    2.5  Release 2.5
    2.5.1  Release 1.5.1
    2.6  Release 2.6
    """

    _2_0 = "2.0"
    _2_0D = "2.0D"
    _2_1 = "2.1"
    _2_2 = "2.2"
    _2_3 = "2.3"
    _2_3_1 = "2.3.1"
    _2_4 = "2.4"
    _2_5 = "2.5"
    _2_5_1 = "2.5.1"
    _2_6 = "2.6"


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


class DischargeDisposition(str, Enum):
    """
    112 - Discharge Disposition

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
    10 ... 19  Discharge to be defined at state level, if necessary
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
    _10_____19 = "10 ... 19"
    _20 = "20"
    _21_____29 = "21 ... 29"
    _30 = "30"
    _31_____39 = "31 ... 39"
    _40 = "40"
    _41 = "41"
    _42 = "42"


class BedStatus(str, Enum):
    """
    116 - Bed Status

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
    119 - Order control codes

    AF  Order/service refill request approval
    CA  Cancel order/service request
    CH  Child order/service
    CN  Combined result
    CR  Canceled as requested
    DC  Discontinue order/service request
    DE  Data errors
    DF  Order/service refill request denied
    DR  Discontinued as requested
    FU  Order/service refilled, unsolicited
    HD  Hold order request
    HR  On hold as requested
    LI  Link order/service to patient care problem or goal
    NA  Number assigned
    SN  Send order/service number
    NW  New order/service
    OC  Order/service canceled
    OD  Order/service discontinued
    OE  Order/service released
    OF  Order/service refilled as requested
    OH  Order/service held
    OK  Order/service accepted & OK
    OP  Notification of order for outside dispense
    OR  Released as requested
    PA  Parent order/service
    PR  Previous Results with new order/service
    PY  Notification of replacement order for outside dispense
    RE  Observations/Performed Service to follow
    RF  Refill order/service request
    RL  Release previous hold
    RO  Replacement order
    RP  Order/service replace request
    RQ  Replaced as requested
    RR  Request received
    RU  Replaced unsolicited
    SC  Status changed
    SR  Response to send order/service status request
    SS  Send order/service status request
    UA  Unable to accept order/service
    UC  Unable to cancel
    UD  Unable to discontinue
    UF  Unable to refill
    UH  Unable to put on hold
    UM  Unable to replace
    UN  Unlink order/service from patient care problem or goal
    UR  Unable to release
    UX  Unable to change
    XO  Change order/service request
    XR  Changed as requested
    XX  Order/service changed, unsol.
    MC  Miscellaneous Charge - not associated with an order
    """

    AF = "AF"
    CA = "CA"
    CH = "CH"
    CN = "CN"
    CR = "CR"
    DC = "DC"
    DE = "DE"
    DF = "DF"
    DR = "DR"
    FU = "FU"
    HD = "HD"
    HR = "HR"
    LI = "LI"
    NA = "NA"
    SN = "SN"
    NW = "NW"
    OC = "OC"
    OD = "OD"
    OE = "OE"
    OF = "OF"
    OH = "OH"
    OK = "OK"
    OP = "OP"
    OR = "OR"
    PA = "PA"
    PR = "PR"
    PY = "PY"
    RE = "RE"
    RF = "RF"
    RL = "RL"
    RO = "RO"
    RP = "RP"
    RQ = "RQ"
    RR = "RR"
    RU = "RU"
    SC = "SC"
    SR = "SR"
    SS = "SS"
    UA = "UA"
    UC = "UC"
    UD = "UD"
    UF = "UF"
    UH = "UH"
    UM = "UM"
    UN = "UN"
    UR = "UR"
    UX = "UX"
    XO = "XO"
    XR = "XR"
    XX = "XX"
    MC = "MC"


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


class ResultStatus(str, Enum):
    """
    123 - Result Status

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


class TransportationMode(str, Enum):
    """
    124 - Transportation Mode

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
    CWE  Coded Entry
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
    DTM  Time Stamp (Date & Time)
    TX  Text Data (Display)
    XAD  Extended Address
    XCN  Extended Composite Name And Number For Persons
    XON  Extended Composite Name And Number For Organizations
    XPN  Extended Person Name
    XTN  Extended Telecommunications Number
    """

    AD = "AD"
    CWE = "CWE"
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
    DTM = "DTM"
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


class AllergenType(str, Enum):
    """
    127 - Allergen Type

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


class AllergySeverity(str, Enum):
    """
    128 - Allergy Severity

    SV  Severe
    MO  Moderate
    MI  Mild
    U  Unknown
    """

    SV = "SV"
    MO = "MO"
    MI = "MI"
    U = "U"


class VisitUserCode(str, Enum):
    """
    130 - Visit User Code

    TE  Teaching
    HO  Home
    MO  Mobile Unit
    PH  Phone
    """

    TE = "TE"
    HO = "HO"
    MO = "MO"
    PH = "PH"


class ContactRole(str, Enum):
    """
    131 - Contact Role

    E  Employer
    C  Emergency Contact
    F  Federal Agency
    I  Insurance Company
    N  Next-of-Kin
    S  State Agency
    O  Other
    U  Unknown
    """

    E = "E"
    C = "C"
    F = "F"
    I = "I"
    N = "N"
    S = "S"
    O = "O"
    U = "U"


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


class Yes_noindicator(str, Enum):
    """
    136 - Yes-no indicator

    Y  Yes
    N  No
    """

    Y = "Y"
    N = "N"


class MailClaimParty(str, Enum):
    """
    137 - Mail Claim Party

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


class MilitaryService(str, Enum):
    """
    140 - Military Service

    USA  US Army
    USN  US Navy
    USAF  US Air Force
    USMC  US Marine Corps
    USCG  US Coast Guard
    USPHS  US Public Health Service
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


class MilitaryRank_Grade(str, Enum):
    """
    141 - Military Rank-Grade

    O3  Officers
    O1  Officers
    O2  Officers
    W4
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
    E1... E9  Enlisted
    E2  Enlisted
    E3  Enlisted
    E4  Enlisted
    E5  Enlisted
    E6  Enlisted
    E8  Enlisted
    E1  Enlisted
    E7  Enlisted
    O1 ... O9  Officers
    W1 ... W4  Warrant Officers
    """

    O3 = "O3"
    O1 = "O1"
    O2 = "O2"
    W4 = "W4"
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
    E1____E9 = "E1... E9"
    E2 = "E2"
    E3 = "E3"
    E4 = "E4"
    E5 = "E5"
    E6 = "E6"
    E8 = "E8"
    E1 = "E1"
    E7 = "E7"
    O1_____O9 = "O1 ... O9"
    W1_____W4 = "W1 ... W4"


class MilitaryStatus(str, Enum):
    """
    142 - Military Status

    ACT  Active duty
    RET  Retired
    DEC  Deceased
    """

    ACT = "ACT"
    RET = "RET"
    DEC = "DEC"


class EligibilitySource(str, Enum):
    """
    144 - Eligibility Source

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


class Moneyorpercentageindicator(str, Enum):
    """
    148 - Money or percentage indicator

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


class Certificationpatienttype(str, Enum):
    """
    150 - Certification patient type

    ER  Emergency
    IPE  Inpatient elective
    OPE  Outpatient elective
    UR  Urgent
    """

    ER = "ER"
    IPE = "IPE"
    OPE = "OPE"
    UR = "UR"


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


class DietCodeSpecificationType(str, Enum):
    """
    159 - Diet Code Specification Type

    D  Diet
    S  Supplement
    P  Preference
    """

    D = "D"
    S = "S"
    P = "P"


class TrayType(str, Enum):
    """
    160 - Tray Type

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


class AllowSubstitution(str, Enum):
    """
    161 - Allow Substitution

    N  Substitutions are NOT authorized.  (This is the default - null.)
    G  Allow generic substitutions.
    T  Allow therapeutic substitutions
    """

    N = "N"
    G = "G"
    T = "T"


class RouteofAdministration(str, Enum):
    """
    162 - Route of Administration

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


class AdministrationDevice(str, Enum):
    """
    164 - Administration Device

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


class AdministrationMethod(str, Enum):
    """
    165 - Administration Method

    CH  Chew
    DI  Dissolve
    DU  Dust
    IF  Infiltrate
    IS  Insert
    IR  Irrigate
    IVPB  IV Piggyback
    IVP  IV Push
    NB  Nebulized
    PT  Paint
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


class CoordinationofBenefits(str, Enum):
    """
    173 - Coordination of Benefits

    CO  Coordination
    IN  Independent
    """

    CO = "CO"
    IN = "IN"


class NatureofService_Test_Observation(str, Enum):
    """
    174 - Nature of Service-Test-Observation

    P  Profile or battery consisting of many independent atomic observations (e.g., SMA12, electrolytes), usually done at one instrument on one specimen
    F  Functional procedure that may consist of one or more interrelated measures (e.g., glucose tolerance test, creatinine clearance), usually done at different times and/or on different specimens
    A  Atomic service/test/observation (test code or treatment code)
    S  Superset-a set of batteries or procedures ordered under a single code unit but processed as separate batteries (e.g., routines = CBC, UA, electrolytes)This set indicates that the code being described is used to order multiple service/test/observation b
    C  Single observation calculated via a rule or formula from other independent observations (e.g., Alveolar-arterial ratio, cardiac output)
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
    OME  Other Observation/Service Item master file
    INV  Inventory master file
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
    INV = "INV"


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


class Active_Inactive(str, Enum):
    """
    183 - Active-Inactive

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


class EthnicGroup(str, Enum):
    """
    189 - Ethnic Group

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
    BI  Billing Address
    N  Birth (nee)  (birth address, not otherwise specified)
    BDL  Birth delivery location  (address where birth occurred)
    F  Country Of Origin
    C  Current Or Temporary
    B  Firm/Business
    H  Home
    L  Legal Address
    M  Mailing
    O  Office/Business
    P  Permanent
    RH  Registry home. Refers to the information system, typically managed by a public health agency, that stores patient information such as immunization histories or cancer data, regardless of where the patient obtains services.
    BR  Residence at birth (home address at time of birth)
    S  Service Location
    SH  Shipping Address
    V  Vacation
    """

    BA = "BA"
    BI = "BI"
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
    S = "S"
    SH = "SH"
    V = "V"


class Typeofreferenceddata(str, Enum):
    """
    191 - Type of referenced data

    AP  Other application data, typically uninterpreted binary data (HL7 V2.3 and later)
    AU  Audio data (HL7 V2.3 and later)
    FT  Formatted text (HL7 V2.2 only)
    IM  Image data (HL7 V2.3 and later)
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
    K  Artist Name
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
    K = "K"
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
    PRS  Personal
    """

    PRN = "PRN"
    ORN = "ORN"
    WPN = "WPN"
    VHN = "VHN"
    ASN = "ASN"
    EMR = "EMR"
    NET = "NET"
    BPN = "BPN"
    PRS = "PRS"


class Telecommunicationequipmenttype(str, Enum):
    """
    202 - Telecommunication equipment type

    PH  Telephone
    FX  Fax
    MD  Modem
    CP  Cellular or Mobile Phone
    SAT  Satellite Phone
    BP  Beeper
    Internet  Internet Address
    X.400  X.400 email address
    TDD  Telecommunications Device for the Deaf
    TTY  Teletypewriter
    """

    PH = "PH"
    FX = "FX"
    MD = "MD"
    CP = "CP"
    SAT = "SAT"
    BP = "BP"
    Internet = "Internet"
    X_400 = "X.400"
    TDD = "TDD"
    TTY = "TTY"


class Identifiertype(str, Enum):
    """
    203 - Identifier type

    AM  American Express
    AMA  American Medical Association Number
    AN  Account number
    ANON  Anonymous identifier
    ANC  Account number Creditor
    AND  Account number debitor
    ANT  Temporary Account Number
    APRN  Advanced Practice Registered Nurse number
    BA  Bank Account Number
    BC  Bank Card Number
    BCT  Birth Certificate
    BR  Birth registry number
    BRN  Breed Registry Number
    CC  Cost Center number
    CONM  Change of Name Document
    CZ  Citizenship Card
    CY  County number
    DDS  Dentist license number
    DEA  Drug Enforcement Administration registration number
    DI  Diner's Club card
    DFN  Drug Furnishing or prescriptive authority Number
    DL  Driver's license number
    DN  Doctor number
    DO  Osteopathic License number
    DP  Diplomatic Passport
    DPM  Podiatrist license number
    DR  Donor Registration Number
    DS  Discover Card
    EI  Employee number
    EN  Employer number
    ESN  Staff Enterprise Number
    FI  Facility ID
    GI  Guarantor internal identifier
    GL  General ledger number
    GN  Guarantor external  identifier
    HC  Health Card Number
    JHN  Jurisdictional health number (Canada)
    IND  Indigenous/Aboriginal
    LI  Labor and industries number
    LN  License number
    LR  Local Registry ID
    MA  Patient Medicaid number
    MB  Member Number
    MC  Patient's Medicare number
    MCD  Practitioner Medicaid number
    MCN  Microchip Number
    MCR  Practitioner Medicare number
    MCT  Marriage Certificate
    MD  Medical License number
    MI  Military ID number
    MR  Medical record number
    MRT  Temporary Medical Record Number
    MS  MasterCard
    NCT  Naturalization Certificate
    NE  National employer identifier
    NH  National Health Plan Identifier
    NI  National unique individual identifier
    NII  National Insurance Organization Identifier
    NIIP  National Insurance Payor Identifier (Payor)
    NNxxx  National Person Identifier where the xxx is the ISO table 3166 3-character (alphabetic) country code
    NP  Nurse practitioner number
    NPI  National provider identifier
    OD  Optometrist license number
    PA  Physician Assistant number
    PC  Parole Card
    PCN  Penitentiary/correctional institution Number
    PE  Living Subject Enterprise Number
    PEN  Pension Number
    PI  Patient internal identifier
    PN  Person number
    PNT  Temporary Living Subject Number
    PPIN  Medicare/CMS Performing Provider Identification Number
    PPN  Passport number
    PRC  Permanent Resident Card Number
    PRN  Provider number
    PT  Patient external identifier
    QA  QA number
    RI  Resource identifier
    RPH  Pharmacist license number
    RN  Registered Nurse Number
    RR  Railroad Retirement number
    RRI  Regional registry ID
    RRP  Railroad Retirement Provider
    SL  State license
    SN  Subscriber Number
    SP  Study Permit
    SR  State registry ID
    SS  Social Security number
    TAX  Tax ID number
    TN  Treaty Number/ (Canada)
    TPR  Temporary Permanent Resident (Canada)
    U  Unspecified identifier
    UPIN  Medicare/CMS (formerly HCFA)'s Universal Physician Identification numbers
    VN  Visit number
    VP  Visitor Permit
    VS  VISA
    WC  WIC identifier
    WCN  Workers' Comp Number
    WP  Work Permit
    XX  Organization identifier
    """

    AM = "AM"
    AMA = "AMA"
    AN = "AN"
    ANON = "ANON"
    ANC = "ANC"
    AND = "AND"
    ANT = "ANT"
    APRN = "APRN"
    BA = "BA"
    BC = "BC"
    BCT = "BCT"
    BR = "BR"
    BRN = "BRN"
    CC = "CC"
    CONM = "CONM"
    CZ = "CZ"
    CY = "CY"
    DDS = "DDS"
    DEA = "DEA"
    DI = "DI"
    DFN = "DFN"
    DL = "DL"
    DN = "DN"
    DO = "DO"
    DP = "DP"
    DPM = "DPM"
    DR = "DR"
    DS = "DS"
    EI = "EI"
    EN = "EN"
    ESN = "ESN"
    FI = "FI"
    GI = "GI"
    GL = "GL"
    GN = "GN"
    HC = "HC"
    JHN = "JHN"
    IND = "IND"
    LI = "LI"
    LN = "LN"
    LR = "LR"
    MA = "MA"
    MB = "MB"
    MC = "MC"
    MCD = "MCD"
    MCN = "MCN"
    MCR = "MCR"
    MCT = "MCT"
    MD = "MD"
    MI = "MI"
    MR = "MR"
    MRT = "MRT"
    MS = "MS"
    NCT = "NCT"
    NE = "NE"
    NH = "NH"
    NI = "NI"
    NII = "NII"
    NIIP = "NIIP"
    NNxxx = "NNxxx"
    NP = "NP"
    NPI = "NPI"
    OD = "OD"
    PA = "PA"
    PC = "PC"
    PCN = "PCN"
    PE = "PE"
    PEN = "PEN"
    PI = "PI"
    PN = "PN"
    PNT = "PNT"
    PPIN = "PPIN"
    PPN = "PPN"
    PRC = "PRC"
    PRN = "PRN"
    PT = "PT"
    QA = "QA"
    RI = "RI"
    RPH = "RPH"
    RN = "RN"
    RR = "RR"
    RRI = "RRI"
    RRP = "RRP"
    SL = "SL"
    SN = "SN"
    SP = "SP"
    SR = "SR"
    SS = "SS"
    TAX = "TAX"
    TN = "TN"
    TPR = "TPR"
    U = "U"
    UPIN = "UPIN"
    VN = "VN"
    VP = "VP"
    VS = "VS"
    WC = "WC"
    WCN = "WCN"
    WP = "WP"
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
    X  No Change
    """

    A = "A"
    D = "D"
    U = "U"
    X = "X"


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


class QueryResponseStatus(str, Enum):
    """
    208 - Query Response Status

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

    ASCII  The printable 7-bit ASCII character set.
    8859/1  The printable characters from the ISO 8859/1 Character set
    8859/2  The printable characters from the ISO 8859/2 Character set
    8859/3  The printable characters from the ISO 8859/3 Character set
    8859/4  The printable characters from the ISO 8859/4 Character set
    8859/5  The printable characters from the ISO 8859/5 Character set
    8859/6  The printable characters from the ISO 8859/6 Character set
    8859/7  The printable characters from the ISO 8859/7 Character set
    8859/8  The printable characters from the ISO 8859/8 Character set
    8859/9  The printable characters from the ISO 8859/9 Character set
    8859/15  The printable characters from the ISO 8859/15 (Latin-15)
    ISO IR14  Code for Information Exchange (one byte)(JIS X 0201-1976).
    ISO IR87  Code for the Japanese Graphic Character set for information interchange (JIS X 0208-1990),
    ISO IR159  Code of the supplementary Japanese Graphic Character set for information interchange (JIS X 0212-1990).
    GB 18030-2000  Code for Chinese Character Set (GB 18030-2000)
    KS X 1001  Code for Korean Character Set (KS X 1001)
    CNS 11643-1992  Code for Taiwanese Character Set (CNS 11643-1992)
    BIG-5  Code for Taiwanese Character Set (BIG-5)
    UNICODE  The world wide character standard from ISO/IEC 10646-1-1993
    UNICODE UTF-8  UCS Transformation Format, 8-bit form
    UNICODE UTF-16  UCS Transformation Format, 16-bit form
    UNICODE UTF-32  UCS Transformation Format, 32-bit form
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
    _8859_15 = "8859/15"
    ISO_IR14 = "ISO IR14"
    ISO_IR87 = "ISO IR87"
    ISO_IR159 = "ISO IR159"
    GB_18030_2000 = "GB 18030-2000"
    KS_X_1001 = "KS X 1001"
    CNS_11643_1992 = "CNS 11643-1992"
    BIG_5 = "BIG-5"
    UNICODE = "UNICODE"
    UNICODE_UTF_8 = "UNICODE UTF-8"
    UNICODE_UTF_16 = "UNICODE UTF-16"
    UNICODE_UTF_32 = "UNICODE UTF-32"


class PurgeStatusCode(str, Enum):
    """
    213 - Purge Status Code

    P  Marked for purge.  User is no longer able to update the visit.
    D  The visit is marked for deletion and the user cannot enter new data against it.
    I  The visit is marked inactive and the user cannot enter new data against it.
    """

    P = "P"
    D = "D"
    I = "I"


class SpecialProgramCode(str, Enum):
    """
    214 - Special Program Code

    CH  Child Health Assistance
    ES  Elective Surgery Program
    FP  Family Planning
    O  Other
    U  Unknown
    """

    CH = "CH"
    ES = "ES"
    FP = "FP"
    O = "O"
    U = "U"


class PublicityCode(str, Enum):
    """
    215 - Publicity Code

    F  Family only
    N  No Publicity
    O  Other
    U  Unknown
    """

    F = "F"
    N = "N"
    O = "O"
    U = "U"


class PatientStatusCode(str, Enum):
    """
    216 - Patient Status Code

    AI  Active Inpatient
    DI  Discharged Inpatient
    """

    AI = "AI"
    DI = "DI"


class VisitPriorityCode(str, Enum):
    """
    217 - Visit Priority Code

    1  Emergency
    2  Urgent
    3  Elective
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"


class LivingArrangement(str, Enum):
    """
    220 - Living Arrangement

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


class LivingDependency(str, Enum):
    """
    223 - Living Dependency

    S  Spouse Dependent
    M  Medical Supervision Required
    C  Small Children Dependent
    O  Other
    U  Unknown
    """

    S = "S"
    M = "M"
    C = "C"
    O = "O"
    U = "U"


class TransportArranged(str, Enum):
    """
    224 - Transport Arranged

    A  Arranged
    N  Not Arranged
    U  Unknown
    """

    A = "A"
    N = "N"
    U = "U"


class EscortRequired(str, Enum):
    """
    225 - Escort Required

    R  Required
    N  Not Required
    U  Unknown
    """

    R = "R"
    N = "N"
    U = "U"


class ManufacturersofVaccines(str, Enum):
    """
    227 - Manufacturers of Vaccines (code=MVX)

    AB  Abbott Laboratories
    AD  Adams Laboratories, Inc.
    ALP  Alpha Therapeutic Corporation
    AR  Armour
    AVB  Aventis Behring L.L.C.
    AVI  Aviron
    BA  Baxter Healthcare Corporation
    BAH  Baxter Healthcare Corporation
    BAY  Bayer Corporation
    BP  Berna Products
    BPC  Berna Products Corporation
    MIP  Bioport Corporation
    CNJ  Cangene Corporation
    CMP  Celltech Medeva Pharmaceuticals
    CEN  Centeon L.L.C.
    CHI  Chiron Corporation
    CON  Connaught
    DVC  DynPort Vaccine Company, LLC
    EVN  Evans Medical Limited
    GEO  GeoVax Labs, Inc.
    SKB  GlaxoSmithKline
    GRE  Greer Laboratories, Inc.
    IAG  Immuno International AG
    IUS  Immuno-U.S., Inc.
    KGC  Korea Green Cross Corporation
    LED  Lederle
    MBL  Massachusetts Biologic Laboratories
    MA  Massachusetts Public Health Biologic Laboratories
    MED  MedImmune, Inc.
    MSD  Merck & Co., Inc.
    IM  Merieux
    MIL  Miles
    NAB  NABI
    NYB  New York Blood Center
    NAV  North American Vaccine, Inc.
    NOV  Novartis Pharmaceutical Corporation
    NVX  Novavax, Inc.
    OTC  Organon Teknika Corporation
    ORT  Ortho-Clinical Diagnostics
    PD  Parkedale Pharmaceuticals
    PWJ  PowderJect Pharmaceuticals
    PRX  Praxis Biologics
    PMC  sanofi pasteur
    JPN  The Research Foundation for Microbial Diseases of Osaka University
    SCL  Sclavo, Inc.
    SOL  Solvay Pharmaceuticals
    SI  Swiss Serum and Vaccine Inst.
    TAL  Talecris Biotherapeutics
    USA  United States Army Medical Research and Material Command
    VXG  VaxGen
    WA  Wyeth-Ayerst
    WAL  Wyeth-Ayerst
    ZLB  ZLB Behring
    OTH  Other manufacturer
    UNK  Unknown manufacturer
    """

    AB = "AB"
    AD = "AD"
    ALP = "ALP"
    AR = "AR"
    AVB = "AVB"
    AVI = "AVI"
    BA = "BA"
    BAH = "BAH"
    BAY = "BAY"
    BP = "BP"
    BPC = "BPC"
    MIP = "MIP"
    CNJ = "CNJ"
    CMP = "CMP"
    CEN = "CEN"
    CHI = "CHI"
    CON = "CON"
    DVC = "DVC"
    EVN = "EVN"
    GEO = "GEO"
    SKB = "SKB"
    GRE = "GRE"
    IAG = "IAG"
    IUS = "IUS"
    KGC = "KGC"
    LED = "LED"
    MBL = "MBL"
    MA = "MA"
    MED = "MED"
    MSD = "MSD"
    IM = "IM"
    MIL = "MIL"
    NAB = "NAB"
    NYB = "NYB"
    NAV = "NAV"
    NOV = "NOV"
    NVX = "NVX"
    OTC = "OTC"
    ORT = "ORT"
    PD = "PD"
    PWJ = "PWJ"
    PRX = "PRX"
    PMC = "PMC"
    JPN = "JPN"
    SCL = "SCL"
    SOL = "SOL"
    SI = "SI"
    TAL = "TAL"
    USA = "USA"
    VXG = "VXG"
    WA = "WA"
    WAL = "WAL"
    ZLB = "ZLB"
    OTH = "OTH"
    UNK = "UNK"


class DiagnosisClassification(str, Enum):
    """
    228 - Diagnosis Classification

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


class DRGPayor(str, Enum):
    """
    229 - DRG Payor

    M  Medicare
    C  Champus
    G  Managed Care Organization
    """

    M = "M"
    C = "C"
    G = "G"


class ProcedureFunctionalType(str, Enum):
    """
    230 - Procedure Functional Type

    A  Anesthesia
    P  Procedure for treatment (therapeutic, including operations)
    I  Invasive procedure not classified elsewhere (e.g., IV, catheter, etc.)
    D  Diagnostic procedure
    """

    A = "A"
    P = "P"
    I = "I"
    D = "D"


class StudentStatus(str, Enum):
    """
    231 - Student Status

    F  Full-time student
    P  Part-time student
    N  Not a student
    """

    F = "F"
    P = "P"
    N = "N"


class InsuranceCompanyContactReason(str, Enum):
    """
    232 - Insurance Company Contact Reason

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


class EventReportedTo(str, Enum):
    """
    236 - Event Reported To

    M  Manufacturer
    L  Local facility/user facility
    R  Regulatory agency
    D  Distributor
    """

    M = "M"
    L = "L"
    R = "R"
    D = "D"


class EventQualification(str, Enum):
    """
    237 - Event Qualification

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
    N  No
    U  Unknown
    """

    Y = "Y"
    N = "N"
    U = "U"


class EventConsequence(str, Enum):
    """
    240 - Event Consequence

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


class PatientOutcome(str, Enum):
    """
    241 - Patient Outcome

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


class PrimaryObserversQualification(str, Enum):
    """
    242 - Primary Observer s Qualification

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


class IdentityMayBeDivulged(str, Enum):
    """
    243 - Identity May Be Divulged

    Y  Yes
    N  No
    NA  Not applicable
    """

    Y = "Y"
    N = "N"
    NA = "NA"


class StatusofEvaluation(str, Enum):
    """
    247 - Status of Evaluation

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


class RelatednessAssessment(str, Enum):
    """
    250 - Relatedness Assessment

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


class ActionTakeninResponsetotheEvent(str, Enum):
    """
    251 - Action Taken in Response to the Event

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


class CausalityObservations(str, Enum):
    """
    252 - Causality Observations

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
    TMSTP  *Time Stamp-Date and Time
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


class LocationEquipment(str, Enum):
    """
    261 - Location Equipment

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


class PrivacyLevel(str, Enum):
    """
    262 - Privacy Level

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


class LevelofCare(str, Enum):
    """
    263 - Level of Care

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


class SpecialtyType(str, Enum):
    """
    265 - Specialty Type

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


class ChargeOnIndicator(str, Enum):
    """
    269 - Charge On Indicator

    O  Charge on Order
    R  Charge on Result
    """

    O = "O"
    R = "R"


class DocumentType(str, Enum):
    """
    270 - Document Type

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


class DocumentConfidentialityStatus(str, Enum):
    """
    272 - Document Confidentiality Status

    V  Very restricted
    R  Restricted
    U  Usual control
    """

    V = "V"
    R = "R"
    U = "U"


class DocumentAvailabilityStatus(str, Enum):
    """
    273 - Document Availability Status

    AV  Available for patient care
    CA  Deleted
    OB  Obsolete
    UN  Unavailable for patient care
    """

    AV = "AV"
    CA = "CA"
    OB = "OB"
    UN = "UN"


class DocumentStorageStatus(str, Enum):
    """
    275 - Document Storage Status

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


class AppointmentTypeCodes(str, Enum):
    """
    277 - Appointment Type Codes

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
    Noshow  The patient did not show up for the appointment
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
    Noshow = "Noshow"


class AllowSubstitutionCodes(str, Enum):
    """
    279 - Allow Substitution Codes

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


class SubtypeofReferencedData(str, Enum):
    """
         291 - Subtype of Referenced Data

         Octet-stream  Uninterpreted binary data
         BASIC  ISDN PCM audio data
         DICOM  Digital Imaging and Communications in Medicine
         FAX  Facsimile data
         GIF  Graphics Interchange Format
         HTML  Hypertext Markup Language
         JPEG  Joint Photographic Experts Group
         XML  Extensible Markup Language (HL7 V2.3.1 and later)
         PICT  PICT format image data
         PostScript  PostScript program
         RTF  Rich Text Format
         SGML  Standard Generalized Markup Language (HL7 V2.3.1 and later)
         TIFF  TIFF image data
         JOT  Electronic ink data (Jot 1.0 standard)
    1312
         x-hl7-cda-level-one  HL7 Clinical Document Architecture Level One document
    """

    Octet_stream = "Octet-stream"
    BASIC = "BASIC"
    DICOM = "DICOM"
    FAX = "FAX"
    GIF = "GIF"
    HTML = "HTML"
    JPEG = "JPEG"
    XML = "XML"
    PICT = "PICT"
    PostScript = "PostScript"
    RTF = "RTF"
    SGML = "SGML"
    TIFF = "TIFF"
    JOT = "JOT"
    x_hl7_cda_level_one = "x-hl7-cda-level-one"


class Vaccinesadministered(str, Enum):
    """
    292 - Vaccines administered

    54  adenovirus, type 4
    55  adenovirus, type 7
    82  adenovirus, NOS1
    24  anthrax
    19  BCG
    27  botulinum antitoxin
    26  cholera
    29  CMVIG
    56  dengue fever
    12  diphtheria antitoxin
    28  DT (pediatric)
    20  DTaP
    106  DTaP, 5 pertussis antigens6
    107  DTaP, NOS
    110  DTaP-Hep B-IPV
    50  DTaP-Hib
    120  DTaP-Hib-IPV
    01  DTP
    22  DTP-Hib
    102  DTP-Hib-Hep B
    57  hantavirus
    52  Hep A, adult
    83  Hep A, ped/adol, 2 dose
    84  Hep A, ped/adol, 3 dose
    31  Hep A, pediatric, NOS
    85  Hep A, NOS
    104  Hep A-Hep B
    30  HBIG
    08  Hep B, adolescent or pediatric
    42  Hep B, adolescent/high risk infant2
    43  Hep B, adult4
    44  Hep B, dialysis
    45  Hep B, NOS
    58  Hep C
    59  Hep E
    60  herpes simplex 2
    46  Hib (PRP-D)
    47  Hib (HbOC)
    48  Hib (PRP-T)
    49  Hib (PRP-OMP)
    17  Hib, NOS
    51  Hib-Hep B
    61  HIV
    118  HPV, bivalent
    62  HPV, quadrivalent
    86  IG
    87  IGIV
    14  IG, NOS
    111  influenza, live, intranasal
    15  influenza, split (incl. purified surface antigen)
    16  influenza, whole
    88  influenza, NOS
    10  IPV
    02  OPV
    89  polio, NOS
    39  Japanese encephalitis
    63  Junin virus
    64  leishmaniasis
    65  leprosy
    66  Lyme disease
    03  MMR
    04  M/R
    94  MMRV
    67  malaria
    05  measles
    68  melanoma
    32  meningococcal
    103  meningococcal C conjugate
    114  meningococcal A,C,Y,W-135 diphtheria conjugate
    108  meningococcal, NOS
    07  mumps
    69  parainfluenza-3
    11  pertussis
    23  plague
    33  pneumococcal
    100  pneumococcal conjugate
    109  pneumococcal, NOS
    70  Q fever
    18  rabies, intramuscular injection
    40  rabies, intradermal injection
    90  rabies, NOS
    72  rheumatic fever
    73  Rift Valley fever
    34  RIG
    119  rotavirus, monovalent
    122  rotavirus, NOS1
    116  rotavirus, pentavalent
    74  rotavirus, tetravalent
    71  RSV-IGIV
    93  RSV-MAb
    06  rubella
    38  rubella/mumps
    76  Staphylococcus bacterio lysate
    113  Td (adult)
    09  Td (adult)
    115  Tdap
    35  tetanus toxoid
    112  tetanus toxoid, NOS
    77  tick-borne encephalitis
    13  TIG
    95  TST-OT tine test
    96  TST-PPD intradermal
    97  TST-PPD tine test
    98  TST, NOS
    78  tularemia vaccine
    91  typhoid, NOS
    25  typhoid, oral
    41  typhoid, parenteral
    53  typhoid, parenteral, AKD (U.S. military)
    101  typhoid, ViCPs
    75  vaccinia (smallpox)
    105  vaccinia (smallpox) diluted
    79  vaccinia immune globulin
    21  varicella
    81  VEE, inactivated
    80  VEE, live
    92  VEE, NOS
    36  VZIG
    117  VZIG (IND)
    37  yellow fever
    121  zoster
    998  no vaccine administered5
    999  unknown
    99  RESERVED - do not use3
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
    _106 = "106"
    _107 = "107"
    _110 = "110"
    _50 = "50"
    _120 = "120"
    _01 = "01"
    _22 = "22"
    _102 = "102"
    _57 = "57"
    _52 = "52"
    _83 = "83"
    _84 = "84"
    _31 = "31"
    _85 = "85"
    _104 = "104"
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
    _118 = "118"
    _62 = "62"
    _86 = "86"
    _87 = "87"
    _14 = "14"
    _111 = "111"
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
    _103 = "103"
    _114 = "114"
    _108 = "108"
    _07 = "07"
    _69 = "69"
    _11 = "11"
    _23 = "23"
    _33 = "33"
    _100 = "100"
    _109 = "109"
    _70 = "70"
    _18 = "18"
    _40 = "40"
    _90 = "90"
    _72 = "72"
    _73 = "73"
    _34 = "34"
    _119 = "119"
    _122 = "122"
    _116 = "116"
    _74 = "74"
    _71 = "71"
    _93 = "93"
    _06 = "06"
    _38 = "38"
    _76 = "76"
    _113 = "113"
    _09 = "09"
    _115 = "115"
    _35 = "35"
    _112 = "112"
    _77 = "77"
    _13 = "13"
    _95 = "95"
    _96 = "96"
    _97 = "97"
    _98 = "98"
    _78 = "78"
    _91 = "91"
    _25 = "25"
    _41 = "41"
    _53 = "53"
    _101 = "101"
    _75 = "75"
    _105 = "105"
    _79 = "79"
    _21 = "21"
    _81 = "81"
    _80 = "80"
    _92 = "92"
    _36 = "36"
    _117 = "117"
    _37 = "37"
    _121 = "121"
    _998 = "998"
    _999 = "999"
    _99 = "99"


class Timeselectioncriteriaparameterclasscodes(str, Enum):
    """
    294 - Time selection criteria parameter class codes

    Prefstart  An indicator that there is a preferred start time for the appointment request, service or resource.
    Prefend  An indicator that there is a preferred end time for the appointment request, service or resource.
    Mon  An indicator that Monday is or is not preferred for the day on which the appointment will occur.
    Tue  An indicator that Tuesday is or is not preferred for the day on which the appointment will occur.
    Wed  An indicator that Wednesday is or is not preferred for the day on which the appointment will occur.
    Thu  An indicator that Thursday is or is not preferred for the day on which the appointment will occur.
    Fri  An indicator that Friday is or is not preferred for the day on which the appointment will occur.
    Sat  An indicator that Saturday is or is not preferred for the day on which the appointment will occur.
    Sun  An indicator that Sunday is or is not preferred for the day on which the appointment will occur.
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

    P  Pro-rate. Apply this price to this interval, pro-rated by whatever portion of the interval has occurred/been consumed
    F  Flat-rate. Apply the entire price to this interval, do not pro-rate the price if the full interval has not occurred/been consumed
    """

    P = "P"
    F = "F"


class Encoding(str, Enum):
    """
    299 - Encoding

    A  No encoding - data are displayable ASCII characters.
    Hex  Hexadecimal encoding - consecutive pairs of hexadecimal digits represent consecutive single octets.
    Base64  Encoding as defined by MIME (Multipurpose Internet Mail Extensions) standard RFC 1521. Four consecutive ASCII characters represent three consecutive octets of binary data. Base64 utilizes a 65-character subset of US-ASCII, consisting of both the upper and
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
    Random  Usually a base64 encoded string of random bits.The uniqueness depends on the length of the bits. Mail systems often generate ASCII string "unique names," from a combination of random bits and system names. Obviously, such identifiers will not be constr
    URI  Uniform Resource Identifier
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
    URI = "URI"
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


class CoverageType(str, Enum):
    """
    309 - Coverage Type

    H  Hospital/institutional
    P  Physician/professional
    B  Both hospital and physician
    RX  Pharmacy
    """

    H = "H"
    P = "P"
    B = "B"
    RX = "RX"


class JobStatus(str, Enum):
    """
    311 - Job Status

    P  Permanent
    T  Temporary
    O  Other
    U  Unknown
    """

    P = "P"
    T = "T"
    O = "O"
    U = "U"


class LivingWillCode(str, Enum):
    """
    315 - Living Will Code

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


class OrganDonorCode(str, Enum):
    """
    316 - Organ Donor Code

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


class DispenseMethod(str, Enum):
    """
    321 - Dispense Method

    TR  Traditional
    UD  Unit Dose
    F  Floor Stock
    AD  Automatic Dispensing
    """

    TR = "TR"
    UD = "UD"
    F = "F"
    AD = "AD"


class CompletionStatus(str, Enum):
    """
    322 - Completion Status

    CP  Complete
    RE  Refused
    NA  Not Administered
    PA  Partially Administered
    """

    CP = "CP"
    RE = "RE"
    NA = "NA"
    PA = "PA"


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


class LocationRelationshipID(str, Enum):
    """
    325 - Location Relationship ID

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


class VisitIndicator(str, Enum):
    """
    326 - Visit Indicator

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


class DisabledPersonCode(str, Enum):
    """
    334 - Disabled Person Code

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
    Q<integer>J<day#>  repeats on a particular day of the week,
    BID  twice a day at institution-specified times
    TID  three times a day at institution-specified times
    QID  four times a day at institution-specified times
    xID  "X" times per day at institution-specified times, where X is a numeral 5 or greater.
    QAM  in the morning at institution-specified time
    QSHIFT  during each of three eight-hour shifts at institution-specified times
    QOD  every other day
    QHS  every day before the hour of sleep
    QPM  in the evening at institution-specified time
    C  service is provided continuously between start time and stop time
    U <spec>  for future use, where  is an interval specification as defined by the UNIX cron specification.
    PRN  given as needed
    PRNxxx  where xxx is some frequency code
    Once  one time only.
    Meal Related Timings  C ("cum")
    A  Ante (before)
    P  Post (after)
    I  Inter
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
    LI  Labor and industries number
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
    LI = "LI"
    L_I = "L&I"
    MCD = "MCD"
    MCR = "MCR"
    QA = "QA"
    SL = "SL"
    TAX = "TAX"
    TRL = "TRL"
    UPIN = "UPIN"


class AdvancedBeneficiaryNoticeCode(str, Enum):
    """
    339 - Advanced Beneficiary Notice Code

    1  Service is subject to medical necessity procedures
    2  Patient has been informed of responsibility, and agrees to pay for service
    3  Patient has been informed of responsibility, and asks that the payer be billed
    4  Advanced Beneficiary Notice has not been signed
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"


class PatientsRelationshiptoInsured(str, Enum):
    """
    344 - Patient s Relationship to Insured

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


class State_province(str, Enum):
    """
         347 - State-province

         AB  Alberta  (US and Canada)
    1312
         MI  Michigan  (US)
    """

    AB = "AB"
    MI = "MI"


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
    ADR_A19  A19
    ADT_A01  A01, A04, A08, A13
    ADT_A02  A02
    ADT_A03  A03
    ADT_A05  A05, A14, A28, A31
    ADT_A06  A06, A07
    ADT_A09  A09, A10, A11
    ADT_A12  A12
    ADT_A15  A15
    ADT_A16  A16
    ADT_A17  A17
    ADT_A18  A18
    ADT_A20  A20
    ADT_A21  A21, A22, A23, A25, A26, A27, A29, A32, A33
    ADT_A24  A24
    ADT_A30  A30, A34, A35, A36, A46, A47, A48, A49
    ADT_A37  A37
    ADT_A38  A38
    ADT_A39  A39, A40, A41, A42
    ADT_A43  A43, A44
    ADT_A45  A45
    ADT_A50  A50, A51
    ADT_A52  A52, A53
    ADT_A54  A54, A55
    ADT_A60  A60
    ADT_A61  A61, A62
    BAR_P01  P01
    BAR_P02  P02
    BAR_P05  P05
    BAR_P06  P06
    BAR_P10  P10
    BAR_P12  P12
    BPS_O29  O29
    BRP_O30  O30
    BRT_O32  O32
    BTS_O31  O31
    CRM_C01  C01, C02, C03, C04, C05, C06, C07, C08
    CSU_C09  C09, C10, C11, C12
    DFT_P03  P03
    DFT_P11  P11
    DOC_T12  T12
    DSR_Q01  Q01
    DSR_Q03  Q03
    EAC_U07  U07
    EAN_U09  U09
    EAR_U08  U08
    EHC_E01  E01
    EHC_E02  E02
    EHC_E04  E04
    EHC_E10  E10
    EHC_E12  E12
    EHC_E13  E13
    EHC_E15  E15
    EHC_E20  E20
    EHC_E21  E21
    EHC_E24  E24
    ESR_U02  U02
    ESU_U01  U01
    INR_U06  U06
    INU_U05  U05
    LSU_U12  U12, U13
    MDM_T01  T01, T03, T05, T07, T09, T11
    MDM_T02  T02, T04, T06, T08, T10
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
    MFN_M13  M13
    MFN_M15  M15
    MFN_M16  M16
    MFN_M17  M17
    MFQ_M01  M01, M02, M03, M04, M05, M06
    MFR_M01  M01, M02, M03,
    MFR_M04  M04
    MFR_M05  M05
    MFR_M06  M06
    MFR_M07  M07
    NMD_N02  N02
    NMQ_N01  N01
    NMR_N01  N01
    OMB_O27  O27
    OMD_O03  O03
    OMG_O19  O19
    OMI_O23  O23
    OML_O21  O21
    OML_O33  O33
    OML_O35  O35
    OMN_O07  O07
    OMP_O09  O09
    OMS_O05  O05
    OPL_O37  O37
    OPR_O38  O38
    OPU_R25  R25
    ORB_O28  O28
    ORD_O04  O04
    ORF_R04  R04
    ORG_O20  O20
    ORI_O24  O24
    ORL_O22  O22
    ORL_O34  O34
    ORL_O36  O36
    ORM_O01  O01
    ORN_O08  O08
    ORP_O10  O10
    ORR_O02  O02
    ORS_O06  O06
    ORU_R01  R01
    ORU_R30  R30
    OSQ_Q06  Q06
    OSR_Q06  Q06
    OUL_R21  R21
    OUL_R22  R22
    OUL_R23  R23
    OUL_R24  R24
    PEX_P07  P07, P08
    PGL_PC6  PC6, PC7, PC8
    PMU_B01  B01, B02
    PMU_B03  B03
    PMU_B04  B04, B05, B06
    PMU_B07  B07
    PMU_B08  B08
    PPG_PCG  PCC, PCG, PCH, PCJ
    PPP_PCB  PCB, PCD
    PPR_PC1  PC1, PC2, PC3
    PPT_PCL  PCL
    PPV_PCA  PCA
    PRR_PC5  PC5
    PTR_PCF  PCF
    QBP_E03  E03
    QBP_E22  E22
    QBP_Q11  Q11
    QBP_Q13  Q13
    QBP_Q15  Q15
    QBP_Q21  Q21, Q22, Q23,Q24, Q25
    QCK_Q02  Q02
    QCN_J01  J01, J02
    QRY_A19  A19
    QRY_PC4  PC4, PC9, PCE, PCK
    QRY_Q01  Q01, Q26, Q27, Q28, Q29, Q30
    QRY_Q02  Q02
    QRY_R02  R02
    QRY_T12  T12
    QSB_Q16  Q16
    QVR_Q17  Q17
    RAR_RAR  RAR
    RAS_O17  O17
    RCI_I05  I05
    RCL_I06  I06
    RDE_O11  O11, O25
    RDR_RDR  RDR
    RDS_O13  O13
    RDY_K15  K15
    REF_I12  I12, I13, I14, I15
    RER_RER  RER
    RGR_RGR  RGR
    RGV_O15  O15
    ROR_ROR  ROR
    RPA_I08  I08, I09. I10, I11
    RPI_I01  I01, I04
    RPI_I04  I04
    RPL_I02  I02
    RPR_I03  I03
    RQA_I08  I08, I09, I10, I11
    RQC_I05  I05, I06
    RQI_I01  I01, I02, I03, I07
    RQP_I04  I04
    RRA_O18  O18
    RRD_O14  O14
    RRE_O12  O12, O26
    RRG_O16  O16
    RRI_I12  I12, I13, I14, I15
    RSP_E03  E03
    RSP_E22  E22
    RSP_K11  K11
    RSP_K21  K21
    RSP_K23  K23, K24
    RSP_K25  K25
    RSP_K31  K31
    RSP_Q11  Q11
    RTB_K13  K13
    SDR_S31  S31, S36
    SDR_S32  S32, S37
    SIU_S12  S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S26
    SLR_S28  S28, S29, S30, S34, S35
    SQM_S25  S25
    SQR_S25  S25
    SRM_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
    SRR_S01  S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11
    SSR_U04  U04
    SSU_U03  U03
    STC_S33  S33
    SUR_P09  P09
    TCU_U10  U10, U11
    UDM_Q05  Q05
    VXQ_V01  V01
    VXR_V03  V03
    VXU_V04  V04
    VXX_V02  V02
    ORU_W01  W01
    QRF_W02  W02
    """

    ACK = "ACK"
    ADR_A19 = "ADR_A19"
    ADT_A01 = "ADT_A01"
    ADT_A02 = "ADT_A02"
    ADT_A03 = "ADT_A03"
    ADT_A05 = "ADT_A05"
    ADT_A06 = "ADT_A06"
    ADT_A09 = "ADT_A09"
    ADT_A12 = "ADT_A12"
    ADT_A15 = "ADT_A15"
    ADT_A16 = "ADT_A16"
    ADT_A17 = "ADT_A17"
    ADT_A18 = "ADT_A18"
    ADT_A20 = "ADT_A20"
    ADT_A21 = "ADT_A21"
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
    BAR_P01 = "BAR_P01"
    BAR_P02 = "BAR_P02"
    BAR_P05 = "BAR_P05"
    BAR_P06 = "BAR_P06"
    BAR_P10 = "BAR_P10"
    BAR_P12 = "BAR_P12"
    BPS_O29 = "BPS_O29"
    BRP_O30 = "BRP_O30"
    BRT_O32 = "BRT_O32"
    BTS_O31 = "BTS_O31"
    CRM_C01 = "CRM_C01"
    CSU_C09 = "CSU_C09"
    DFT_P03 = "DFT_P03"
    DFT_P11 = "DFT_P11"
    DOC_T12 = "DOC_T12"
    DSR_Q01 = "DSR_Q01"
    DSR_Q03 = "DSR_Q03"
    EAC_U07 = "EAC_U07"
    EAN_U09 = "EAN_U09"
    EAR_U08 = "EAR_U08"
    EHC_E01 = "EHC_E01"
    EHC_E02 = "EHC_E02"
    EHC_E04 = "EHC_E04"
    EHC_E10 = "EHC_E10"
    EHC_E12 = "EHC_E12"
    EHC_E13 = "EHC_E13"
    EHC_E15 = "EHC_E15"
    EHC_E20 = "EHC_E20"
    EHC_E21 = "EHC_E21"
    EHC_E24 = "EHC_E24"
    ESR_U02 = "ESR_U02"
    ESU_U01 = "ESU_U01"
    INR_U06 = "INR_U06"
    INU_U05 = "INU_U05"
    LSU_U12 = "LSU_U12"
    MDM_T01 = "MDM_T01"
    MDM_T02 = "MDM_T02"
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
    MFN_M13 = "MFN_M13"
    MFN_M15 = "MFN_M15"
    MFN_M16 = "MFN_M16"
    MFN_M17 = "MFN_M17"
    MFQ_M01 = "MFQ_M01"
    MFR_M01 = "MFR_M01"
    MFR_M04 = "MFR_M04"
    MFR_M05 = "MFR_M05"
    MFR_M06 = "MFR_M06"
    MFR_M07 = "MFR_M07"
    NMD_N02 = "NMD_N02"
    NMQ_N01 = "NMQ_N01"
    NMR_N01 = "NMR_N01"
    OMB_O27 = "OMB_O27"
    OMD_O03 = "OMD_O03"
    OMG_O19 = "OMG_O19"
    OMI_O23 = "OMI_O23"
    OML_O21 = "OML_O21"
    OML_O33 = "OML_O33"
    OML_O35 = "OML_O35"
    OMN_O07 = "OMN_O07"
    OMP_O09 = "OMP_O09"
    OMS_O05 = "OMS_O05"
    OPL_O37 = "OPL_O37"
    OPR_O38 = "OPR_O38"
    OPU_R25 = "OPU_R25"
    ORB_O28 = "ORB_O28"
    ORD_O04 = "ORD_O04"
    ORF_R04 = "ORF_R04"
    ORG_O20 = "ORG_O20"
    ORI_O24 = "ORI_O24"
    ORL_O22 = "ORL_O22"
    ORL_O34 = "ORL_O34"
    ORL_O36 = "ORL_O36"
    ORM_O01 = "ORM_O01"
    ORN_O08 = "ORN_O08"
    ORP_O10 = "ORP_O10"
    ORR_O02 = "ORR_O02"
    ORS_O06 = "ORS_O06"
    ORU_R01 = "ORU_R01"
    ORU_R30 = "ORU_R30"
    OSQ_Q06 = "OSQ_Q06"
    OSR_Q06 = "OSR_Q06"
    OUL_R21 = "OUL_R21"
    OUL_R22 = "OUL_R22"
    OUL_R23 = "OUL_R23"
    OUL_R24 = "OUL_R24"
    PEX_P07 = "PEX_P07"
    PGL_PC6 = "PGL_PC6"
    PMU_B01 = "PMU_B01"
    PMU_B03 = "PMU_B03"
    PMU_B04 = "PMU_B04"
    PMU_B07 = "PMU_B07"
    PMU_B08 = "PMU_B08"
    PPG_PCG = "PPG_PCG"
    PPP_PCB = "PPP_PCB"
    PPR_PC1 = "PPR_PC1"
    PPT_PCL = "PPT_PCL"
    PPV_PCA = "PPV_PCA"
    PRR_PC5 = "PRR_PC5"
    PTR_PCF = "PTR_PCF"
    QBP_E03 = "QBP_E03"
    QBP_E22 = "QBP_E22"
    QBP_Q11 = "QBP_Q11"
    QBP_Q13 = "QBP_Q13"
    QBP_Q15 = "QBP_Q15"
    QBP_Q21 = "QBP_Q21"
    QCK_Q02 = "QCK_Q02"
    QCN_J01 = "QCN_J01"
    QRY_A19 = "QRY_A19"
    QRY_PC4 = "QRY_PC4"
    QRY_Q01 = "QRY_Q01"
    QRY_Q02 = "QRY_Q02"
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
    RDY_K15 = "RDY_K15"
    REF_I12 = "REF_I12"
    RER_RER = "RER_RER"
    RGR_RGR = "RGR_RGR"
    RGV_O15 = "RGV_O15"
    ROR_ROR = "ROR_ROR"
    RPA_I08 = "RPA_I08"
    RPI_I01 = "RPI_I01"
    RPI_I04 = "RPI_I04"
    RPL_I02 = "RPL_I02"
    RPR_I03 = "RPR_I03"
    RQA_I08 = "RQA_I08"
    RQC_I05 = "RQC_I05"
    RQI_I01 = "RQI_I01"
    RQP_I04 = "RQP_I04"
    RRA_O18 = "RRA_O18"
    RRD_O14 = "RRD_O14"
    RRE_O12 = "RRE_O12"
    RRG_O16 = "RRG_O16"
    RRI_I12 = "RRI_I12"
    RSP_E03 = "RSP_E03"
    RSP_E22 = "RSP_E22"
    RSP_K11 = "RSP_K11"
    RSP_K21 = "RSP_K21"
    RSP_K23 = "RSP_K23"
    RSP_K25 = "RSP_K25"
    RSP_K31 = "RSP_K31"
    RSP_Q11 = "RSP_Q11"
    RTB_K13 = "RTB_K13"
    SDR_S31 = "SDR_S31"
    SDR_S32 = "SDR_S32"
    SIU_S12 = "SIU_S12"
    SLR_S28 = "SLR_S28"
    SQM_S25 = "SQM_S25"
    SQR_S25 = "SQR_S25"
    SRM_S01 = "SRM_S01"
    SRR_S01 = "SRR_S01"
    SSR_U04 = "SSR_U04"
    SSU_U03 = "SSU_U03"
    STC_S33 = "STC_S33"
    SUR_P09 = "SUR_P09"
    TCU_U10 = "TCU_U10"
    UDM_Q05 = "UDM_Q05"
    VXQ_V01 = "VXQ_V01"
    VXR_V03 = "VXR_V03"
    VXU_V04 = "VXU_V04"
    VXX_V02 = "VXX_V02"
    ORU_W01 = "ORU_W01"
    QRF_W02 = "QRF_W02"


class Primarykeyvaluetype(str, Enum):
    """
    355 - Primary key value type

    PL  Person location
    CE  Coded element
    CWE  Coded with Exceptions
    """

    PL = "PL"
    CE = "CE"
    CWE = "CWE"


class Alternatecharactersethandlingscheme(str, Enum):
    """
    356 - Alternate character set handling scheme

    ISO 2022-1994  This standard is titled "Information Technology - Character Code Structure and Extension Technique". .
    2.3  The character set switching mode specified in HL7 2.5, section 2.7.2, "Escape sequences supporting multiple character sets" and section 2.A.46, "XPN - extended person name".
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


class DiagnosisPriority(str, Enum):
    """
         359 - Diagnosis Priority

         0  Not included in diagnosis ranking
         1  The primary diagnosis
         2  For ranked secondary diagnoses
    1312
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class Degree_license_certificate(str, Enum):
    """
    360 - Degree-license-certificate

    PN  Advanced Practice Nurse
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
    BSN  Bachelor on Science - Nursing
    BT  Bachelor of Theology
    CER  Certificate
    CANP  Certified Adult Nurse Practitioner
    CMA  Certified Medical Assistant
    CNP  Certified Nurse Practitioner
    CNM  Certified Nurse Midwife
    CRN  Certified Registered Nurse
    CNS  Certified Nurse Specialist
    CPNP  Certified Pediatric Nurse Practitioner
    DIP  Diploma
    DBA  Doctor of Business Administration
    DED  Doctor of Education
    PharmD  Doctor of Pharmacy
    PHE  Doctor of Engineering
    PHD  Doctor of Philosophy
    PHS  Doctor of Science
    MD  Doctor of Medicine
    DO  Doctor of Osteopathy
    EMT  Emergency Medical Technician
    EMTP  Emergency Medical Technician - Paramedic
    FPNP  Family Practice Nurse Practitioner
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
    MSN  Master of Science - Nursing
    MT  Master of Theology
    MDA  Medical Assistant
    NG  Non-Graduate
    NP  Nurse Practitioner
    PA  Physician Assistant
    RMA  Registered Medical Assistant
    RPH  Registered Pharmacist
    SEC  Secretarial Certificate
    TS  Trade School Graduate
    """

    PN = "PN"
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
    BSN = "BSN"
    BT = "BT"
    CER = "CER"
    CANP = "CANP"
    CMA = "CMA"
    CNP = "CNP"
    CNM = "CNM"
    CRN = "CRN"
    CNS = "CNS"
    CPNP = "CPNP"
    DIP = "DIP"
    DBA = "DBA"
    DED = "DED"
    PharmD = "PharmD"
    PHE = "PHE"
    PHD = "PHD"
    PHS = "PHS"
    MD = "MD"
    DO = "DO"
    EMT = "EMT"
    EMTP = "EMTP"
    FPNP = "FPNP"
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
    MSN = "MSN"
    MT = "MT"
    MDA = "MDA"
    NG = "NG"
    NP = "NP"
    PA = "PA"
    RMA = "RMA"
    RPH = "RPH"
    SEC = "SEC"
    TS = "TS"


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
    1312
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
    1312
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
    1312
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


class SpecimenRole(str, Enum):
    """
    369 - Specimen Role

    B  Blind Sample
    C  Calibrator, used for initial setting of calibration
    E  Electronic QC, used with manufactured reference providing signals that simulate QC results
    F  Specimen used for testing proficiency of the organization performing the testing (Filler)
    G  Group (where a specimen consists of multiple individual elements that are not individually identified)
    L  Pool (aliquots of individual specimens combined to form a single specimen representing all of the components.)
    O  Specimen used for testing Operator Proficiency
    P  Patient (default if blank component value)
    Q  Control specimen
    R  Replicate (of patient sample as a control)
    V  Verifying Calibrator, used for periodic calibration checks
    """

    B = "B"
    C = "C"
    E = "E"
    F = "F"
    G = "G"
    L = "L"
    O = "O"
    P = "P"
    Q = "Q"
    R = "R"
    V = "V"


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


class Additive_Preservative(str, Enum):
    """
    371 - Additive-Preservative

    F10  10% Formalin
    C32  3.2%  Citrate
    C38  3.8% Citrate
    HCL6  6N HCL
    ACDA  ACD Solution A
    ACDB  ACD Solution B
    ACET  Acetic Acid
    AMIES  Amies transport medium
    HEPA  Ammonium heparin
    BACTM  Bacterial Transport medium
    BOR  Borate Boric Acid
    BOUIN  Bouin's solution
    BF10  Buffered 10% formalin
    WEST  Buffered Citrate (Westergren Sedimentation Rate)
    BSKM  Buffered skim milk
    CARS  Carson's Modified 10% formalin
    CARY  Cary Blair Medium
    CHLTM  Chlamydia transport medium
    CTAD  CTAD (this should be spelled out if not universally understood)
    ENT  Enteric bacteria transport medium
    ENT+  Enteric plus
    JKM  Jones Kendrick Medium
    KARN  Karnovsky's fixative
    LIA  Lithium iodoacetate
    HEPL  Lithium/Li  Heparin
    M4  M4
    M4RT  M4-RT
    M5  M5
    MICHTM  Michel's transport medium
    MMDTM  MMD transport medium
    HNO3  Nitric Acid
    NONE  None
    PAGE  Pages's Saline
    PHENOL  Phenol
    KOX  Potassium Oxalate
    EDTK  Potassium/K EDTA
    EDTK15  Potassium/K EDTA 15%
    EDTK75  Potassium/K EDTA 7.5%
    PVA  PVA (polyvinylalcohol)
    RLM  Reagan Lowe Medium
    SST  Serum Separator Tube (Polymer Gel)
    SILICA  Siliceous earth, 12 mg
    NAF  Sodium Fluoride
    FL100  Sodium Fluoride, 100mg
    FL10  Sodium Fluoride, 10mg
    NAPS  Sodium polyanethol sulfonate 0.35% in 0.85% sodium chloride
    HEPN  Sodium/Na  Heparin
    EDTN  Sodium/Na EDTA
    SPS  SPS(this should be spelled out if not universally understood)
    STUTM  Stuart transport medium
    THROM  Thrombin
    FDP  Thrombin NIH; soybean trypsin inhibitor (Fibrin Degradation Products)
    THYMOL  Thymol
    THYO  Thyoglycollate broth
    TOLU  Toluene
    URETM  Ureaplasma transport medium
    VIRTM  Viral Transport medium
    """

    F10 = "F10"
    C32 = "C32"
    C38 = "C38"
    HCL6 = "HCL6"
    ACDA = "ACDA"
    ACDB = "ACDB"
    ACET = "ACET"
    AMIES = "AMIES"
    HEPA = "HEPA"
    BACTM = "BACTM"
    BOR = "BOR"
    BOUIN = "BOUIN"
    BF10 = "BF10"
    WEST = "WEST"
    BSKM = "BSKM"
    CARS = "CARS"
    CARY = "CARY"
    CHLTM = "CHLTM"
    CTAD = "CTAD"
    ENT = "ENT"
    ENT_ = "ENT+"
    JKM = "JKM"
    KARN = "KARN"
    LIA = "LIA"
    HEPL = "HEPL"
    M4 = "M4"
    M4RT = "M4RT"
    M5 = "M5"
    MICHTM = "MICHTM"
    MMDTM = "MMDTM"
    HNO3 = "HNO3"
    NONE = "NONE"
    PAGE = "PAGE"
    PHENOL = "PHENOL"
    KOX = "KOX"
    EDTK = "EDTK"
    EDTK15 = "EDTK15"
    EDTK75 = "EDTK75"
    PVA = "PVA"
    RLM = "RLM"
    SST = "SST"
    SILICA = "SILICA"
    NAF = "NAF"
    FL100 = "FL100"
    FL10 = "FL10"
    NAPS = "NAPS"
    HEPN = "HEPN"
    EDTN = "EDTN"
    SPS = "SPS"
    STUTM = "STUTM"
    THROM = "THROM"
    FDP = "FDP"
    THYMOL = "THYMOL"
    THYO = "THYO"
    TOLU = "TOLU"
    URETM = "URETM"
    VIRTM = "VIRTM"


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


class SpecialHandlingCode(str, Enum):
    """
    376 - Special Handling Code

    C37  Body temperature
    AMB  Ambient temperature
    CAMB  Critical ambient temperature
    REF  Refrigerated temperature
    CREF  Critical refrigerated temperature
    FRZ  Frozen temperature
    CFRZ  Critical frozen temperature
    DFRZ  Deep frozen
    UFRZ  Ultra frozen
    NTR  Liquid nitrogen
    PRTL  Protect from light
    CATM  Protect from air
    DRY  Dry
    PSO  No shock
    PSA  Do not shake
    UPR  Upright
    MTLF  Metal Free
    """

    C37 = "C37"
    AMB = "AMB"
    CAMB = "CAMB"
    REF = "REF"
    CREF = "CREF"
    FRZ = "FRZ"
    CFRZ = "CFRZ"
    DFRZ = "DFRZ"
    UFRZ = "UFRZ"
    NTR = "NTR"
    PRTL = "PRTL"
    CATM = "CATM"
    DRY = "DRY"
    PSO = "PSO"
    PSA = "PSA"
    UPR = "UPR"
    MTLF = "MTLF"


class Otherenvironmentalfactors(str, Enum):
    """
    377 - Other environmental factors

    ATM  Opened container, atmosphere and duration unspecified
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
    MR  Multiple Test Reagent
    DI  Diluent
    PT  Pretreatment
    RC  Reagent Calibrator
    CO  Control
    PW  Purified Water
    LW  Liquid Waste
    SW  Solid Waste
    SC  Countable Solid Item
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
    ER  Command cannot be completed because of error condition
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

    FINANCIAL_COMMON_ORDER
    ADMINISTRATION
    ALLERGY
    APP_STATS
    APP_STATUS
    ASSOCIATED_PERSON
    ASSOCIATED_RX_ADMIN
    ASSOCIATED_RX_ORDER
    AUTHORIZATION
    AUTHORIZATION_CONTACT
    CERTIFICATE
    CLOCK
    CLOCK_AND_STATISTICS
    CLOCK_AND_STATS_WITH_NOTE
    COMMAND
    COMMAND_RESPONSE
    COMMON_ORDER
    COMPONENT
    COMPONENTS
    CONTAINER
    DEFINITION
    DIET
    DISPENSE
    ENCODED ORDER
    ENCODED_ORDER
    ENCODING
    EXPERIENCE
    FINANCIAL
    FINANCIAL_COMMON ORDER
    FINANCIAL_INSURANCE
    FINANCIAL_OBSERVATION
    FINANCIAL_ORDER
    FINANCIAL_PROCEDURE
    FINANCIAL_TIMING QUANTITY
    FINANCIAL_TIMING_QUANTITY
    GENERAL RESOURCE
    GENERAL_RESOURCE
    GIVE
    GOAL
    GOAL_OBSERVATION
    GOAL_PATHWAY
    GOAL_ROLE
    GUARANTOR_INSURANCE
    INSURANCE
    LOCATION RESOURCE
    LOCATION_RESOURCE
    MERGE_INFO
    MF
    MF_CDM
    MF_CLIN_STUDY
    MF_CLIN_STUDY_SCHED
    MF_INV_ITEM
    MF_LOC_DEPT
    MF_LOCATION
    MF_OBS_ATTRIBUTES
    MF_PHASE_SCHED_DETAIL
    MF_QUERY
    MF_SITE_DEFINED
    MF_STAFF
    MF_TEST
    MF_TEST_BATT_DETAIL
    MF_TEST_BATTERIES
    MF_TEST_CALC_DETAIL
    MF_TEST_CALCULATED
    MF_TEST_CAT_DETAIL
    MF_TEST_CATEGORICAL
    MF_TEST_NUMERIC
    NK1_TIMING_QTY
    NOTIFICATION
    OBSERVATION
    OBSERVATION_PRIOR
    OBSERVATION_REQUEST
    OMSERVATION
    ORDER
    ORDER_CHOICE
    ORDER_DETAIL
    ORDER_DETAIL_SUPPLEMENT
    ORDER_DIET
    ORDER_ENCODED
    ORDER_OBSERVATION
    ORDER_PRIOR
    ORDER_TRAY
    PATHWAY
    PATHWAY_ROLE
    PATIENT
    PATIENT VISIT
    PATIENT_PRIOR
    PATIENT_RESULT
    PATIENT_VISIT
    PATIENT_VISIT_PRIOR
    PERSONNEL RESOURCE
    PERSONNEL_RESOURCE
    PEX_CAUSE
    PEX_OBSERVATION
    PRIOR_RESULT
    PROBLEM
    PROBLEM_OBSERVATION
    PROBLEM_PATHWAY
    PROBLEM_ROLE
    PROCEDURE
    PRODUCT
    PRODUCT_STATUS
    PROVIDER
    PROVIDER_CONTACT
    QBP
    QRY_WITH_DETAIL
    QUERY_RESPONSE
    QUERY_RESULT_CLUSTER
    REQUEST
    RESOURCE
    RESOURCES
    RESPONSE
    RESULT
    RESULTS
    RESULTS_NOTES
    ROW_DEFINITION
    RX_ADMINISTRATION
    RX_ORDER
    SCHEDULE
    SERVICE
    SPECIMEN
    SPECIMEN_CONTAINER
    STAFF
    STUDY
    STUDY_OBSERVATION
    STUDY_PHASE
    STUDY_SCHEDULE
    TEST_CONFIGURATION
    TIMING
    TIMING_DIET
    TIMING_ENCODED
    TIMING_GIVE
    TIMING_PRIOR
    TIMING_QTY
    TIMING_QUANTITY
    TIMING_TRAY
    TREATMENT
    VISIT
    """

    FINANCIAL_COMMON_ORDER = "FINANCIAL_COMMON_ORDER"
    ADMINISTRATION = "ADMINISTRATION"
    ALLERGY = "ALLERGY"
    APP_STATS = "APP_STATS"
    APP_STATUS = "APP_STATUS"
    ASSOCIATED_PERSON = "ASSOCIATED_PERSON"
    ASSOCIATED_RX_ADMIN = "ASSOCIATED_RX_ADMIN"
    ASSOCIATED_RX_ORDER = "ASSOCIATED_RX_ORDER"
    AUTHORIZATION = "AUTHORIZATION"
    AUTHORIZATION_CONTACT = "AUTHORIZATION_CONTACT"
    CERTIFICATE = "CERTIFICATE"
    CLOCK = "CLOCK"
    CLOCK_AND_STATISTICS = "CLOCK_AND_STATISTICS"
    CLOCK_AND_STATS_WITH_NOTE = "CLOCK_AND_STATS_WITH_NOTE"
    COMMAND = "COMMAND"
    COMMAND_RESPONSE = "COMMAND_RESPONSE"
    COMMON_ORDER = "COMMON_ORDER"
    COMPONENT = "COMPONENT"
    COMPONENTS = "COMPONENTS"
    CONTAINER = "CONTAINER"
    DEFINITION = "DEFINITION"
    DIET = "DIET"
    DISPENSE = "DISPENSE"
    ENCODED_ORDER = "ENCODED ORDER"
    ENCODED_ORDER_2 = "ENCODED_ORDER_2"
    ENCODING = "ENCODING"
    EXPERIENCE = "EXPERIENCE"
    FINANCIAL = "FINANCIAL"
    FINANCIAL_COMMMON_ORDER = "FINANCIAL_COMMMON ORDER"
    FINANCIAL_INSURANCE = "FINANCIAL_INSURANCE"
    FINANCIAL_OBSERVATION = "FINANCIAL_OBSERVATION"
    FINANCIAL_ORDER = "FINANCIAL_ORDER"
    FINANCIAL_PROCEDURE = "FINANCIAL_PROCEDURE"
    FINANCIAL_TIMING_QUANTITY = "FINANCIAL_TIMING QUANTITY"
    FINANCIAL_TIMING_QUANTITY_2 = "FINANCIAL_TIMING_QUANTITY_2"
    GENERAL_RESOURCE = "GENERAL RESOURCE"
    GENERAL_RESOURCE_2 = "GENERAL_RESOURCE_2"
    GIVE = "GIVE"
    GOAL = "GOAL"
    GOAL_OBSERVATION = "GOAL_OBSERVATION"
    GOAL_PATHWAY = "GOAL_PATHWAY"
    GOAL_ROLE = "GOAL_ROLE"
    GUARANTOR_INSURANCE = "GUARANTOR_INSURANCE"
    INSURANCE = "INSURANCE"
    LOCATION_RESOURCE = "LOCATION RESOURCE"
    LOCATION_RESOURCE_2 = "LOCATION_RESOURCE_2"
    MERGE_INFO = "MERGE_INFO"
    MF = "MF"
    MF_CDM = "MF_CDM"
    MF_CLIN_STUDY = "MF_CLIN_STUDY"
    MF_CLIN_STUDY_SCHED = "MF_CLIN_STUDY_SCHED"
    MF_INV_ITEM = "MF_INV_ITEM"
    MF_LOC_DEPT = "MF_LOC_DEPT"
    MF_LOCATION = "MF_LOCATION"
    MF_OBS_ATTRIBUTES = "MF_OBS_ATTRIBUTES"
    MF_PHASE_SCHED_DETAIL = "MF_PHASE_SCHED_DETAIL"
    MF_QUERY = "MF_QUERY"
    MF_SITE_DEFINED = "MF_SITE_DEFINED"
    MF_STAFF = "MF_STAFF"
    MF_TEST = "MF_TEST"
    MF_TEST_BATT_DETAIL = "MF_TEST_BATT_DETAIL"
    MF_TEST_BATTERIES = "MF_TEST_BATTERIES"
    MF_TEST_CALC_DETAIL = "MF_TEST_CALC_DETAIL"
    MF_TEST_CALCULATED = "MF_TEST_CALCULATED"
    MF_TEST_CAT_DETAIL = "MF_TEST_CAT_DETAIL"
    MF_TEST_CATEGORICAL = "MF_TEST_CATEGORICAL"
    MF_TEST_NUMERIC = "MF_TEST_NUMERIC"
    NK1_TIMING_QTY = "NK1_TIMING_QTY"
    NOTIFICATION = "NOTIFICATION"
    OBSERVATION = "OBSERVATION"
    OBSERVATION_PRIOR = "OBSERVATION_PRIOR"
    OBSERVATION_REQUEST = "OBSERVATION_REQUEST"
    OMSERVATION = "OMSERVATION"
    ORDER = "ORDER"
    ORDER_CHOICE = "ORDER_CHOICE"
    ORDER_DETAIL = "ORDER_DETAIL"
    ORDER_DETAIL_SUPPLEMENT = "ORDER_DETAIL_SUPPLEMENT"
    ORDER_DIET = "ORDER_DIET"
    ORDER_ENCODED = "ORDER_ENCODED"
    ORDER_OBSERVATION = "ORDER_OBSERVATION"
    ORDER_PRIOR = "ORDER_PRIOR"
    ORDER_TRAY = "ORDER_TRAY"
    PATHWAY = "PATHWAY"
    PATHWAY_ROLE = "PATHWAY_ROLE"
    PATIENT = "PATIENT"
    PATIENT_VISIT = "PATIENT VISIT"
    PATIENT_PRIOR = "PATIENT_PRIOR"
    PATIENT_RESULT = "PATIENT_RESULT"
    PATIENT_VISIT_2 = "PATIENT_VISIT"
    PATIENT_VISIT_PRIOR = "PATIENT_VISIT_PRIOR"
    PERSONNEL_RESOURCE = "PERSONNEL RESOURCE"
    PERSONNEL_RESOURCE_2 = "PERSONNEL_RESOURCE"
    PEX_CAUSE = "PEX_CAUSE"
    PEX_OBSERVATION = "PEX_OBSERVATION"
    PRIOR_RESULT = "PRIOR_RESULT"
    PROBLEM = "PROBLEM"
    PROBLEM_OBSERVATION = "PROBLEM_OBSERVATION"
    PROBLEM_PATHWAY = "PROBLEM_PATHWAY"
    PROBLEM_ROLE = "PROBLEM_ROLE"
    PROCEDURE = "PROCEDURE"
    PRODUCT = "PRODUCT"
    PRODUCT_STATUS = "PRODUCT_STATUS"
    PROVIDER = "PROVIDER"
    PROVIDER_CONTACT = "PROVIDER_CONTACT"
    QBP = "QBP"
    QRY_WITH_DETAIL = "QRY_WITH_DETAIL"
    QUERY_RESPONSE = "QUERY_RESPONSE"
    QUERY_RESULT_CLUSTER = "QUERY_RESULT_CLUSTER"
    REQUEST = "REQUEST"
    RESOURCE = "RESOURCE"
    RESOURCES = "RESOURCES"
    RESPONSE = "RESPONSE"
    RESULT = "RESULT"
    RESULTS = "RESULTS"
    RESULTS_NOTES = "RESULTS_NOTES"
    ROW_DEFINITION = "ROW_DEFINITION"
    RX_ADMINISTRATION = "RX_ADMINISTRATION"
    RX_ORDER = "RX_ORDER"
    SCHEDULE = "SCHEDULE"
    SERVICE = "SERVICE"
    SPECIMEN = "SPECIMEN"
    SPECIMEN_CONTAINER = "SPECIMEN_CONTAINER"
    STAFF = "STAFF"
    STUDY = "STUDY"
    STUDY_OBSERVATION = "STUDY_OBSERVATION"
    STUDY_PHASE = "STUDY_PHASE"
    STUDY_SCHEDULE = "STUDY_SCHEDULE"
    TEST_CONFIGURATION = "TEST_CONFIGURATION"
    TIMING = "TIMING"
    TIMING_DIET = "TIMING_DIET"
    TIMING_ENCODED = "TIMING_ENCODED"
    TIMING_GIVE = "TIMING_GIVE"
    TIMING_PRIOR = "TIMING_PRIOR"
    TIMING_QTY = "TIMING_QTY"
    TIMING_QUANTITY = "TIMING_QUANTITY"
    TIMING_TRAY = "TIMING_TRAY"
    TREATMENT = "TREATMENT"
    VISIT = "VISIT"


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

    LINKSOFT_2.01  Proprietary algorithm for LinkSoft v2.01
    MATCHWARE_1.2  Proprietary algorithm for MatchWare v1.2
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


class Codingsystem(str, Enum):
    """
    396 - Coding system

    99zzz or L  Local general code (where z is an alphanumeric character)
    ACR  American College of Radiology finding codes
    ALPHAID2006  German Alpha-ID v2006
    ALPHAID2007  German Alpha-ID v2007
    ALPHAID2008  German Alpha-ID v2008
    ART  WHO Adverse Reaction Terms
    ANS+  HL7 set of units of measure
    AS4  ASTM E1238/ E1467 Universal
    AS4E  AS4 Neurophysiology Codes
    ATC  American Type Culture Collection
    C4  CPT-4
    C5  CPT-5
    CAS  Chemical abstract codes
    CCC  Clinical Care Classification system
    CD2  CDT-2 Codes
    CDCA  CDC Analyte Codes
    CDCM  CDC Methods/Instruments Codes
    CDS  CDC Surveillance
    CE (obsolete)  CEN ECG diagnostic codes
    CLP  CLIP
    CPTM  CPT Modifier Code
    CST  COSTART
    CVX  CDC Vaccine Codes
    DCM  DICOM Controlled Terminology
    E  EUCLIDES
    E5  Euclides  quantity codes
    E6  Euclides Lab method codes
    E7  Euclides Lab equipment codes
    ENZC  Enzyme Codes
    FDDC  First DataBank Drug Codes
    FDDX  First DataBank Diagnostic Codes
    FDK  FDA K10
    GDRG2004  G-DRG German DRG Codes v2004
    GDRG2005  G-DRG German DRG Codes v2005
    GDRG2006  G-DRG German DRG Codes v2006
    GDRG2007  G-DRG German DRG Codes v2007
    GDRG2008  G-DRG German DRG Codes v2008
    GMDC2004  German Major Diagnostic Codes v2004
    GMDC2005  German Major Diagnostic Codes v2005
    GMDC2006  German Major Diagnostic Codes v2006
    GMDC2007  German Major Diagnostic Codes v2007
    GMDC2008  German Major Diagnostic Codes v2008
    HB  HIBCC
    HCPCS  CMS (formerly HCFA)  Common Procedure Coding System
    HCPT  Health Care Provider Taxonomy
    HHC  Home Health Care
    HI  Health Outcomes
    HL7nnnn  HL7 Defined Codes where nnnn is the HL7 table number
    HOT  Japanese Nationwide Medicine Code
    HPC  CMS (formerly HCFA )Procedure Codes (HCPCS)
    I10  ICD-10
    I10P  ICD-10  Procedure Codes
    I9  ICD9
    I9C  ICD-9CM
    I9CDX  ICD-9CM Diagnosis codes
    I9CP  ICD-9CM Procedure codes
    IBT  ISBT
    IBTnnnn  ISBT 128 codes where nnnn  specifies a specific table within ISBT 128.
    I10G2004  ICD 10 Germany v2004
    I10G2005  ICD 10 Germany v2005
    I10G2006  ICD 10 Germany v2006
    ICD10GM2007  ICD 10 Germany v2007
    ICD10GM2008  ICD 10 Germany v2008
    ICD10AM  ICD-10 Australian modification
    ICD10CA  ICD-10 Canada
    ICDO  International Classification of Diseases for Oncology
    ICS  ICCS
    ICSD  International Classification of Sleep Disorders
    ISOnnnn  ISO Defined Codes where nnnn is the ISO table number
    ISO+  ISO 2955.83 (units of measure) with HL7 extensions
    ITIS  Integrated Taxonomic Information System
    IUPP  IUPAC/IFCC Property Codes
    IUPC  IUPAC/IFCC Component Codes
    JC8  Japanese Chemistry
    JC10  JLAC/JSLM, nationwide laboratory code
    JJ1017  Japanese Image Examination Cache
    LB  Local billing code
    LN  Logical Observation Identifier Names and Codes (LOINCÂ®)
    MCD  Medicaid
    MCR  Medicare
    MDC  Medical Device Communication
    MDDX  Medispan Diagnostic Codes
    MEDC  Medical Economics Drug Codes
    MEDR  Medical Dictionary for Drug Regulatory Affairs (MEDDRA)
    MEDX  Medical Economics Diagnostic Codes
    MGPI  Medispan GPI
    MVX  CDC Vaccine Manufacturer Codes
    NCPDPnnnnsss  NCPDP code list for data element nnnn [as used in segment sss]
    NDA  NANDA
    NDC  National drug codes
    NIC  Nursing Interventions Classification
    NPI  National Provider Identifier
    NUBC  National Uniform Billing Committee Code
    OHA  Omaha System
    O301  German Procedure Codes
    O3012004  OPS Germany v2004
    O3012005  OPS Germany v2005
    O3012006  OPS Germany v2006
    OPS2007  OPS Germany v2007
    OPS2008  OPS Germany v2008
    POS  POS Codes
    RC  Read Classification
    SCT  SNOMED Clinical Terms
    SCT2  SNOMED Clinical Terms alphanumeric codes
    SDM  SNOMED- DICOM Microglossary
    SNM  Systemized Nomenclature of Medicine (SNOMED)
    SNM3  SNOMED International
    SNT  SNOMED topology codes (anatomic sites)
    UB04FL14  Priority (Type) of Visit
    UB04FL15  Point of Origin
    UB04FL17  Patient Discharge Status
    UC  UCDS
    UCUM  UCUM code set for units of measure(from Regenstrief)
    UMD  MDNS
    UML  Unified Medical Language
    UPC  Universal Product Code
    UPIN  UPIN
    USPS  United States Postal Service
    W1  WHO record # drug codes (6 digit)
    W2  WHO record # drug codes (8 digit)
    W4  WHO record # code with ASTM extension
    WC  WHO ATC
    X12DEnnnn  ASC X12 Code List nnnn
    """

    _99zzz___L = "99zzz or L"
    ACR = "ACR"
    ALPHAID2006 = "ALPHAID2006"
    ALPHAID2007 = "ALPHAID2007"
    ALPHAID2008 = "ALPHAID2008"
    ART = "ART"
    ANS_ = "ANS+"
    AS4 = "AS4"
    AS4E = "AS4E"
    ATC = "ATC"
    C4 = "C4"
    C5 = "C5"
    CAS = "CAS"
    CCC = "CCC"
    CD2 = "CD2"
    CDCA = "CDCA"
    CDCM = "CDCM"
    CDS = "CDS"
    CE_OBSOLETE = "CE (obsolete)"
    CLP = "CLP"
    CPTM = "CPTM"
    CST = "CST"
    CVX = "CVX"
    DCM = "DCM"
    E = "E"
    E5 = "E5"
    E6 = "E6"
    E7 = "E7"
    ENZC = "ENZC"
    FDDC = "FDDC"
    FDDX = "FDDX"
    FDK = "FDK"
    GDRG2004 = "GDRG2004"
    GDRG2005 = "GDRG2005"
    GDRG2006 = "GDRG2006"
    GDRG2007 = "GDRG2007"
    GDRG2008 = "GDRG2008"
    GMDC2004 = "GMDC2004"
    GMDC2005 = "GMDC2005"
    GMDC2006 = "GMDC2006"
    GMDC2007 = "GMDC2007"
    GMDC2008 = "GMDC2008"
    HB = "HB"
    HCPCS = "HCPCS"
    HCPT = "HCPT"
    HHC = "HHC"
    HI = "HI"
    HL7nnnn = "HL7nnnn"
    HOT = "HOT"
    HPC = "HPC"
    I10 = "I10"
    I10P = "I10P"
    I9 = "I9"
    I9C = "I9C"
    I9CDX = "I9CDX"
    I9CP = "I9CP"
    IBT = "IBT"
    IBTnnnn = "IBTnnnn"
    I10G2004 = "I10G2004"
    I10G2005 = "I10G2005"
    I10G2006 = "I10G2006"
    ICD10GM2007 = "ICD10GM2007"
    ICD10GM2008 = "ICD10GM2008"
    ICD10AM = "ICD10AM"
    ICD10CA = "ICD10CA"
    ICDO = "ICDO"
    ICS = "ICS"
    ICSD = "ICSD"
    ISOnnnn = "ISOnnnn"
    ISO_ = "ISO+"
    ITIS = "ITIS"
    IUPP = "IUPP"
    IUPC = "IUPC"
    JC8 = "JC8"
    JC10 = "JC10"
    JJ1017 = "JJ1017"
    LB = "LB"
    LN = "LN"
    MCD = "MCD"
    MCR = "MCR"
    MDC = "MDC"
    MDDX = "MDDX"
    MEDC = "MEDC"
    MEDR = "MEDR"
    MEDX = "MEDX"
    MGPI = "MGPI"
    MVX = "MVX"
    NCPDPnnnnsss = "NCPDPnnnnsss"
    NDA = "NDA"
    NDC = "NDC"
    NIC = "NIC"
    NPI = "NPI"
    NUBC = "NUBC"
    OHA = "OHA"
    O301 = "O301"
    O3012004 = "O3012004"
    O3012005 = "O3012005"
    O3012006 = "O3012006"
    OPS2007 = "OPS2007"
    OPS2008 = "OPS2008"
    POS = "POS"
    RC = "RC"
    SCT = "SCT"
    SCT2 = "SCT2"
    SDM = "SDM"
    SNM = "SNM"
    SNM3 = "SNM3"
    SNT = "SNT"
    UB04FL14 = "UB04FL14"
    UB04FL15 = "UB04FL15"
    UB04FL17 = "UB04FL17"
    UC = "UC"
    UCUM = "UCUM"
    UMD = "UMD"
    UML = "UML"
    UPC = "UPC"
    UPIN = "UPIN"
    USPS = "USPS"
    W1 = "W1"
    W2 = "W2"
    W4 = "W4"
    WC = "WC"
    X12DEnnnn = "X12DEnnnn"


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


class CountryCode(str, Enum):
    """
     0399 - Country Code

    ABW	 Aruba
    AFG	 Afghanistan
    AGO	 Angola
    AIA	 Anguilla
    ALA	 Åland Islands
    ALB	 Albania
    AND	 Andorra
    ARE	 United Arab Emirates
    ARG	 Argentina
    ARM	 Armenia
    ASM	 American Samoa
    ATA	 Antarctica
    ATF	 French Southern Territories
    ATG	 Antigua and Barbuda
    AUS	 Australia
    AUT	 Austria
    AZE	 Azerbaijan
    BDI	 Burundi
    BEL	 Belgium
    BEN	 Benin
    BES	 Bonaire, Saint Eustatius and Saba
    BFA	 Burkina Faso
    BGD	 Bangladesh
    BGR	 Bulgaria
    BHR	 Bahrain
    BHS	 Bahamas
    BIH	 Bosnia and Herzegovina
    BLM	 Saint Barthélemy
    BLR	 Belarus
    BLZ	 Belize
    BMU	 Bermuda
    BOL	 Bolivia, Plurinational State of
    BRA	 Brazil
    BRB	 Barbados
    BRN	 Brunei Darussalam
    BTN	 Bhutan
    BVT	 Bouvet Island
    BWA	 Botswana
    CAF	 Central African Republic
    CAN	 Canada
    CCK	 Cocos (Keeling) Islands
    CHE	 Switzerland
    CHL	 Chile
    CHN	 China
    CIV	 Côte d'Ivoire
    CMR	 Cameroon
    COD	 Congo, the Democratic Republic of the
    COG	 Congo
    COK	 Cook Islands
    COL	 Colombia
    COM	 Comoros
    CPV	 Cape Verde
    CRI	 Costa Rica
    CUB	 Cuba
    CUW	 Curaçao
    CXR	 Christmas Island
    CYM	 Cayman Islands
    CYP	 Cyprus
    CZE	 Czech Republic
    DEU	 Germany
    DJI	 Djibouti
    DMA	 Dominica
    DNK	 Denmark
    DOM	 Dominican Republic
    DZA	 Algeria
    ECU	 Ecuador
    EGY	 Egypt
    ERI	 Eritrea
    ESH	 Western Sahara
    ESP	 Spain
    EST	 Estonia
    ETH	 Ethiopia
    FIN	 Finland
    FJI	 Fiji
    FLK	 Falkland Islands (Malvinas)
    FRA	 France
    FRO	 Faroe Islands
    FSM	 Micronesia, Federated States of
    GAB	 Gabon
    GBR	 United Kingdom
    GEO	 Georgia
    GGY	 Guernsey
    GHA	 Ghana
    GIB	 Gibraltar
    GIN	 Guinea
    GLP	 Guadeloupe
    GMB	 Gambia
    GNB	 Guinea-Bissau
    GNQ	 Equatorial Guinea
    GRC	 Greece
    GRD	 Grenada
    GRL	 Greenland
    GTM	 Guatemala
    GUF	 French Guiana
    GUM	 Guam
    GUY	 Guyana
    HKG	 Hong Kong
    HMD	 Heard Island and McDonald Islands
    HND	 Honduras
    HRV	 Croatia
    HTI	 Haiti
    HUN	 Hungary
    IDN	 Indonesia
    IMN	 Isle of Man
    IND	 India
    IOT	 British Indian Ocean Territory
    IRL	 Ireland
    IRN	 Iran, Islamic Republic of
    IRQ	 Iraq
    ISL	 Iceland
    ISR	 Israel
    ITA	 Italy
    JAM	 Jamaica
    JEY	 Jersey
    JOR	 Jordan
    JPN	 Japan
    KAZ	 Kazakhstan
    KEN	 Kenya
    KGZ	 Kyrgyzstan
    KHM	 Cambodia
    KIR	 Kiribati
    KNA	 Saint Kitts and Nevis
    KOR	 Korea, Republic of
    KWT	 Kuwait
    LAO	 Lao People's Democratic Republic
    LBN	 Lebanon
    LBR	 Liberia
    LBY	 Libyan Arab Jamahiriya
    LCA	 Saint Lucia
    LIE	 Liechtenstein
    LKA	 Sri Lanka
    LSO	 Lesotho
    LTU	 Lithuania
    LUX	 Luxembourg
    LVA	 Latvia
    MAC	 Macao
    MAF	 Saint Martin (French part)
    MAR	 Morocco
    MCO	 Monaco
    MDA	 Moldova, Republic of
    MDG	 Madagascar
    MDV	 Maldives
    MEX	 Mexico
    MHL	 Marshall Islands
    MKD	 Macedonia, the former Yugoslav Republic of
    MLI	 Mali
    MLT	 Malta
    MMR	 Myanmar
    MNE	 Montenegro
    MNG	 Mongolia
    MNP	 Northern Mariana Islands
    MOZ	 Mozambique
    MRT	 Mauritania
    MSR	 Montserrat
    MTQ	 Martinique
    MUS	 Mauritius
    MWI	 Malawi
    MYS	 Malaysia
    MYT	 Mayotte
    NAM	 Namibia
    NCL	 New Caledonia
    NER	 Niger
    NFK	 Norfolk Island
    NGA	 Nigeria
    NIC	 Nicaragua
    NIU	 Niue
    NLD	 Netherlands
    NOR	 Norway
    NPL	 Nepal
    NRU	 Nauru
    NZL	 New Zealand
    OMN	 Oman
    PAK	 Pakistan
    PAN	 Panama
    PCN	 Pitcairn
    PER	 Peru
    PHL	 Philippines
    PLW	 Palau
    PNG	 Papua New Guinea
    POL	 Poland
    PRI	 Puerto Rico
    PRK	 Korea, Democratic People's Republic of
    PRT	 Portugal
    PRY	 Paraguay
    PSE	 Palestinian Territory, Occupied
    PYF	 French Polynesia
    QAT	 Qatar
    REU	 Réunion
    ROU	 Romania
    RUS	 Russian Federation
    RWA	 Rwanda
    SAU	 Saudi Arabia
    SDN	 Sudan
    SEN	 Senegal
    SGP	 Singapore
    SGS	 South Georgia and the South Sandwich Islands
    SHN	 Saint Helena, Ascension and Tristan da Cunha
    SJM	 Svalbard and Jan Mayen
    SLB	 Solomon Islands
    SLE	 Sierra Leone
    SLV	 El Salvador
    SMR	 San Marino
    SOM	 Somalia
    SPM	 Saint Pierre and Miquelon
    SRB	 Serbia
    STP	 Sao Tome and Principe
    SUR	 Suriname
    SVK	 Slovakia
    SVN	 Slovenia
    SWE	 Sweden
    SWZ	 Swaziland
    SXM	 Sint Maarten (Dutch part)
    SYC	 Seychelles
    SYR	 Syrian Arab Republic
    TCA	 Turks and Caicos Islands
    TCD	 Chad
    TGO	 Togo
    THA	 Thailand
    TJK	 Tajikistan
    TKL	 Tokelau
    TKM	 Turkmenistan
    TLS	 Timor-Leste
    TON	 Tonga
    TTO	 Trinidad and Tobago
    TUN	 Tunisia
    TUR	 Turkey
    TUV	 Tuvalu
    TWN	 Taiwan, Province of China
    TZA	 Tanzania, United Republic of
    UGA	 Uganda
    UKR	 Ukraine
    UMI	 United States Minor Outlying Islands
    URY	 Uruguay
    USA	 United States
    UZB	 Uzbekistan
    VAT	 Holy See (Vatican City State)
    VCT	 Saint Vincent and the Grenadines
    VEN	 Venezuela, Bolivarian Republic of
    VGB	 Virgin Islands, British
    VIR	 Virgin Islands, U.S.
    VNM	 Viet Nam
    VUT	 Vanuatu
    WLF	 Wallis and Futuna
    WSM	 Samoa
    YEM	 Yemen
    ZAF	 South Africa
    ZMB	 Zambia
    ZWE	 Zimbabwe
    """

    ABW = "Aruba"
    AFG = "Afghanistan"
    AGO = "Angola"
    AIA = "Anguilla"
    ALA = "Åland Islands"
    ALB = "Albania"
    AND = "Andorra"
    ARE = "United Arab Emirates"
    ARG = "Argentina"
    ARM = "Armenia"
    ASM = "American Samoa"
    ATA = "Antarctica"
    ATF = "French Southern Territories"
    ATG = "Antigua and Barbuda"
    AUS = "Australia"
    AUT = "Austria"
    AZE = "Azerbaijan"
    BDI = "Burundi"
    BEL = "Belgium"
    BEN = "Benin"
    BES = "Bonaire Saint Eustatius and Saba"
    BFA = "Burkina Faso"
    BGD = "Bangladesh"
    BGR = "Bulgaria	"
    BHR = "Bahrain	"
    BHS = "Bahamas	"
    BIH = "Bosnia and Herzegovina"
    BLM = "Saint Barthélemy"
    BLR = "Belarus"
    BLZ = "Belize"
    BMU = "Bermuda"
    BOL = "Bolivia, Plurinational State of"
    BRA = "Brazil"
    BRB = "Barbados"
    BRN = "Brunei Darussalam"
    BTN = "Bhutan"
    BVT = "Bouvet Island"
    BWA = "Botswana"
    CAF = "Central African Republic"
    CAN = "Canada"
    CCK = "Cocos (Keeling) Islands"
    CHE = "Switzerland"
    CHL = "Chile"
    CHN = "China"
    CIV = "Côte dIvoire"
    CMR = "Cameroon"
    COD = "Congo the Democratic Republic of the"
    COG = "Congo"
    COK = "Cook Islands"
    COL = "Colombia"
    COM = "Comoros"
    CPV = "Cape Verde"
    CRI = "Costa Rica"
    CUB = "Cuba"
    CUW = "Curaçao"
    CXR = "Christmas Island"
    CYM = "Cayman Islands"
    CYP = "Cyprus"
    CZE = "Czech Republic"
    DEU = "Germany"
    DJI = "Djibouti"
    DMA = "Dominica"
    DNK = "Denmark"
    DOM = "Dominican Republic"
    DZA = "Algeria"
    ECU = "Ecuador"
    EGY = "Egypt"
    ERI = "Eritrea"
    ESH = "Western Sahara"
    ESP = "Spain"
    EST = "Estonia"
    ETH = "Ethiopia"
    FIN = "Finland"
    FJI = "Fiji"
    FLK = "Falkland Islands (Malvinas)"
    FRA = "France"
    FRO = "Faroe Islands"
    FSM = "Micronesia Federated States of"
    GAB = "Gabon"
    GBR = "United Kingdom"
    GEO = "Georgia"
    GGY = "Guernsey"
    GHA = "Ghana"
    GIB = "Gibraltar"
    GIN = "Guinea"
    GLP = "Guadeloupe"
    GMB = "Gambia"
    GNB = "Guinea Bissau"
    GNQ = "Equatorial Guinea"
    GRC = "Greece"
    GRD = "Grenada"
    GRL = "Greenland"
    GTM = "Guatemala"
    GUF = "French Guiana"
    GUM = "Guam"
    GUY = "Guyana"
    HKG = "Hong Kong"
    HMD = "Heard Island and McDonald Islands"
    HND = "Honduras"
    HRV = "Croatia"
    HTI = "Haiti"
    HUN = "Hungary"
    IDN = "Indonesia"
    IMN = "Isle of Man"
    IND = "India"
    IOT = "British Indian Ocean Territory"
    IRL = "Ireland"
    IRN = "Iran Islamic Republic of"
    IRQ = "Iraq"
    ISL = "Iceland"
    ISR = "Israel"
    ITA = "Italy"
    JAM = "Jamaica"
    JEY = "Jersey"
    JOR = "Jordan"
    JPN = "Japan"
    KAZ = "Kazakhstan"
    KEN = "Kenya"
    KGZ = "Kyrgyzstan"
    KHM = "Cambodia"
    KIR = "Kiribati"
    KNA = "Saint Kitts and Nevis"
    KOR = "Korea Republic of"
    KWT = "Kuwait"
    LAO = "Lao People's Democratic Republic"
    LBN = "Lebanon"
    LBR = "Liberia"
    LBY = "Libyan Arab Jamahiriya"
    LCA = "Saint Lucia"
    LIE = "Liechtenstein"
    LKA = "Sri Lanka"
    LSO = "Lesotho"
    LTU = "Lithuania"
    LUX = "Luxembourg"
    LVA = "Latvia"
    MAC = "Macao"
    MAF = "Saint Martin (French part)"
    MAR = "Morocco"
    MCO = "Monaco"
    MDA = "Moldova Republic of"
    MDG = "Madagascar"
    MDV = "Maldives"
    MEX = "Mexico"
    MHL = "Marshall Islands"
    MKD = "Macedonia the former Yugoslav Republic of"
    MLI = "Mali"
    MLT = "Malta"
    MMR = "Myanmar"
    MNE = "Montenegro"
    MNG = "Mongolia"
    MNP = "Northern Mariana Islands"
    MOZ = "Mozambique"
    MRT = "Mauritania"
    MSR = "Montserrat"
    MTQ = "Martinique"
    MUS = "Mauritius"
    MWI = "Malawi"
    MYS = "Malaysia"
    MYT = "Mayotte"
    NAM = "Namibia"
    NCL = "New Caledonia"
    NER = "Niger"
    NFK = "Norfolk Island"
    NGA = "Nigeria"
    NIC = "Nicaragua"
    NIU = "Niue"
    NLD = "Netherlands"
    NOR = "Norway"
    NPL = "Nepal"
    NRU = "Nauru"
    NZL = "New Zealand"
    OMN = "Oman"
    PAK = "Pakistan"
    PAN = "Panama"
    PCN = "Pitcairn"
    PER = "Peru"
    PHL = "Philippines"
    PLW = "Palau"
    PNG = "Papua New Guinea"
    POL = "Poland"
    PRI = "Puerto Rico"
    PRK = "Korea Democratic People's Republic of"
    PRT = "Portugal"
    PRY = "Paraguay"
    PSE = "Palestinian Territory, Occupied"
    PYF = "French Polynesia"
    QAT = "Qatar"
    REU = "Réunion"
    ROU = "Romania"
    RUS = "Russian Federation"
    RWA = "Rwanda"
    SAU = "Saudi Arabia"
    SDN = "Sudan"
    SEN = "Senegal"
    SGP = "Singapore"
    SGS = "South Georgia and the South Sandwich Islands"
    SHN = "Saint Helena, Ascension and Tristan da Cunha"
    SJM = "Svalbard and Jan Mayen"
    SLB = "Solomon Islands"
    SLE = "Sierra Leone"
    SLV = "El Salvador"
    SMR = "San Marino"
    SOM = "Somalia"
    SPM = "Saint Pierre and Miquelon"
    SRB = "Serbia"
    STP = "Sao Tome and Principe"
    SUR = "Suriname"
    SVK = "Slovakia"
    SVN = "Slovenia"
    SWE = "Sweden"
    SWZ = "Swaziland"
    SXM = "Sint Maarten (Dutch part)"
    SYC = "Seychelles"
    SYR = "Syrian Arab Republic"
    TCA = "Turks and Caicos Islands"
    TCD = "Chad"
    TGO = "Togo"
    THA = "Thailand"
    TJK = "Tajikistan"
    TKL = "Tokelau"
    TKM = "Turkmenistan"
    TLS = "Timor-Leste"
    TON = "Tonga"
    TTO = "Trinidad and Tobago"
    TUN = "Tunisia"
    TUR = "Turkey"
    TUV = "Tuvalu"
    TWN = "Taiwan Province of China"
    TZA = "Tanzania, United Republic of"
    UGA = "Uganda"
    UKR = "Ukraine"
    UMI = "United States Minor Outlying Islands"
    URY = "Uruguay"
    USA = "United States"
    UZB = "Uzbekistan"
    VAT = "Holy See (Vatican City State)"
    VCT = "Saint Vincent and the Grenadines"
    VEN = "Venezuela, Bolivarian Republic of"
    VGB = "Virgin Islands, British"
    VIR = "Virgin Islands, U.S"
    VNM = "Viet Nam"
    VUT = "Vanuatu"
    WLF = "Wallis and Futuna"
    WSM = "Samoa"
    YEM = "Yemen"
    ZAF = "South Africa"
    ZMB = "Zambia"
    ZWE = "Zimbabwe"


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


class LanguageAbility(str, Enum):
    """
    403 - Language Ability

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


class LanguageProficiency(str, Enum):
    """
    404 - Language Proficiency

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


class DRGTransferType(str, Enum):
    """
    415 - DRG Transfer Type

    N  DRG Non Exempt
    E  DRG Exempt
    """

    N = "N"
    E = "E"


class ProcedureDRGType(str, Enum):
    """
    416 - Procedure DRG Type

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


class TissueTypeCode(str, Enum):
    """
    417 - Tissue Type Code

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


class ProcedurePriority(str, Enum):
    """
         418 - Procedure Priority

         0  the admitting procedure
         1  the primary procedure
         2  for ranked secondary procedures
    1312
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class SeverityofIllnessCode(str, Enum):
    """
    421 - Severity of Illness Code

    MI  Mild
    MO  Moderate
    SE  Severe
    """

    MI = "MI"
    MO = "MO"
    SE = "SE"


class TriageCode(str, Enum):
    """
    422 - Triage Code

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


class CaseCategoryCode(str, Enum):
    """
    423 - Case Category Code

    D  Doctor's Office Closed
    """

    D = "D"


class GestationCategoryCode(str, Enum):
    """
    424 - Gestation Category Code

    1  Premature / Pre-term
    2  Full Term
    3  Overdue / Post-term
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"


class NewbornCode(str, Enum):
    """
    425 - Newborn Code

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


class BloodProductCode(str, Enum):
    """
    426 - Blood Product Code

    CRYO  Cryoprecipitated AHF
    CRYOP  Pooled Cryoprecipitate
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


class RiskManagementIncidentCode(str, Enum):
    """
    427 - Risk Management Incident Code

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


class IncidentTypeCode(str, Enum):
    """
    428 - Incident Type Code

    P  Preventable
    U  User Error
    O  Other
    """

    P = "P"
    U = "U"
    O = "O"


class ProductionClassCode(str, Enum):
    """
    429 - Production Class Code

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


class ModeofArrivalCode(str, Enum):
    """
    430 - Mode of Arrival Code

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


class RecreationalDrugUseCode(str, Enum):
    """
    431 - Recreational Drug Use Code

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


class AdmissionLevelofCareCode(str, Enum):
    """
    432 - Admission Level of Care Code

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


class PrecautionCode(str, Enum):
    """
    433 - Precaution Code

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


class PatientConditionCode(str, Enum):
    """
    434 - Patient Condition Code

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


class AdvanceDirectiveCode(str, Enum):
    """
    435 - Advance Directive Code

    DNR  Do not resuscitate
    N  No directive
    """

    DNR = "DNR"
    N = "N"


class SensitivitytoCausativeAgentCode(str, Enum):
    """
    436 - Sensitivity to Causative Agent Code

    AD  Adverse Reaction (Not otherwise classified)
    AL  Allergy
    CT  Contraindication
    IN  Intolerance
    """

    AD = "AD"
    AL = "AL"
    CT = "CT"
    IN = "IN"


class AlertDeviceCode(str, Enum):
    """
    437 - Alert Device Code

    B  Bracelet
    N  Necklace
    W  Wallet Card
    """

    B = "B"
    N = "N"
    W = "W"


class AllergyClinicalStatus(str, Enum):
    """
    438 - Allergy Clinical Status

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
    AUI  Authorization information
    CCD  Charge code and date
    CCP  Channel calibration parameters
    CD  Channel definition
    CE  Coded element
    CF  Coded element with formatted values
    CK  Composite ID with check digit
    CM  Composite
    CN  Composite ID number and name
    CNE  Coded with no exceptions
    CNS  Composite ID number and name simplified
    CP  Composite price
    CQ  Composite quantity with units
    CSU  Channel sensitivity
    CWE  Coded with exceptions
    CX  Extended composite ID with check digit
    DDI  Daily deductible information
    DIN  Date and institution name
    DLD  Discharge to location and date
    DLN  Driver's license number
    DLT  Delta
    DR  Date/time range
    DT  Date
    DTM  Date/time
    DTN  Day type and number
    ED  Encapsulated data
    EI  Entity identifier
    EIP  Entity identifier pair
    ELD  Error location and description
    ERL  Error location
    FC  Financial class
    FN  Family name
    FT  Formatted text
    GTS  General timing specification
    HD  Hierarchic designator
    ICD  Insurance certification definition
    ID  Coded values for HL7 tables
    IS  Coded value for user-defined tables
    JCC  Job code/class
    LA1  Location with address variation 1
    LA2  Location with address variation 2
    MA  Multiplexed array
    MO  Money
    MOC  Money and charge code
    MOP  Money or percentage
    MSG  Message type
    NA  Numeric array
    NDL  Name with location and date
    NM  Numeric
    NR  Numeric range
    OCD  Occurrence code and date
    OSD  Order sequence definition
    OSP  Occurrence span code and date
    PIP  Practitioner institutional privileges
    PL  Person location
    PLN  Practitioner license or other ID number
    PN  Person name
    PPN  Performing person time stamp
    PRL  Parent result link
    PT  Processing type
    PTA  Policy type and amount
    QIP  Query input parameter list
    QSC  Query selection criteria
    RCD  Row column definition
    RFR  Reference range
    RI  Repeat interval
    RMC  Room coverage
    RP  Reference pointer
    RPT  Repeat pattern
    SAD  Street Address
    SCV  Scheduling class value pair
    SI  Sequence ID
    SN  Structured numeric
    SPD  Specialty description
    SPS  Specimen source
    SRT  Sort order
    ST  String
    TM  Time
    TN  Telephone number
    TQ  Timing/quantity
    TS  Time stamp
    TX  Text data
    UVC  UB value code and amount
    VH  Visiting hours
    VID  Version identifier
    VR  Value range
    WVI  Channel Identifier
    WVS  Waveform source
    XAD  Extended address
    XCN  Extended composite ID number and name
    XON  Extended composite name and ID number for organizations
    XPN  Extended person name
    XTN  Extended telecommunications number
    """

    AD = "AD"
    AUI = "AUI"
    CCD = "CCD"
    CCP = "CCP"
    CD = "CD"
    CE = "CE"
    CF = "CF"
    CK = "CK"
    CM = "CM"
    CN = "CN"
    CNE = "CNE"
    CNS = "CNS"
    CP = "CP"
    CQ = "CQ"
    CSU = "CSU"
    CWE = "CWE"
    CX = "CX"
    DDI = "DDI"
    DIN = "DIN"
    DLD = "DLD"
    DLN = "DLN"
    DLT = "DLT"
    DR = "DR"
    DT = "DT"
    DTM = "DTM"
    DTN = "DTN"
    ED = "ED"
    EI = "EI"
    EIP = "EIP"
    ELD = "ELD"
    ERL = "ERL"
    FC = "FC"
    FN = "FN"
    FT = "FT"
    GTS = "GTS"
    HD = "HD"
    ICD = "ICD"
    ID = "ID"
    IS = "IS"
    JCC = "JCC"
    LA1 = "LA1"
    LA2 = "LA2"
    MA = "MA"
    MO = "MO"
    MOC = "MOC"
    MOP = "MOP"
    MSG = "MSG"
    NA = "NA"
    NDL = "NDL"
    NM = "NM"
    NR = "NR"
    OCD = "OCD"
    OSD = "OSD"
    OSP = "OSP"
    PIP = "PIP"
    PL = "PL"
    PLN = "PLN"
    PN = "PN"
    PPN = "PPN"
    PRL = "PRL"
    PT = "PT"
    PTA = "PTA"
    QIP = "QIP"
    QSC = "QSC"
    RCD = "RCD"
    RFR = "RFR"
    RI = "RI"
    RMC = "RMC"
    RP = "RP"
    RPT = "RPT"
    SAD = "SAD"
    SCV = "SCV"
    SI = "SI"
    SN = "SN"
    SPD = "SPD"
    SPS = "SPS"
    SRT = "SRT"
    ST = "ST"
    TM = "TM"
    TN = "TN"
    TQ = "TQ"
    TS = "TS"
    TX = "TX"
    UVC = "UVC"
    VH = "VH"
    VID = "VID"
    VR = "VR"
    WVI = "WVI"
    WVS = "WVS"
    XAD = "XAD"
    XCN = "XCN"
    XON = "XON"
    XPN = "XPN"
    XTN = "XTN"


class ImmunizationRegistryStatus(str, Enum):
    """
    441 - Immunization Registry Status

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


class LocationServiceCode(str, Enum):
    """
    442 - Location Service Code

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
    TR  Transcriptionist
    PI  Primary Interpreter
    AI  Assistant/Alternate Interpreter
    TN  Technician
    """

    AD = "AD"
    AT = "AT"
    CP = "CP"
    FHCP = "FHCP"
    PP = "PP"
    RP = "RP"
    RT = "RT"
    TR = "TR"
    PI = "PI"
    AI = "AI"
    TN = "TN"


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


class EventType(str, Enum):
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


class OverallClaimDispositionCode(str, Enum):
    """
    457 - Overall Claim Disposition Code

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


class OCEEditCode(str, Enum):
    """
         458 - OCE Edit Code

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


class DenialorRejectionCode(str, Enum):
    """
    460 - Denial or Rejection Code

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


class AmbulatoryPaymentClassificationCode(str, Enum):
    """
         466 - Ambulatory Payment Classification Code

         031  Dental procedures
         163  Excision/biopsy
         181  Level 1 skin repair.
    1312
    """

    _031 = "031"
    _163 = "163"
    _181 = "181"


class ModifierEditCode(str, Enum):
    """
    467 - Modifier Edit Code

    0  Modifier does NOT exist
    1  Modifier present, no errors
    2  Modifier invalid
    3  Modifier NOT approved for ASC/HOPD use
    4  Modifier approved for ASC/HOPD use, inappropriate for code
    U  Modifier edit code unknown
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    U = "U"


class PaymentAdjustmentCode(str, Enum):
    """
    468 - Payment Adjustment Code

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


class PackagingStatusCode(str, Enum):
    """
    469 - Packaging Status Code

    0  Not packaged
    1  Packaged service (status indicator N, or no HCPCS code and certain revenue codes)
    2  Packaged as part of partial hospitalization per diem or daily mental health service per diem
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class ReimbursementTypeCode(str, Enum):
    """
    470 - Reimbursement Type Code

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


class TQconjunctionID(str, Enum):
    """
    472 - TQ conjunction ID

    S  Synchronous
    A  Asynchronous
    C  Actuation Time
    """

    S = "S"
    A = "A"
    C = "C"


class FormularyStatus(str, Enum):
    """
    473 - Formulary Status

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
    U  Subdepartment
    S  Subdivision
    V  Division
    """

    D = "D"
    F = "F"
    U = "U"
    S = "S"
    V = "V"


class ChargeTypeReason(str, Enum):
    """
    475 - Charge Type Reason

    01  Allergy
    02  Intolerance
    03  Treatment Failure
    04  Patient Request
    05  No Exception
    """

    _01 = "01"
    _02 = "02"
    _03 = "03"
    _04 = "04"
    _05 = "05"


class ControlledSubstanceSchedule(str, Enum):
    """
    477 - Controlled Substance Schedule

    I  Schedule I
    II  Schedule II
    III  Schedule III
    IV  Schedule IV
    V  Schedule V
    VI  Schedule VI
    """

    I = "I"
    II = "II"
    III = "III"
    IV = "IV"
    V = "V"
    VI = "VI"


class FormularysStatus(str, Enum):
    """
    478 - Formulary Status

    Y  Pharmaceutical substance is in the formulary
    N  Pharmaceutical substance is NOT in the formulary
    R  Pharmaceutical substance is in the formulary, but restrictions apply
    G  Pharmaceutical substance is in the formulary, but guidelines apply
    """

    Y = "Y"
    N = "N"
    R = "R"
    G = "G"


class PharmacyOrderTypes(str, Enum):
    """
    480 - Pharmacy Order Types

    M  Medication
    S  IV Large Volume Solutions
    O  Other solution as medication orders
    """

    M = "M"
    S = "S"
    O = "O"


class OrderType(str, Enum):
    """
    482 - Order Type

    I  Inpatient Order
    O  Outpatient Order
    """

    I = "I"
    O = "O"


class AuthorizationMode(str, Enum):
    """
    483 - Authorization Mode

    EL  Electronic
    EM  E-mail
    FX  Fax
    IP  In Person
    MA  Mail
    PA  Paper
    PH  Phone
    RE  Reflexive (Automated system)
    VC  Video-conference
    VO  Voice
    """

    EL = "EL"
    EM = "EM"
    FX = "FX"
    IP = "IP"
    MA = "MA"
    PA = "PA"
    PH = "PH"
    RE = "RE"
    VC = "VC"
    VO = "VO"


class DispenseType(str, Enum):
    """
    484 - Dispense Type

    B  Trial Quantity Balance
    C  Compassionate Fill
    N  New/Renew - Full Fill
    P  New/Renew - Part Fill
    Q  Refill - Part Fill
    R  Refill - Full Fill
    S  Manufacturer Sample
    T  Trial Quantity
    Z  Non-Prescription Fill
    """

    B = "B"
    C = "C"
    N = "N"
    P = "P"
    Q = "Q"
    R = "R"
    S = "S"
    T = "T"
    Z = "Z"


class ExtendedPriorityCodes(str, Enum):
    """
    485 - Extended Priority Codes

    S  Stat
    A  ASAP
    R  Routine
    P  Preop
    C  Callback
    T  Timing critical
    TS<integer>
    TM<integer>
    TH<integer>
    TD<integer>
    TW<integer>
    TL<integer>
    PRN  As needed
    """

    S = "S"
    A = "A"
    R = "R"
    P = "P"
    C = "C"
    T = "T"
    TS_integer_ = "TS<integer>"
    TM_integer_ = "TM<integer>"
    TH_integer_ = "TH<integer>"
    TD_integer_ = "TD<integer>"
    TW_integer_ = "TW<integer>"
    TL_integer_ = "TL<integer>"
    PRN = "PRN"


class SpecimenCollectionMethod(str, Enum):
    """
    488 - Specimen Collection Method

    FNA  Aspiration, Fine Needle
    PNA  Aterial puncture
    BIO  Biopsy
    BCAE  Blood Culture, Aerobic Bottle
    BCAN  Blood Culture, Anaerobic Bottle
    BCPD  Blood Culture, Pediatric Bottle
    CAP  Capillary Specimen
    CATH  Catheterized
    EPLA  Environmental, Plate
    ESWA  Environmental, Swab
    LNA  Line, Arterial
    CVP  Line, CVP
    LNV  Line, Venous
    MARTL  Martin-Lewis Agar
    ML11  Mod. Martin-Lewis Agar
    PACE  Pace, Gen-Probe
    PIN  Pinworm Prep
    KOFFP  Plate, Cough
    MLP  Plate, Martin-Lewis
    NYP  Plate, New York City
    TMP  Plate, Thayer-Martin
    ANP  Plates, Anaerobic
    BAP  Plates, Blood Agar
    PRIME  Pump Prime
    PUMP  Pump Specimen
    QC5  Quality Control For Micro
    SCLP  Scalp, Fetal Vein
    SCRAPS  Scrapings
    SHA  Shaving
    SWA  Swab
    SWD  Swab, Dacron tipped
    WOOD  Swab, Wooden Shaft
    TMOT  Transport Media,
    TMAN  Transport Media, Anaerobic
    TMCH  Transport Media, Chalamydia
    TMM4  Transport Media, M4
    TMMY  Transport Media, Mycoplasma
    TMPV  Transport Media, PVA
    TMSC  Transport Media, Stool Culture
    TMUP  Transport Media, Ureaplasma
    TMVI  Transport Media, Viral
    VENIP  Venipuncture
    """

    FNA = "FNA"
    PNA = "PNA"
    BIO = "BIO"
    BCAE = "BCAE"
    BCAN = "BCAN"
    BCPD = "BCPD"
    CAP = "CAP"
    CATH = "CATH"
    EPLA = "EPLA"
    ESWA = "ESWA"
    LNA = "LNA"
    CVP = "CVP"
    LNV = "LNV"
    MARTL = "MARTL"
    ML11 = "ML11"
    PACE = "PACE"
    PIN = "PIN"
    KOFFP = "KOFFP"
    MLP = "MLP"
    NYP = "NYP"
    TMP = "TMP"
    ANP = "ANP"
    BAP = "BAP"
    PRIME = "PRIME"
    PUMP = "PUMP"
    QC5 = "QC5"
    SCLP = "SCLP"
    SCRAPS = "SCRAPS"
    SHA = "SHA"
    SWA = "SWA"
    SWD = "SWD"
    WOOD = "WOOD"
    TMOT = "TMOT"
    TMAN = "TMAN"
    TMCH = "TMCH"
    TMM4 = "TMM4"
    TMMY = "TMMY"
    TMPV = "TMPV"
    TMSC = "TMSC"
    TMUP = "TMUP"
    TMVI = "TMVI"
    VENIP = "VENIP"


class RiskCodes(str, Enum):
    """
    489 - Risk Codes

    BIO  Biological
    COR  Corrosive
    ESC  Escape Risk
    AGG  Aggressive
    IFL  MaterialDangerInflammable
    EXP  Explosive
    INF  MaterialDangerInfectious
    BHZ  Biohazard
    INJ  Injury Hazard
    POI  Poison
    RAD  Radioactive
    """

    BIO = "BIO"
    COR = "COR"
    ESC = "ESC"
    AGG = "AGG"
    IFL = "IFL"
    EXP = "EXP"
    INF = "INF"
    BHZ = "BHZ"
    INJ = "INJ"
    POI = "POI"
    RAD = "RAD"


class SpecimenRejectReason(str, Enum):
    """
    490 - Specimen Reject Reason

    EX  Expired
    QS  Quantity not sufficient
    RB  Broken container
    RC  Clotting
    RD  Missing collection date
    RA  Missing patient ID number
    RE  Missing patient name
    RH  Hemolysis
    RI  Identification problem
    RM  Labeling
    RN  Contamination
    RP  Missing phlebotomist ID
    RR  Improper storage
    RS  Name misspelling
    """

    EX = "EX"
    QS = "QS"
    RB = "RB"
    RC = "RC"
    RD = "RD"
    RA = "RA"
    RE = "RE"
    RH = "RH"
    RI = "RI"
    RM = "RM"
    RN = "RN"
    RP = "RP"
    RR = "RR"
    RS = "RS"


class SpecimenQuality(str, Enum):
    """
    491 - Specimen Quality

    E  Excellent
    G  Good
    F  Fair
    P  Poor
    """

    E = "E"
    G = "G"
    F = "F"
    P = "P"


class SpecimenAppropriateness(str, Enum):
    """
    492 - Specimen Appropriateness

    P  Preferred
    A  Appropriate
    I  Inappropriate
    ??  Inappropriate due to ...
    """

    P = "P"
    A = "A"
    I = "I"
    QQ = "??"


class SpecimenCondition(str, Enum):
    """
    493 - Specimen Condition

    AUT  Autolyzed
    CLOT  Clotted
    CON  Contaminated
    COOL  Cool
    FROZ  Frozen
    HEM  Hemolyzed
    LIVE  Live
    ROOM  Room temperature
    SNR  Sample not received
    """

    AUT = "AUT"
    CLOT = "CLOT"
    CON = "CON"
    COOL = "COOL"
    FROZ = "FROZ"
    HEM = "HEM"
    LIVE = "LIVE"
    ROOM = "ROOM"
    SNR = "SNR"


class SpecimenChildRole(str, Enum):
    """
    494 - Specimen Child Role

    A  Aliquot
    C  Component
    M  Modified from original specimen
    """

    A = "A"
    C = "C"
    M = "M"


class BodySiteModifier(str, Enum):
    """
    495 - Body Site Modifier

    ANT  Anterior
    BIL  Bilateral
    DIS  Distal
    EXT  External
    LAT  Lateral
    L  Left
    LOW  Lower
    MED  Medial
    POS  Posterior
    PRO  Proximal
    LLQ  Quadrant, Left Lower
    LUQ  Quadrant, Left Upper
    RLQ  Quadrant, Right Lower
    RUQ  Quadrant, Right Upper
    R  Right
    UPP  Upper
    """

    ANT = "ANT"
    BIL = "BIL"
    DIS = "DIS"
    EXT = "EXT"
    LAT = "LAT"
    L = "L"
    LOW = "LOW"
    MED = "MED"
    POS = "POS"
    PRO = "PRO"
    LLQ = "LLQ"
    LUQ = "LUQ"
    RLQ = "RLQ"
    RUQ = "RUQ"
    R = "R"
    UPP = "UPP"


class ConsentType(str, Enum):
    """
    496 - Consent Type

    001  Release of Information/MR / Authorization to Disclosure Protected Health Information
    002  Medical Procedure (invasive)
    003  Acknowledge Receipt of Privacy Notice
    004  Abortion
    005  Abortion/Laminaria
    006  Accutane - Information
    007  Accutane - Woman
    008  Advanced Beneficiary Notice
    009  AFP (Alpha Fetoprotein) Screening
    010  Amniocentesis (consent & refusal)
    011  Anatomical Gift (organ donation)
    012  Anesthesia - Complications
    013  Anesthesia - Questionnaire
    014  Angiogram
    015  Angioplasty
    016  Anticancer Drugs
    017  Antipsychotic Medications
    018  Arthrogram
    019  Autopsy
    020  AZT Therapy
    021  Biliary Drainage
    022  Biliary Stone Extraction
    023  Biopsy
    024  Bleeding Time Test
    025  Bronchogram
    026  Cardiac Catheterization
    027  Coronary Angiography
    028  ""      "" w/o Surgery Capability
    029  Cataract Op/Implant of FDA Aprvd Lens
    030  Cataract Op/Implant of Investigational Lens
    031  Cataract Surgery
    032  Cholera Immunization
    033  Cholesterol Screening
    034  Circumcision - Newborn
    035  Colonoscopy
    036  Contact Lenses
    037  CT Scan - Cervical & Lumbar
    038  CT Scan w/ IV Contrast Media into Vein
    039  CVS (Chorionic Villus) Sampling
    040  Cystospy
    041  Disclosure of Protected Health Information to Family/Friends
    042  D & C and Conization
    043  Dacryocystogram
    044  Diagnostic Isotope
    045  Drainage of an Abscess
    046  Drug Screening
    047  Electronic Monitoring of Labor - Refusal
    048  Endometrial Biopsy
    049  Endoscopy/Sclerosis of Esophageal Varices
    050  ERCP
    051  Exposure to reportable Communicable Disease
    052  External Version
    053  Fluorescein Angioscopy
    054  Hepatitis B - Consent/Declination
    055  Herniogram
    056  HIV Test - Consent Refusal
    057  HIV Test - Disclosure
    058  HIV Test - Prenatal
    059  Home IV Treatment Program
    060  Home Parenteral Treatment Program
    061  Hysterectomy
    062  Hysterosalpingogram
    063  Injection Slip/ Consent
    064  Intrauterine Device
    065  Intrauterine Device/Sterilization
    066  Intravascular Infusion of Streptokinase/Urokinase
    067  Intravenous Cholangiogram
    068  Intravenous Digital Angiography
    069  Iodine Administration
    070  ISG
    071  IVP
    072  Laser Photocoagulation
    073  Laser treatment
    074  Lithium Carbonate
    075  Liver Biopsy
    076  Lumbar Puncture
    077  Lymphangiogram
    078  MAO Inhibitors
    079  Med, Psych, and/or Drug/Alcohol
    080  Medical Treatment - Refusal
    081  Morning-after Pill
    082  MRI - Adult
    083  MRI - Pediatric
    084  Myelogram
    085  Needle Biopsy
    086  Needle Biopsy of Lung
    087  Newborn Treatment and Release
    088  Norplant Subdermal Birth Control Implant
    089  Operations, Anesthesia, Transfusions
    090  Oral Contraceptives
    091  Organ Donation
    092  Patient Permits, Consents
    093  Patient Treatment Permit, Release & Admission
    094  Penile Injections
    095  Percutaneous Nephrostomy
    096  Percutaneous Transhepatic Cholangiogram
    097  Photographs
    098  Photographs - Employee
    099  Photographs - Medical Research
    100  Photographs - news Media
    101  Psychiatric Admission - Next of Kin
    102  Psychiatric Information During Hospital Stay
    103  Public Release of Information
    104  Radiologic Procedure
    105  Refusal of Treatment
    106  Release of Body
    107  Release of Limb
    108  Rh Immune Globulin
    109  Rights of Medical Research Participants
    110  Request to Restrict Access/Disclosure to Medical Record/Protected Health Information
    111  Request for Remain Anonymous
    112  Seat Belt Exemption
    113  Sialogram
    114  Sigmoidoscopy
    115  Sterilization - Anesthesia & Medical Services
    116  Sterilization -Federally Funded
    117  Sterilization - Female
    118  Sterilization - Laparoscopy/Pomeroy
    119  Sterilization - Non-Federally Funded
    120  Sterilization - Secondary
    121  Tranquilizers
    122  Transfer - Acknowledgement
    123  Transfer - Authorization
    124  Transfer Certification - Physician
    125  Transfer/Discharge Request
    126  Transfer for Non-Medical Reasons
    127  Transfer - Interfaculty Neonatal
    128  Transfer Refusal
    129  Transfer Refusal of Further Treatment
    130  Treadmill & EKG
    131  Treadmill, Thallium-201
    132  Typhoid
    133  Use of Investigational Device
    134  Use of Investigational Drug
    135  Venogram
    136  Videotape
    1137  Voiding Cystogram
    """

    _001 = "001"
    _002 = "002"
    _003 = "003"
    _004 = "004"
    _005 = "005"
    _006 = "006"
    _007 = "007"
    _008 = "008"
    _009 = "009"
    _010 = "010"
    _011 = "011"
    _012 = "012"
    _013 = "013"
    _014 = "014"
    _015 = "015"
    _016 = "016"
    _017 = "017"
    _018 = "018"
    _019 = "019"
    _020 = "020"
    _021 = "021"
    _022 = "022"
    _023 = "023"
    _024 = "024"
    _025 = "025"
    _026 = "026"
    _027 = "027"
    _028 = "028"
    _029 = "029"
    _030 = "030"
    _031 = "031"
    _032 = "032"
    _033 = "033"
    _034 = "034"
    _035 = "035"
    _036 = "036"
    _037 = "037"
    _038 = "038"
    _039 = "039"
    _040 = "040"
    _041 = "041"
    _042 = "042"
    _043 = "043"
    _044 = "044"
    _045 = "045"
    _046 = "046"
    _047 = "047"
    _048 = "048"
    _049 = "049"
    _050 = "050"
    _051 = "051"
    _052 = "052"
    _053 = "053"
    _054 = "054"
    _055 = "055"
    _056 = "056"
    _057 = "057"
    _058 = "058"
    _059 = "059"
    _060 = "060"
    _061 = "061"
    _062 = "062"
    _063 = "063"
    _064 = "064"
    _065 = "065"
    _066 = "066"
    _067 = "067"
    _068 = "068"
    _069 = "069"
    _070 = "070"
    _071 = "071"
    _072 = "072"
    _073 = "073"
    _074 = "074"
    _075 = "075"
    _076 = "076"
    _077 = "077"
    _078 = "078"
    _079 = "079"
    _080 = "080"
    _081 = "081"
    _082 = "082"
    _083 = "083"
    _084 = "084"
    _085 = "085"
    _086 = "086"
    _087 = "087"
    _088 = "088"
    _089 = "089"
    _090 = "090"
    _091 = "091"
    _092 = "092"
    _093 = "093"
    _094 = "094"
    _095 = "095"
    _096 = "096"
    _097 = "097"
    _098 = "098"
    _099 = "099"
    _100 = "100"
    _101 = "101"
    _102 = "102"
    _103 = "103"
    _104 = "104"
    _105 = "105"
    _106 = "106"
    _107 = "107"
    _108 = "108"
    _109 = "109"
    _110 = "110"
    _111 = "111"
    _112 = "112"
    _113 = "113"
    _114 = "114"
    _115 = "115"
    _116 = "116"
    _117 = "117"
    _118 = "118"
    _119 = "119"
    _120 = "120"
    _121 = "121"
    _122 = "122"
    _123 = "123"
    _124 = "124"
    _125 = "125"
    _126 = "126"
    _127 = "127"
    _128 = "128"
    _129 = "129"
    _130 = "130"
    _131 = "131"
    _132 = "132"
    _133 = "133"
    _134 = "134"
    _135 = "135"
    _136 = "136"
    _1137 = "1137"


class ConsentMode(str, Enum):
    """
    497 - Consent Mode

    V  Verbal
    W  Written
    T  Telephone
    """

    V = "V"
    W = "W"
    T = "T"


class ConsentStatus(str, Enum):
    """
    498 - Consent Status

    A  Active - Consent has been granted
    L  Limited - Consent has been granted with limitations
    R  Refused - Consent has been refused
    P  Pending - Consent has not yet been sought
    X  Rescinded - Consent was initially granted, but was subsequently revoked or ended.
    B  Bypassed (Consent not sought)
    """

    A = "A"
    L = "L"
    R = "R"
    P = "P"
    X = "X"
    B = "B"


class ConsentBypassReason(str, Enum):
    """
    499 - Consent Bypass Reason

    E  Emergency
    PJ  Professional Judgment
    """

    E = "E"
    PJ = "PJ"


class ConsentDisclosureLevel(str, Enum):
    """
    500 - Consent Disclosure Level

    F  Full Disclosure
    P  Partial Disclosure
    N  No Disclosure
    """

    F = "F"
    P = "P"
    N = "N"


class ConsentNon_DisclosureReason(str, Enum):
    """
    501 - Consent Non-Disclosure Reason

    E  Emergency
    RX  Rx Private
    PR  Patient Request
    """

    E = "E"
    RX = "RX"
    PR = "PR"


class Non_SubjectConsenterReason(str, Enum):
    """
    502 - Non-Subject Consenter Reason

    MIN  Subject is a minor
    NC  Subject is not competent to consent
    LM  Legally mandated
    """

    MIN = "MIN"
    NC = "NC"
    LM = "LM"


class Sequence_ResultsFlag(str, Enum):
    """
    503 - Sequence-Results Flag

    S  Sequential
    C  Cyclical
    R  Reserved for future use
    """

    S = "S"
    C = "C"
    R = "R"


class SequenceConditionCode(str, Enum):
    """
    504 - Sequence Condition Code

    EE  End related service request(s), end current service request.
    ES  End related service request(s), start current service request.
    SS  Start related service request(s), start current service request.
    SE  Start related service request(s), end current service request.
    """

    EE = "EE"
    ES = "ES"
    SS = "SS"
    SE = "SE"


class CyclicEntry_ExitIndicator(str, Enum):
    """
    505 - Cyclic Entry-Exit Indicator

    *  The first service request in a cyclic group
    #  The last service request in a cyclic group.
    """

    star = "*"
    hashtag = "#"


class ServiceRequestRelationship(str, Enum):
    """
    506 - Service Request Relationship

    N  Nurse prerogative
    C  Compound
    T  Tapering
    E  Exclusive
    S  Simultaneous
    """

    N = "N"
    C = "C"
    T = "T"
    E = "E"
    S = "S"


class ObservationResultHandling(str, Enum):
    """
    507 - Observation Result Handling

    F  Film-with-patient
    N  Notify provider when ready
    """

    F = "F"
    N = "N"


class BloodProductProcessingRequirements(str, Enum):
    """
    508 - Blood Product Processing Requirements

    LR  Leukoreduced
    IR  Irradiated
    CS  CMV Safe
    FR  Fresh unit
    AU  Autologous Unit
    DI  Directed Unit
    HL  HLA Matched
    CM  CMV Negative
    HB  Hemoglobin S Negative
    WA  Washed
    IG  IgA Deficient
    """

    LR = "LR"
    IR = "IR"
    CS = "CS"
    FR = "FR"
    AU = "AU"
    DI = "DI"
    HL = "HL"
    CM = "CM"
    HB = "HB"
    WA = "WA"
    IG = "IG"


class BloodProductDispenseStatus(str, Enum):
    """
    510 - Blood Product Dispense Status

    RI  Received into inventory (for specified patient)
    RD  Reserved and ready to dispense
    RS  Reserved (ordered and product allocated for the patient)
    RE  Released (no longer allocated for the patient)
    DS  Dispensed to patient location
    RA  Returned unused/no longer needed
    RL  Returned unused/keep linked to patient for possible use later
    WA  Wasted (product no longer viable)
    PT  Presumed transfused (dispensed and not returned)
    CR  Released into inventory for general availability
    RQ  Request to dispense blood product
    """

    RI = "RI"
    RD = "RD"
    RS = "RS"
    RE = "RE"
    DS = "DS"
    RA = "RA"
    RL = "RL"
    WA = "WA"
    PT = "PT"
    CR = "CR"
    RQ = "RQ"


class BPObservationStatusCodesInterpretation(str, Enum):
    """
    511 - BP Observation Status Codes Interpretation

    C  Record coming over is a correction and thus replaces a final status
    D  Deletes the BPX record
    F  Final status; Can only be changed with a corrected status
    O  Order detail description only (no status)
    P  Preliminary status
    W  Post original as wrong, e.g., transmitted for wrong patient
    """

    C = "C"
    D = "D"
    F = "F"
    O = "O"
    P = "P"
    W = "W"


class BloodProductTransfusion_DispositionStatus(str, Enum):
    """
    513 - Blood Product Transfusion-Disposition Status

    RA  Returned unused/no longer needed
    RL  Returned unused/keep linked to patient for possible use later
    WA  Wasted (product no longer viable)
    TX  Transfused
    TR  Transfused with adverse reaction
    """

    RA = "RA"
    RL = "RL"
    WA = "WA"
    TX = "TX"
    TR = "TR"


class TransfusionAdverseReaction(str, Enum):
    """
    514 - Transfusion Adverse Reaction

    ABOINC  ABO Incompatible Transfusion Reaction
    ACUTHEHTR  Acute Hemolytic Transfusion Reaction
    ALLERGIC1  Allergic Reaction - First
    ALLERGIC2  Allergic Reaction - Recurrent
    ALLERGICR  Allergic Reaction - Repeating
    ANAPHYLAC  Anaphylactic Reaction
    BACTCONTAM  Reaction to Bacterial Contamination
    DELAYEDHTR  Delayed Hemolytic Transfusion Reaction
    DELAYEDSTR  Delayed Serological Transfusion Reaction
    GVHD  Graft vs Host Disease - Transfusion - Associated
    HYPOTENS  Non-hemolytic Hypotensive Reaction
    NONHTR1  Non-Hemolytic Fever Chill Transfusion Reaction - First
    NONHTR2  Non-Hemolytic Fever Chill Transfusion Reaction - Recurrent
    NONHTRREC  Non-Hemolytic Fever Chill Transfusion Reaction - Repeating
    NONIMMUNE  Non-Immune Hemolysis
    NONSPEC  Non-Specific, Non-Hemolytic Transfusion Reaction
    NORXN  No Evidence of Transfusion Reaction
    PTP  Posttransfusion Purpura
    VOLOVER  Symptoms most likely due to volume overload
    """

    ABOINC = "ABOINC"
    ACUTHEHTR = "ACUTHEHTR"
    ALLERGIC1 = "ALLERGIC1"
    ALLERGIC2 = "ALLERGIC2"
    ALLERGICR = "ALLERGICR"
    ANAPHYLAC = "ANAPHYLAC"
    BACTCONTAM = "BACTCONTAM"
    DELAYEDHTR = "DELAYEDHTR"
    DELAYEDSTR = "DELAYEDSTR"
    GVHD = "GVHD"
    HYPOTENS = "HYPOTENS"
    NONHTR1 = "NONHTR1"
    NONHTR2 = "NONHTR2"
    NONHTRREC = "NONHTRREC"
    NONIMMUNE = "NONIMMUNE"
    NONSPEC = "NONSPEC"
    NORXN = "NORXN"
    PTP = "PTP"
    VOLOVER = "VOLOVER"


class Errorseverity(str, Enum):
    """
    516 - Error severity

    W  Warning
    I  Information
    E  Error
    F  Fatal Error
    """

    W = "W"
    I = "I"
    E = "E"
    F = "F"


class Informpersoncode(str, Enum):
    """
    517 - Inform person code

    PAT  Inform patient
    NPAT  Do NOT inform patient
    USR  Inform User
    HD  Inform help desk
    """

    PAT = "PAT"
    NPAT = "NPAT"
    USR = "USR"
    HD = "HD"


class Overridetype(str, Enum):
    """
    518 - Override type

    EXTN  Extension Override
    INLV  Interval Override
    EQV  Equivalence Override
    """

    EXTN = "EXTN"
    INLV = "INLV"
    EQV = "EQV"


class Messagewaitingpriority(str, Enum):
    """
    520 - Message waiting priority

    H  High
    M  Medium
    L  Low
    """

    H = "H"
    M = "M"
    L = "L"


class Computationtype(str, Enum):
    """
    523 - Computation type

    %  Indicates a percent change
    a  Absolute Change
    """

    percent = "%"
    a = "a"


class Sequencecondition(str, Enum):
    """
    524 - Sequence condition

    S  Sequence conditions
    C  Repeating cycle of orders
    R  Reserved for possible future use
    """

    S = "S"
    C = "C"
    R = "R"


class Calendaralignment(str, Enum):
    """
    527 - Calendar alignment

    MY  month of the year
    WY  week of the year
    DM  day of the month
    DY  day of the year
    DW  day of the week (begins with Monday)
    HD  hour of the day
    NH  minute of the hour
    SN  second of the minute
    """

    MY = "MY"
    WY = "WY"
    DM = "DM"
    DY = "DY"
    DW = "DW"
    HD = "HD"
    NH = "NH"
    SN = "SN"


class Eventrelatedperiod(str, Enum):
    """
    528 - Event related period

    HS  the hour of sleep (e.g., H18-22)
    AC  before meal (from lat. ante cibus)
    PC  after meal (from lat. post cibus)
    IC  between meals (from lat. inter cibus)
    ACM  before breakfast (from lat. ante cibus matutinus)
    ACD  before lunch (from lat. ante cibus diurnus)
    ACV  before dinner (from lat. ante cibus vespertinus)
    PCM  after breakfast (from lat. post cibus matutinus)
    PCD  after lunch (from lat. post cibus diurnus)
    PCV  after dinner (from lat. post cibus vespertinus)
    ICM  between breakfast and lunch
    ICD  between lunch and dinner
    ICV  between dinner and the hour of sleep
    """

    HS = "HS"
    AC = "AC"
    PC = "PC"
    IC = "IC"
    ACM = "ACM"
    ACD = "ACD"
    ACV = "ACV"
    PCM = "PCM"
    PCD = "PCD"
    PCV = "PCV"
    ICM = "ICM"
    ICD = "ICD"
    ICV = "ICV"


class Organizationagencydepartment(str, Enum):
    """
    530 - Organization  agency  department

    AE  American Express
    DEA  Drug Enforcement Agency
    DOD  Department of Defense
    MC  Master Card
    VA  Veterans Affairs
    VI  Visa
    """

    AE = "AE"
    DEA = "DEA"
    DOD = "DOD"
    MC = "MC"
    VA = "VA"
    VI = "VI"


class Expandedyes_noindicator(str, Enum):
    """
    532 - Expanded yes-no indicator

    Y  Yes
    N  No
    NI  No Information
    NA  not applicable
    UNK  unknown
    NASK  not asked
    ASKU  asked but unknown
    NAV  temporarily unavailable
    NP  not present
    """

    Y = "Y"
    N = "N"
    NI = "NI"
    NA = "NA"
    UNK = "UNK"
    NASK = "NASK"
    ASKU = "ASKU"
    NAV = "NAV"
    NP = "NP"


class NotifyClergyCode(str, Enum):
    """
    534 - Notify Clergy Code

    Y  Yes
    N  No
    L  Last Rites only
    O  Other
    U  Unknown
    """

    Y = "Y"
    N = "N"
    L = "L"
    O = "O"
    U = "U"


class SignatureCode(str, Enum):
    """
    535 - Signature Code

    C  Signed CMS-1500 claim form on file, e.g., authorization for release of any medical or other information necessary to process this claim and assignment of benefits.
    S  Signed authorization for release of any medical or other information necessary to process this claim on file.
    M  Signed authorization for assignment of benefits on file.
    P  Signature generated by provider because the patient was not physically present for services.
    """

    C = "C"
    S = "S"
    M = "M"
    P = "P"


class CertificateStatus(str, Enum):
    """
    536 - Certificate Status

    P  Provisional
    R  Revoked
    V  Active/Valid
    E  Expired
    I  Inactive
    """

    P = "P"
    R = "R"
    V = "V"
    E = "E"
    I = "I"


class InstitutionRelationshipType(str, Enum):
    """
    538 - Institution Relationship Type

    EMP  Employee
    VOL  Volunteer
    CON  Contractor
    CST  Consultant
    """

    EMP = "EMP"
    VOL = "VOL"
    CON = "CON"
    CST = "CST"


class InactiveReasonCode(str, Enum):
    """
    540 - Inactive Reason Code

    L  Leave of Absence
    T  Termination
    R  Retired
    """

    L = "L"
    T = "T"
    R = "R"


class JurisdictionalBreadth(str, Enum):
    """
    547 - Jurisdictional Breadth

    C  County/Parish
    S  State/Province
    N  Country
    """

    C = "C"
    S = "S"
    N = "N"


class SignatorysRelationshiptoSubject(str, Enum):
    """
    548 - Signatory s Relationship to Subject

    1  Self
    2  Parent
    3  Next of Kin
    4  Durable Power of Attorney in Healthcare Affairs
    5  Conservator
    6  Emergent Practitioner (practitioner judging case as emergency requiring care without a consent)
    7  Non-Emergent Practitioner (i.e. medical ethics committee)
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"


class BodyParts(str, Enum):
    """
    550 - Body Parts

    JUGE  Jugular, External
    ADB  Abdomen
    ACET  Acetabulum
    ACHIL  Achilles
    ADE  Adenoids
    ADR  Adrenal
    AMN  Amniotic fluid
    AMS  Amniotic Sac
    ANAL  Anal
    ANKL  Ankle
    ANTEC  Antecubital
    ANTECF  Antecubital Fossa
    ANTR  Antrum
    ANUS  Anus
    AORTA  Aorta
    AR  Aortic Rim
    AV  Aortic Valve
    APDX  Appendix
    AREO  Areola
    ARM  Arm
    ARTE  Artery
    ASCIT  Ascites
    ASCT  Ascitic Fluid
    ATR  Atrium
    AURI  Auricular
    AXI  Axilla
    BACK  Back
    BARTD  Bartholin Duct
    BARTG  Bartholin Gland
    BRTGF  Bartholin Gland Fluid
    BPH  Basophils
    BID  Bile Duct
    BIFL  Bile fluid
    BLAD  Bladder
    BLOOD  Blood
    BLDA  Blood,  Arterial
    BLDC  Blood,  Capillary
    BLDV  Blood,  Venous
    CBLD  Blood, Cord
    BLD  Blood, Whole
    BDY  Body, Whole
    BON  Bone
    BMAR  Bone marrow
    BOWEL  Bowel
    BOWLA  Bowel, Large
    BOWSM  Bowel, Small
    BRA  Brachial
    BRAIN  Brain
    BCYS  Brain Cyst Fluid
    BRST  Breast
    BRSTFL  Breast fluid
    BRO  Bronchial
    BROCH  Bronchiole/Bronchiolar
    BRONC  Bronchus/Bronchial
    BRV  Broviac
    BUCCA  Buccal
    BURSA  Bursa
    BURSF  Bursa Fluid
    BUTT  Buttocks
    CALF  Calf
    CANAL  Canal
    CANLI  Canaliculis
    CNL  Cannula
    CANTH  Canthus
    CDM  Cardiac Muscle
    CARO  Carotid
    CARP  Carpal
    CAVIT  Cavity
    CHE  Cavity, Chest
    CECUM  Cecum/Cecal
    CSF  Cerebral Spinal Fluid
    CVX  Cervix
    CERVUT  Cervix/Uterus
    CHEEK  Cheek
    CHES  Chest
    CHEST  Chest Tube
    CHIN  Chin
    CIRCU  Circumcision Site
    CLAVI  Clavicle/Clavicular
    CLITO  Clitoral
    CLIT  Clitoris
    COCCG  Coccygeal
    COCCY  Coccyx
    COLON  Colon
    COLOS  Colostomy
    COS  Colostomy Stoma
    CDUCT  Common Duct
    CONJ  Conjunctiva
    CORAL  Coral
    COR  Cord
    CORD  Cord Blood
    CORN  Cornea
    CRANE  Cranium, ethmoid
    CRANF  Cranium, frontal
    CRANO  Cranium, occipital
    CRANP  Cranium, parietal
    CRANS  Cranium, sphenoid
    CRANT  Cranium, temporal
    CUBIT  Cubitus
    CUFF  Cuff
    CULD  Cul De Sac
    CULDO  Culdocentesis
    DELT  Deltoid
    DENTA  Dental
    DEN  Dental Gingiva
    DIAF  Dialysis Fluid
    DPH  Diaphragm
    DIGIT  Digit
    DISC  Disc
    DORS  Dorsum/Dorsal
    DUFL  Duodenal Fluid
    DUODE  Duodenum/Duodenal
    DUR  Dura
    EAR  Ear
    EARBI  Ear bone, incus
    EARBM  Ear bone, malleus
    EARBS  Ear bone,stapes
    EARLO  Ear Lobe
    ELBOW  Elbow
    ELBOWJ  Elbow Joint
    ENDC  Endocardium
    EC  Endocervical
    EOLPH  endolpthamitis
    ENDM  Endometrium
    ET  Endotracheal
    EUR  Endourethral
    EOS  Eosinophils
    EPICA  Epicardial
    EPICM  Epicardium
    EPD  Epididymis
    EPIDU  Epidural
    EPIGL  Epiglottis
    ESOPG  Esophageal
    ESO  Esophagus
    ETHMO  Ethmoid
    Â   External Jugular
    EYE  Eye
    BROW  Eyebrow
    EYELI  Eyelid
    FACE  Face
    FBINC  Facial bone, inferior nasal concha
    FBLAC  Facial bone, lacrimal
    FBMAX  Facial bone, maxilla
    FBNAS  Facial bone, nasal
    FBPAL  Facial bone, palatine
    FBVOM  Facial bone, vomer
    FBZYG  Facial bone, zygomatic
    FALLT  Fallopian Tube
    FEMOR  Femoral
    FMH  Femoral Head
    FEMUR  Femur
    FET  Fetus
    FIBU  Fibula
    FING  Finger
    FINGN  Finger Nail
    FOL  Follicle
    FOOT  Foot
    FOREA  Forearm
    FOREH  Forehead
    FORES  Foreskin
    FOURC  Fourchette
    GB  Gall Bladder
    GEN  Genital
    GVU  Genital - Vulva
    GENC  Genital Cervix
    GL  Genital Lesion
    GENL  Genital Lochia
    GLAND  Gland
    GLANS  Glans
    GLUTE  Gluteal
    GLUT  Gluteus
    GLUTM  Gluteus Medius
    GROIN  Groin
    GUM  Gum
    HAR  Hair
    HAL  Hallux
    HAND  Hand
    HEAD  Head
    HART  Heart
    HV  Heart Valve
    HVB  Heart Valve, Bicuspid
    HVT  Heart Valve, Tricuspid
    HEEL  Heel
    HEM  Hemorrhoid
    HIP  Hip
    HIPJ  Hip Joint
    HUMER  Humerus
    HYMEN  Hymen
    ILC  Ileal Conduit
    ILE  Ileal Loop
    ILEOS  Ileostomy
    ILEUM  Ileum
    ILIAC  Iliac
    ILCR  Iliac Crest
    ILCON  Ilical Conduit
    INGUI  Inguinal
    JUGI  Jugular, Internal
    INT  Intestine
    ICX  Intracervical
    INASA  Intranasal
    INTRU  Intrauterine
    INTRO  Introitus
    ISCHI  Ischium
    JAW  Jaw
    KIDN  Kidney
    KNEE  Knee
    KNEEF  Knee Fluid
    KNEEJ  Knee Joint
    LABIA  Labia
    LABMA  Labia Majora
    LABMI  Labia Minora
    LACRI  Lacrimal
    LAM  Lamella
    INSTL  Intestine, Large
    LARYN  Larynx
    LEG  Leg
    LENS  Lens
    WBC  Leukocytes
    LING  Lingual
    LINGU  Lingula
    LIP  Lip
    STOOLL  Liquid Stool
    LIVER  Liver
    LOBE  Lobe
    LOCH  Lochia
    ISH  Loop, Ishial
    LUMBA  Lumbar
    LMN  Lumen
    LUNG  Lung
    LN  Lymph Node
    LNG  Lymph Node, Groin
    LYM  Lymphocytes
    MAC  Macrophages
    MALLE  Malleolus
    MANDI  Mandible/Mandibular
    MAR  Marrow
    MAST  Mastoid
    MAXIL  Maxilla/Maxillary
    MAXS  Maxillary Sinus
    MEATU  Meatus
    MEC  Meconium
    MEDST  Mediastinum
    MEDU  Medullary
    MOU  Membrane
    MPB  Meninges
    METAC  Metacarpal
    METAT  Metatarsal
    MILK  Milk, Breast
    MITRL  Mitral Valve
    MOLAR  Molar
    MP  Mons Pubis
    MONSU  Mons Ureteris
    MONSV  Mons Veneris(Mons Pubis)
    MOUTH  Mouth
    MRSA2  Mrsa:
    MYO  Myocardium
    NAIL  Nail
    NAILB  Nail Bed
    NAILF  Nail, Finger
    NAILT  Nail, Toe
    NARES  Nares
    NASL  Nasal
    NSS  Nasal Septum
    NLACR  Nasolacrimal
    NP  Nasopharyngeal
    NTRAC  Nasotracheal
    NAVEL  Navel
    NECK  Neck
    NERVE  Nerve
    NIPPL  Nipple
    NOSE  Nose
    NOS  Nose (Nasal Passage)
    NOSTR  Nostril
    OCCIP  Occipital
    OLECR  Olecranon
    OMEN  Omentum
    ORBIT  Orbit/Orbital
    ORO  Oropharynx
    OSCOX  Os coxa (pelvic girdle)
    OVARY  Ovary
    PALAT  Palate
    PLATH  Palate, Hard
    PLATS  Palate, Soft
    PALM  Palm
    PANCR  Pancreas
    PAFL  Pancreatic Fluid
    PAS  Parasternal
    PARAT  Paratracheal
    PARIE  Parietal
    PARON  Paronychia
    PAROT  Parotid
    PATEL  Patella
    PELV  Pelvis
    PENSH  Penile Shaft
    PENIS  Penis
    PANAL  Perianal/Perirectal
    PERI  Pericardial Fluid
    PCARD  Pericardium
    PCLIT  Periclitoral
    PERIH  Perihepatic
    PNEAL  Perineal
    PERIN  Perineal Abscess
    PNEPH  Perinephric
    PNM  Perineum
    PORBI  Periorbital
    PERRA  Perirectal
    PERIS  Perisplenic
    PER  Peritoneal
    PERT  Peritoneal Fluid
    PERIT  Peritoneum
    PTONS  Peritonsillar
    PERIU  Periurethal
    PERIV  Perivesicular
    PHALA  Phalanyx
    PILO  Pilonidal
    PINNA  Pinna
    PLC  Placenta
    PLACF  Placenta (Fetal Side)
    PLACM  Placenta (Maternal Side)
    PLANT  Plantar
    PLEUR  Pleura
    PLEU  Pleural Fluid
    PLR  Pleural Fluid (Thoracentesis Fld)
    POPLI  Popliteal
    PREAU  Preauricular
    PRERE  Prerenal
    PRST  Prostate Gland
    PROS  Prostatic Fluid
    PUBIC  Pubic
    PUL  Pulmonary Artery
    RADI  Radial
    RADIUS  Radius
    RECTL  Rectal
    RECTU  Rectum
    RBC  Red Blood Cells
    RENL  Renal
    RNP  Renal Pelvis
    RPERI  Retroperitoneal
    RIB  Rib
    SACRA  Sacral
    SACRO  Sacrococcygeal
    SACIL  Sacroiliac
    SACRU  Sacrum
    SALGL  Salivary Gland
    SCALP  Scalp
    SCAPU  Scapula/Scapular
    SCLER  Sclera
    SCROT  Scrotum/Scrotal
    SEMN  Semen
    SEM  Seminal Fluid
    SEPTU  Septum/Septal
    SEROM  Seroma
    SHIN  Shin
    SHOLJ  Sholder Joint
    SHOL  Shoulder
    SIGMO  Sigmoid
    SINUS  Sinus
    SKM  Skeletal Muscle
    SKENE  Skene's Gland
    SKULL  Skull
    INSTS  Intestine, Small
    SOLE  Sole
    SPRM  Spermatozoa
    SPHEN  Sphenoid
    SPCOR  Spinal Cord
    SPLN  Spleen
    STER  Sternum/Sternal
    STOM  Stoma
    USTOM  Stoma, Urinary
    STOMA  Stomach
    STUMP  Stump
    SCLV  Sub Clavian
    SDP  Subdiaphramatic
    SUB  Subdural
    SUBD  Subdural Fluid
    SGF  Subgaleal Fluid
    SUBM  Submandibular
    SUBX  Submaxillary
    SUBME  Submental
    SUBPH  Subphrenic
    SPX  Supra Cervical
    SCLAV  Supraclavicle/Supraclavicular
    SUPRA  Suprapubic
    SUPB  Suprapubic Specimen
    SWT  Sweat
    SWTG  Sweat Gland
    SYNOL  Synovial
    SYN  Synovial Fluid
    SYNOV  Synovium
    TARS  Tarsal
    TDUCT  Tear Duct
    TEAR  Tears
    TEMPL  Temple
    TEMPO  Temporal
    TML  Temporal Lobe
    TESTI  Testicle(Testis)
    THIGH  Thigh
    THORA  Thoracentesis
    THRB  Throat
    THUMB  Thumb
    TNL  Thumbnail
    THM  Thymus
    THYRD  Thyroid
    TIBIA  Tibia
    TOE  Toe
    TOEN  Toe Nail
    TONG  Tongue
    TONS  Tonsil
    TOOTH  Tooth
    TSK  Tooth Socket
    TRCHE  Trachea/Tracheal
    TBRON  Transbronchial
    TCN  Transcarina Asp
    ULNA  Ulna/Ulnar
    UMB  Umbilical Blood
    UMBL  Umbilicus
    URET  Ureter
    URTH  Urethra
    UTERI  Uterine
    SAC  Uterine Cul/De/Sac
    UTER  Uterus
    VAGIN  Vagina/Vaginal
    VCUFF  Vaginal Cuff
    VGV  Vaginal Vault
    VAL  Valve
    VAS  Vas Deferens
    VASTL  Vastus Lateralis
    VAULT  Vault
    VEIN  Vein
    VENTG  Ventragluteal
    VCSF  Ventricular CSF
    VERMI  Vermis Cerebelli
    VERTC  Vertebra, cervical
    VERTL  Vertebra, lumbar
    VERTT  Vertebra, thoracic
    VESI  Vesicle
    VESCL  Vesicular
    VESFLD  Vesicular Fluid
    VESTI  Vestibule(Genital)
    VITR  Vitreous Fluid
    VOC  Vocal Cord
    VULVA  Vulva
    WRIST  Wrist
    """

    JUGE = "JUGE"
    ADB = "ADB"
    ACET = "ACET"
    ACHIL = "ACHIL"
    ADE = "ADE"
    ADR = "ADR"
    AMN = "AMN"
    AMS = "AMS"
    ANAL = "ANAL"
    ANKL = "ANKL"
    ANTEC = "ANTEC"
    ANTECF = "ANTECF"
    ANTR = "ANTR"
    ANUS = "ANUS"
    AORTA = "AORTA"
    AR = "AR"
    AV = "AV"
    APDX = "APDX"
    AREO = "AREO"
    ARM = "ARM"
    ARTE = "ARTE"
    ASCIT = "ASCIT"
    ASCT = "ASCT"
    ATR = "ATR"
    AURI = "AURI"
    AXI = "AXI"
    BACK = "BACK"
    BARTD = "BARTD"
    BARTG = "BARTG"
    BRTGF = "BRTGF"
    BPH = "BPH"
    BID = "BID"
    BIFL = "BIFL"
    BLAD = "BLAD"
    BLOOD = "BLOOD"
    BLDA = "BLDA"
    BLDC = "BLDC"
    BLDV = "BLDV"
    CBLD = "CBLD"
    BLD = "BLD"
    BDY = "BDY"
    BON = "BON"
    BMAR = "BMAR"
    BOWEL = "BOWEL"
    BOWLA = "BOWLA"
    BOWSM = "BOWSM"
    BRA = "BRA"
    BRAIN = "BRAIN"
    BCYS = "BCYS"
    BRST = "BRST"
    BRSTFL = "BRSTFL"
    BRO = "BRO"
    BROCH = "BROCH"
    BRONC = "BRONC"
    BRV = "BRV"
    BUCCA = "BUCCA"
    BURSA = "BURSA"
    BURSF = "BURSF"
    BUTT = "BUTT"
    CALF = "CALF"
    CANAL = "CANAL"
    CANLI = "CANLI"
    CNL = "CNL"
    CANTH = "CANTH"
    CDM = "CDM"
    CARO = "CARO"
    CARP = "CARP"
    CAVIT = "CAVIT"
    CHE = "CHE"
    CECUM = "CECUM"
    CSF = "CSF"
    CVX = "CVX"
    CERVUT = "CERVUT"
    CHEEK = "CHEEK"
    CHES = "CHES"
    CHEST = "CHEST"
    CHIN = "CHIN"
    CIRCU = "CIRCU"
    CLAVI = "CLAVI"
    CLITO = "CLITO"
    CLIT = "CLIT"
    COCCG = "COCCG"
    COCCY = "COCCY"
    COLON = "COLON"
    COLOS = "COLOS"
    COS = "COS"
    CDUCT = "CDUCT"
    CONJ = "CONJ"
    CORAL = "CORAL"
    COR = "COR"
    CORD = "CORD"
    CORN = "CORN"
    CRANE = "CRANE"
    CRANF = "CRANF"
    CRANO = "CRANO"
    CRANP = "CRANP"
    CRANS = "CRANS"
    CRANT = "CRANT"
    CUBIT = "CUBIT"
    CUFF = "CUFF"
    CULD = "CULD"
    CULDO = "CULDO"
    DELT = "DELT"
    DENTA = "DENTA"
    DEN = "DEN"
    DIAF = "DIAF"
    DPH = "DPH"
    DIGIT = "DIGIT"
    DISC = "DISC"
    DORS = "DORS"
    DUFL = "DUFL"
    DUODE = "DUODE"
    DUR = "DUR"
    EAR = "EAR"
    EARBI = "EARBI"
    EARBM = "EARBM"
    EARBS = "EARBS"
    EARLO = "EARLO"
    ELBOW = "ELBOW"
    ELBOWJ = "ELBOWJ"
    ENDC = "ENDC"
    EC = "EC"
    EOLPH = "EOLPH"
    ENDM = "ENDM"
    ET = "ET"
    EUR = "EUR"
    EOS = "EOS"
    EPICA = "EPICA"
    EPICM = "EPICM"
    EPD = "EPD"
    EPIDU = "EPIDU"
    EPIGL = "EPIGL"
    ESOPG = "ESOPG"
    ESO = "ESO"
    ETHMO = "ETHMO"
    ANBSP = "Â "
    EYE = "EYE"
    BROW = "BROW"
    EYELI = "EYELI"
    FACE = "FACE"
    FBINC = "FBINC"
    FBLAC = "FBLAC"
    FBMAX = "FBMAX"
    FBNAS = "FBNAS"
    FBPAL = "FBPAL"
    FBVOM = "FBVOM"
    FBZYG = "FBZYG"
    FALLT = "FALLT"
    FEMOR = "FEMOR"
    FMH = "FMH"
    FEMUR = "FEMUR"
    FET = "FET"
    FIBU = "FIBU"
    FING = "FING"
    FINGN = "FINGN"
    FOL = "FOL"
    FOOT = "FOOT"
    FOREA = "FOREA"
    FOREH = "FOREH"
    FORES = "FORES"
    FOURC = "FOURC"
    GB = "GB"
    GEN = "GEN"
    GVU = "GVU"
    GENC = "GENC"
    GL = "GL"
    GENL = "GENL"
    GLAND = "GLAND"
    GLANS = "GLANS"
    GLUTE = "GLUTE"
    GLUT = "GLUT"
    GLUTM = "GLUTM"
    GROIN = "GROIN"
    GUM = "GUM"
    HAR = "HAR"
    HAL = "HAL"
    HAND = "HAND"
    HEAD = "HEAD"
    HART = "HART"
    HV = "HV"
    HVB = "HVB"
    HVT = "HVT"
    HEEL = "HEEL"
    HEM = "HEM"
    HIP = "HIP"
    HIPJ = "HIPJ"
    HUMER = "HUMER"
    HYMEN = "HYMEN"
    ILC = "ILC"
    ILE = "ILE"
    ILEOS = "ILEOS"
    ILEUM = "ILEUM"
    ILIAC = "ILIAC"
    ILCR = "ILCR"
    ILCON = "ILCON"
    INGUI = "INGUI"
    JUGI = "JUGI"
    INT = "INT"
    ICX = "ICX"
    INASA = "INASA"
    INTRU = "INTRU"
    INTRO = "INTRO"
    ISCHI = "ISCHI"
    JAW = "JAW"
    KIDN = "KIDN"
    KNEE = "KNEE"
    KNEEF = "KNEEF"
    KNEEJ = "KNEEJ"
    LABIA = "LABIA"
    LABMA = "LABMA"
    LABMI = "LABMI"
    LACRI = "LACRI"
    LAM = "LAM"
    INSTL = "INSTL"
    LARYN = "LARYN"
    LEG = "LEG"
    LENS = "LENS"
    WBC = "WBC"
    LING = "LING"
    LINGU = "LINGU"
    LIP = "LIP"
    STOOLL = "STOOLL"
    LIVER = "LIVER"
    LOBE = "LOBE"
    LOCH = "LOCH"
    ISH = "ISH"
    LUMBA = "LUMBA"
    LMN = "LMN"
    LUNG = "LUNG"
    LN = "LN"
    LNG = "LNG"
    LYM = "LYM"
    MAC = "MAC"
    MALLE = "MALLE"
    MANDI = "MANDI"
    MAR = "MAR"
    MAST = "MAST"
    MAXIL = "MAXIL"
    MAXS = "MAXS"
    MEATU = "MEATU"
    MEC = "MEC"
    MEDST = "MEDST"
    MEDU = "MEDU"
    MOU = "MOU"
    MPB = "MPB"
    METAC = "METAC"
    METAT = "METAT"
    MILK = "MILK"
    MITRL = "MITRL"
    MOLAR = "MOLAR"
    MP = "MP"
    MONSU = "MONSU"
    MONSV = "MONSV"
    MOUTH = "MOUTH"
    MRSA2 = "MRSA2"
    MYO = "MYO"
    NAIL = "NAIL"
    NAILB = "NAILB"
    NAILF = "NAILF"
    NAILT = "NAILT"
    NARES = "NARES"
    NASL = "NASL"
    NSS = "NSS"
    NLACR = "NLACR"
    NP = "NP"
    NTRAC = "NTRAC"
    NAVEL = "NAVEL"
    NECK = "NECK"
    NERVE = "NERVE"
    NIPPL = "NIPPL"
    NOSE = "NOSE"
    NOS = "NOS"
    NOSTR = "NOSTR"
    OCCIP = "OCCIP"
    OLECR = "OLECR"
    OMEN = "OMEN"
    ORBIT = "ORBIT"
    ORO = "ORO"
    OSCOX = "OSCOX"
    OVARY = "OVARY"
    PALAT = "PALAT"
    PLATH = "PLATH"
    PLATS = "PLATS"
    PALM = "PALM"
    PANCR = "PANCR"
    PAFL = "PAFL"
    PAS = "PAS"
    PARAT = "PARAT"
    PARIE = "PARIE"
    PARON = "PARON"
    PAROT = "PAROT"
    PATEL = "PATEL"
    PELV = "PELV"
    PENSH = "PENSH"
    PENIS = "PENIS"
    PANAL = "PANAL"
    PERI = "PERI"
    PCARD = "PCARD"
    PCLIT = "PCLIT"
    PERIH = "PERIH"
    PNEAL = "PNEAL"
    PERIN = "PERIN"
    PNEPH = "PNEPH"
    PNM = "PNM"
    PORBI = "PORBI"
    PERRA = "PERRA"
    PERIS = "PERIS"
    PER = "PER"
    PERT = "PERT"
    PERIT = "PERIT"
    PTONS = "PTONS"
    PERIU = "PERIU"
    PERIV = "PERIV"
    PHALA = "PHALA"
    PILO = "PILO"
    PINNA = "PINNA"
    PLC = "PLC"
    PLACF = "PLACF"
    PLACM = "PLACM"
    PLANT = "PLANT"
    PLEUR = "PLEUR"
    PLEU = "PLEU"
    PLR = "PLR"
    POPLI = "POPLI"
    PREAU = "PREAU"
    PRERE = "PRERE"
    PRST = "PRST"
    PROS = "PROS"
    PUBIC = "PUBIC"
    PUL = "PUL"
    RADI = "RADI"
    RADIUS = "RADIUS"
    RECTL = "RECTL"
    RECTU = "RECTU"
    RBC = "RBC"
    RENL = "RENL"
    RNP = "RNP"
    RPERI = "RPERI"
    RIB = "RIB"
    SACRA = "SACRA"
    SACRO = "SACRO"
    SACIL = "SACIL"
    SACRU = "SACRU"
    SALGL = "SALGL"
    SCALP = "SCALP"
    SCAPU = "SCAPU"
    SCLER = "SCLER"
    SCROT = "SCROT"
    SEMN = "SEMN"
    SEM = "SEM"
    SEPTU = "SEPTU"
    SEROM = "SEROM"
    SHIN = "SHIN"
    SHOLJ = "SHOLJ"
    SHOL = "SHOL"
    SIGMO = "SIGMO"
    SINUS = "SINUS"
    SKM = "SKM"
    SKENE = "SKENE"
    SKULL = "SKULL"
    INSTS = "INSTS"
    SOLE = "SOLE"
    SPRM = "SPRM"
    SPHEN = "SPHEN"
    SPCOR = "SPCOR"
    SPLN = "SPLN"
    STER = "STER"
    STOM = "STOM"
    USTOM = "USTOM"
    STOMA = "STOMA"
    STUMP = "STUMP"
    SCLV = "SCLV"
    SDP = "SDP"
    SUB = "SUB"
    SUBD = "SUBD"
    SGF = "SGF"
    SUBM = "SUBM"
    SUBX = "SUBX"
    SUBME = "SUBME"
    SUBPH = "SUBPH"
    SPX = "SPX"
    SCLAV = "SCLAV"
    SUPRA = "SUPRA"
    SUPB = "SUPB"
    SWT = "SWT"
    SWTG = "SWTG"
    SYNOL = "SYNOL"
    SYN = "SYN"
    SYNOV = "SYNOV"
    TARS = "TARS"
    TDUCT = "TDUCT"
    TEAR = "TEAR"
    TEMPL = "TEMPL"
    TEMPO = "TEMPO"
    TML = "TML"
    TESTI = "TESTI"
    THIGH = "THIGH"
    THORA = "THORA"
    THRB = "THRB"
    THUMB = "THUMB"
    TNL = "TNL"
    THM = "THM"
    THYRD = "THYRD"
    TIBIA = "TIBIA"
    TOE = "TOE"
    TOEN = "TOEN"
    TONG = "TONG"
    TONS = "TONS"
    TOOTH = "TOOTH"
    TSK = "TSK"
    TRCHE = "TRCHE"
    TBRON = "TBRON"
    TCN = "TCN"
    ULNA = "ULNA"
    UMB = "UMB"
    UMBL = "UMBL"
    URET = "URET"
    URTH = "URTH"
    UTERI = "UTERI"
    SAC = "SAC"
    UTER = "UTER"
    VAGIN = "VAGIN"
    VCUFF = "VCUFF"
    VGV = "VGV"
    VAL = "VAL"
    VAS = "VAS"
    VASTL = "VASTL"
    VAULT = "VAULT"
    VEIN = "VEIN"
    VENTG = "VENTG"
    VCSF = "VCSF"
    VERMI = "VERMI"
    VERTC = "VERTC"
    VERTL = "VERTL"
    VERTT = "VERTT"
    VESI = "VESI"
    VESCL = "VESCL"
    VESFLD = "VESFLD"
    VESTI = "VESTI"
    VITR = "VITR"
    VOC = "VOC"
    VULVA = "VULVA"
    WRIST = "WRIST"


class InvoiceControlCode(str, Enum):
    """
    553 - Invoice Control Code

    OR  Original Invoice
    CN  Cancel Invoice
    CG  Cancel Invoice Product/Service Group
    CL  Cancel Invoice Product/Service Line Item
    PD  Pre-Determination Invoice
    RA  Re-Assessment
    OA  Original Authorization
    SA  Special Authorization
    AI  Combined Authorization and Adjudication request
    PA  Pre-Authorization
    AA  Authorization request for inpatient admission
    EA  Authorization request for inpatient stay extension
    RC  Referral Pre-Authorization
    CA  Cancel Authorization request
    CP  Copy of Invoice
    CQ  Coverage Register Query
    RU  Referral authorization
    """

    OR = "OR"
    CN = "CN"
    CG = "CG"
    CL = "CL"
    PD = "PD"
    RA = "RA"
    OA = "OA"
    SA = "SA"
    AI = "AI"
    PA = "PA"
    AA = "AA"
    EA = "EA"
    RC = "RC"
    CA = "CA"
    CP = "CP"
    CQ = "CQ"
    RU = "RU"


class InvoiceReasonCodes(str, Enum):
    """
    554 - Invoice Reason Codes

    LATE  Late Invoice
    NORM  Normal submission
    SUB  Subscriber coverage problem
    """

    LATE = "LATE"
    NORM = "NORM"
    SUB = "SUB"


class InvoiceType(str, Enum):
    """
    555 - Invoice Type

    FS  Fee for Service
    SS  By Session
    GP  Group
    BK  Block
    SL  Salary
    IN  Information Only
    NP  Non Patient
    FN  Final
    PA  Partial
    SU  Supplemental
    """

    FS = "FS"
    SS = "SS"
    GP = "GP"
    BK = "BK"
    SL = "SL"
    IN = "IN"
    NP = "NP"
    FN = "FN"
    PA = "PA"
    SU = "SU"


class BenefitGroup(str, Enum):
    """
    556 - Benefit Group

    AMB  AMBULATORY CARE
    DENT  DENTAL
    """

    AMB = "AMB"
    DENT = "DENT"


class PayeeType(str, Enum):
    """
    557 - Payee Type

    ORG  Payee Organization
    PERS  Person
    PPER  Pay Person
    EMPL  Employer
    """

    ORG = "ORG"
    PERS = "PERS"
    PPER = "PPER"
    EMPL = "EMPL"


class PayeeRelationshiptoInvoice(str, Enum):
    """
    558 - Payee Relationship to Invoice

    PT  Patient
    FM  Family Member
    SB  Subscriber
    GT  Guarantor
    """

    PT = "PT"
    FM = "FM"
    SB = "SB"
    GT = "GT"


class Product_ServiceStatus(str, Enum):
    """
    559 - Product-Service Status

    P  Processed
    D  Denied
    R  Rejected
    """

    P = "P"
    D = "D"
    R = "R"


class QuantityUnits(str, Enum):
    """
    560 - Quantity Units

    FL  Units
    HS  Hours
    DY  Days
    MN  Month
    YY  Years
    """

    FL = "FL"
    HS = "HS"
    DY = "DY"
    MN = "MN"
    YY = "YY"


class Product_ServicesClarificationCodes(str, Enum):
    """
    561 - Product-Services Clarification Codes

    DTCTR  Data Center Number
    SEQ  Sequence Number
    DGAPP  Diagnostic Approval Number
    CLCTR  Claim Center
    ENC  Encounter Number
    OOP  Out of Province Indicator
    GFTH  Good Faith Indicator
    """

    DTCTR = "DTCTR"
    SEQ = "SEQ"
    DGAPP = "DGAPP"
    CLCTR = "CLCTR"
    ENC = "ENC"
    OOP = "OOP"
    GFTH = "GFTH"


class ProcessingConsiderationCodes(str, Enum):
    """
    562 - Processing Consideration Codes

    PAPER  Paper documentation to follow
    EFORM  Electronic form to follow
    FAX  Fax to follow
    RTADJ  Real Time Adjudication Processing
    DFADJ  Deferred Adjudication Processing
    PYRDELAY  Delayed by a Previous Payer
    """

    PAPER = "PAPER"
    EFORM = "EFORM"
    FAX = "FAX"
    RTADJ = "RTADJ"
    DFADJ = "DFADJ"
    PYRDELAY = "PYRDELAY"


class AdjustmentCategoryCode(str, Enum):
    """
    564 - Adjustment Category Code

    EA  Edit/Adjudication Response
    IN  Information
    PA  Provider Adjustment
    PR  Processing Result
    """

    EA = "EA"
    IN = "IN"
    PA = "PA"
    PR = "PR"


class ProviderAdjustmentReasonCode(str, Enum):
    """
    565 - Provider Adjustment Reason Code

    PST  Provincial Sales Tax
    GST  Goods and Services Tax
    HST  Harmonized Sales Tax
    DISP  Dispensing Fee
    MKUP  Mark up Fee
    """

    PST = "PST"
    GST = "GST"
    HST = "HST"
    DISP = "DISP"
    MKUP = "MKUP"


class AdjustmentAction(str, Enum):
    """
    569 - Adjustment Action

    EOB  Print on EOB
    PAT  Inform Patient
    PRO  Inform Provider
    """

    EOB = "EOB"
    PAT = "PAT"
    PRO = "PRO"


class PaymentMethodCode(str, Enum):
    """
    570 - Payment Method Code

    CASH  Cash
    CCCA  Credit Card
    CCHK  Cashier's Check
    CDAC  Credit/Debit Account
    CHCK  Check
    DDPO  Direct Deposit
    DEBC  Debit Card
    SWFT  Society for Worldwide Interbank Financial Telecommunications (S.W.I.F.T.)
    TRAC  Traveler's Check
    VISN  VISA Special Electronic Funds Transfer Network
    """

    CASH = "CASH"
    CCCA = "CCCA"
    CCHK = "CCHK"
    CDAC = "CDAC"
    CHCK = "CHCK"
    DDPO = "DDPO"
    DEBC = "DEBC"
    SWFT = "SWFT"
    TRAC = "TRAC"
    VISN = "VISN"


class InvoiceProcessingResultsStatus(str, Enum):
    """
    571 - Invoice Processing Results Status

    ACK  Acknowledge
    REJECT  Reject
    PEND  Pending
    ADJZER  Adjudicated to Zero
    ADJSUB  Adjudicated as Submitted
    ADJ  Adjudicated with Adjustments
    PAID  Paid
    PRED  Pre-Determination
    """

    ACK = "ACK"
    REJECT = "REJECT"
    PEND = "PEND"
    ADJZER = "ADJZER"
    ADJSUB = "ADJSUB"
    ADJ = "ADJ"
    PAID = "PAID"
    PRED = "PRED"


class Taxstatus(str, Enum):
    """
    572 - Tax status

    RVAT  Registered in VAT register
    UVAT  Unregistered in VAT register
    """

    RVAT = "RVAT"
    UVAT = "UVAT"


class UserAuthenticationCredentialTypeCode(str, Enum):
    """
    615 - User Authentication Credential Type Code

    KERB  Kerberos Service Ticket
    SAML  Authenticated User Identity Assertion
    """

    KERB = "KERB"
    SAML = "SAML"


class AddressExpirationReason(str, Enum):
    """
    616 - Address Expiration Reason

    M  Moved
    E  Added in error
    R  On request
    C  Corrected
    """

    M = "M"
    E = "E"
    R = "R"
    C = "C"


class AddressUsage(str, Enum):
    """
    617 - Address Usage

    M  Mailing
    V  Visit
    C  Classification
    """

    M = "M"
    V = "V"
    C = "C"


class ProtectionCode(str, Enum):
    """
    618 - Protection Code

    LI  Listed
    UL  Unlisted (Should not appear in directories)
    UP  Unpublished
    """

    LI = "LI"
    UL = "UL"
    UP = "UP"


class ItemStatusCodes(str, Enum):
    """
    625 - Item Status Codes

    1  Active
    2  Pending Inactive
    3  Inactive
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"


class ItemImportanceCodes(str, Enum):
    """
    634 - Item Importance Codes

    CRT  Critical
    """

    CRT = "CRT"


class ReorderTheoryCodes(str, Enum):
    """
    642 - Reorder Theory Codes

    D  DOP/DOQ
    M  MIN/MAX
    O  Override
    """

    D = "D"
    M = "M"
    O = "O"


class LaborCalculationType(str, Enum):
    """
    651 - Labor Calculation Type

    TME  Time
    CST  Cost
    """

    TME = "TME"
    CST = "CST"


class DateFormat(str, Enum):
    """
    653 - Date Format

    1  mm/dd/yy
    2  yy.mm.dd
    3  dd/mm/yy
    4  dd.mm.yy
    5  yy/mm/dd
    6  Yymmdd
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"


class DeviceType(str, Enum):
    """
    657 - Device Type

    1  EO Gas Sterilizer
    2  Steam Sterilizer
    3  Peracetic Acid
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"


class LotControl(str, Enum):
    """
    659 - Lot Control

    1  OR Mode Without Operator
    2  OR Mode with Operator
    3  CPD Mode Without Operator
    4  CPD Mode With Operator
    5  Offline Mode
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"


class DeviceDataState(str, Enum):
    """
    667 - Device Data State

    0  Real Time Values
    1  Historic Values
    """

    _0 = "0"
    _1 = "1"


class LoadStatus(str, Enum):
    """
    669 - Load Status

    LLD  Building a Load
    LCP  Load In Process
    LCC  Load is Complete
    LCN  Load Canceled
    """

    LLD = "LLD"
    LCP = "LCP"
    LCC = "LCC"
    LCN = "LCN"


class DeviceStatus(str, Enum):
    """
    682 - Device Status

    0  Ready
    1  Not Ready
    """

    _0 = "0"
    _1 = "1"


class CycleType(str, Enum):
    """
    702 - Cycle Type

    FLS  Flash
    PRV  Prevac
    GRV  Gravity
    LQD  Liquid
    EXP  Express
    DRT  Dart
    DRW  Dart Warm-up Cycle
    THR  Thermal
    ISO  Isothermal
    BWD  Bowie-Dick Test
    LKT  Leak Test
    WFP  Wrap/Steam Flush Pressure Pulse (Wrap/SFPP)
    SFP  Steam Flush Pressure Pulse
    CMW  Chemical Wash
    PEA  Peracetic Acid
    EOH  EO High Temperature
    EOL  EO Low Temperature
    CRT  Cart Wash
    UTL  Utensil Wash
    IST  Instrument Wash
    GLS  Glassware
    PLA  Plastic Goods Wash
    ANR  Anesthesia/Respiratory
    GTL  Gentle
    OPW  Optional Wash
    BDP  Bedpans
    TRB  Tray/Basin
    GNP  Gen. Purpose
    COD  Code
    RNS  Rinse
    2RS  Second Rinse
    DEC  Decontamination
    """

    FLS = "FLS"
    PRV = "PRV"
    GRV = "GRV"
    LQD = "LQD"
    EXP = "EXP"
    DRT = "DRT"
    DRW = "DRW"
    THR = "THR"
    ISO = "ISO"
    BWD = "BWD"
    LKT = "LKT"
    WFP = "WFP"
    SFP = "SFP"
    CMW = "CMW"
    PEA = "PEA"
    EOH = "EOH"
    EOL = "EOL"
    CRT = "CRT"
    UTL = "UTL"
    IST = "IST"
    GLS = "GLS"
    PLA = "PLA"
    ANR = "ANR"
    GTL = "GTL"
    OPW = "OPW"
    BDP = "BDP"
    TRB = "TRB"
    GNP = "GNP"
    COD = "COD"
    RNS = "RNS"
    _2RS = "2RS"
    DEC = "DEC"


class AccessRestrictionValue(str, Enum):
    """
    717 - Access Restriction Value

    ALL  All
    DEM  All demographic data
    LOC  Patient Location
    PID-7  Date of Birth
    PID-17  Religion
    HIV  HIV status and results
    STD  Sexually transmitted diseases
    PSY  Psychiatric Mental health
    DRG  Drug
    SMD  Sensitive medical data
    NO  None
    OO  Opt out all registries (HIPAA)
    OI  Opt in all registries (HIPAA)
    """

    ALL = "ALL"
    DEM = "DEM"
    LOC = "LOC"
    PID_7 = "PID-7"
    PID_17 = "PID-17"
    HIV = "HIV"
    STD = "STD"
    PSY = "PSY"
    DRG = "DRG"
    SMD = "SMD"
    NO = "NO"
    OO = "OO"
    OI = "OI"


class AccessRestrictionReasonCode(str, Enum):
    """
    719 - Access Restriction Reason Code

    PAT  Patient Request
    PHY  Physician Request
    REG  Regulatory requirement
    ORG  Organizational policy or requirement
    EMP  Employee of this organization
    DIA  Diagnosis-related
    VIP  Very important person or celebrity
    """

    PAT = "PAT"
    PHY = "PHY"
    REG = "REG"
    ORG = "ORG"
    EMP = "EMP"
    DIA = "DIA"
    VIP = "VIP"


class MoodCodes(str, Enum):
    """
    725 - Mood Codes

    INT  Intent
    APT  Appointment
    ARQ  Appointment Request
    PRMS  Promise
    PRP  Proposal
    RQO  Request-Order
    EVN  Event
    EVN.CRT  Event Criterion
    EXP  Expectation
    """

    INT = "INT"
    APT = "APT"
    ARQ = "ARQ"
    PRMS = "PRMS"
    PRP = "PRP"
    RQO = "RQO"
    EVN = "EVN"
    EVN_CRT = "EVN.CRT"
    EXP = "EXP"


class CCLValue(str, Enum):
    """
    728 - CCL Value

    0  Nothing obvious
    1  Low
    2  Moderate
    3  High
    4  Very high
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"


class DRGDiagnosisDeterminationStatus(str, Enum):
    """
    731 - DRG Diagnosis Determination Status

    0  Valid code
    1  Invalid code
    2  Two primary diagnosis codes
    3  Invalid for this gender
    4  Invalid for this age
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"


class GrouperStatus(str, Enum):
    """
    734 - Grouper Status

    0  Normal grouping
    1  Invalid or missing primary diagnosis
    2  Diagnosis is not allowed to be primary
    3  Data does not fulfill DRG criteria
    4  Invalid age, admission date, date of birth or discharge date
    5  Invalid gender
    6  Invalid discharge status
    7  Invalid weight ad admission
    8  Invalid length of stay
    9  Invalid field "same day"
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


class StatusPatient(str, Enum):
    """
    739 - Status Patient

    1  Normal length of stay
    2  Short length of stay
    3  Long length of stay
    """

    _1 = "1"
    _2 = "2"
    _3 = "3"


class DRGStatusFinancialCalculation(str, Enum):
    """
    742 - DRG Status Financial Calculation

    00  Effective weight calculated
    01  Hospital specific contract
    03  Eeffective weight for transfer/referral calculated
    04  Referral from other hospital based on a cooperation (no DRG reimbursement)
    05  Invalid length of stay
    10  No information/entry in cost data for this DRG
    11  No relative weight found for department (type)
    """

    _00 = "00"
    _01 = "01"
    _03 = "03"
    _04 = "04"
    _05 = "05"
    _10 = "10"
    _11 = "11"


class DRGGroupingStatus(str, Enum):
    """
    749 - DRG Grouping Status

    0  Valid code; not used for grouping
    1  Valid code; used for grouping
    2  Invalid code; not used for grouping
    3  Invalid code; code is relevant for grouping
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"


class StatusWeightAtBirth(str, Enum):
    """
    755 - Status Weight At Birth

    0  No weight reported at admission used for grouping
    1  Weight reported at admission used for grouping
    2  Default weight (>2499g) used for grouping
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class StatusRespirationMinutes(str, Enum):
    """
    757 - Status Respiration Minutes

    0  Respiration minutes not used for grouping
    1  Listed respiration minutes used for grouping
    2  OPS code value used for grouping
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class StatusAdmission(str, Enum):
    """
    759 - Status Admission

    0  Admission status is valid; used for grouping
    1  Admission status is valid; not used for grouping
    2  Admission status is invalid; not used for grouping
    3  Admission status is invalid; default value used for grouping
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"


class DRGProcedureDeterminationStatus(str, Enum):
    """
    761 - DRG Procedure Determination Status

    0  Valid code
    1  Invalid code
    2  Not used
    3  Invalid for this gender
    4  Invalid for this age
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"


class DRGProcedureRelevance(str, Enum):
    """
    763 - DRG Procedure Relevance

    0  Neither operation relevant nor non-operation relevant procedure
    1  Operation relevant procedure
    2  Non-operation relevant procedure
    """

    _0 = "0"
    _1 = "1"
    _2 = "2"


class ItemStatus(str, Enum):
    """
    776 - Item Status

    A  Active
    P  Pending Inactive
    I  Inactive
    """

    A = "A"
    P = "P"
    I = "I"


class ItemType(str, Enum):
    """
    778 - Item Type

    EQP  Equipment
    SUP  Supply
    IMP  Implant
    MED  Medication
    TDC  Tubes, Drains, and Catheters
    """

    EQP = "EQP"
    SUP = "SUP"
    IMP = "IMP"
    MED = "MED"
    TDC = "TDC"


class ApprovingRegulatoryAgency(str, Enum):
    """
    790 - Approving Regulatory Agency

    FDA  Food and Drug Administration
    AMA  American Medical Association
    """

    FDA = "FDA"
    AMA = "AMA"


class RulingAct(str, Enum):
    """
    793 - Ruling Act

    SMDA  Safe Medical Devices Act
    """

    SMDA = "SMDA"


class SterilizationType(str, Enum):
    """
    806 - Sterilization Type

    EOG  Ethylene Oxide Gas
    PCA  Peracetic acid
    STM  Steam
    """

    EOG = "EOG"
    PCA = "PCA"
    STM = "STM"


class Package(str, Enum):
    """
    818 - Package

    CS  Case
    BX  Box
    EA  Each
    SET  Set
    """

    CS = "CS"
    BX = "BX"
    EA = "EA"
    SET = "SET"


class MIMETypes(str, Enum):
    """
    834 - MIME Types

    application  Application data
    audio  Audio data
    image  Image data
    model  Model data
    text  Text data
    video  Video data
    multipart  MIME multipart package
    """

    application = "application"
    audio = "audio"
    image = "image"
    model = "model"
    text = "text"
    video = "video"
    multipart = "multipart"


class ProblemSeverity(str, Enum):
    """
    836 - Problem Severity

    No Values Defined
    """

    No_Values_Defined = "No Values Defined"


class ProblemPerspective(str, Enum):
    """
    838 - Problem Perspective

    No Values Defined
    """

    No_Values_Defined = "No Values Defined"


class Telecommunicationexpirationreason(str, Enum):
    """
    868 - Telecommunication expiration reason

    M  Moved
    E  Added in error
    R  On request
    C  Corrected
    N  No longer in service
    """

    M = "M"
    E = "E"
    R = "R"
    C = "C"
    N = "N"


class SupplyRiskCodes(str, Enum):
    """
    871 - Supply Risk Codes

    COR  Corrosive
    FLA  Flammable
    EXP  Explosive
    INJ  Injury Hazard
    TOX  Toxic
    RAD  Radioactive
    UNK  Unknown
    """

    COR = "COR"
    FLA = "FLA"
    EXP = "EXP"
    INJ = "INJ"
    TOX = "TOX"
    RAD = "RAD"
    UNK = "UNK"


class RoleExecutingPhysician(str, Enum):
    """
    881 - Role Executing Physician

    T  Technical Part
    P  Professional Part
    B  Both
    """

    T = "T"
    P = "P"
    B = "B"


class MedicalRoleExecutingPhysician(str, Enum):
    """
    882 - Medical Role Executing Physician

    E  Employed
    SE  Self-employed
    """

    E = "E"
    SE = "SE"


class Sideofbody(str, Enum):
    """
    894 - Side of body

    L  Left
    R  Right
    """

    L = "L"
    R = "R"


class PresentOnAdmission_Indicator(str, Enum):
    """
    895 - Present On Admission (POA) Indicator

    Y  Yes
    N  No
    U  Unknown
    W  Not applicable
    E  Exempt
    """

    Y = "Y"
    N = "N"
    U = "U"
    W = "W"
    E = "E"
