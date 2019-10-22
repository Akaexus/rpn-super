from modules.operator import Operator


class UniversalQuantification(Operator):
    # noinspection SpellCheckingInspection
    symbols = ['FORALL', '∀']

    def __str__(self):
        return '{} {} ({})'.format(self.symbols[0], self.arguments[0], self.arguments[1])

