def alternatingcharacters(s):
    count = 0
    for c in range(1,len(s)):
        if s[c]==s[c-1]:
            count += 1

    return count

input1 = int(input())

for i in range(input1):
    input2 = input()
    result = alternatingcharacters(input2)
    print(result)