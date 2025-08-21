def gen_matrix(n, m):
    return [[0 for _ in range(m)] for _ in range(n)]

def fill_diag(matrix):
    num = 1
    n = len(matrix) #высота мартицы
    m = len(matrix[0]) #ширина матрицы
    for k in range(n + m - 1):
        for i in range(n):
            for j in range(m):
                if i + j == k:
                    matrix[i][j] = num
                    num += 1
                    break
    return matrix

def print_matrix(matrix):
    print('\n'.join([' '.join([str(j).ljust(3) for j in i]) for i in matrix]))

n, m = [int(i) for i in input().split()]
matrix = fill_diag(gen_matrix(n, m))
print_matrix(matrix)