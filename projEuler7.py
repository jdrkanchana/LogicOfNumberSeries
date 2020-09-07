import math
from decimal import Decimal
def primea(num):
	prime=1
	if(num%3==0):
		prime=0
	if(num%5==0):
		prime=0
	if(num%7==0):
		prime=0
	rem=math.sqrt(num)
	ans=Decimal((rem)%1==0)
	if(ans==True):
		prime=0
	div=round(rem)
	print(div)
	for j in range(11,int(div)):
		if(num%j==0):
			prime=0
	return prime

prime=1
count=6
num=11
prime_n=[]
while(count<10003):
	prime=primea(num)
	if(prime==1):
		count=count+1
		prime_n.append(num)
	num=num+2

print(prime_n)
