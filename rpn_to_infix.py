from modules.operator.operators import *
from modules.constant import Constant
from modules.variable import Variable
from modules.function import Function
from modules.predicate import Predicate

stack = []


def take_from_stack(n):
    args = []
    global stack
    for i in range(n):
        args.append(stack.pop())
    return list(reversed(args))


def detect_entity(raw_entity):
    entities = [Constant, Variable, Function, Predicate] + operators
    entities = list(filter(lambda ec: ec.test(raw_entity), entities))
    if len(entities) == 1:
        entity_class = entities[0]
        e = entity_class(raw_entity) if hasattr(entity_class, 'passToConstructor') else entity_class()
        if hasattr(entity_class, 'apply_arguments'):
            e.apply_arguments(take_from_stack(e.numberOfArguments))
        return e
    else:
        return None


while True:
    try:
        stack = []
        rpn = input().split()
        for entity in rpn:
            entity = detect_entity(entity)
            if entity:
                stack.append(entity)
        print(stack[0])
    except EOFError:
        break

