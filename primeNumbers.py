#Start of comments
#A number x says is equal to 5
#Then x=5 is a prime number, as 5 is divisible only by 5, and 1
#Say x is equal to 4
#x=4 is not a prime number, as 4 is divisible by 1,4 and also by another third number 2
#Hence to find if a number is a prime number or not, divide the given number by a range excluding number=1 and the value of the number given
#if the given number is divisible by a three numbers, the given number is not a prime number
a = int(input("Please enter a string:\n"))
z=1
b=a-1
for x in range(2,b):
    y=a%x
    if y==0:
        z=0
        break
if z==1:
    print(a,'is a prime number')
else:
    print(a, 'is not a prime number')
