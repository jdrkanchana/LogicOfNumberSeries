#include <stdio.h>
#include <math.h>
int main()
{
int num,sum,a,p,y,b,i;
int Grandtotal=0;
int array[6];

for (b=2;b<1000000;b++)
{ 
   num=b;
   a=b;
   sum=0,p=0;
  // printf("%d",num);
  
  for(i=0;i<6;i++){
  	array[i]=a%10;
  //	printf("%d",array[i]);
  	a=a/10;
  	p=pow(array[i],5);
  	sum=sum+p;
  
  }
   
        			
    if (sum==num){
        printf("%d is an armstrong number",num);
        Grandtotal=Grandtotal+num;
        }
}
printf("the total is %d",Grandtotal);
return 0;
}
