compare=[]
similar=True
# if a number
#word=str(151)
word="amma"
original=list(word)
compare=list(word)
compare.reverse()
for x in range(0,len(word)):
	if(original[x]!=compare[x]):
	  similar=False
if (similar==True):
	print("palindrome")
