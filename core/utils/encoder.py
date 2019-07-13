import random
import re

WORD_RE = re.compile(r'(\w+)')


class WeirdTextEncoder:
    """
    Class for text encoding.

    Every word in text gets shuffled except its first and last letter.
    Does not affect punctuation and whitespaces. Encoded text is wrapped
    in \n--weird--\n clause. In the last line a list of sorted original
    word is appended.
    """

    def __init__(self, text: str):
        self.text = text
        self.words = WORD_RE.findall(self.text)

    def encode(self):
        """Build encoder output."""

    def encode_text(self) -> str:
        """Build encoded string from text."""
        encoded_text = self.text
        for word in self.words:
            encoded_text = re.sub(word, self.encode_word(word), encoded_text)
        return encoded_text

    @staticmethod
    def encode_word(word: str) -> str:
        """Encode single word. Shuffle all letters except last and first."""
        if len(word) <= 3:
            return word
        letters = list(word)
        inner_letters = letters[1:-1]
        shuffled_inner = inner_letters
        while inner_letters == shuffled_inner:
            shuffled_inner = random.sample(inner_letters, len(inner_letters))
        letters[1:-1] = shuffled_inner
        return ''.join(letters)
