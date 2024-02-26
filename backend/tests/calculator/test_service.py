import pytest
from apps.calculator.v1.calculator import SimpleCalculator


@pytest.mark.parametrize(
    "tokens", ["2 2", "2 + +", "3 3 -", "3 + 3 / 2 * 8 - 1 -", "+ 3 + 3"]
)
def test_evaluate_invalid_equation(tokens):
    with pytest.raises(ValueError) as err:
        SimpleCalculator.evaluate(tokens)
    assert str(err.value) == "Expression is invalid"


@pytest.mark.parametrize(
    "expression",
    [
        "2 + 2",
        "2 / 3.1 + 3 * 5.5",
        "5 - 2.3 / -3 + 1.8888 - 3 * 5",
    ],
)
def test_evaluate_successfully(expression):
    correct_tokens = [
        float(i) if i.lstrip("-").replace(".", "").isdigit() else i
        for i in expression.split()
    ]
    assert eval(expression) == SimpleCalculator.evaluate(correct_tokens)
