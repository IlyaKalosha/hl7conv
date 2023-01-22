from enum import Enum


class ValueType(str, Enum):
    """
    0125 - Value type

    AD  Address
    CE	Coded Entry
    CF	Coded Element With Formatted Values
    CK	Composite ID With Check Digit
    CN	Composite ID And Name
    CP	Composite Price
    CX	Extended Composite ID With Check Digit
    DT	Date
    ED	Encapsulated Data
    FT	Formatted Text (Display)
    MO	Money
    NM	Numeric
    PN	Person Name
    RP	Reference Pointer
    SN	Structured Numeric
    ST	String Data.
    TM	Time
    TN	Telephone Number
    TS	Time Stamp (Date & Time)
    TX	Text Data (Display)
    XAD	Extended Address
    XCN	Extended Composite Name And Number For Persons
    XON	Extended Composite Name And Number For Organizations
    XPN	Extended Person Name
    XTN	Extended Telecommunications Number
    """

    AD = "AD"
    CE = "CE"
    CF = "CF"
    CK = "CK"
    CN = "CN"
    CP = "CP"
    CX = "CX"
    DT = "DT"
    ED = "ED"
    FT = "FT"
    MO = "MO"
    NM = "NM"
    PN = "PN"
    RP = "RP"
    SN = "SN"
    ST = "ST"
    TM = "TM"
    TN = "TN"
    TS = "TS"
    TX = "TX"
    XAD = "XAD"
    XCN = "XCN"
    XON = "XON"
    XPN = "XPN"
    XTN = "XTN"
