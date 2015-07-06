def countDivisors(n):
    divisors = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            divisors += 2
        i += 1
    return divisors

def factorList(n):
    factorList = []
    for i in range(1,n+1):
        if n % i == 0:
            factorList.append(i)
    return factorList

#print(factorList(28))

def createTriangularNumber(n):
    num = 0
    for i in range(1,n+1):
        num += i
    return num

#print(createTriangularNumber(10))

def find500():
    n = 1
    t = createTriangularNumber(n)
    d = countDivisors(t)
    while d < 500:
        n += 1
        t = createTriangularNumber(n)
        d = countDivisors(t)

    return createTriangularNumber(n)

print(find500())       

#x = createTriangularNumber(2015)
#countDivisors(x)
