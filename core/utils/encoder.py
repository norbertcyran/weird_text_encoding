import random
import re

WORD_RE = re.compile(r'(\w+)')


def weird_text_encode(text):
    """Shortcut function for weird text encoding."""
    encoder = WeirdTextEncoder(text)
    return encoder.encode()


class WeirdTextEncoder:
    """
    Class for text encoding.

    Every word in text gets shuffled except its first and last letter.
    Does not affect punctuation and whitespaces. Encoded text is wrapped
    in \n—weird—\n separator. In the last line a list of sorted original
    word is appended.
    """
    separator = '\n—weird—\n'

    def __init__(self, text: str):
        self.text = text
        self.words = WORD_RE.findall(self.text)

    def encode(self):
        """Build encoder output."""
        encoded_text = self.encode_text()
        return self.wrap_output(encoded_text)

    def encode_text(self) -> str:
        """Build encoded string from text."""
        encoded_text = self.text
        for word in self.words:
            encoded_text = re.sub(word, self.encode_word(word), encoded_text)
        return encoded_text

    @staticmethod
    def encode_word(word: str) -> str:
        """Encode single word. Shuffle all letters except last and first."""
        letters = list(word)
        inner_letters = letters[1:-1]
        if len(set(inner_letters)) < 2:
            return word
        shuffled_inner = inner_letters
        while inner_letters == shuffled_inner:
            shuffled_inner = random.sample(inner_letters, len(inner_letters))
        letters[1:-1] = shuffled_inner
        return ''.join(letters)

    def wrap_output(self, output: str) -> str:
        """Wrap encoded output in separator and sorted list of words."""
        sorted_words = ' '.join(sorted(self.words, key=str.lower))
        return f'{self.separator}{output}{self.separator}{sorted_words}'
