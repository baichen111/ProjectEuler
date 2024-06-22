n = 20

while True:
    for i in range(1,21):
        if not n % i == 0:
            n += 1
            break 
    else:
        print(n)  #232792560
        break