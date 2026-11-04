"""Explicit SemRel string payload contract over EAL's verbatim string literals."""
import json

ENCODING = 'json-string-content-v1'


def decode_arguments(arguments):
    """Decode only parameters that explicitly declare the SemRel encoding."""
    if arguments.get('string_encoding') != ENCODING:
        return dict(arguments)
    return {key: json.loads('"' + value + '"') if isinstance(value, str) else value
            for key, value in arguments.items()}
