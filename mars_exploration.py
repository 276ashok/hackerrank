def marsExploration(s):
    count = 0

    for i in range(len(s)//3):
        if s[i*3]!="S":
            count +=1
        
        if s[i*3+1]!="O":
            count +=1

        if s [i*3+2]!="S":
            count +=1

    return count

s = input()
result = marsExploration(s)
print(result) 

"""
sample input
SOSSPSSQSSOR

sample output
3
"""