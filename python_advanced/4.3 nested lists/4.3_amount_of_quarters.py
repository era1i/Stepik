def gen_matrix(n):
    m = [input().split() for _ in range(n)]
    return [[int(j) for j in i] for i in m]

def sum_calc(m):
    sum_up, sum_right, sum_down, sum_left = 0, 0, 0, 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i < j and i < len(m) - 1 - j:
                sum_up += m[i][j]
            elif i < j and i > len(m) - 1 - j:
                sum_right += m[i][j]
            elif i > j and i > len(m) - 1 - j:
                sum_down += m[i][j]
            elif i > j and i < len(m) - 1 - j:
                sum_left += m[i][j]
    return sum_up, sum_right, sum_down, sum_left

def print_sums(sum_up, sum_right, sum_down, sum_left):
    print(f"Верхняя четверть: {sum_up}\nПравая четверть: {sum_right}\nНижняя четверть: {sum_down}\nЛевая четверть: {sum_left}")

n = int(input())
m = gen_matrix(n)
print_sums(*sum_calc(m))