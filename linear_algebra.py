# vector shape in shape()
# vector addition in vector_add()
# vector subtraction in vector_sub()
# vector multiplication by a scalar in vector_multiply()
# mean of multiple vectors in vector_mean()
# dot product in dot()
# magnitude in magnitude()
class ShapeError(Exception):
    pass

def shape(vector):
    return (len(vector), )

def vector_add(a, b):
    vector = [a + b for a, b in zip(a, b)]
    return vector

def vector_add_is_commutative(a, b):
    pass

def vector_add_checks_shapes():
    pass


def vector_sub (a, b):
    vector = [x - y for x, y in zip(a, b)]
    return vector

def vector_sum (a, b, c, d, e):
    vector = [a + b + c + d + e for a, b, c, d, e in zip(a, b, c, d, e)]
    return vector

    # vector = [sum(args) for x in zip(args)]
