numbers = "0123456789"
lower_case = "qwertyuioplkjhgfdsazxcvbnm"
upper_case = "zxcvbnmlkjhgfdsaqwertyuiop"
special_character = "!@#$%^&*+-"

def strong_password(n,password):
    res = 0

    if not any(x in numbers for x in password):
        res+=1

    if not any(x in lower_case for x in password):
        res+=1

    if not any(x in upper_case for x in password):
        res+=1

    if not any(x in special_character for x in password):
        res+1

    if len(password)<6:
        return max(res, 6-len(password))
    
    return res
        

input1 = input()
password = input()
result = strong_password(input1,password)
print(result)