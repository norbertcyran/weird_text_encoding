from rest_framework.exceptions import ParseError
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .utils.exceptions import DecoderInputError
from .utils.decoder import weird_text_decode
from .utils.encoder import weird_text_encode
from .serializers import EncodeSerializer, DecodeSerializer


class EncodeView(GenericAPIView):
    """API endpoint for weird text encoding."""
    serializer_class = EncodeSerializer

    def post(self, request, *args, **kwargs):
        """Encodes given data in weird text encoding format. Accepts JSON
        with key 'text'."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data['text']
        encoded_text = weird_text_encode(text)
        return Response({
            'encoded_text': encoded_text
        }, status=200)


class DecodeView(GenericAPIView):
    """API endpoint for weird text decoding."""
    serializer_class = DecodeSerializer

    def post(self, request, *args, **kwargs):
        """Decodes data encoded with weird encoding. Accepts JSON with key
        'encoded_text'."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        encoded_text = serializer.validated_data['encoded_text']

        try:
            decoded_text = weird_text_decode(encoded_text)
        except DecoderInputError as error:
            raise ParseError(detail=error) from error

        return Response({
            'decoded_text': decoded_text
        }, status=200)
