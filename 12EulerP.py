import math

def divisor(natural):
	count=0
	div=math.sqrt(natural)
	for x in range(2,int(div)):
		if(natural%x==0):
			count=count+2
	return count
divisor_count=[]		
triArray=[]
natural=28
for a in range(8,100000):
	natural=natural+a
	div_count=divisor(natural)
	div_count=div_count+2 #all number divide by itself and number one
	print("for the triangle number",natural,"the divisor number is",div_count)
	if (div_count>=500):
		triArray.append(natural)
		divisor_count.append(div_count)
print(triArray)
print(divisor_count)
	
