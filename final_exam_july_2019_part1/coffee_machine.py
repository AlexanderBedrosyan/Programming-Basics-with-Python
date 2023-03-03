drinks_type = input()
sugar = input()
drinks_units = int(input())

if drinks_type == "Espresso":
    price = 0.9
    price_norm = 1
    price_sug = 1.20

elif drinks_type == "Cappuccino":
    price = 1
    price_norm = 1.20
    price_sug = 1.60

elif drinks_type == "Tea":
    price = 0.5
    price_norm = 0.6
    price_sug = 0.7

if sugar == "Without":
    total_price = (price - (price * 0.35)) * drinks_units

elif sugar == "Normal":
    total_price = price_norm * drinks_units

elif sugar == "Extra":
    total_price = price_sug * drinks_units

if drinks_type == "Espresso" and drinks_units >= 5:
    total_price = total_price - (total_price * 0.25)

if total_price > 15:
    total_price = total_price - (total_price * 0.20)

print(f"You bought {drinks_units} cups of {drinks_type} for {total_price:.2f} lv.")
