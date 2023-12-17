number = "0123456789"
upper = "QWERTYUIOPLKJHGFDSAZXCVBNM"
lower = "qwertyuioplkjhgfdsazxcvbnm"
spec = "!@#$%^&*()_+=-"

def strong_password(n, password):

    count = 0

    if not any(i in number for i in password):
        count += 1

    if not any(i in upper for i in password):
        count += 1

    if not any(i in lower for i in password):
        count += 1

    if not any(i in spec for i in password):
        count += 1

    if len(password) < 6:
        return max(count, 6-len(password))
    
    return count

n = int(input())
password = input()
result = strong_password(n, password)
print(result)