def is_empty(stack_empty,s_list):
	if s_list==[]:
		stack_empty=True
	return stack_empty

def push(s_list):
	print("enter element to add to stack")
	new_element=int(input())
	s_list.append(new_element)
	return s_list

def pop(stack_empty,s_list):
	if stack_empty==True:
		print("No elements to remove stack is empty")
		return s_list
	else:
		s_list.remove(s_list[-1])
		print("last element successfully removed from stack")
		return s_list

def peek(stack_empty,s_list):
	if stack_empty==True:
		print("No elements to display stack is empty")
	else:
		print("the last element in the stack is",s_list[-1])
		
s_list=[1,2,3,4,5,6,7,8,9,10]
stack_full=False
stack_empty=False
print("The stack currrently has numbers 1 to 10 consectively")
print("To add another element, type add")
print("To remove an element, type remove")
print("To view element at top, type view")
user_input=input()
stack_empty=is_empty(stack_empty,s_list)
if user_input=="add":
	s_list=push(s_list)
	print(s_list)
elif user_input=="remove":
	s_list=pop(stack_empty,s_list)
	print(s_list)
elif user_input=="view":
	peek(stack_empty,s_list)
