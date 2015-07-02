
def isDivisible():
    check=[]
    num = 12252240
    while num > 0:
        for x in range(1,21):
            if num%x == 0:
                check.append(1)
            else:
                check.append(0)

        if all(elements == 1 for elements in check):
            print(num)
            return
        else:
            check=[]
            num += 20
        
isDivisible()
