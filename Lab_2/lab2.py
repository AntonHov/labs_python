import random as rand
import numpy as np

file = open('lab2', 'w')
n = int(input("Введите количество строк матрицы: "))
m = int(input("Введите количество столбцов матрицы: "))
matrica = np.array([[rand.randint(0, 10) for j in range(m)] for i in range(n)])
print("Исходная матрица: ")
print(matrica)
file.write(str(n) + " " + str(m))
file.write("\n" + str(matrica) + "\n")
l = int(input("Введите номер строки, элементы которой будут суммироваться к соответствующим элементам строк: "))
while l > n:
    print(f"Не существует строки под номером {l}, повторите ввод")
    l = int(input("Введите номер строки, элементы которой будут суммироваться к соответствующим элементам строк: "))
for j in range(m):
    for i in range(n):
        matrica[i][j] += matrica[l][j]
        if i == l:
            i += 1
print(matrica)
file.write("\n" + str(l))
file.write("\n" + str(matrica))
file.close()



