from .function import Function

# define a range of reusable simple functions
@Function
def multiply(x, y):
    return x * y

@Function
def add(x, y):
    return x + y

@Function
def sub(x, y):
    return x - y

# define a Transformation of composed simple functions
t = multiply(2) * add(100) * sub(1)
