from apps.calculator.types import ExpressionTokens
from apps.calculator.v1.calculator import SimpleCalculator
from apps.calculator.v1.serializers import CalculateRequestSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CalculateAPIView(APIView):
    def _get_data_from_request(self, request: Request) -> dict:
        serializer = CalculateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return serializer.data

    def post(self, request: Request) -> Response:
        tokens = self._get_data_from_request(request)["tokens"]
        try:
            result = SimpleCalculator.evaluate(tokens)
        except Exception as e:
            raise ValidationError({"tokens": [e]})
        return Response({"result": result})
