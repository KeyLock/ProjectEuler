num1 = 1
num2 = 999

def isPalindrome(a,b):
    check = str(a*b)
    if check == check[::-1]:
        return 'true'
    else:
        return 'false'


def findLargest(a,b):
    for a in range(1,999):
        if isPalindrome(a,b) == 'true':
            print('LOOK HERE!')
            print(a,'x',b,'is a palindrome',a*b)
            print()
            if a < b:
                b -= 1
                a = 1
                findLargest(a,b)


        

findLargest(num1,num2)
    
'''
This prints the correct response (913 x 993 = 906609),
however it needs to be refined to eliminate the other smaller responses.
'''
 
