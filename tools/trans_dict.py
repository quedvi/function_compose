from .function import Function

# define a range of reusable simple functions
def add_key(key, value_function):
    @Function
    def f(x):
        x[key] = value_function(x)
        return x
    return f

def map_value(key, value_function):
    @Function
    def f(x):
        x[key] = value_function(x[key])
        return x
    return f

def rename_keys(trans_dict):
    @Function
    def f(x):
        for key in trans_dict:
            if key in x:
                x[trans_dict[key]] = x[key]
                del x[key]
        return x
    return f

def delete_keys(key_array):
    @Function
    def f(x):
        for key in key_array:
            if key in x:
                del x[key]
        return x
    return f



# methods to apply to values of the dictionary
def normalize(a, b):
    return a/(a+b)

# Transformation of composed elementary functions
t = (
    add_key('a', lambda z : 2) 
    * add_key('b', lambda z : z['a']) 
    * map_value('b', lambda z : z * 4)
    * add_key('c', lambda z : normalize(z['a'], z['b']))
    * add_key('d', lambda z : normalize(z['b'], z['a']))
    * delete_keys(['d', 'e'])
    * rename_keys({'c': 'e'})
)
