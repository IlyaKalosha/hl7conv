from pydantic import BaseModel, Field


class OBX(BaseModel):
    OBX_1: int = Field(None, alias="1")
