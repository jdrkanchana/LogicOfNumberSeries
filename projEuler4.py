
listP=[]
for x in range(100,999):
	for y in range(100,999):
		a=x*y
		b=str(a)
		z=len(b)
		if(z==5):
			if(b[0]==b[4] and b[1]==b[3]):
				listP.append(a)
		elif(z==6):
			if(b[0]==b[5] and b[1]==b[4]):
				if(b[2]==b[3]):
					listP.append(a)
listP.sort()
length=len(listP)
print(length)
final=length-1
largeP=listP[final]
print(largeP)
