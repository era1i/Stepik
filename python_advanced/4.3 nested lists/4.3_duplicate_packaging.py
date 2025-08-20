# put your python code here

def compressor(s):
    ret = []
    temp = []
    for c in s:
        if not temp or c == temp[-1]:
            temp.append(c)
        else:
            ret.append(temp)
            temp = [c]
    ret.append(temp)
    return ret

s = input().split()
print(compressor(s))