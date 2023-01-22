from pydantic import BaseModel, Field


class OBX(BaseModel):
    obx_1: int = Field(None, alias="1")
    obx_2: str = Field(None, alias="2")
    obx_3: str = Field(None, alias="3")
    obx_4: str = Field(None, alias="4")
    obx_5: str = Field(None, alias="5")
    obx_6: str = Field(None, alias="6")
    obx_7: int = Field(None, alias="7")
    obx_8: str = Field(None, alias="8")
    obx_9: str = Field(None, alias="9")
    obx_10: str = Field(None, alias="10")
    obx_11: str = Field(None, alias="11")
    obx_12: str = Field(None, alias="12")
