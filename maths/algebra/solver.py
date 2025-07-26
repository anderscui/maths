# coding=utf-8
from math import isclose


def f(x):
    return x ** 3 - 2 * x - 5


def f_d(x):
    return 3 * x * x - 2


def newton_method(raw_f, derivative_f, start, precision=6, n_max=10):
    tolerance = 10 ** (-precision)

    xs = [start]
    for i in range(n_max):
        prev_x = xs[-1]
        next_x = prev_x - raw_f(prev_x) / derivative_f(prev_x)
        xs.append(next_x)

        if isclose(prev_x, next_x, abs_tol=tolerance):
            print(f'x cannot move closer now: iter {i+1}, x diff: {abs(next_x - prev_x)}')
            print(f'function error: {raw_f(next_x)}')
            break

    return xs


if __name__ == '__main__':
    from math import sin, cos, pow

    print(newton_method(f, f_d, 2.0, n_max=100))
    print()

    # for cos(x) = x
    def f1(x):
        return cos(x) - x
    def fd1(x):
        return -sin(x) - 1
    print(newton_method(f1, fd1, start=1))

    # another q.
    def f2(x):
        return pow(x, 5) - pow(x, 4) + 3 * pow(x, 2) - 3 * x - 2
    def fd2(x):
        return 5 * x ** 4 - 4 * x ** 3 + 6 * x - 3
    print(newton_method(f2, fd2, start=1))
