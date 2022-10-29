from util import split_segments


def split_hl7_parent_field_to_json(parent_key: int, parent_value: str) -> dict:
    list_of_sub_fields: list = parent_value.split('^')
    children_json = dict(enumerate(list_of_sub_fields, start=1))
    for key in children_json.copy().keys():
        children_json[f'{parent_key}.{key}'] = children_json.pop(key)
    return children_json


def split_hl7_seg_to_json(seg: str) -> dict:
    list_of_fields = seg.split('|')
    parents_json = dict()
    for key, parent_value in enumerate(list_of_fields):
        if not key:
            key = 'segment_name'
        if '^' in parent_value and '^~\\&' not in parent_value:
            children_json = split_hl7_parent_field_to_json(key, parent_value)
            parents_json.update(children_json)
        else:
            parents_json[str(key)] = parent_value
    return parents_json


def convert_hl7_to_json(hl7_string: str, version: str | None = None):
    message_json = list()
    for seg in split_segments(hl7_string):
        seg_json = split_hl7_seg_to_json(seg)
        message_json.append(seg_json)

    return message_json
