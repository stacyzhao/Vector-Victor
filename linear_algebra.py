# vector shape in shape()
# vector addition in vector_add()
# vector subtraction in vector_sub()
# vector multiplication by a scalar in vector_multiply()
# mean of multiple vectors in vector_mean()
# dot product in dot()
# magnitude in magnitude()
import math

class ShapeError(Exception):
    pass

def shape(vector):
    return (len(vector), )

def vector_add(a, b):
    if len(a) != len(b):
        raise ShapeError
    return [a + b for a, b in zip(a, b)]

def vector_sub (a, b):
    if len(a) != len(b):
        raise ShapeError
    return [x - y for x, y in zip(a, b)]

# def vector_sum (*args):
#     max_len = max([len(x) for x in args])
#     vector = [sum(x) for arg in zip(args)]
#     return vector

def vector_multiply(vector, scalar):
    return [x * scalar for x in vector]

def dot(a, b):
    if len(a) != len(b):
        raise ShapeError
    return sum([a*b for (a, b) in zip(a, b)])

def vector_mean(vector1 ,vector2):
    return [(a + b) / 2 for a, b in zip(vector1, vector2)]

def are_equal():
    pass

def magnitude(vector):
    return math.sqrt(sum([x**2 for x in vector]))
# def vector_sum(*args):
    # find max length of args
    # pad smaller lists with 0s
    # sum all lists
