from pydantic import BaseModel, Field, validator

from hl7conv.schemas.general_types import si_validator
from hl7conv.schemas.versions.v2_5_1.enums import ValueType


class OBX(BaseModel):
    obx_1: int = Field(None, alias="1")
    obx_2: str = Field(None, alias="2")
    obx_3: ValueType = Field(..., alias="3")
    obx_4: str = Field(None, alias="4")
    obx_5: str = Field(None, alias="5")
    obx_6: str = Field(None, alias="6")

    _obx_1_val = validator('obx_1', allow_reuse=True)(si_validator)


a = OBX()