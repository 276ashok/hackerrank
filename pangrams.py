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

"""
sample input 1
We promptly judged antique ivory buckles for the next prize

sample output 1
pangrams

sample input 2
We promptly judged antique ivory buckles for the prize

sample output 2
not pangrams
"""