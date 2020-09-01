sum=0
d=1
for x in range(1,1000):
    a=d%3
    b=d%5
    if (a==0 or b==0):
        sum=sum+d
    d=d+1
print(sum,'is the total')
