# Q2. Write a fuction to add two numbers


def doMath(num1, sign, num2):
	if(sign == "-"):
		return num2-num1
	if(sign == "+"):
		return num1+num2
	if(sign == "*"):
		return num1*num2
	if(sign == "/"):
		return num1//num2
	if(sign == "**"):
		return num1**num2
	else:
		return "Please enter valid input"

num1 = int(input("Input  first number\n"))
sign = input("Input  sign\n")
num2 = int(input("Input  second number\n"))

print(doMath(num1,sign,num2))