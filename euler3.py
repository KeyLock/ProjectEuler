TEST = 13195

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

def printPrimes(x):
    index = 1
    while index < x:
        if isPrime(index)=='true':
            print(index,'is prime.')
        index+=1

def listPrimes(x):
    index = 1
    primes = []
    while index < x:
        if isPrime(index) == 'true':
            primes.append(index)
        index += 1
    return primes

def isFactor(x):
    factors = []
    primes = listPrimes(10000)
    index = 0
    while index < len(primes):
        if x % primes[index]==0:
            factors.append(primes[index])
        index += 1
    return factors
    
def main():
    x = int(input('Enter a number to find the prime factors: '))
    print(isFactor(x))

main()

        
         
     
