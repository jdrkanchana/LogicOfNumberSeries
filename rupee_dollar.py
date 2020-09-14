#run in python 3
print("A program to convert the dollar to rupees and rupee to dollar")
print("If you want to convert dollar to rupee, type d")
print("If you want to convert rupee to dollar, type r")
user_input=input()

if (user_input=="d"):
	print("Enter the dollar value to convert")
	dollar=input()
	rup_value=float(dollar)/185.00
	print(rup_value)

elif user_input=="r":
	print("Enter the rupee value to convert")
	rupee=input()
	dollar_value=float(rupee)*185.00
	print(dollar_value)
