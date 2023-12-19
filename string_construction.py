def stringconstruction(s):
    return len(set(s))

q=int(input())
for i in range(q):
    n=input()
    result=stringconstruction(n)
    print(result)

"""
sample input
2
abcd
abab

sample output
4
2
"""