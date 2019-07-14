from rest_framework import serializers


class EncodeSerializer(serializers.Serializer):
    """Serializer for text encode input."""
    text = serializers.CharField()

    def validate_text(self, value):
        return value.replace('\\n', '\n')


class DecodeSerializer(serializers.Serializer):
    """Serializer for text decode input."""
    encoded_text = serializers.CharField()

    def validate_encoded_text(self, value):
        return value.replace('\\n', '\n')
