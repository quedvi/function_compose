from .function import Function

# define a range of reusable simple functions
def multiply(y):
    @Function
    def f(x):
        return x * 1.0
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

def scale(k, d):
    @Function
    def f(x):
        return x * k + d
    return f


# define a Transformation of composed simple functions
t = multiply(2) * add(1) * scale(0.5, -1)
