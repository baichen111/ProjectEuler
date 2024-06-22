def isPrimer(num):
    if num == 0 or num ==1:
        return False
    for x in range(2,num):
        if num % x == 0:
            return False
    else:
        return True



def LargestPrimeFactor(n):
    factors = []
    for i in range(2,int(n**.5)):
        if n % i ==0:
            factors.extend([i,int(n/i)])
    factors = sorted(factors,reverse=True)
    for factor in factors:
        if isPrimer(factor):
            return factor
    else:
        return
    
n = 600851475143
print(LargestPrimeFactor(n))  #6857


