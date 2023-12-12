def camelcase(s):
    count = 1
    for i in s:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            count += 1
    return count

input = input()
result = camelcase(input)
print(result)