fib=0
x=1
y=2
sum=2
while fib < 4000000:
    fib = x+y
    x = y
    y = fib
    if fib < 4000000 and fib % 2 == 0:
        sum += fib
print(sum)
