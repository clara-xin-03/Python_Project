
#principle
while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero.")
    else: 
        break

#interest rate
while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than zero.")
    else:
        break

#time
while True:
    time = int(input("Enter the time in years: "))
    if time < 0:
        print("This can't be less than zero")
    else:
        break

#calculation
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

