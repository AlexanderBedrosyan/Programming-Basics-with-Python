people = int(input())
season = input()

price = 0

if people <= 5:
    if season == "spring":
        price = 50
    elif season == "summer":
        price = 48.50
    elif season == "autumn":
        price = 60
    elif season == "winter":
        price = 86
elif people > 5:
    if season == "spring":
        price = 48
    elif season == "summer":
        price = 45
    elif season == "autumn":
        price = 49.50
    elif season == "winter":
        price = 85

total_price = price * people

if season == "summer":
    total_price *= 0.85
if season == "winter":
    total_price *= 1.08

print(f"{total_price:.2f} leva.")
