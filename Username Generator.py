x=input("Enter your first name: ")
y=input("Enter your birth year: ")
first_letter=x.split()[0]
user_name=first_letter[0:3].lower()+y
print("Your username is: ",user_name)