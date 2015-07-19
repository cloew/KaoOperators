
class Operator:
    """ Represents an operator in Python """
    
    def __init__(self, method, opFn=None, builderFn=None):
        """ Build the operator """
        self.method = method
        self.opFn = opFn
        self.builderFn = builderFn
        self.reverseOperator = None
        
    def apply(self, cls, valueToUseFn):
        """ Apply the Operator to the given class """
        print(self.builderFn)
        setattr(cls, self.method, self.builderFn(cls, self, valueToUseFn))
        if self.reverseOperator is not None:
            self.reverseOperator.apply(cls, valueToUseFn)
        
    def requireReverseOperator(self, reverseOp):
        """ Require this operator to provide a reverse operation as well """
        self.reverseOperator = reverseOp
        
    def __call__(self, *args, **kwargs):
        """ Call this operator """
        return self.opFn(*args, **kwargs)