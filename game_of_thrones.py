s = input()
cnt = {}

for char in cnt:
    if char in cnt:
        cnt[char] +=1
    else:
        cnt[char] = 1
        
odd = False

for key in cnt:
    if cnt[key]%2==1:
        if odd:
            print("NO")
            break
        odd = True

else:
    print("YES")

"""
sample input
aaabbbb

sample output
YES

sample input 1
cdefghmnopqrstuvw

sample output 1
NO
"""
