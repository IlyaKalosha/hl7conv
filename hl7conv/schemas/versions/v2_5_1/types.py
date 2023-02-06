from pydantic import BaseModel, Field

from hl7conv.schemas.versions.v2_5_1.enums import (
    Additive_Preservative,
    Addresstype,
    Bodysite,
    BodySiteModifier,
    Checkdigitscheme,
    Codingsystem,
    CountryCode,
    Degreeorlicenseorcertificate,
    Identifiertype,
    MonetaryDenominationCode,
    Name_addressrepresentation,
    Nameassemblyorder,
    Organizationalnametype,
    Personlocationtype,
    Precision,
    Repeatpattern,
    Sequencecondition,
    SpecimenRole,
    Telecommunicationequipmenttype,
    Telecommunicationusecode,
    TQconjunctionID,
    UniversalIDtype,
)


class CodedElement(BaseModel):
    ce_1: str = Field(None, alias="1", description="Identifier")
    ce_2: str = Field(None, alias="2", description="Text")
    ce_3: str = Field(None, alias="3", description="Name Of Coding System")
    ce_4: str = Field(None, alias="4", description="Alternate Identifier")
    ce_5: str = Field(None, alias="5", description="Alternate Text")
    ce_6: str = Field(None, alias="6", description="Name Of Alternate Coding System")


class ParentResultLink(BaseModel):
    prl_1: CodedElement = Field(
        ..., alias="1", description="Parent Observation Identifier"
    )
    prl_2: str = Field(None, alias="2", description="Parent Observation Sub-identifier")
    prl_3: str = Field(
        None, alias="3", description="Parent Observation Value Descriptor"
    )


class Money(BaseModel):
    mo_1: float = Field(None, alias="1", description="Quantity")
    mo_2: MonetaryDenominationCode = Field(None, alias="2", description="Denomination")


class MoneyAndCode(BaseModel):
    moc_1: Money = Field(None, alias="1", description="Monetary Amount")
    moc_2: CodedElement = Field(None, alias="2", description="Charge Code")


class CompositeQuantityWithUnits(BaseModel):
    cq_1: float = Field(None, alias="1", description="Quantity")
    cq_2: CodedElement = Field(None, alias="2", description="Units")


class RepeatInterval(BaseModel):
    ri_1: Repeatpattern = Field(None, alias="1", description="Repeat Pattern")
    ri_2: str = Field(None, alias="2", description="Explicit Time Interval")


class EntityIdentifier(BaseModel):
    ei_1: str = Field(None, alias="1", description="Entity Identifier")
    ei_2: str = Field(None, alias="2", description="Namespace Id")
    ei_3: str = Field(None, alias="3", description="Universal Id")
    ei_4: UniversalIDtype = Field(None, alias="4", description="Universal Id Type")


class EntityIdentifierPair(BaseModel):
    eip_1: EntityIdentifier = Field(
        None, alias="1", description="Placer Assigned Identifier"
    )
    eip_2: EntityIdentifier = Field(
        None, alias="2", description="Filler Assigned Identifier"
    )


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


class SpecimenSource(BaseModel):
    sps_1: CodedWithExceptions = Field(
        None, alias="1", description="Specimen Source Name Or Code"
    )
    sps_2: Additive_Preservative = Field(None, alias="2", description="Additives")
    sps_3: str = Field(None, alias="3", description="Specimen Collection Method")
    sps_4: Bodysite = Field(None, alias="4", description="Body Site")
    sps_5: BodySiteModifier = Field(None, alias="5", description="Site Modifier")
    sps_6: CodedWithExceptions = Field(
        None, alias="6", description="Collection Method Modifier Code"
    )
    sps_7: SpecimenRole = Field(None, alias="7", description="Specimen Role")


class TimeStamp(BaseModel):
    ts_1: str = Field(..., alias="1", description="Time")
    ts_2: Precision = Field(None, alias="2", description="Degree Of Precision")


class OrderSequenceDefinition(BaseModel):
    osd_1: Sequencecondition = Field(
        ..., alias="1", description="Sequence/Results Flag"
    )
    osd_2: str = Field(
        ..., alias="2", description="Placer Order Number: Entity Identifier"
    )
    osd_3: str = Field(None, alias="3", description="Placer Order Number: Namespace Id")
    osd_4: str = Field(
        ..., alias="4", description="Filler Order Number: Entity Identifier"
    )
    osd_5: str = Field(None, alias="5", description="Filler Order Number: Namespace Id")
    osd_6: str = Field(None, alias="6", description="Sequence Condition Value")
    osd_7: float = Field(None, alias="7", description="Maximum Number Of Repeats")
    osd_8: str = Field(..., alias="8", description="Placer Order Number: Universal Id")
    osd_9: UniversalIDtype = Field(
        None, alias="9", description="Placer Order Number: Universal Id Type"
    )
    osd_10: str = Field(
        ..., alias="10", description="Filler Order Number: Universal Id"
    )
    osd_11: UniversalIDtype = Field(
        None, alias="11", description="Filler Order Number: Universal Id Type"
    )


class TimingQuantity(BaseModel):
    tq_1: CompositeQuantityWithUnits = Field(None, alias="1", description="Quantity")
    tq_2: RepeatInterval = Field(None, alias="2", description="Interval")
    tq_3: str = Field(None, alias="3", description="Duration")
    tq_4: TimeStamp = Field(None, alias="4", description="Start Date/Time")
    tq_5: TimeStamp = Field(None, alias="5", description="End Date/Time")
    tq_6: str = Field(None, alias="6", description="Priority")
    tq_7: str = Field(None, alias="7", description="Condition")
    tq_8: str = Field(None, alias="8", description="Text")
    tq_9: TQconjunctionID = Field(None, alias="9", description="Conjunction")
    tq_10: OrderSequenceDefinition = Field(
        None, alias="10", description="Order Sequencing"
    )
    tq_11: CodedElement = Field(None, alias="11", description="Occurrence Duration")
    tq_12: float = Field(None, alias="12", description="Total Occurrences")


class DateAndTimeRange(BaseModel):
    dr_1: TimeStamp = Field(None, alias="1", description="Range Start Date/Time")
    dr_2: TimeStamp = Field(None, alias="2", description="Range End Date/Time")


class HierarchicDesignator(BaseModel):
    hd_1: str = Field(None, alias="1", description="Namespace Id")
    hd_2: str = Field(None, alias="2", description="Universal Id")
    hd_3: str = Field(None, alias="3", description="Universal Id Type")


class CompositeIDNumberAndNameSimplified(BaseModel):
    cnn_1: str = Field(None, alias="1", description="Id Number")
    cnn_2: str = Field(None, alias="2", description="Family Name")
    cnn_3: str = Field(None, alias="3", description="Given Name")
    cnn_4: str = Field(
        None,
        alias="4",
        description="Second And Further Given Names Or Initials Thereof",
    )
    cnn_5: str = Field(None, alias="5", description="Suffix")
    cnn_6: str = Field(None, alias="6", description="Prefix")
    cnn_7: Degreeorlicenseorcertificate = Field(None, alias="7", description="Degree")
    cnn_8: str = Field(None, alias="8", description="Source Table")
    cnn_9: str = Field(
        None, alias="9", description="Assigning Authority - Namespace Id"
    )
    cnn_10: str = Field(
        None, alias="10", description="Assigning Authority- Universal Id"
    )
    cnn_11: UniversalIDtype = Field(
        None, alias="11", description="Assigning Authority - Universal Id Type"
    )


class NameWithDateAndLocation(BaseModel):
    ndl_1: CompositeIDNumberAndNameSimplified = Field(
        None, alias="1", description="Name"
    )
    ndl_2: TimeStamp = Field(None, alias="2", description="Start Date/Time")
    ndl_3: TimeStamp = Field(None, alias="3", description="End Date/Time")
    ndl_4: str = Field(None, alias="4", description="Point Of Care")
    ndl_5: str = Field(None, alias="5", description="Room")
    ndl_6: str = Field(None, alias="6", description="Bed")
    ndl_7: HierarchicDesignator = Field(None, alias="7", description="Facility")
    ndl_8: str = Field(None, alias="8", description="Location Status")
    ndl_9: Personlocationtype = Field(
        None, alias="9", description="Patient Location Type"
    )
    ndl_10: str = Field(None, alias="10", description="Building")
    ndl_11: str = Field(None, alias="11", description="Floor")


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


class ExtendedTelecommunicationNumber(BaseModel):
    xtn_1: str = Field(None, alias="1", description="Telephone Number")
    xtn_2: Telecommunicationusecode = Field(
        None, alias="2", description="Telecommunication Use Code"
    )
    xtn_3: Telecommunicationequipmenttype = Field(
        None, alias="3", description="Telecommunication Equipment Type"
    )
    xtn_4: str = Field(None, alias="4", description="Email Address")
    xtn_5: float = Field(None, alias="5", description="Country Code")
    xtn_6: float = Field(None, alias="6", description="Area/City Code")
    xtn_7: float = Field(None, alias="7", description="Local Number")
    xtn_8: float = Field(None, alias="8", description="Extension")
    xtn_9: str = Field(None, alias="9", description="Any Text")
    xtn_10: str = Field(None, alias="10", description="Extension Prefix")
    xtn_11: str = Field(None, alias="11", description="Speed Dial Code")
    xtn_12: str = Field(None, alias="12", description="Unformatted Telephone Number")


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
