import math

missing_days = int(input())
food_kg = int(input())
first_deer = float(input())
second_deer = float(input())
third_deer = float(input())

total_needed_food = missing_days * (first_deer + second_deer + third_deer)

if total_needed_food <= food_kg:
    print(f"{math.floor(food_kg - total_needed_food)} kilos of food left.")
else:
    print(f"{math.ceil(total_needed_food - food_kg)} more kilos of food are needed.")
