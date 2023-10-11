
name = input("Enter your full name: ")
phone_num = input("Enter your phone number: ")

result = len(name)
result = name.find("o")
result = name.rfind("q")
result = name.find("e")

name = name.capitalize()
name = name.upper()
name = name.lower()

result = name.isdigit()
result = name.isalpha()

print(name)


result = phone_num.count("-")
result = phone_num.replace("-", " ")
print(result)

help(str)