# -*- coding: cp1251 -*-
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


np.random.seed(42)
X = np.random.rand(100, 1) * 10
y = 2 * X + 1 + np.random.randn(100, 1) * 2  

_X = sm.add_constant(X)

model = sm.OLS(y, _X)

results = model.fit()

print(results.summary())

plt.scatter(X, y, label='Исходные данные')
plt.plot(X, results.predict(_X), color='red', label='Линейная регрессия')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()
