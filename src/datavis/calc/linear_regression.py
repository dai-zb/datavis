import numpy as np


# 使用numpy实现 #线性回归
def linear_regression(x, y, order=1):
    assert order >= 1, order
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    if not isinstance(y, np.ndarray):
        y = np.array(y)

    _x = x.reshape(-1, 1)
    x = np.insert(_x, 1, values=1, axis=1)
    if order > 1:
        for n in range(2, order + 1):
            x = np.concatenate((_x ** n, x), axis=-1)
    # x^3 x^2 x 1
    y = y.reshape(-1, 1)

    # (X^T * X)^(-1) * X^T * Y
    xT_x_inv = np.linalg.inv(np.dot(x.T, x))
    return np.dot(np.dot(xT_x_inv, x.T), y).flatten().tolist()
