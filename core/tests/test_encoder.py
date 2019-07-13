from unittest import TestCase
from random import Random

from ..utils.encoder import WeirdTextEncoder

SAMPLE_TEXT = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
               "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")


class EncoderTests(TestCase):
    """Test case for Encoder class."""
    def setUp(self):
        self.random = Random(20)
        self.encoder = WeirdTextEncoder(SAMPLE_TEXT)

    def test_encode_word(self):
        """Letters in words are shuffled except first and last letter."""
        word = 'Lorem'
        encoded = self.encoder.encode_word(word)

        self.assertEqual(encoded, 'Leorm')
