x=1
y=2
sum=0
tot=2

while(sum<4000000):
    sum=x+y
    x=y
    y=sum
    if (sum%2==0):
        tot=tot+sum
    
print(tot,'is the total')
