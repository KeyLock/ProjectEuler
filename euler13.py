

lines = open('euler13.txt').read().splitlines()
lines = map(int,lines)
sum = 0

for i in lines:
    sum += i

print(sum)
