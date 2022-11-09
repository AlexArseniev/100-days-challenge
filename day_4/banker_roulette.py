import random

names = input().split(', ')
person_to_pay = random.randint(0, len(names) - 1)
print(f"{names[person_to_pay]} is going to buy the meal today!")
