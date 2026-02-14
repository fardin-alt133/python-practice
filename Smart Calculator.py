x=float(input("Enter the first number: "))
y=float(input("Enter the second number: "))
print("Select the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation=int(input("Enter the number corresponding to the operation: "))
if operation==1:
    result=x+y
    print("The result of addition is: ", result)
elif operation==2:
    result=x-y
    print("The result of subtraction is: ", result)
elif operation==3:
    result=x*y
    print("The result of multiplication is: ", result)
elif operation==4:
    if y!=0:
        result=x/y
        print("The result of division is: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation selected.")
    