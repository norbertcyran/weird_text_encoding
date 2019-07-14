from unittest import TestCase

from ..utils.decoder import WeirdTextDecoder
from ..utils.exceptions import DecoderInputError


class DecoderTestCase(TestCase):
    """Test case for WeirdTextDecoder class."""

    def test_wrong_input_format(self):
        """Exception is raised when encoded text does not match weird text
        encoding format."""
        wrong_decoder_input = 'Lreom ispum dloor sit aemt'
        with self.assertRaisesRegex(DecoderInputError, 'Invalid data format'):
            WeirdTextDecoder(wrong_decoder_input)
