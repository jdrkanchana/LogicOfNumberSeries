def is_empty(queue_empty,q_list):
	if q_list==[]:
		queue_empty=True
	return queue_empty

def push(q_list):
	print("enter element to add to queue")
	new_element=int(input())
	q_list.append(new_element)
	return q_list

def pop(queue_empty,q_list):
	if queue_empty==True:
		print("No elements to remove queue is empty")
		return q_list
	else:
		q_list.remove(q_list[0])
		print("first element successfully removed from queue")
		return q_list

def peek(queue_empty,q_list):
	if queue_empty==True:
		print("No elements to display queue is empty")
	else:
		print("the first element in the queue is",q_list[0])
		
q_list=[1,2,3,4,5,6,7,8,9,10]
queue_empty=False
print("The queue currrently has numbers 1 to 10 consectively")
print("To add another element, type add")
print("To remove an element, type remove")
print("To view element at top, type view")
user_input=input()
queue_empty=is_empty(queue_empty,q_list)
if user_input=="add":
	q_list=push(q_list)
	print(q_list)
elif user_input=="remove":
	q_list=pop(queue_empty,q_list)
	print(q_list)
elif user_input=="view":
	peek(queue_empty,q_list)
