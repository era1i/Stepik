def gen_spiral_matrix (n, m):
    matrix = [[None for j in range(m)] for i in range(n)]
    upper_limit, left_border = 0, 0    # ������� � ����� �������
    lower_limit, right_border = n - 1, m - 1    # ������ � ������ �������
    pos_x, pos_y = 0, 0    # ������� �� x � y
    d = 0    # direction ��� �����������: 0 - �����, 1 - ����, 2 - �����, 3 - �����
    if m == 1:   # ������� ������, ���� ������� ������� �� 1 �������
        d = 1
    for k in range(1, n * m + 1):
        if d == 0:
            matrix[pos_y][pos_x] = k
            pos_x += 1
            if pos_x == right_border:
                d = 1
                upper_limit += 1
        elif d == 1:
            matrix[pos_y][pos_x] = k
            pos_y += 1
            if pos_y == lower_limit:
                d = 2
                right_border -= 1
        elif d == 2:
            matrix[pos_y][pos_x] = k
            pos_x -= 1
            if pos_x == left_border:
                d = 3
                lower_limit -= 1
        else:
            matrix[pos_y][pos_x] = k
            pos_y -= 1
            if pos_y == upper_limit:
                d = 0
                left_border += 1
    return matrix

def print_matrix(matrix):
    print('\n'.join([' '.join([str(j).ljust(3) for j in i]) for i in matrix]))
          

n, m = [int(i) for i in input().split()]
print_matrix(gen_spiral_matrix(n, m))