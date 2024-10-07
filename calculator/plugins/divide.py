# plugins/divide_command.py
from calculator import Calculator
from . import Command

class DivideCommand(Command):
    def execute(self, a, b):
        calculator = Calculator()
        return calculator.divide(a, b)

    def help(self):
        return "Usage: divide <value1> <value2> - Divides the first number by the second."
