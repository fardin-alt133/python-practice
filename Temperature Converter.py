x=float(input("Enter the temperature in Celsius: "))
print("chose the conversion you want to do: ")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
choice=int(input("Enter your choice (1 or 2): "))
if choice==1:
    y=(x*9/5)+32
    print(f"{x} degrees Celsius is equal to {y} degrees Fahrenheit.")
elif choice==2:
    y=x+273.15
    print(f"{x} degrees Celsius is equal to {y} degrees Kelvin.")
else:
    print("Invalid choice. Please enter 1 or 2.")
