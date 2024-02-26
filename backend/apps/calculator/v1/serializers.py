from numbers import Number

from apps.calculator.enums import CORE_OPERANDS
from apps.calculator.types import ExpressionTokens
from rest_framework import serializers
from rest_framework.validators import ValidationError


class CalculateRequestSerializer(serializers.Serializer):
    tokens = serializers.ListField()

    def validate_tokens(self, tokens: list[any]) -> ExpressionTokens:
        for t in tokens:
            if not (isinstance(t, Number) or t in CORE_OPERANDS):
                raise ValidationError(
                    detail=f"Tokens should be an array containing numbers with operands {CORE_OPERANDS}"
                )
        return tokens
