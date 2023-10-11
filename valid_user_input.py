username = input("Enter a username : ")

if len(username) > 12:
    print("username cannot be more than 12 characters.")
elif username.find(" ") > 0:
    print("username cannot contain space")
elif not username.isalpha():
    print("username must not contain digits")
