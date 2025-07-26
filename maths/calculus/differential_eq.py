# coding=utf-8
import math


def euler_method(df, initial_value, step_size, n_max_steps=10, upper_bound=None):
    """
    `df` is the derivative of f, described by x and y, F(x, y);
    `initial_value' is the start point, (x_0, y_0)
    """
    cur_x, cur_y = initial_value

    if upper_bound is None:
        upper_bound = cur_x + step_size * n_max_steps

    # n_steps = 0
    points = [initial_value]
    while cur_x + step_size <= upper_bound:
        next_x = cur_x + step_size
        next_y = cur_y + step_size * df(cur_x, cur_y)

        points.append((round(next_x, 6), round(next_y, 6)))
        cur_x, cur_y = next_x, next_y

    return points


def logistic_growth_model(capacity, k, p0):
    a = (capacity - p0) / p0
    return lambda t: capacity / (1 + a * math.exp(-k * t))


def logistic_growth_time(capacity, k, p0, target_p):
    a = (capacity - p0) / p0
    return (math.log(a) - math.log(capacity/target_p - 1)) / k


if __name__ == '__main__':
    df1 = lambda x, y: x + y
    init_value = (0, 1)
    print(euler_method(df1, init_value, 0.1, upper_bound=1.01))

    df2 = lambda t, i: 15 - 3 * i
    init_value = (0, 0)
    print(euler_method(df2, init_value, 0.1, upper_bound=0.51))

    df3 = lambda x, y: y
    init_value = (0, 1)
    print(euler_method(df3, init_value, 0.1, upper_bound=0.41))
    print(euler_method(df3, init_value, 0.01, upper_bound=0.41)[-10:])
    print(euler_method(df3, init_value, 0.001, upper_bound=0.401)[-10:])
    print(math.exp(0.4))  # true value

    df4 = lambda x, y: 6 * x ** 2 - 3 * (x ** 2) * y
    init_value = (0, 3)
    print(euler_method(df4, init_value, 0.001, upper_bound=1.001)[-5:])  # 2.3681

    lm1 = logistic_growth_model(1200, k=0.04, p0=60)
    print(lm1(10))

    cap = 8 * 10**7
    k = 0.71
    p0 = 2 * 10**7
    lm2 = logistic_growth_model(cap, k, p0)
    print('population:', lm2(1))
    print('time:', logistic_growth_time(cap, k, p0, target_p=4*10**7))
