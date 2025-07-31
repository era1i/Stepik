def pasc(n):
    ret = []
    for i in range(n):
        temp = []
        for j in range(i):
            if j == 0:
                temp.append(1)
            else:
                temp.append(ret[i - 1][j - 1] + ret[i - 1][j])
        temp.append(1)
        ret.append(temp)
    return ret

def print_list(l):
    print('\n'.join(*[str(i) for i in l]))

print_list(pasc(4))


