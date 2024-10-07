# plugins/subtract_command.py
from calculator import Calculator
from . import Command

class SubtractCommand(Command):
    def execute(self, a, b):
        calculator = Calculator()
        return calculator.subtract(a, b)

    def help(self):
        return "Usage: subtract <value1> <value2> - Subtracts second number from the first."
