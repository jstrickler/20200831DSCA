from getpass import getpass, getuser

user_name = input("Enter your name: ")
raw_quantity = input("Enter quantity: ")
password = getpass("Enter password: ")

quantity = int(raw_quantity)

print(f"{user_name} wants {quantity} jelly bean(s) (password is {password})")

print("User name is:", getuser())  #  LOGNAME, USER, LNAME, USERNAME