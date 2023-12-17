def pangrams(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()

    for i in alpha:
        if i not in s:
            return "not pangrams"
        
    return "pangrams"

input1 = input()
result = pangrams(input1)
print(result)