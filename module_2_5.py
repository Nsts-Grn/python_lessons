n = int(input('Задайте количество строк матрицы: '))
m = int(input('Задайте количество столбцов матрицы: '))
value = input(f'Задайте значения матрицы: ')

def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    if n <= 0:
        print("Матрица пуста, задано неверное количество строк:", n)
    elif m <= 0:
        print("Матрица пуста, задано неверное количество столбцов:", m)
    else:
        print(matrix)
matrix = get_matrix(n, m, value)
