def diagonalDifference(arr):
    add = 0
    sub = 0

    for i in range(len(arr)):
        add = add + arr[i][i]

    for j in range(len(arr)):
        sub = sub + arr[j][len(arr)-1-j]
    
    return add-sub    

input1=int(input())

arr=[]
for i in range(input1):
    arr.append(list(map(int,input().split())))

# print(arr)
result = diagonalDifference(arr)
print(abs(result))