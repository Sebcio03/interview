import abc
from numbers import Number
from typing import Generator, Self

from apps.calculator.types import ExpressionToken, ExpressionTokens


class BaseCalculator(abc.ABC):
    @abc.abstractmethod
    def _is_expression_valid(tokens: list[str | ExpressionToken]) -> bool:
        ...

    @abc.abstractmethod
    def _evaluate_reverse_polish_notation(
        tokens: list[str | ExpressionToken],
    ) -> Number:
        ...

    @abc.abstractmethod
    def _tokens_to_reverse_polish_notation(
        tokens: list[str | ExpressionToken],
    ) -> Generator[ExpressionToken, None, None]:
        ...

    @classmethod
    def evaluate(cls: Self, tokens: list[str | ExpressionToken]) -> Number:
        if not cls._is_expression_valid(tokens):
            raise ValueError("Expression is invalid")
        rpn = cls._tokens_to_reverse_polish_notation(tokens)
        return cls._evaluate_reverse_polish_notation(rpn)


class SimpleCalculator(BaseCalculator):
    OPERATOR_PRECEDENCE = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
    }

    def _is_expression_valid(tokens: ExpressionTokens) -> bool:
        if len(tokens) < 3 or isinstance(tokens[0], str):
            return False

        for i in range(2, len(tokens)):
            if isinstance(tokens[i - 1], str) != isinstance(tokens[i], Number):
                return False
        return True

    def _evaluate_reverse_polish_notation(
        tokens: Generator[ExpressionToken, None, None]
    ) -> Number:
        s = []
        for t in tokens:
            if isinstance(t, str):
                a, b = s[-2], s[-1]
                s = s[0:-2]
            match t:
                case "+":
                    s.append(a + b)
                case "/":
                    s.append(a / b)
                case "*":
                    s.append(a * b)
                case "-":
                    s.append(a - b)
                case _:
                    s.append(t)
        return s[0]

    def _tokens_to_reverse_polish_notation(
        tokens: ExpressionTokens,
    ) -> Generator[ExpressionToken, None, None]:
        stack = []
        for t in tokens:
            if isinstance(t, Number):
                yield t
            else:
                while (
                    stack
                    and SimpleCalculator.OPERATOR_PRECEDENCE[t]
                    <= SimpleCalculator.OPERATOR_PRECEDENCE[stack[-1]]
                ):
                    yield stack.pop()
                stack.append(t)

        for i in range(len(stack) - 1, -1, -1):
            yield stack[i]
