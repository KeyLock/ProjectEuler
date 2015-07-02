def sumOfSquares(x):
    sum=0
    for i in range(0,x+1):
        square = i*i
        sum += square
    return sum

def squareOfSum(x):
    sum=0
    for i in range(0,x+1):
        sum += i
    square = sum*sum
    return square

def difference(x):
    diff = squareOfSum(x) - sumOfSquares(x)
    return diff

print(sumOfSquares(10))
print(squareOfSum(10))
print(difference(10))
print()
print(sumOfSquares(100))
print(squareOfSum(100))
print(difference(100))
