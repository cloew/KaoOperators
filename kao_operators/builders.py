                 
def GetTwoParamOperatorMethod(cls, op, valueToUseFn):
    """ Return the method to be used to run an opertaion """
    def operator(self, other):
        otherValue = valueToUseFn(other) if isinstance(other, cls) else other
        return op(valueToUseFn(self), otherValue)
    return operator