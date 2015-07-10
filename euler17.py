a = 'one'
b = 'two'
c = 'three'
d = 'four'
e = 'five'
f = 'six'
g = 'seven'
h = 'eight'
i = 'nine'
j = 'ten'
k = 'eleven'
l = 'twelve'
m = 'thirteen'
n = 'fourteen'
o = 'fifteen'
p = 'sixteen'
q = 'seventeen'
r = 'eighteen'
s = 'nineteen'
t = 'twenty'
u = 'thirty'
v = 'forty'
w = 'fifty'
x = 'sixty'
y = 'seventy'
z = 'eighty'
aa = 'ninety'
bb = 'hundred'
cc = 'thousand'

oneToOneThousand = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s

nums = [a,b,c,d,e,f,g,h,i]

teens = [k,j,l,m,n,o,p,q,r,s]



twenty = 'twenty'

for num in nums:
    twenty += t + num

oneToOneThousand += twenty

thirty = 'thirty'

for num in nums:
    thirty += u + num

oneToOneThousand += thirty

forty = 'forty'

for num in nums:
    forty += v + num

oneToOneThousand += forty

fifty = 'fifty'

for num in nums:
    fifty += w + num

oneToOneThousand += fifty

sixty = 'sixty'

for num in nums:
    sixty += x + num

oneToOneThousand += sixty

seventy = 'seventy'

for num in nums:
    seventy += y + num

oneToOneThousand += seventy

eighty = 'eighty'

for num in nums:
    eighty += z + num

oneToOneThousand += eighty

ninety = 'ninety'

for num in nums:
    ninety += aa + num

oneToOneThousand += ninety

tens = [twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety]

onehundred = 'onehundred'
oneHundred = ''

oneToOneThousand += onehundred

for num in nums:
    oneHundred += onehundred + 'and' + num

for teen in teens:
    oneHundred += onehundred + 'and' + teen

for ten in tens:
    oneHundred += 10*onehundred + 10*'and' + ten

oneToOneThousand += oneHundred

twohundred = 'twohundred'
twoHundred = ''

oneToOneThousand += twohundred

for num in nums:
    twoHundred += twohundred + 'and' + num

for teen in teens:
    twoHundred += twohundred + 'and' + teen

for ten in tens:
    twoHundred += 10*twohundred + 10*'and' + ten

oneToOneThousand += twoHundred

threehundred = 'threehundred'
threeHundred = ''

oneToOneThousand += threehundred

for num in nums:
    threeHundred += threehundred + 'and' + num

for teen in teens:
    threeHundred += threehundred + 'and' + teen

for ten in tens:
    threeHundred += 10*threehundred + 10*'and' + ten

oneToOneThousand += threeHundred

fourhundred = 'fourhundred'
fourHundred = ''

oneToOneThousand += fourhundred

for num in nums:
    fourHundred += fourhundred + 'and' + num

for teen in teens:
    fourHundred += fourhundred + 'and' + teen

for ten in tens:
    fourHundred += 10*fourhundred + 10*'and' + ten

oneToOneThousand += fourHundred

oneToOneThousand += fourHundred #5

oneToOneThousand += oneHundred #6

oneToOneThousand += threeHundred #7

oneToOneThousand += threeHundred #8

oneToOneThousand += fourHundred #9

oneToOneThousand += 'one' + cc

oneToOneThousand += 'fivehundredsixhundredsevenhundredeighthundredninehundred'
# correction for missing 5,6,7,8,9 hundred



print(len(oneToOneThousand))


