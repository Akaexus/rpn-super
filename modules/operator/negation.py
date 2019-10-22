from modules.operator import Operator


class Negation(Operator):
    symbols = ['~', 'NOT', '¬']
    numberOfArguments = 1
