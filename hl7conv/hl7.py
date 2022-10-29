from convert import convert_hl7_to_json


class HL7:
    """
    validate: converted JSON will be validated according to current hl7 version.
    """
    def __init__(self, hl7_string: str, version: str | None = None, validate: bool = True):
        self._validate = validate
        self._version = version
        self._hl7_string = self.replace_eof(hl7_string)

    @classmethod
    def from_file(cls, path: str, version: str | None = None, validate: bool = True):
        with open(path, mode='r') as f:
            hl7string = f.read()
            hl7string = HL7.replace_eof(hl7string)
        return cls(hl7string, version, validate)

    @classmethod
    def replace_eof(cls, hl7string) -> str:
        return hl7string.replace('\r\n', '\n').replace('\n\r', '\n').replace('\r', '\n')

    @property
    def hl7_string(self):
        return self._hl7_string

    @property
    def hl7_json(self):
        return convert_hl7_to_json(self._hl7_string, self._version)
