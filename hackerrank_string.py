def hackerrankInString(s):
    ret = 'NO'
    target = 'hackerrank'
    idx = 0

    for c in s:
        if c == target[idx]:
            idx += 1
        if idx == len(target):
            ret = 'YES'
            break

    return ret

q = int(input())

for q_itr in range(q):
    s = input()
    result = hackerrankInString(s)
    print(result)