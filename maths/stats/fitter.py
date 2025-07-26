# coding=utf-8
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


def poly_fit_example():
    points = [(0.0, 450.0),
              (1.0, 445.0),
              (2.0, 431.0),
              (3.0, 408.0),
              (4.0, 375.0),
              (5.0, 332.0),
              (6.0, 279.0),
              (7.0, 216.0),
              (8.0, 143.0),
              (9.0, 61.0)]

    X = np.array([x for x, y in points]).reshape((-1, 1))
    y = np.array([y for x, y in points]).reshape((-1, 1))

    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_feats = poly.fit_transform(X)
    print('degree 2 features:')
    print(poly_feats)

    model = LinearRegression()
    model.fit(poly_feats, y)
    a1, a2 = model.coef_[0]
    a0 = model.intercept_[0]
    print(f'{a2:.5} * t^2 + {a1:.5} * t + {a0:.5}')


if __name__ == '__main__':
    poly_fit_example()
