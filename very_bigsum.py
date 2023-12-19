def aVeryBigSum(ar):
    sum = 0
    for i in range(0,input1):
        sum+=ar[i]
    return sum


input1 = int(input())
input2=list(map(int,input().split()))

result=aVeryBigSum(input2)

print(result)

"""
sample input
5
1000000001 1000000002 1000000003 1000000004 1000000005

sample output
5000000015
"""