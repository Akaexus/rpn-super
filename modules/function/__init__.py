import re


class Function:
    passToConstructor = True

    def __init__(self, function):
        self.numberOfArguments = int(function[2:])  # for most cases
        self.letter = function[0]
        self.arguments = []

    def __str__(self):
        return '{}({})'.format(self.letter, ', '.join(map(str, self.arguments)))

    def apply_arguments(self, args):
        self.arguments = args

    @staticmethod
    def test(expression):
        pattern = re.compile('^\\w/\\d+$')
        if pattern.match(expression):
            if 'f' <= expression[0] <= 'n':
                return True
            else:
                return False
        else:
            return False

