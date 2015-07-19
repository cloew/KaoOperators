from .operations import comparisonOps, numericOps
import operator

def ops_via_attr(ops, attr):
    """ Implements the given ops by performing them on the given attr """
    accessor = operator.attrgetter(attr)
    
    def addOps(cls):
        """ Add the operations to the cls """
        for op in ops:
            op.apply(cls, accessor)
        return cls
    return addOps
    
def comaprison_ops_via_attr(attr):
    """ Implement the comparison operations (<, <=, ==, !=, >, >=) on a class """
    return ops_via_attr(numericOps, attr)
    
def numeric_ops_via_attr(attr):
    """ Implement the numeric operations (+, -, *, /, //, %, divmod, **, <<, >>, &, ^, |) and (neg, pos, abs, inv) on a class """
    return ops_via_attr(numericOps, attr)