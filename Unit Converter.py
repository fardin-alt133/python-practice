print("Welcome to the Unit Converter!"
      "\nPlease select the type of conversion you would like to perform:")
print("1. Length")
print("2. Weight")
print("3. Temperature")
print("4. Volume")
print("5. Time")
conversion_type = input("Enter the number corresponding to your choice: ")
if conversion_type == "1":
    print("You have selected Length conversion.")
    print("Available conversions:")
    print("1. Meters to Feet")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")
    length_conversion = input("Enter the number corresponding to your choice: ")
    if length_conversion == "1":
        meters = float(input("Enter the length in meters: "))
        feet = meters * 3.28084
        print(f"{meters} meters is equal to {feet} feet.")
    elif length_conversion == "2":
        feet = float(input("Enter the length in feet: "))
        meters = feet / 3.28084
        print(f"{feet} feet is equal to {meters} meters.")
    elif length_conversion == "3":
        kilometers = float(input("Enter the length in kilometers: "))
        miles = kilometers * 0.621371
        print(f"{kilometers} kilometers is equal to {miles} miles.")
    elif length_conversion == "4":
        miles = float(input("Enter the length in miles: "))
        kilometers = miles / 0.621371
        print(f"{miles} miles is equal to {kilometers} kilometers.")
    else:
        print("Invalid choice for Length conversion.")
elif conversion_type == "2":
    print("You have selected Weight conversion.")
    print("Available conversions:")
    print("1. Kilograms to Pounds")
    print("2. Pounds to Kilograms")
    weight_conversion = input("Enter the number corresponding to your choice: ")
    if weight_conversion == "1":
        kilograms = float(input("Enter the weight in kilograms: "))
        pounds = kilograms * 2.20462
        print(f"{kilograms} kilograms is equal to {pounds} pounds.")
    elif weight_conversion == "2":
        pounds = float(input("Enter the weight in pounds: "))
        kilograms = pounds / 2.20462
        print(f"{pounds} pounds is equal to {kilograms} kilograms.")
    else:
        print("Invalid choice for Weight conversion.")
elif conversion_type == "3":
    print("You have selected Temperature conversion.")
    print("Available conversions:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    temperature_conversion = input("Enter the number corresponding to your choice: ")
    if temperature_conversion == "1":
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")
    elif temperature_conversion == "2":
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius} degrees Celsius.")
    else:
        print("Invalid choice for Temperature conversion.")
elif conversion_type == "4":
    print("You have selected Volume conversion.")
    print("Available conversions:")
    print("1. Liters to Gallons")
    print("2. Gallons to Liters")
    volume_conversion = input("Enter the number corresponding to your choice: ")
    if volume_conversion == "1":
        liters = float(input("Enter the volume in liters: "))
        gallons = liters * 0.264172
        print(f"{liters} liters is equal to {gallons} gallons.")
    elif volume_conversion == "2":
        gallons = float(input("Enter the volume in gallons: "))
        liters = gallons / 0.264172
        print(f"{gallons} gallons is equal to {liters} liters.")
    else:
        print("Invalid choice for Volume conversion.")
elif conversion_type == "5":
    print("You have selected Time conversion.")
    print("Available conversions:")
    print("1. Seconds to Minutes")
    print("2. Minutes to Seconds")
    time_conversion = input("Enter the number corresponding to your choice: ")
    if time_conversion == "1":
        seconds = float(input("Enter the time in seconds: "))
        minutes = seconds / 60
        print(f"{seconds} seconds is equal to {minutes} minutes.")
    elif time_conversion == "2":
        minutes = float(input("Enter the time in minutes: "))
        seconds = minutes * 60
        print(f"{minutes} minutes is equal to {seconds} seconds.")
    else:
        print("Invalid choice for Time conversion.")
else:
    print("Invalid choice for conversion type.")
    