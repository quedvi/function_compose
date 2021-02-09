from .composition import Composition

class FunctionInner:
    def __init__(self, function):
        self.function = function
    
    def  __call__(self, value):
        return self.function(value)

    def __mul__(self, other):
        return Composition(self, other)