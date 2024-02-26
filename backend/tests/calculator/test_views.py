from decimal import Decimal
from random import choice, randrange

import pytest
from rest_framework import status

CALCULATE_URL = "/api/calculator/v1/calculate/"


@pytest.mark.parametrize(
    "tokens,error",
    [
        [
            [-3, "+", "3.3330000000000001847411112976260483264923095703125", ";"],
            "Tokens should be an array containing numbers with operands ['+', '-', '/', '*']",
        ],
        [
            [float(1), "ELOELO", Decimal(1.99999)],
            "Tokens should be an array containing numbers with operands ['+', '-', '/', '*']",
        ],
        [
            [1, "+", "1"],
            "Tokens should be an array containing numbers with operands ['+', '-', '/', '*']",
        ],
    ],
)
def test_raise_invalid_request_body(api, tokens, error):
    request_body = {"tokens": tokens}

    response = api.post(CALCULATE_URL, request_body)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert error == response.json()["tokens"][0]


@pytest.mark.parametrize(
    "tokens,error",
    [
        [[float(3), "+", Decimal(1.99999), 1], "Expression is invalid"],
        [["+", 3, Decimal(1.99999)], "Expression is invalid"],
    ],
)
def test_raise_invalid_expression(api, tokens, error):
    request_body = {"tokens": tokens}
    response_body = {"tokens": [error]}

    response = api.post(CALCULATE_URL, request_body)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == response_body


def test_calculate_successfully(api):
    expressions = []

    # Create valid mathematical expressions to test
    for _ in range(100):
        eq = []
        for i in range(9):
            if i % 2:
                eq.append(choice(["+", "-", "*", "/"]))
            else:
                eq.append(float(randrange(1, 1000) / 1000))
        expressions.append(eq)

    for e in expressions:
        request_body = {"tokens": e}
        response_body = {"result": eval(" ".join([str(c) for c in e]))}

        response = api.post(CALCULATE_URL, request_body)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == response_body
