age = int(input("Enter your age: "))

if age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't born yet!")
else:
    print("You must be 18+ to sign up")

################################

response = input("Would you like food? (Y/N): ")

if response == "Y":
    print("Have some food!")
else: 
    print("No food for you!")

name = input("Enter your name: ")

if name == "":
    print("You did not type your name!")
else:
    print(f"Hello {name}")

###############################

for_sale = False

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = False
if not online:
    print("The user is online")
else:
    print("The user is offline")