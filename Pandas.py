# -*- coding: cp1251 -*-
import pandas as pd
import numpy as np

data = {
    'Name': ['Dima', 'BoBa', 'Maks', 'Pety', 'Danil'],
    'Age': [25, 30, 35, 22, 28],
    'Salary': [50000, 60000, 75000, 45000, 70000],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance']
}

df = pd.DataFrame(data)

print("Исходные данные:")
print(df.head())


print("Основные статистики:")
print(df.describe())

it_dep = df[df['Department'] == 'IT']
print("\nСотрудники из IT-отдела:")
print(it_dep)

salary_dep = df.groupby('Department')['Salary'].mean()
print("\nСредняя зарплата по отделам:")
print(salary_dep)

df['Bonus'] = np.where(df['Age'] > 30, 5000, 0)
print("\nDataFrame с новым столбцом 'Bonus':")
print(df)

df.to_csv('employee_data.csv', index=False)
