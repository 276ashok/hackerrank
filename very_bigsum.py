def aVeryBigSum(ar):
    sum = 0
    for i in range(0,input1):
        sum+=ar[i]
    return sum


input1 = int(input())
input2=list(map(int,input().split()))

result=aVeryBigSum(input2)

print(result)