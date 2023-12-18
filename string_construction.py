def stringconstruction(s):
    return len(set(s))

q=int(input())
for i in range(q):
    n=input()
    result=stringconstruction(n)
    print(result)