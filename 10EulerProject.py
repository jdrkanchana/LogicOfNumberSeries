#include<stdio.h>
#include <math.h>
int aprime(int num, int prime,double float_result);    

int main(){
	int num,prime,i;
	prime=1;
	double float_result;
    float_result = sqrt(num);

	for (num = 11; num < 2000000; num=num+2)
  	{

    prime=aprime(num,prime,float_result); 

  	}
	
	return 0;
}



int aprime(int num, int prime,double float_result)
{ 
	static int x=0;
	static long sum=17;
    int int_result,a,y;
    int array[600000];
    int array_prime[500000];
    y=0,prime=1;
    int_result=float_result;
    if((num%3==0)||(num%5==0)){
    	prime=0;
  
    }
    else if((num%7==0)||(num%2==0)){
    	prime=0;
    	
    }
    else if(float_result==int_result){
    	prime=0;
    }

    if(prime==1)
    {
		array[x]=num;
		x++;
	}

	for (a = 0; a < 250000; a++)
	{
		if(array[a]!=0){
			if((num%array[a]==0)&&(num!=array[a]))
			{
				prime=0;
			}
		}
	}
	if(prime==1)
    {
		array_prime[y]=num;
		y++;
		sum=sum+num;
	}
	printf("%ld\n",sum );

    return prime;
}
