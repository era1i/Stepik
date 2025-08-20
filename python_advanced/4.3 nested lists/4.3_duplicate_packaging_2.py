def compress(s):
    ret = [[s.pop(0)]]
    for c in s:
        if c in ret[-1]:
            ret[-1].append(c)
        else:
            ret.append([c])
    return ret

s = input().split()
print(compress(s))