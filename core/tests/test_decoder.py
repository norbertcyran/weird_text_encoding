from unittest import TestCase

from ..utils.decoder import WeirdTextDecoder
from ..utils.exceptions import DecoderInputError

ENCODED_TEXT = ('\n—weird—\n'
                'Lroem iupsm doolr sit aemt, ceecottnusr acisnipdig eilt, '
                'sed do emsouid toepmr inudciindt ut lrboae et doolre manga aquila.'
                '\n—weird—\n'
                'adipiscing aliqua amet consectetur do dolor dolore eiusmod elit'
                ' et incididunt ipsum labore Lorem magna sed sit tempor ut')

DECODED_TEXT = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
                "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")


class DecoderTestCase(TestCase):
    """Test case for WeirdTextDecoder class."""

    def setUp(self):
        self.decoder = WeirdTextDecoder(ENCODED_TEXT)

    def test_wrong_input_format(self):
        """Exception is raised when encoded text does not match weird text
        encoding format."""
        wrong_decoder_input = 'Lreom ispum dloor sit aemt'
        with self.assertRaisesRegex(DecoderInputError, 'Invalid data format'):
            WeirdTextDecoder(wrong_decoder_input)

    def test_decode_word(self):
        """Word is correctly decoded to its initial form."""
        word = 'Lroem'
        decoded_word = self.decoder.decode_word('Lroem')

        self.assertEqual(decoded_word, 'Lorem')