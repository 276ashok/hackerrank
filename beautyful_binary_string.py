def beautifulBinaryString(b):
    res = 0
    while "010" in b:
        res +=1
        b=b.replace("010","011",1)
    return res

n = int(input())
b = input()
result = beautifulBinaryString(b)
print(result)