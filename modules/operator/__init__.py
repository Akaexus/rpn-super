from modules.variable import Variable
from modules.constant import Constant
from modules.predicate import Predicate
from modules.function import Function


# noinspection SpellCheckingInspection
class Operator:
    symbols = []
    numberOfArguments = 2  # for most cases

    def __init__(self):
        self.arguments = []

    def apply_arguments(self, args):
        self.arguments = args

    def __str__(self):
        if self.numberOfArguments == 2:
            return '{} {} {}'.format(self.arguments[0], self.symbols[0], self.bracketize_argument(self.arguments[1]))
        elif self.numberOfArguments == 1:
            return '{} {}'.format(self.symbols[0], self.bracketize_argument(self.arguments[0]))

    @staticmethod
    def bracketize_argument(arg):
        return ('{}' if type(arg) in [Variable, Constant, Function, Predicate] else '({})').format(arg)

    @classmethod
    def test(cls, expression):
        return expression in cls.symbols
