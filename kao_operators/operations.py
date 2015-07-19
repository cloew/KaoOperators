from .operator import Operator
from .reverse_operator import ReverseOperator
from .builders import GetOneParamOperatorMethod, GetTwoParamOperatorMethod

import operator

def BuildOperatorWithReverse(method1, method2, opFn=None):
    """ Build an Operation and its Reverse counterpart """
    op = Operator(method1, opFn=opFn, builderFn=GetTwoParamOperatorMethod)
    reverseOp = ReverseOperator(method2, op)
    op.requireReverseOperator(reverseOp)
    return op, reverseOp
    

# Numeric Ops
add, radd = BuildOperatorWithReverse("__add__", "__radd__", opFn=operator.add)
sub, rsub = BuildOperatorWithReverse("__sub__", "__rsub__", opFn=operator.sub)
mul, rmul = BuildOperatorWithReverse("__mul__", "__rmul__", opFn=operator.mul)
truediv, rtruediv = BuildOperatorWithReverse("__truediv__", "__rtruediv__", opFn=operator.truediv)
floordiv, rfloordiv = BuildOperatorWithReverse("__floordiv__", "__rfloordiv__", opFn=operator.floordiv)
mod, rmod = BuildOperatorWithReverse("__mod__", "__rmod__", opFn=operator.mod)
divmod, rdivmod = BuildOperatorWithReverse("__divmod__", "__rdivmod__", opFn=divmod)
pow, rpow = BuildOperatorWithReverse("__pow__", "__rpow__", opFn=operator.pow)
lshift, rlshift = BuildOperatorWithReverse("__lshift__", "__rlshift__", opFn=operator.lshift)
rshift, rrshift = BuildOperatorWithReverse("__rshift__", "__rrshift__", opFn=operator.rshift)
and_, rand = BuildOperatorWithReverse("__and__", "__rand__", opFn=operator.and_)
xor, rxor = BuildOperatorWithReverse("__xor__", "__rxor__", opFn=operator.xor)
or_, ror = BuildOperatorWithReverse("__or__", "__ror__", opFn=operator.or_)

neg = Operator("__neg__", opFn=operator.neg, builderFn=GetOneParamOperatorMethod)
pos = Operator("__pos__", opFn=operator.pos, builderFn=GetOneParamOperatorMethod)
abs = Operator("__abs__", opFn=operator.abs, builderFn=GetOneParamOperatorMethod)
invert = Operator("__invert__", opFn=operator.invert, builderFn=GetOneParamOperatorMethod)

numericOps = [add, sub, mul, truediv, floordiv, mod, divmod, pow, lshift, rshift, and_, xor, or_, neg, pos, abs, invert]