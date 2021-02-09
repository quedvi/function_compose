from .function import Function

# define a range of reusable simple functions
@Function
def multiply(x, y):
    return x * 1.0
    
@Function
def add(x, y):
    return x + y

@Function
def sub(x, y):
    return x - y

@Function
def scale(x, k, d):
    return x * k + d


# define a Transformation of composed simple functions
t = multiply(2) * add(1) * scale(0.5, -1)
