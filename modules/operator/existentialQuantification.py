from modules.operator import Operator


class ExistentialQuantification(Operator):
    symbols = ['EXISTS', '∃']

    def __str__(self):
        return '{} {} ({})'.format(self.symbols[0], self.arguments[0], self.arguments[1])

