from pydantic import BaseModel, Field, validator

from hl7conv.schemas.versions.v2_5_1.enums import (
    Abnormalflags,
    DiagnosticServiceSectionID,
    EscortRequired,
    NatureofAbnormalTesting,
    ObservationResultHandling,
    Observationresultstatuscodesinterpretation,
    ResultStatus,
    SpecimenActionCode,
    TransportArranged,
    TransportationMode,
    ValueType,
)
from hl7conv.schemas.versions.v2_5_1.primitive_validators import si_validator
from hl7conv.schemas.versions.v2_5_1.types import (
    CodedElement,
    CodedWithExceptions,
    CompositeQuantityWithUnits,
    EntityIdentifier,
    EntityIdentifierPair,
    ExtendedAddress,
    ExtendedCompositeIDNumberandNameforPersons,
    ExtendedCompositeNameAndIdentificationNumberForOrganizations,
    ExtendedTelecommunicationNumber,
    MoneyAndCode,
    NameWithDateAndLocation,
    ParentResultLink,
    SpecimenSource,
    TimeStamp,
    TimingQuantity,
)


class OBX(BaseModel):
    obx_1: int = Field(None, alias="1", max_length=4, description="Set ID - OBX")
    obx_2: ValueType = Field(..., alias="2", max_length=2, description="Value Type")
    obx_3: CodedElement = Field(
        ..., alias="3", max_length=250, description="Observation Identifier"
    )
    obx_4: str = Field(None, alias="4", max_length=20, description="Observation Sub-ID")
    obx_5: str = Field(
        None, alias="5", max_length=99999, description="Observation Value"
    )
    obx_6: CodedElement = Field(None, alias="6", max_length=250, description="Units")
    obx_7: str = Field(None, alias="7", max_length=60, description="References Range")
    obx_8: Abnormalflags = Field(
        ..., alias="8", max_length=5, description="Abnormal Flags"
    )
    obx_9: int = Field(None, alias="9", max_length=5, description="Probability")
    obx_10: NatureofAbnormalTesting = Field(
        None, alias="10", max_length=2, description="Nature of Abnormal Test"
    )
    obx_11: Observationresultstatuscodesinterpretation = Field(
        ..., alias="11", max_length=1, description="Observation Result Status"
    )
    obx_12: TimeStamp = Field(
        None, alias="12", max_length=26, description="Effective Date of Reference Range"
    )
    obx_13: str = Field(
        None, alias="13", max_length=20, description="User Defined Access Checks"
    )
    obx_14: TimeStamp = Field(
        None, alias="14", max_length=26, description="Date/Time of the Observation"
    )
    obx_15: CodedElement = Field(
        None, alias="15", max_length=250, description="Producer's ID"
    )
    obx_16: ExtendedCompositeIDNumberandNameforPersons = Field(
        None, alias="16", max_length=250, description="Responsible Observer"
    )
    obx_17: CodedElement = Field(
        None, alias="17", max_length=250, description="Observation Method"
    )
    obx_18: EntityIdentifier = Field(
        None, alias="18", max_length=22, description="Equipment Instance Identifier"
    )
    obx_19: TimeStamp = Field(
        None, alias="19", max_length=26, description="Date/Time of the Analysis"
    )
    obx_20: str = Field(
        None, alias="20", description="Reserved for harmonization with V2.6"
    )
    obx_21: str = Field(
        None, alias="21", description="Reserved for harmonization with V2.6"
    )
    obx_22: str = Field(
        None, alias="22", description="Reserved for harmonization with V2.6"
    )
    obx_23: ExtendedCompositeNameAndIdentificationNumberForOrganizations = Field(
        None, alias="23", max_length=567, description="Performing Organization Name"
    )
    obx_24: ExtendedAddress = Field(
        None, alias="24", max_length=631, description="Performing Organization Address"
    )
    obx_25: ExtendedCompositeIDNumberandNameforPersons = Field(
        None,
        alias="25",
        max_length=3002,
        description="Performing Organization Medical Director",
    )

    _obx_1_val = validator("obx_1", allow_reuse=True)(si_validator)


class OBR(BaseModel):
    obr_1: int = Field(None, alias="1", max_length=4, description="Set ID - OBR")
    obr_2: EntityIdentifier = Field(
        None, alias="2", max_length=22, description="Placer Order Number"
    )
    obr_3: EntityIdentifier = Field(
        None, alias="3", max_length=22, description="Filler Order Number"
    )
    obr_4: CodedElement = Field(
        ..., alias="4", max_length=250, description="Universal Service Identifier"
    )
    obr_5: str = Field(None, alias="5", max_length=2, description="Priority - OBR")
    obr_6: TimeStamp = Field(
        None, alias="6", max_length=26, description="Requested Date/Time"
    )
    obr_7: TimeStamp = Field(
        None, alias="7", max_length=26, description="Observation Date/Time"
    )
    obr_8: TimeStamp = Field(
        None, alias="8", max_length=26, description="Observation End Date/Time"
    )
    obr_9: CompositeQuantityWithUnits = Field(
        None, alias="9", max_length=20, description="Collection Volume"
    )
    obr_10: ExtendedCompositeIDNumberandNameforPersons = Field(
        None, alias="10", max_length=250, description="Collector Identifier"
    )
    obr_11: SpecimenActionCode = Field(
        None, alias="11", max_length=1, description="Specimen Action Code"
    )
    obr_12: CodedElement = Field(
        None, alias="12", max_length=250, description="Danger Code"
    )
    obr_13: str = Field(
        None, alias="13", max_length=300, description="Relevant Clinical Information"
    )
    obr_14: TimeStamp = Field(
        None, alias="14", max_length=26, description="Specimen Received Date/Time"
    )
    obr_15: SpecimenSource = Field(
        None, alias="15", max_length=300, description="Specimen Source"
    )
    obr_16: ExtendedCompositeIDNumberandNameforPersons = Field(
        None, alias="16", max_length=250, description="Ordering Provider"
    )
    obr_17: ExtendedTelecommunicationNumber = Field(
        None, alias="17", max_length=250, description="Order Callback Phone Number"
    )
    obr_18: str = Field(None, alias="18", max_length=60, description="Placer Field 1")
    obr_19: str = Field(None, alias="19", max_length=60, description="Placer Field 2")
    obr_20: str = Field(None, alias="20", max_length=60, description="Filler Field 1")
    obr_21: str = Field(None, alias="21", max_length=60, description="Filler Field 2")
    obr_22: TimeStamp = Field(
        None,
        alias="22",
        max_length=26,
        description="Results Rpt/Status Chng - Date/Time",
    )
    obr_23: MoneyAndCode = Field(
        None, alias="23", max_length=40, description="Charge to Practice"
    )
    obr_24: DiagnosticServiceSectionID = Field(
        None, alias="24", max_length=10, description="Diagnostic Serv Sect ID"
    )
    obr_25: ResultStatus = Field(
        None, alias="25", max_length=1, description="Result Status"
    )
    obr_26: ParentResultLink = Field(
        None, alias="26", max_length=400, description="Parent Result"
    )
    obr_27: TimingQuantity = Field(
        None, alias="27", max_length=200, description="Quantity/Timing"
    )
    obr_28: ExtendedCompositeIDNumberandNameforPersons = Field(
        None, alias="28", max_length=250, description="Result Copies To"
    )
    obr_29: EntityIdentifierPair = Field(
        None, alias="29", max_length=200, description="Parent"
    )
    obr_30: TransportationMode = Field(
        None, alias="30", max_length=20, description="Transportation Mode"
    )
    obr_31: CodedElement = Field(
        None, alias="31", max_length=250, description="Reason for Study"
    )
    obr_32: NameWithDateAndLocation = Field(
        None, alias="32", max_length=200, description="Principal Result Interpreter"
    )
    obr_33: NameWithDateAndLocation = Field(
        None, alias="33", max_length=200, description="Assistant Result Interpreter"
    )
    obr_34: NameWithDateAndLocation = Field(
        None, alias="34", max_length=200, description="Technician"
    )
    obr_35: NameWithDateAndLocation = Field(
        None, alias="35", max_length=200, description="Transcriptionist"
    )
    obr_36: TimeStamp = Field(
        None, alias="36", max_length=26, description="Scheduled Date/Time"
    )
    obr_37: float = Field(
        None, alias="37", max_length=4, description="Number of Sample Containers"
    )
    obr_38: CodedElement = Field(
        None,
        alias="38",
        max_length=250,
        description="Transport Logistics of Collected Sample",
    )
    obr_39: CodedElement = Field(
        None, alias="39", max_length=250, description="Collector's Comment"
    )
    obr_40: CodedElement = Field(
        None,
        alias="40",
        max_length=250,
        description="Transport Arrangement Responsibility",
    )
    obr_41: TransportArranged = Field(
        None, alias="41", max_length=30, description="Transport Arranged"
    )
    obr_42: EscortRequired = Field(
        None, alias="42", max_length=1, description="Escort Required"
    )
    obr_43: CodedElement = Field(
        None,
        alias="43",
        max_length=250,
        description="Planned Patient Transport Comment",
    )
    obr_44: CodedElement = Field(
        None, alias="44", max_length=250, description="Procedure Code"
    )
    obr_45: CodedElement = Field(
        None, alias="45", max_length=250, description="Procedure Code Modifier"
    )
    obr_46: CodedElement = Field(
        None,
        alias="46",
        max_length=250,
        description="Placer Supplemental Service Information",
    )
    obr_47: CodedElement = Field(
        None,
        alias="47",
        max_length=250,
        description="Filler Supplemental Service Information",
    )
    obr_48: CodedWithExceptions = Field(
        None,
        alias="48",
        max_length=250,
        description="Medically Necessary Duplicate Procedure Reason",
    )
    obr_49: ObservationResultHandling = Field(
        None, alias="49", max_length=2, description="Result Handling"
    )
    obr_50: CodedWithExceptions = Field(
        None,
        alias="50",
        max_length=250,
        description="Parent Universal Service Identifier",
    )

    _obr_1_val = validator("obr_1", allow_reuse=True)(si_validator)
