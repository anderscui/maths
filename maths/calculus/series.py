# coding=utf-8
import math
from typing import Callable

from pymysql.converters import escape_item


def partial_sums(f_term: Callable, n, start=1, n_digits=6):
    terms = [f_term(i) for i in range(start, start+n)]
    sums = [round(terms[0], n_digits)]
    for i in range(1, len(terms)):
        cur_sum = sums[-1] + terms[i]
        sums.append(round(cur_sum, n_digits))
    return sums


if __name__ == '__main__':
    import math

    ft1 = lambda n: n
    print(partial_sums(ft1, 5))

    ft2 = lambda n: 1/(n**3)
    print(partial_sums(ft2, 8))

    ft3 = lambda n: math.sin(n)
    print(partial_sums(ft3, 8))

    ft4 = lambda n: 1/(n**4+n**2)
    print(partial_sums(ft4, 8))

    f_i = lambda x: 1/(10 * (2*x + 1)**5)
    f_error = lambda n: 1/2 * (f_i(n) - f_i(n+1))
    # for i in range(1, 10):
    #     print(i,  f_error(i))
    f5 = lambda x: 1/(2*x+1)**6
    psum = f5(1) + f5(2)
    estimate = psum + (f_i(2) + f_i(3)) / 2
    print(estimate)

    ft6 = lambda n: math.pow(-1, n) / math.factorial(2*n)
    print(partial_sums(ft6, 5))

    ft7 = lambda n: (math.pow(-1, n) * n)/math.pow(math.e, 2*n)
    print(partial_sums(ft7, 6))

    ft8 = lambda n: 1/(2+5**n)
    print(partial_sums(ft8, 8))

