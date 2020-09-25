#the given array is reversed without making another array
array=[3,16,28,49,57]
y=len(array)-1
print(y)
print("the original array",array)

for x in range(y,0,-1):
	print(array[x])
