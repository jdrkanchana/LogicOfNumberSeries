x=[]
arr=[]
x=6249192251196744265747423553491949349698352
z=x
length=len(str(x))+1
factor=14*(length-13)
temp=1
count=1
m_count=0
start=0
i=0
for y in range(start,factor):
    if(count<=13):
        rem=int(x%10)
        temp=temp*rem
        count=count+1
        x=x/10
    else:
        arr.append(temp)
        count=1
        start=start+1
        length=length+1
        temp=1
        x=z
        x=int(x/10)
        m_count=m_count+1
          
print(arr)
