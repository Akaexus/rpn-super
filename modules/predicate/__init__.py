import re


class Predicate:
    passToConstructor = True

    def __init__(self, predicate):
        self.numberOfArguments = int(predicate[2:])  # for most cases
        self.letter = predicate[0]
        self.arguments = []

    def __str__(self):
        return '{}({})'.format(self.letter, ', '.join(map(str, self.arguments)))

    def apply_arguments(self, args):
        self.arguments = args

    @staticmethod
    def test(expression):
        pattern = re.compile('^\\w/\\d+$')
        if pattern.match(expression):
            if 'p' <= expression[0] <= 'z':
                return True
            else:
                return False
        else:
            return False
