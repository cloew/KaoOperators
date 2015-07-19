
class ReverseOperator:
    """ Represents an operator that takes arguments in the reverse order """
    
    def __init__(self, method, op):
        """ Initialize with the op to reverse """
        self.method = method
        self.op = op
        
    def apply(self, cls, valueToUseFn):
        """ Apply the Operator to the given class """
        setattr(cls, self.method, self.builderFn(cls, self, valueToUseFn))
        
    def __call__(self, *args, **kwargs):
        """ Call this operator """
        return self.opFn(args[1], args[0], *args[2:], **kwargs)
        
    @property
    def builderFn(self):
        """ Return the base operations op function """
        return self.op.builderFn
        
    @property
    def opFn(self):
        """ Return the base operations op function """
        return self.op.opFn
        
    def __repr__(self):
        return self.method