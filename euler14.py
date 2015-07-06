def generateChain(n):
    chain = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
            chain.append(n)
        else:
            n = 3*n + 1
            chain.append(n)
    return chain


def longestChain():
    x = 1
    chainLen = []
    while x < 1000000:
        chainLen.append(len(generateChain(x)))
        x += 1
    val = max(chainLen)
    num = chainLen.index(val)
    print(num+1)
    return max(chainLen)

print(longestChain())

