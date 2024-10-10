def get_matrix(n, m, value):
    matrix = []
    for stroki in range(n):
        matrix_2 = []
        matrix.append(matrix_2)
        for stolbci in range(m):
            matrix_2.append(value)
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
