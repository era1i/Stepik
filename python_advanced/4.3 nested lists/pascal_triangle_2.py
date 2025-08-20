# put your python code here

def pasc(n):
    ret = list()
    for i in range(n):
        temp = list()
        for j in range(i):
            if j == 0:
                temp.append(1)
            else:
                temp.append(ret[i - 1][j - 1] + ret[i - 1][j])
        temp.append(1)
        ret.append(temp)
    return ret

def print_mat(m):
    print('\n'.join([str(j).replace('[', '').replace(']', '').replace(',', '') for j in m]))

n = int(input())
print_mat(pasc(n))