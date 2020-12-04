#include <stdio.h>

int is_empty(int queue_empty, int q_array[]);
int is_full(int queue_full, int q_array[]);
void push(int queue_full, int q_array[]);
void pull(int queue_full, int q_array[]);


int main()
{
    int user_input;
    int queue_empty=0;
    int queue_full=0;
    int q_array[20] = {1,2,3,4,5,6,7,8,9};
    printf("The queue has numbers 1 to 10 consectively\n ");
    printf("To add a number to the queue, type +1\n ");
    printf("To remove a number from the queue, type -1 ");
    queue_full=is_full(queue_full,q_array);
    queue_empty=is_empty(queue_empty,q_array);
    scanf("%d",&user_input);
    if(user_input==1){
    	push(queue_full,q_array);
    }
    if(user_input==-1){
    	pull(queue_empty,q_array);
    }
	//printing out the final queue after adding or removing elements
    for(int z;z<20;z++)
    {
    	printf("%d",q_array[z]);
    }
    return 0;
}

int is_empty(int queue_empty, int q_array[])
{
	//if the first element in queue is empty
	if(q_array[0]=='\0')
	{
		printf("queue is empty");
		queue_empty=1;
		return queue_empty;
	}
	else
	{
		return queue_empty;
	}
}

int is_full(int queue_full, int q_array[])
{
	if(q_array[19]=='\0')
	{
		return queue_full;
	}
	//when the last element in the queue is not empty, queue is full
	else
	{
		printf("queue is full");
		queue_full=1;
		return queue_full;
	}
}

void push(int queue_full, int q_array[])
{
	int user_add;
	if(queue_full==0)
	{
		for(int x=0;x<20;x++)
		{
			if(q_array[x]=='\0')
			{
				printf("enter the number to insert to queue");
				scanf("%d",&user_add);
				q_array[x]=user_add;
				break;
			}

		}
		
	}
	
}

void pull(int queue_empty, int q_array[])
{
	int swap[20];
	if(queue_empty==1)
	{
		printf("array is empty\n");

	}
	else
	{

		for(int x=0;x<20;x++)
		{
			swap[x]=q_array[x];
		}
		for(int y=0;y<20;y++)
		{
			if((y+1)!=20)
			{
			q_array[y]=swap[y+1];
			}
		}
	}
	
}
