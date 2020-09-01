#Start of comments
# x   y     sumTot
# 0   1     1     ColA
# 1   1     2     ColB
# 1   2     3     ColC
# 2   3     5     ColD
#The sum denotes how the fibonacci series go on 1,1,2,3,5,8,13,21 and so forth
#Its understood that eventually the sumTot in ColB(previous column) is the y of Col C (next column)
#Its understood that x in ColB, is the y in (previous column)ColA
#End of logic explanation

#Here I m taking user input as a, on the fibonacci term user want to stop printing the series
a = input("Please enter a string:\n")
x=0
y=1
print(x,y)
sum=0
count=0
while (count != a):
    sum=x+y
    x=y
    y=sum
    count=count+1
    print(sum)
