z=1
b=600851475143 
a=2
x=2
while(b!=1):
    y=a%x
    a=a+1
    if y==0:
    	rem=b%x
    	if(rem==0):
    		b=b/x
    		if(b==1):
    			break
    x=x+1
    final=x
print(final,'is a largest multiple of given number 600851475143 ')
