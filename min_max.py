def miniMaxSum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    print(sum-max(arr),sum-min(arr))

input1=list(map(int,input().split()))
miniMaxSum(input1)

"""
sample input
1 2 3 4 5

sample output
10 14
"""