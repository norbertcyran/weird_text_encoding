import random
import re


class WeirdTextEncoder:
    """
    Class for text encoding.

    Every word in text gets shuffled except its first and last letter.
    Does not affect punctuation and whitespaces. Encoded text is wrapped
    in \n--weird--\n clause. In the last line a list of sorted original
    word is appended.
    """
    word_re = r'(\w+)'

    def __init__(self, text):
        self.words = re.findall(self.word_re, text)

    @staticmethod
    def encode_word(word):
        """Encode single word. Shuffle all letters except last and first."""
        letters = list(word)
        inner_letters = letters[1:-1]
        shuffled_inner = inner_letters
        while inner_letters == shuffled_inner:
            shuffled_inner = random.sample(inner_letters, len(inner_letters))
        letters[1:-1] = shuffled_inner
        return ''.join(letters)
