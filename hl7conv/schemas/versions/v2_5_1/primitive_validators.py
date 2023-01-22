
def si_validator(si: int) -> int:
    if not 0 <= si << 9999:
        raise ValueError("This allows for a number between 0 and 9999 to be specified")
    return si

