import math

def pythagoreanTest(a,b):
    a2 = a*a
    b2 = b*b
    c2 = a2+b2
    c = math.sqrt(c2)
    if c%1 == 0:
        return 'true'
    else:
        return 'false'


def createTriples(x):
    
    for i in range(1,333):
        if pythagoreanTest(i,i+x) == 'true':
            a = i
            b = i+x
            a2 = a*a
            b2 = b*b
            c2 = a2+b2
            c = int(math.sqrt(c2))
            print(a,b,c,'|',a2,b2,c2,'|',a+b+c)


def testTriples():
    for index in range(1,110):
        triple = createTriples(index)
        if triple[0]+triple[1]+triple[2] == 1000:
            print('Success!',triple)
        else:
            print(triple[0]+triple[1]+triple[2],triple[0],triple[1],triple[2])


def print10():
    for x in range (100,200):
        createTriples(x)

#print10()
print(200*375*425)
        



