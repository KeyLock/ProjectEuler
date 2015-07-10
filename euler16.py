def f(x):
    n = 1
    for i in range (x):
        n = 2*n
    return n

num = str(f(1000))

num = list(num)

num = map(int, num)

num = sum(num)

print(num)
