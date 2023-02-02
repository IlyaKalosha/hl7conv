from pydantic import BaseModel, Field, validator

from hl7conv.schemas.versions.v2_5_1.enums import (
    Abnormalflags,
    NatureofAbnormalTesting,
    Observationresultstatuscodesinterpretation,
    ValueType,
)
from hl7conv.schemas.versions.v2_5_1.primitive_validators import si_validator
from hl7conv.schemas.versions.v2_5_1.types import (
    CodedElement,
    EntityIdentifier,
    ExtendedAddress,
    ExtendedCompositeIDNumberandNameforPersons,
    ExtendedCompositeNameAndIdentificationNumberForOrganizations,
    TimeStamp,
)


class OBX(BaseModel):
    obx_1: int = Field(None, alias="1", max_length=4, description='Set ID - OBX')
    obx_2: ValueType = Field(..., alias="2", max_length=2, description='Value Type')
    obx_3: CodedElement = Field(..., alias="3", max_length=250, description='Observation Identifier')
    obx_4: str = Field(None, alias="4", max_length=20, description='Observation Sub-ID')
    obx_5: str = Field(None, alias="5", max_length=99999, description='Observation Value')
    obx_6: CodedElement = Field(None, alias="6", max_length=250, description='Units')
    obx_7: str = Field(None, alias="7", max_length=60, description='References Range')
    obx_8: Abnormalflags = Field(..., alias="8", max_length=5, description='Abnormal Flags')
    obx_9: int = Field(None, alias="9", max_length=5, description='Probability')
    obx_10: NatureofAbnormalTesting = Field(None, alias="10", max_length=2, description='Nature of Abnormal Test')
    obx_11: Observationresultstatuscodesinterpretation = Field(..., alias="11", max_length=1, description='Observation Result Status')
    obx_12: TimeStamp = Field(None, alias="12", max_length=26, description='Effective Date of Reference Range')
    obx_13: str = Field(None, alias="13", max_length=20, description='User Defined Access Checks')
    obx_14: TimeStamp = Field(None, alias="14", max_length=26, description='Date/Time of the Observation')
    obx_15: CodedElement = Field(None, alias="15", max_length=250, description="Producer's ID")
    obx_16: ExtendedCompositeIDNumberandNameforPersons = Field(None, alias="16", max_length=250, description='Responsible Observer')
    obx_17: CodedElement = Field(None, alias="17", max_length=250, description='Observation Method')
    obx_18: EntityIdentifier = Field(None, alias="18", max_length=22, description='Equipment Instance Identifier')
    obx_19: TimeStamp = Field(None, alias="19", max_length=26, description='Date/Time of the Analysis')
    obx_20: str = Field(None, alias="20", description='Reserved for harmonization with V2.6')
    obx_21: str = Field(None, alias="21", description='Reserved for harmonization with V2.6')
    obx_22: str = Field(None, alias="22", description='Reserved for harmonization with V2.6')
    obx_23: ExtendedCompositeNameAndIdentificationNumberForOrganizations = Field(None, alias="23", max_length=567, description='Performing Organization Name')
    obx_24: ExtendedAddress = Field(None, alias="24", max_length=631, description='Performing Organization Addres')
    obx_25: ExtendedCompositeIDNumberandNameforPersons = Field(None, alias="25", max_length=3002, description='Performing Organization Medical Director')

    _obx_1_val = validator('obx_1', allow_reuse=True)(si_validator)