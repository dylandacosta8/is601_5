# plugins/add_command.py
from calculator import Calculator
from . import Command

class AddCommand(Command):
    def execute(self, a, b):
        calculator = Calculator()
        return calculator.add(a, b)

    def help(self):
        return "Usage: add <value1> <value2> - Adds two numbers."
