def isPrimer(num):
    if num == 0 or num ==1:
        return False
    for x in range(2,num):
        if num % x == 0:
            return False
    else:
        return True

count = 0
num = 1
while True:
    if isPrimer(num):
        print(num)
        count += 1
    if count == 10001:
        break
    num += 1

print(num) #104743