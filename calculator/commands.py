from abc import ABC, abstractmethod

# Command Interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass

# Calculator Command Implementations
class AddCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self) -> float:
        return self.calculator.add(self.a, self.b)

class SubtractCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self) -> float:
        return self.calculator.subtract(self.a, self.b)

class MultiplyCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self) -> float:
        return self.calculator.multiply(self.a, self.b)

class DivideCommand(Command):
    def __init__(self, calculator, a, b):
        self.calculator = calculator
        self.a = a
        self.b = b

    def execute(self) -> float:
        return self.calculator.divide(self.a, self.b)
