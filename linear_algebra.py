import math

def shape(vector):
    return (len(vector), )

def vector_add(vector1, vector2):
    if len(a) != len(b):
        raise ShapeError
    return [a + b for a, b in zip(vector1, vector2)]

def vector_sub (vector1, vector2):
    if len(a) != len(b):
        raise ShapeError
    return [x - y for x, y in zip(vector1, vector2)]

# def vector_sum(*args):
#     max_len = max([len(x) for x in args])

# def vector_sum (*args):
#     vector = [sum(x) for arg in zip(args)]
#     [for x in args, None]
#     return vector
# def vector_sum(*args):
    # find max length of args
    # pad smaller lists with 0s
    # sum all lists


def vector_multiply(vector, scalar):
    return [x * scalar for x in vector]

def dot(vector1, vector2):
    if len(a) != len(b):
        raise ShapeError
    return sum([a*b for a, b in zip(vector1, vector2)])

# def vector_mean(a_args, *b_args):
#     return [(a + b) / 2 for a, b in zip(a_args, b_args)]

def vector_mean(vector1 ,vector2):
    return [(a + b) / 2 for a, b in zip(vector1, vector2)]

# def are_equal(a, b):
#     [for a,b in zip[a,b]
#     pass

def magnitude(vector):
    return math.sqrt(sum([x**2 for x in vector]))

class ShapeError(Exception):
    pass
