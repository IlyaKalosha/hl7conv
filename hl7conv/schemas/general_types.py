from pydantic import Field, BaseModel


class CodedElement(BaseModel):
    ce_1: str = Field(None, alias="1", description='Identifier')
    ce_2: str = Field(None, alias="2", description='Text')
    ce_3: str = Field(None, alias="3", description='Name Of Coding System')
    ce_4: str = Field(None, alias="4", description='Alternate Identifier')
    ce_5: str = Field(None, alias="5", description='Alternate Text')
    ce_6: str = Field(None, alias="6", description='Name Of Alternate Coding System')
