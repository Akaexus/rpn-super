class Variable:
    passToConstructor = True

    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def print(self):
        return self.symbol

    @staticmethod
    def test(expression):
        return len(expression) == 1 and expression.isupper()

