#a code to count the number of vowels, use python 3 to implement,input() not work with python 2 
print("Enter a word")
user_input=[]
count=0
user_input=input()
x=len(user_input)
for a in range(0,x):
	if ((user_input[a]=='a') or (user_input[a]=='A')):
		count=count+1
	if ((user_input[a]=='e') or (user_input[a]=='E')):
		count=count+1
	if ((user_input[a]=='i') or (user_input[a]=='I')):
		count=count+1
	if ((user_input[a]=='o') or (user_input[a]=='O')):
		count=count+1
	if ((user_input[a]=='u') or (user_input[a]=='U')):
		count=count+1
print("the word you entered has",count,"number of vowels")
