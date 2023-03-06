diesel = 2.10
tour_guide = 100
discount = 0

budget = float(input())
diesel_needed = float(input())
day = input()

if day == "Saturday":
    discount = 0.90
else:
    discount = 0.80

total_price = (diesel * diesel_needed + tour_guide) * discount

if total_price <= budget:
    print(f"Safari time! Money left: {budget - total_price:.2f} lv.")
else:
    print(f"Not enough money! Money needed: {total_price - budget:.2f} lv.")
