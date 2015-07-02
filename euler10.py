import math

def isPrime(x):
    root = math.sqrt(x)
    if x < 2:
        return 'false'
    if x > 1 and x < 4:
        return 'true'
    if x%2 == 0:
        return 'false'
    if x % root == 0:
        return 'false'
    if x % 3 == 0:
        return 'false'
    i = 5
    while i*i < x:
        if x % i ==0 or x % (i + 2) == 0:
            return 'false'
        i += 6
    else:
        return 'true'

def primeList(x):
    index = 1
    primeList = []
    while index < x:
        if isPrime(index)=='true':
            primeList.append(index)
#            print(index,'is prime.')
        index+=1
    return primeList

print(sum(primeList(2000000)))
