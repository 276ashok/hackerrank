def gemstone(arr):

    uni_char = list(set(''.join(arr)))
    count = len(uni_char)

    for c in uni_char:
        for j in arr:
            if c not in j:
                count -= 1
                break

    return count


n = int(input())
arr = []
for i in range(n):
    arr_item = input()
    arr.append(arr_item)
    result = gemstone(arr)
    print(result)

"""
sample input
3
abcdde
baccd
eeabg

sample output
2
"""