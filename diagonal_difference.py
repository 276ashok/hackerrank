def diagonalDifference(arr):

    add = 0
    sub = 0
    for i in range(0,len(arr)):
        add = add + arr[i][i]
        # print(add)

    for j in range(0,len(arr)):
        sub = sub + arr[j][len(arr)-1-j]
        # print(sub)

    return add-sub

input1 = int(input())
arr=[]
for i in range(input1):
    arr.append(list(map(int,input().split())))

result=diagonalDifference(arr)
print(abs(result))