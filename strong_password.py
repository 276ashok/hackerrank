def strongpassword(s):
    upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    lower = "qwertyuioplkjhgfdsazxcvbnm"
    number = 1234567890
    spec = "!@#$%^&*()_+=-"

    count = 0

    if any(i in upper for i in s) == False:
        count += 1

    if any(i in lower for i in s) == False:
        count += 1

    if any(i in number for i in s) == False:
        count += 1

    if any(i in spec for i in s) == False:
        count += 1

    return max(count, 6-s)


input = input()
result = strongpassword(input)
print(result)
