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

    def decode(self):
        """Decode weird encoded text into its initial form."""
        decoded_text = self.encoded_text
        words = re.findall(r'(\w+)', self.encoded_text)
        for word in words:
            decoded_text = re.sub(word, self.decode_word(word), decoded_text)
        return decoded_text

    def decode_word(self, word):
        """Decode single word to its initial form."""
        if len(word) <= 3:
            return word
        for initial_word in self.words:
            if self.is_encoded_by(initial_word, word):
                return initial_word
        return word

    @staticmethod
    def is_encoded_by(word, initial_word):
        """Check if given initial word is encoded by word."""
        if (len(initial_word) != len(word) or initial_word[0] != word[0]
                and initial_word[-1] != word[-1]):
            return False

        for letter in word[1:-1]:
            if letter not in initial_word[1:-1]:
                return False
        return True
