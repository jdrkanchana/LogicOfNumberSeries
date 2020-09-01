sum1=0
for a in range(1,101):
	mul=a*a
	sum1=sum1+mul
add=0
for b in range(1,101):
	add=add+b
sum2=add*add
diff=sum2-sum1
print(diff)
