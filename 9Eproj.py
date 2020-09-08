import math
arr=[]
sum_arr=[]
for x in range(1,751):
	squ=x*x
	arr.append(squ)
arr1=[]
arr1=arr
for z in range(1,750):
	for i in range(1,750):
		summation=arr1[z]+(i*i)
		rem=math.sqrt(summation)
		v1=1000-rem
		value=(rem).is_integer()
		if(value==True) :
			if(rem<1000):
				sum_arr.append(v1)
		rem2=math.sqrt(arr1[z])
		value2=(rem2).is_integer()
		if (value2==True):
			v2=rem2+i
			if(v1==v2):
				print("I m sleeeppppppppinggggggg",i,rem,rem2)
				product=i*rem*rem2
sum_arr.sort()
print(sum_arr)
print(product)
