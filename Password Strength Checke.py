x = input("Enter your password: ")

if len(x) < 6:
    print("Your password is weak")

elif any(char.isdigit() for char in x):
    print("Your password is medium")

elif any(char.isupper() for char in x):
    print("Your password is strong")

else:
    print("Password condition not matched")
