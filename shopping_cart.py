foods = []
prices = []
total = 0

#input food & price
while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input("Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

#print all food
for food in foods:
    print(food, end=" ")

#adding prices into total
for price in prices:
    total += price

#to skip one line
print("testing1")

print(f"Your total is : ${total}")
