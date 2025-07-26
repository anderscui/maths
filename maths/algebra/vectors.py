# coding=utf-8
import math


def vector_of_points(p1, p2):
    return tuple(e2-e1 for e1, e2 in zip(p1, p2))


def magnitude(v):
    return math.sqrt(sum([elem**2 for elem in v]))


def dot_product(v1, v2):
    prod = 0
    for e1, e2 in zip(v1, v2):
        prod += e1 * e2
    return prod


def cross_product(v1, v2):
    a1, a2, a3 = v1
    b1, b2, b3 = v2
    return (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)


def area_of_vector_parallelogram(v1, v2):
    m1 = magnitude(v1)
    m2 = magnitude(v2)
    dp = dot_product(v1, v2)
    cos = dp/(m1*m2)
    sin = math.sin(math.acos(cos))
    return m1 * m2 * sin


if __name__ == '__main__':
    print(magnitude((5, 12)))

    u = (6, -1)
    v = (2, 3)
    print(area_of_vector_parallelogram(u, v))

    u = (2, 3, 0)
    v = (1, 0, 5)
    print(cross_product(u, v))  # (15, -10, -3)

    p = (3, 1, 1)
    q = (5, 2, 4)
    r = (8, 5, 3)
    print(vector_of_points(p, q))
    print(vector_of_points(p, r))
    # 三角形面积
    print(area_of_vector_parallelogram(vector_of_points(p, q), vector_of_points(p, r)) / 2)

    # velocity
    s1 = (1.8, -3.8, -0.7)
    
