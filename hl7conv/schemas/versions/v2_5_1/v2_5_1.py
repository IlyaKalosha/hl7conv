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
    obx_1: int = Field(None, alias="1", max_length=4)
    obx_2: ValueType = Field(..., alias="2")
    obx_3: CodedElement = Field(..., alias="3")
    obx_4: str = Field(None, alias="4")
    obx_5: str = Field(None, alias="5")
    obx_6: str = Field(None, alias="6")
    obx_7: str = Field(None, alias="7")
    obx_8: Abnormalflags = Field(..., alias="8")
    obx_9: int = Field(None, alias="9")
    obx_10: NatureofAbnormalTesting = Field(None, alias="10")
    obx_11: Observationresultstatuscodesinterpretation = Field(..., alias="11")
    obx_12: TimeStamp = Field(None, alias="12")
    obx_13: str = Field(None, alias="13")
    obx_14: TimeStamp = Field(None, alias="14")
    obx_15: CodedElement = Field(None, alias="15")
    obx_16: ExtendedCompositeIDNumberandNameforPersons = Field(None, alias="16")
    obx_17: CodedElement = Field(None, alias="17")
    obx_18: EntityIdentifier = Field(None, alias="18")
    obx_19: TimeStamp = Field(None, alias="19")
    obx_20: str = Field(None, alias="20")
    obx_21: str = Field(None, alias="21")
    obx_22: str = Field(None, alias="22")
    obx_23: ExtendedCompositeNameAndIdentificationNumberForOrganizations = Field(None, alias="23")
    obx_24: ExtendedAddress = Field(None, alias="24")
    obx_25: ExtendedCompositeIDNumberandNameforPersons = Field(None, alias="25")

    _obx_1_val = validator('obx_1', allow_reuse=True)(si_validator)