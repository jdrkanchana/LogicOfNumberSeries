count_max=0
n=13
while(n<1000000):
	count=0
	a=n
	while(a!=1):
		if a%2==0:
			a=a/2
			count+=1
		else:
			a=3*a+1
			count+=1
		if count>count_max:
			count_max=count
			n_max=n
	n+=3
		 
n=n_max
while(n<1000000):
	count=0
	a=n
	while(a!=1 and a%3!=0):
		if a%2==0:
			a=a/2
			count+=1
		else:
			a=3*a+1
			count+=1
		if count>count_max:
			count_max=count
			n_max=n
	n+=1
		 
		 
print(n_max)
print(count_max)
