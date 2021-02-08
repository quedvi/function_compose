from .function import Function

# define a range of reusable simple functions
def multiply(y):
    @Function
    def f(x):
        return x * y
    return f

def add(y):
    @Function
    def f(x):
        return x + y
    return f

def sub(y):
    @Function
    def f(x):
        return x - y
    return f

# define a Transformation of composed simple functions
t = multiply(2) * add(100) * sub(1)
