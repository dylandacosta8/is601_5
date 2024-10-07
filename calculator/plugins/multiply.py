# plugins/multiply_command.py
from calculator import Calculator
from . import Command

class MultiplyCommand(Command):
    def execute(self, a, b):
        calculator = Calculator()
        return calculator.multiply(a, b)

    def help(self):
        return "Usage: multiply <value1> <value2> - Multiplies two numbers."
