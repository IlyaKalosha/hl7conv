from pydantic import BaseModel, Field


class OBX(BaseModel):
    obx_1: int = Field(None, alias="1")
    obx_2: str = Field(None, alias="2")
    obx_3: str = Field(None, alias="3")
    obx_4: str = Field(None, alias="4")
    obx_5: str = Field(None, alias="5")
    obx_6: str = Field(None, alias="6")
