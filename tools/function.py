from .function_inner import FunctionInner
class Function:
    
    def __init__(self, func):
        self.func = func
        
    def __call__(self, *args, **kwargs):
        
        @FunctionInner
        def inner(x):
            return self.func(x, *args, **kwargs)
            
        return inner