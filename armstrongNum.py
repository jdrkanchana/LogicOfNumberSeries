
a = int(input("Please enter a positive number:\n"))
num=a
sum=0
while (a%10!=0):
    y=a%10
    if(y>4):
        a=a-y
    else:
        a=a
    a=round(a/10)
    sum=sum+(y**3)
    print(sum)
if (sum==num):
    print(num,'is a palindrome number')
else:
    print(num, 'is not a palindrome number')
    print('The summation of cube of',num 'is', sum)
