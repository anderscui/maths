# coding=utf-8
import numpy as np


def linear_combination(vectors, weights):
    result = np.zeros_like(vectors[0])
    for vec, weight in zip(vectors, weights):
        result += vec * weight
    return result


def diagonal(m):
    n_rows, n_cols = m.shape
    elements = [m[i][i] for i in range(min(n_rows, n_cols))]
    return np.array(elements)


def anti_diagonal(m):
    n_rows, n_cols = m.shape
    n_min = min(n_rows, n_cols)
    elements = [m[i][n_cols-1-i] for i in range(n_min)]
    return np.array(elements)


def matmul_by_layer(m1: np.ndarray, m2: np.ndarray):
    m, n = m1.shape
    k = m2.shape[1]

    result = np.zeros((m, k))
    for i in range(n):
        result += np.outer(m1[:, i], m2[i, :])
    return result


def matmul_by_column(m1: np.ndarray, m2: np.ndarray):
    m, n = m1.shape
    k = m2.shape[1]

    result = np.zeros((m, k))
    m1_cols = [col for col in m1.T]
    # for each column in the product
    for i in range(k):
        m2_col = m2[:, i]
        result[:, i] = linear_combination(m1_cols, m2_col)
    return result


def matmul_by_row(m1: np.ndarray, m2: np.ndarray):
    m, n = m1.shape
    k = m2.shape[1]

    result = np.zeros((m, k))
    m2_rows = [row for row in m2]
    # for each row in the product
    for i in range(m):
        m1_row = m1[i, :]
        result[i, :] = linear_combination(m2_rows, m1_row)
    return result


def vectorize(m: np.ndarray, order='C'):
    # return m.reshape(m.size)
    return m.flatten(order)


def frobenius_dot_product(m1: np.ndarray, m2: np.ndarray):
    v1 = vectorize(m1)
    v2 = vectorize(m2)
    return np.dot(v1, v2)


def frobenius_product(m1: np.ndarray, m2: np.ndarray):
    return np.trace(m1.T @ m2)


def create_matrix_of_rank(n_rows: int, n_cols: int, rank: int):
    if rank > min(n_rows, n_cols):
        raise ValueError(f'rank ({rank}) should be less or equal to the min of rows ({n_rows}) and cols ({n_cols})')
    if rank == 0:
        return np.zeros((n_rows, n_cols))

    m1 = np.random.randn(n_rows, rank)
    m2 = np.random.randn(rank, n_cols)
    return m1 @ m2


def get_row_switching_matrix(m: np.ndarray, i, j):
    n_rows = m.shape[0]
    left_matrix = np.identity(n_rows)
    left_matrix[[i, j]] = left_matrix[[j, i]]
    return left_matrix


def get_row_multiplication_matrix(m: np.ndarray, i, k):
    n_rows = m.shape[0]
    left_matrix = np.identity(n_rows)
    left_matrix[i, i] = k * left_matrix[i, i]
    return left_matrix


def get_row_addition_matrix(m: np.ndarray, i, j, k):
    n_rows = m.shape[0]
    left_matrix = np.identity(n_rows)
    left_matrix[[i]] += k * left_matrix[[j]]
    return left_matrix


def apply_row_operations(m, op_matrices: list):
    for om in op_matrices:
        m = om @ m
    return m


if __name__ == '__main__':
    a = np.array([[2, 3], [-2, 2]])
    lm = get_row_switching_matrix(a, 0, 1)
    print(lm)
    print(lm @ a)

    lmm = get_row_multiplication_matrix(a, 0, 3)
    print(lmm)
    print(lmm @ a)

    lma = get_row_addition_matrix(a, 1, 0, 2)
    print(lma)
    print(lma @ a)

    a2 = np.array([[2, 2, 1], [4, 0, 1], [3, 1, 1]])
    lms = [get_row_addition_matrix(a2, 1, 0, -2),
           get_row_addition_matrix(a2, 2, 0, -3 / 2),
           get_row_addition_matrix(a2, 2, 1, -1 / 2)]

    a2_r = a2.copy()
    print(apply_row_operations(a2_r, lms))

    a3 = np.array([[2, 1, 4], [4, 2, 9], [8, 5, 3]])
    lms = [get_row_addition_matrix(a3, 1, 0, -2),
           get_row_addition_matrix(a3, 2, 0, -4),
           get_row_switching_matrix(a3, 1, 2)]

    print(apply_row_operations(a3, lms))
