from modules.operator.negation import Negation
from modules.operator.conjunction import Conjunction
from modules.operator.disjunction import Disjunction
from modules.operator.equivalence import Equivalence
from modules.operator.implication import Implication
from modules.operator.universalQuantification import UniversalQuantification
from modules.operator.exclusiveDisjunction import ExclusiveDisjunction
from modules.operator.existentialQuantification import ExistentialQuantification

operators = [
    Negation,
    Conjunction,
    Disjunction,
    Equivalence,
    Implication,
    UniversalQuantification,
    ExclusiveDisjunction,
    ExistentialQuantification
]
