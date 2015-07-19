from .operations import numericOps
import operator

def numeric_ops_via_attr(attr):
    """ Implement the numeric operations (+, -, *, /, //, %, divmod, **, <<, >>, &, ^, |) on a class """
    ops = numericOps
    accessor = operator.attrgetter(attr)
    
    def addOps(cls):
        """ Add the operations to the cls """
        for op in ops:
            op.apply(cls, accessor)
        return cls
    return addOps