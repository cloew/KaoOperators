from .operator import Operator
from .reverse_operator import ReverseOperator
from .builders import GetTwoParamOperatorMethod

import operator

add = Operator("__add__", opFn=operator.add, builderFn=GetTwoParamOperatorMethod)
radd = ReverseOperator("__radd__", add)
add.requireReverseOperator(radd)

numericOps = [add]