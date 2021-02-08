from .function import Function

# define a range of reusable simple functions
@Function
def twice(x):
    return 2*x

@Function
def square(x):
    return x*x

@Function
def decrement(x):
    return x-1

# define a Transformation of composed simple functions
t = (
    twice 
    * square
    * decrement
)
