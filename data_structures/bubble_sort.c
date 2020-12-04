#include<stdio.h>
int main(){
int x,j;
int swap;
int arr[10]={9,8,7,6,5,4,3,2,1};
//sorting the array named arr
for(x=0;x<10;x++)
	{
	for(j=x+1;j<10;j++)
	{
		if(arr[x]>arr[j])
		{
			swap=arr[x];
			arr[x]=arr[j];
			arr[j]=swap;
		}
	}
	
	}
for(x=0;x<10;x++)
{
	printf("%d",arr[x]);
}
return 0;
}
