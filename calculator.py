num1 = int(input("Enter a number: "))
num2= int(input("Enter a number: "))
operator= input("enter + - * / ** fac mod ... ")

if operator == "-":
    result = num1 - num2
    print(f"result = {result}")
result = 0

if operator == '+':
    result = num1 + num2
    print(f"result = {result}")

elif operator =="*":
    result = num1 * num2
    print(f"result = {result}")
    