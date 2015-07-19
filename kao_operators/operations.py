from .operator import Operator
from .builders import GetTwoParamOperatorMethod

import operator

add = Operator("__add__", opFn=operator.add, builderFn=GetTwoParamOperatorMethod)

numericOps = [add]