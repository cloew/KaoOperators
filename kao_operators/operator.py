
class Operator:
    """ Represents an operator in Python """
    
    def __init__(self, method, opFn=None, builderFn=None):
        """ Build the operator """
        self.method = method
        self.opFn = opFn
        self.builderFn = builderFn
        
    def apply(self, cls, valueToUseFn):
        """ Apply the Operator to the given class """
        setattr(cls, self.method, self.builderFn(cls, self, valueToUseFn))
        
    def __call__(self, *args, **kwargs):
        """ Call this operator """
        return self.opFn(*args, **kwargs)