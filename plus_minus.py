def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in range(len(arr)):
        if arr[i]>0:
            positive+=1
        elif arr[i]<0:
            negative+=1
        else:
            zero+=1

    print(positive/len(arr))
    print(negative/len(arr))
    print(zero/len(arr))


input1 = int(input())
arr = list(map(int,input().split()))
plusMinus(arr)

"""
sample input
6
-4 3 -9 0 4 1

sample output
0.500000
0.333333
0.166667
"""