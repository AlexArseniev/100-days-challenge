pizza_ingredients = {"S": 15,
                     "M": 20,
                     "L": 25,
                     "PS": 2,
                     "PM": 3,
                     "PL": 3,
                     "Cheese": 1}

total_price = 0
size = input("What pizza size do you want?: ")
pepperoni = input("Do you want pepperoni?: ")
extra_cheese = input("Do you want extra cheese?: ")

total_price += pizza_ingredients[size]

if pepperoni == "Y":
    total_price += pizza_ingredients[f"P{size}"]

if extra_cheese == "Y":
    total_price += pizza_ingredients["Cheese"]

print(f"Your final bill is: ${total_price}")
