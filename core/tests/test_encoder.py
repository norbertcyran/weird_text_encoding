from unittest import TestCase, mock
from random import Random

from ..utils.encoder import WeirdTextEncoder

SAMPLE_TEXT = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
               "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

ENCODED_TEXT = ("Leorm iupsm doolr sit aemt, cnutseceotr acnipsidig eilt, "
                "sed do euoismd teompr iidicndnut ut lboare et doolre manga alquia.")


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

    @mock.patch('core.utils.encoder.random.sample')
    def test_encode_text(self, sample_mock):
        """Full text is encoded, with punctuation and whitespaces unchanged."""
        sample_mock.side_effect = self.random.sample

        encoded_text = self.encoder.encode_text()

        self.assertEqual(encoded_text, ENCODED_TEXT)
