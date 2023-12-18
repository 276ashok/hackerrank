def theLoveLetterMystery(s):
    count =0
    for i in range(int(len(s) / 2)):
        count += abs(ord(s[i])-ord(s[-(i+1)]))
    return count

q=int(input())
for i in range(q):
    s=input()
    result=theLoveLetterMystery(s)
    print(result)