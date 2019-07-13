from unittest import TestCase, mock
from random import Random

from ..utils.encoder import WeirdTextEncoder

SAMPLE_TEXT = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
               "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")


class EncoderTests(TestCase):
    """Test case for Encoder class."""
    def setUp(self):
        self.random = Random(20)
        self.encoder = WeirdTextEncoder(SAMPLE_TEXT)

    @mock.patch('core.utils.encoder.random.sample')
    def test_encode_word(self, sample_mock):
        """Letters in words are shuffled except first and last letter."""
        sample_mock.side_effect = self.random.sample
        word = 'Lorem'
        encoded = self.encoder.encode_word(word)

        self.assertEqual(encoded, 'Leorm')
