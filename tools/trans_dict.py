from .function import Function

# define a range of reusable simple functions
@Function
def add_key(x, key, value_function):
    x[key] = value_function(x)
    return x
    
@Function
def map_value(x, key, value_function):
    x[key] = value_function(x[key])
    return x

@Function
def rename_keys(x, trans_dict):
    for key in trans_dict:
        if key in x:
            x[trans_dict[key]] = x.pop(key)
    return x
 
@Function
def delete_keys(x, key_array):
    return dict([(key, val) for key, val in x.items() if key not in key_array])



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
