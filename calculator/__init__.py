from typing import List
from decimal import Decimal

class Calculation:
    def __init__(self, operation: str, operands: List[Decimal], result: Decimal):
        self.operation = operation
        self.operands = operands
        self.result = result

    def __str__(self) -> str:
        return f"{self.operation.capitalize()}: {self.operands} = {self.result}"

    def get_operands(self) -> List[Decimal]:
        return self.operands

    def get_result(self) -> Decimal:
        return self.result

class Calculator:
    history: List[Calculation] = []

    def __init__(self) -> None:
        pass

    def add(self, a: Decimal, b: Decimal) -> Decimal:
        self._validate_inputs(a, b)
        result = a + b
        self._add_to_history("add", [a, b], result)
        return result

    def subtract(self, a: Decimal, b: Decimal) -> Decimal:
        self._validate_inputs(a, b)
        result = a - b
        self._add_to_history("subtract", [a, b], result)
        return result

    def multiply(self, a: Decimal, b: Decimal) -> Decimal:
        self._validate_inputs(a, b)
        result = a * b
        self._add_to_history("multiply", [a, b], result)
        return result

    def divide(self, a: Decimal, b: Decimal) -> Decimal:
        self._validate_inputs(a, b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self._add_to_history("divide", [a, b], result)
        return result

    def _add_to_history(self, operation: str, operands: List[Decimal], result: Decimal) -> None:
        calc = Calculation(operation, operands, result)
        Calculator.history.append(calc)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls) -> None:
        cls.history.clear()

    @staticmethod
    def _validate_inputs(a: Decimal, b: Decimal) -> None:
        if not isinstance(a, (int, float, Decimal)) or not isinstance(b, (int, float, Decimal)):
            raise ValueError("Operands must be numeric.")

    @classmethod
    def get_last_calculation(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        else:
            raise IndexError("No calculations in history.")

    @classmethod
    def get_calculations_by_type(cls, operation: str) -> List[Calculation]:
        return [calc for calc in cls.history if calc.operation == operation]
