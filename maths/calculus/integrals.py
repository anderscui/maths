# coding=utf-8
import math
import re


def get_sample_point(start, end, sample_type='right'):
    if sample_type == 'right':
        return end
    elif sample_type == 'left':
        return start
    elif sample_type == 'middle':
        return (start + end) / 2
    else:
        raise ValueError('unsupported sample type')


def riemann_sum(f, a, b, n_sub_intervals=5, sample_type='right'):
    if sample_type == 'trapezoidal':
        left_sum = riemann_sum(f, a, b, n_sub_intervals, sample_type='left')
        right_sum = riemann_sum(f, a, b, n_sub_intervals, sample_type='right')
        return (left_sum + right_sum) / 2

    if sample_type == 'simpson':
        assert n_sub_intervals % 2 == 0
        tn = riemann_sum(f, a, b, n_sub_intervals // 2, sample_type='trapezoidal')
        mn = riemann_sum(f, a, b, n_sub_intervals // 2, sample_type='middle')
        return 1/3*tn + 2/3*mn

    delta_x = (b - a) / n_sub_intervals
    sub_intervals = [(a + delta_x * (i-1), a + delta_x * i) for i in range(1, n_sub_intervals+1)]
    sample_points = [get_sample_point(start, end, sample_type=sample_type) for start, end in sub_intervals]
    sub_areas = [f(sp) * delta_x for sp in sample_points]
    return sum(sub_areas)


def get_sample_point_2d(x_range, y_range, sample_type='upper_right'):
    a, b = x_range
    c, d = y_range
    if sample_type == 'upper_right':
        return b, d
    elif sample_type == 'lower_left':
        return a, c
    elif sample_type == 'middle':
        return (a+b)/2, (c+d)/2
    else:
        raise ValueError('unsupported sample type')


def riemann_sum_2d(f, x_range, y_range, x_subs, y_subs, sample_type='upper_right'):
    a, b = x_range
    c, d = y_range
    delta_x = (b-a)/x_subs
    delta_y = (d-c)/y_subs
    delta_a = delta_x * delta_y

    x_intervals = [(a + delta_x * (i-1), a + delta_x * i) for i in range(1, x_subs+1)]
    y_intervals = [(c + delta_y * (j-1), c + delta_y * j) for j in range(1, y_subs+1)]

    sample_points = [get_sample_point_2d(xi, yi, sample_type) for xi in x_intervals for yi in y_intervals]
    sub_volumes = [f(sp[0], sp[1]) * delta_a for sp in sample_points]
    return sum(sub_volumes)


if __name__ == '__main__':
    # f1 = lambda x: x ** 2  # 1/ 3
    # print(riemann_sum(f1, 0, 1, 5))
    # print(riemann_sum(f1, 0, 1, 1000))
    #
    # f2 = lambda x: x - 1  # -10 when n = 5
    # print(riemann_sum(f2, -6, 4, 5))
    #
    # f3 = lambda x: x ** 2 - 4  # -49/16=-3.0625
    # print(riemann_sum(f3, 0, 3, n_sub_intervals=6, sample_type='middle'))
    #
    # f4 = lambda x: x ** 2  # 168
    # print(riemann_sum(f4, 0, 8, n_sub_intervals=4, sample_type='middle'))
    #
    # f5 = lambda x: x/ (x ** 2 + 8)  # 0.3186
    # print(riemann_sum(f5, 1, 3, n_sub_intervals=5, sample_type='middle'))
    #
    # f6 = lambda x: 1/x
    # print(riemann_sum(f6, 1, 2, n_sub_intervals=5, sample_type='middle'))
    # print(riemann_sum(f6, 1, 2, n_sub_intervals=5, sample_type='trapezoidal'))
    # print(riemann_sum(f6, 1, 2, n_sub_intervals=10, sample_type='simpson'))
    #
    # f7 = lambda x: math.exp(x*x)
    # print(riemann_sum(f7, 0, 1, n_sub_intervals=10, sample_type='simpson'))
    #
    # f8 = lambda x: (1+x**3)**(1/2)
    # print(riemann_sum(f8, 0, 1, n_sub_intervals=4, sample_type='trapezoidal'))
    # print(riemann_sum(f8, 0, 1, n_sub_intervals=4, sample_type='middle'))
    # print(riemann_sum(f8, 0, 1, n_sub_intervals=4, sample_type='simpson'))
    #
    # f9 = lambda x: math.exp(x+math.cos(x))
    # print(riemann_sum(f9, -1, 2, n_sub_intervals=6, sample_type='trapezoidal'))
    # print(riemann_sum(f9, -1, 2, n_sub_intervals=6, sample_type='middle'))
    # print(riemann_sum(f9, -1, 2, n_sub_intervals=6, sample_type='simpson'))
    #
    # f10 = lambda x: math.sqrt(1 + (math.sin(x) + x*math.cos(x))**2)
    # print(riemann_sum(f10, 0, 2*math.pi, n_sub_intervals=10, sample_type='simpson'))

    f20 = lambda x, y: 16 - x**2 - 2 * y**2
    print(riemann_sum_2d(f20, (0, 2), (0, 2), x_subs=2, y_subs=2))  # 34

    f21 = lambda x, y: x - 3 * y ** 2  # exact value: -12
    print(riemann_sum_2d(f21, (0, 2), (1, 2), x_subs=2, y_subs=2, sample_type='middle'))  # -11.875
    print(riemann_sum_2d(f21, (0, 2), (1, 2), x_subs=16, y_subs=16, sample_type='middle'))  # -11.9980

    f22 = lambda x, y: x * y  #
    print(riemann_sum_2d(f22, (0, 6), (0, 4), x_subs=3, y_subs=2, sample_type='upper_right'))  # 288.0
    print(riemann_sum_2d(f22, (0, 6), (0, 4), x_subs=3, y_subs=2, sample_type='middle'))  # 144

    f23 = lambda x, y: x * math.exp(-x*y)
    print(riemann_sum_2d(f23, (0, 2), (0, 1), x_subs=2, y_subs=2, sample_type='upper_right'))  # 0.990
    print(riemann_sum_2d(f23, (0, 2), (0, 1), x_subs=2, y_subs=2, sample_type='middle'))  # 1.151
