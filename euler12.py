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
    n = 2015
    t = createTriangularNumber(n)
    f = factorList(t)
    while len(f) < 500:
        n += 1
        t = createTriangularNumber(n)
        f = factorList(t)

    print(n)
    return createTriangularNumber(n)

print(find500())       
