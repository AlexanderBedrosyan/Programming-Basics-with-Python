budget = float(input())
city = input()
season = input()
days = int(input())

dubai = [45000, 40000]
sofia = [17000, 12500]
london = [24000, 20250]

amount_per_day = 0

if season == "Winter":
    if city == "Dubai":
        amount_per_day = dubai[0]
    elif city == "Sofia":
        amount_per_day = sofia[0]
    else:
        amount_per_day = london[0]
else:
    if city == "Dubai":
        amount_per_day = dubai[1]
    elif city == "Sofia":
        amount_per_day = sofia[1]
    else:
        amount_per_day = london[1]

if city == "Dubai":
    amount_per_day *= 0.70
elif city == "Sofia":
    amount_per_day *= 1.25

final_price = amount_per_day * days

if final_price <= budget:
    print(f"The budget for the movie is enough! We have {budget - final_price:.2f} leva left!")
else:
    print(f"The director needs {final_price - budget:.2f} leva more!")
