from typing import Iterable, Literal, TypeVar

from apps.calculator.enums import CORE_OPERANDS

ExpressionToken = TypeVar("ExpressionToken", int, float, Literal[CORE_OPERANDS])
ExpressionTokens = Iterable[ExpressionToken]
