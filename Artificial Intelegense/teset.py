import csv
import numpy as np
import pandas

# открываем файл с помощью pandas
file = pandas.read_excel("file.xlsx")
print(file)

# выводим файл в csv без индексов строк
file.to_csv("123.csv", index=False)

# считываем с помощью csv reader
with open("123.csv", 'r') as pre_table:
    table = csv.reader(pre_table)
    A_list = [list(map(int, row)) for row in table]
A = np.array(A_list)
print(A)
B = A.T
print(B)
C = np.dot(A, B)
sum_C = np.sum(C)
print("Сумма элементов матрицы C = AB:", sum_C)
# находим сумму элементов по каждому столбцу матрицы A
d = np.sum(A, axis=0)
sum_d_squares = np.sum(np.square(d))
print("Сумма квадратов элементов d:", sum_d_squares)
print("Кузнецов Виктор")