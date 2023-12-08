# input_arr = int(input())
# number = list(map(int, input().split()))
# # print(number)
# sum = 0
# for i in number:
#     sum += i
#     # print(sum,end=" ")
# print(sum)

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

input_arr = int(input())
number = list(map(int, input().split()))
result = simpleArraySum(number)

print(result)