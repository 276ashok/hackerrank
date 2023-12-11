def bithdayCakeCandles(arr):
    count=0
    big = max(arr)
    for i in range(len(arr)):
        if arr[i]==big:
            count+=1
    return count

input1=int(input())
input2 = list(map(int, input().split()))
result = bithdayCakeCandles(input2)
print(result)
