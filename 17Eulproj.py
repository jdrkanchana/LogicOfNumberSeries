def one_digit(n,count):
	if n==1 or n==2 or n==6:
		count=count+3
	elif n==4 or n==5 or n==9:
		count=count+4
	elif n==3 or n==7 or n==8:
		count=count+5
	print(count)
	return count
	
	
def two_digit(n,count):
	if n==2 or n==3 or n==8 or n==9:
		count=count+6
	elif n==4 or n==5 or n==6:
		count=count+5
	elif n==7:
		count=count+7
	return count
	
	
def three_digit(n,count):
	count=count+10
	count=one_digit(n,count)
	return count
	
	
def teen_digit(n,count):
	if n==11 or n==12 :
		count=count+6
	elif n==15 or n==16:
		count=count+7
	elif n==13 or n==14 or n==18 or n==19:
		count=count+8
	elif n==17:
		count=count+9
	return count
	
count=0
for a in range(1,10):
	count=one_digit(a,count)
	
for b in range(20,100):
	x=b%10
	b=b-x
	b=(b/10)
	if(x!=0):
		count=one_digit(x,count)
	count=two_digit(b,count)
for c in range(100,1000):
	e=c%100
	y=c%10
	if e<20 and e>10:
		count=teen_digit(e,count)
	elif(y!=0)and (e>20 or e<10) :
		count=one_digit(y,count)
	c=c-y
	d=c%100
	z=d/10
	if(z>1):
		count=two_digit(z,count)
	# for all the 10(tens) like 310, 910
	elif (z==1 and y==0):
		count=one_digit(z,count)
	w=c-d
	w=w/100
	count=three_digit(w,count)

count=count+70+11-27
# 70 represents ten(10) to nineteen(19)
# 11 represents one thousand
# 27 represent the and characters printed for 100,200,300,400,500,600,700,800,900
print("total",count)
