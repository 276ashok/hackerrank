# a = input().strip()
# b = input().strip()
# main_count = 0
# total = 0
# string1_set = set(a + b)
# for i in range(len(string1_set)):
#                count = a.count(list(string1_set)[i])
#                count2 = b.count(list(string1_set)[i])
#                if count > count2: 
#                         main_count = count - count2
#                elif count2 > count :
#                         main_count = count2 - count
#                elif count2 == count :
#                         main_count = 0
#                total = total + main_count
# print(total)

def makinganagrams(a,b):
        main_count = 0
        total = 0
        string1_set = set(a+b)
        for i in range(len(string1_set)):
                count = a.count(list(string1_set)[i])
                count2=b.count(list(string1_set)[i])
                if count>count2:
                        main_count = count -count2
                elif count2>count:
                        main_count = count2-count
                elif count==count2:
                        main_count = 0
                total = total+main_count

        return total

a=input()
b=input()
result = makinganagrams(a,b)
print(result)

"""
sample input
cde
abc

sample output
4
"""