#Here w is used, not a for append, hence file will be overwritten
emp=open("employee.txt","w")
#print file
#All the existing content of file is replaced by the new overwritten line
emp.write("\n Janny   on Probation")
emp.close()
