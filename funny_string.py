def funnystring(s):

    s_rev = s[::-1]
    l1=[abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1)]
    l2=[abs(ord(s_rev[i])-ord(s_rev[i+1])) for i in range(len(s_rev)-1)]

    if l1==l2:
        return "Funny"
    return "Not Funny"

input1 = int(input())

for i in range(input1):
    s=input()
    result = funnystring(s)
    print(result)

"""
sample input
2
acxz
bcxz

sample output
Funny
Not Funny
"""