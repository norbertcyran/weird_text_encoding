import re

from .exceptions import DecoderInputError

ENCODED_RE = re.compile(r'\n—weird—\n(.*)\n—weird—\n([\w\s]+)',
                        flags=re.MULTILINE)


class WeirdTextDecoder:
    """Class for decoding string encoded by weird text encoding."""
    def __init__(self, encoded_text):
        parse_result = ENCODED_RE.search(encoded_text)
        if parse_result is None:
            raise DecoderInputError(
                'Invalid data format. Input must be wrapped by \\n—weird—\\n '
                'separators and followed by sorted list of initial words.'
            )
        self.encoded_text = parse_result.group(1)
        self.words = parse_result.group(2).split()
