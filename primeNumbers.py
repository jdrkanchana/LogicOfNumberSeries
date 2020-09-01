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
