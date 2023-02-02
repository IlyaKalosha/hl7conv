from pydantic import BaseModel, Field

from hl7conv.schemas.versions.v2_5_1.enums import (
    Addresstype,
    Checkdigitscheme,
    Codingsystem,
    CountryCode,
    Degreeorlicenseorcertificate,
    Identifiertype,
    Name_addressrepresentation,
    Nameassemblyorder,
    Organizationalnametype,
    Precision,
    UniversalIDtype,
)


class CodedElement(BaseModel):
    ce_1: str = Field(None, alias="1", description="Identifier")
    ce_2: str = Field(None, alias="2", description="Text")
    ce_3: str = Field(None, alias="3", description="Name Of Coding System")
    ce_4: str = Field(None, alias="4", description="Alternate Identifier")
    ce_5: str = Field(None, alias="5", description="Alternate Text")
    ce_6: str = Field(None, alias="6", description="Name Of Alternate Coding System")


class EntityIdentifier(BaseModel):
    ei_1: str = Field(None, alias="1", description="Entity Identifier")
    ei_2: str = Field(None, alias="2", description="Namespace Id")
    ei_3: str = Field(None, alias="3", description="Universal Id")
    ei_4: UniversalIDtype = Field(None, alias="4", description="Universal Id Type")


class CodedWithExceptions(BaseModel):
    cwe_1: str = Field(None, alias="1", description="Identifier")
    cwe_2: str = Field(None, alias="2", description="Text")
    cwe_3: Codingsystem = Field(None, alias="3", description="Name Of Coding System")
    cwe_4: str = Field(None, alias="4", description="Alternate Identifier")
    cwe_5: str = Field(None, alias="5", description="Alternate Text")
    cwe_6: Codingsystem = Field(
        None, alias="6", description="Name Of Alternate Coding System"
    )
    cwe_7: str = Field(None, alias="7", description="Coding System Version Id")
    cwe_8: str = Field(
        None, alias="8", description="Alternate Coding System Version Id"
    )
    cwe_9: str = Field(None, alias="9", description="Original Text")


class TimeStamp(BaseModel):
    ts_1: str = Field(..., alias="1", description="Time")
    ts_2: Precision = Field(None, alias="2", description="Degree Of Precision")


class DateAndTimeRange(BaseModel):
    dr_1: TimeStamp = Field(None, alias="1", description="Range Start Date/Time")
    dr_2: TimeStamp = Field(None, alias="2", description="Range End Date/Time")


class HierarchicDesignator(BaseModel):
    hd_1: str = Field(None, alias="1", description="Namespace Id")
    hd_2: str = Field(None, alias="2", description="Universal Id")
    hd_3: str = Field(None, alias="3", description="Universal Id Type")


class FamilyName(BaseModel):
    fn_1: str = Field(..., alias="1", description="Surname")
    fn_2: str = Field(None, alias="2", description="Own Surname Prefix")
    fn_3: str = Field(None, alias="3", description="Own Surname")
    fn_4: str = Field(None, alias="4", description="Surname Prefix From Partner/Spouse")
    fn_5: str = Field(None, alias="5", description="Surname From Partner/Spouse")


class ExtendedAddress(BaseModel):
    xad_1: str = Field(None, alias="1", description="Street Address")
    xad_2: str = Field(None, alias="2", description="Other Designation")
    xad_3: str = Field(None, alias="3", description="City")
    xad_4: str = Field(None, alias="4", description="State Or Province")
    xad_5: str = Field(None, alias="5", description="Zip Or Postal Code")
    xad_6: CountryCode = Field(None, alias="6", description="Country")
    xad_7: Addresstype = Field(None, alias="7", description="Address Type")
    xad_8: str = Field(None, alias="8", description="Other Geographic Designation")
    xad_9: str = Field(None, alias="9", description="County/Parish Code")
    xad_10: str = Field(None, alias="10", description="Census Tract")
    xad_11: Name_addressrepresentation = Field(
        None, alias="11", description="Address Representation Code"
    )
    xad_12: DateAndTimeRange = Field(
        None, alias="12", description="Address Validity Range"
    )
    xad_13: TimeStamp = Field(None, alias="13", description="Effective Date")
    xad_14: TimeStamp = Field(None, alias="14", description="Expiration Date")


class ExtendedCompositeNameAndIdentificationNumberForOrganizations(BaseModel):
    xon_1: str = Field(None, alias="1", description="Organization Name")
    xon_2: Organizationalnametype = Field(
        None, alias="2", description="Organization Name Type Code"
    )
    xon_3: int = Field(None, alias="3", description="Id Number")
    xon_4: int = Field(None, alias="4", description="Check Digit")
    xon_5: Checkdigitscheme = Field(None, alias="5", description="Check Digit Scheme")
    xon_6: HierarchicDesignator = Field(
        None, alias="6", description="Assigning Authority"
    )
    xon_7: Identifiertype = Field(None, alias="7", description="Identifier Type Code")
    xon_8: HierarchicDesignator = Field(
        None, alias="8", description="Assigning Facility"
    )
    xon_9: Name_addressrepresentation = Field(
        None, alias="9", description="Name Representation Code"
    )
    xon_10: str = Field(None, alias="10", description="Organization Identifier")


class ExtendedCompositeIDNumberandNameforPersons(BaseModel):
    xcn_1: str = Field(None, alias="1", description="Id Number")
    xcn_2: FamilyName = Field(None, alias="2", description="Family Name")
    xcn_3: str = Field(None, alias="3", description="Given Name")
    xcn_4: str = Field(
        None,
        alias="4",
        description="Second And Further Given Names Or Initials Thereof",
    )
    xcn_5: str = Field(None, alias="5", description="Suffix (e.g., Jr Or Iii)")
    xcn_6: str = Field(None, alias="6", description="Prefix (e.g., Dr)")
    xcn_7: Degreeorlicenseorcertificate = Field(
        None, alias="7", description="Degree (e.g., Md)"
    )
    xcn_8: str = Field(None, alias="8", description="Source Table")
    xcn_9: HierarchicDesignator = Field(
        None, alias="9", description="Assigning Authority"
    )
    xcn_10: str = Field(None, alias="10", description="Name Type Code")
    xcn_11: str = Field(None, alias="11", description="Identifier Check Digit")
    xcn_12: Checkdigitscheme = Field(None, alias="12", description="Check Digit Scheme")
    xcn_13: Identifiertype = Field(None, alias="13", description="Identifier Type Code")
    xcn_14: HierarchicDesignator = Field(
        None, alias="14", description="Assigning Facility"
    )
    xcn_15: Name_addressrepresentation = Field(
        None, alias="15", description="Name Representation Code"
    )
    xcn_16: CodedElement = Field(None, alias="16", description="Name Context")
    xcn_17: DateAndTimeRange = Field(
        None, alias="17", description="Name Validity Range"
    )
    xcn_18: Nameassemblyorder = Field(
        None, alias="18", description="Name Assembly Order"
    )
    xcn_19: TimeStamp = Field(None, alias="19", description="Effective Date")
    xcn_20: TimeStamp = Field(None, alias="20", description="Expiration Date")
    xcn_21: str = Field(None, alias="21", description="Professional Suffix")
    xcn_22: CodedWithExceptions = Field(
        None, alias="22", description="Assigning Jurisdiction"
    )
    xcn_23: CodedWithExceptions = Field(
        None, alias="23", description="Assigning Agency Or Department"
    )
