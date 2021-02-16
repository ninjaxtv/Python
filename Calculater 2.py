num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
op = input("Enter operator: ")


if op == "+":
    print(num1 + num2 + num3)
elif op == "-":
    print(num1 - num2 - num3)
elif op == "/":
    print(num1 / num2 / num3)
elif op == "*":
    print(num1 * num2 * num3)

else:
     print("Invalid operator, you can only enter +,*,-,/")
    
