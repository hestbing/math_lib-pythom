# -*- coding: cp1251 -*-
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)


arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)

arr3 = np.array([10, 11, 12, 13, 14])
result1 = arr1 + arr3
result2 = arr1 * arr3
print("Сложение массивов:")
print(result1)
print("Умножение массивов:")
print(result2)


result1 = np.sqrt(arr1)
result2 = np.exp(arr1)
result3 = np.log(arr1)
print("Квадратный корень:")
print(result1)
print("Экспонента:")
print(result2)
print("Натуральный логарифм:")
print(result3)

print("Индексация и срезы:")
print("Первый элемент arr1:", arr1[0])
print("Второй столбец arr2:", arr2[:, 1])
print("Срез arr1 с шагом 2:", arr1[::2])
