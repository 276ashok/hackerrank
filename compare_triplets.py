def compareTriplets(a,b):
    Alice = 0
    Bob = 0

    for i in range(0,3):
        if a[i] > b[i]:
            Alice += 1
        elif a[i]<b[i]:
            Bob += 1
        else:
            Alice += 0
            Bob += 0
    return (Alice,Bob)
    
alice = list(map(int,input().split()))
bob = list(map(int, input().split()))

result = compareTriplets(alice,bob)
output = ' '.join(map(str,result))
print(output)