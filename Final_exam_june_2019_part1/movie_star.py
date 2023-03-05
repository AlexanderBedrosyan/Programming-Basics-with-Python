budget = float(input())

total_amount = 0

while True:
    name = input()
    if name == "ACTION":
        print(f"We are left with {budget - total_amount:.2f} leva.")
        break

    if len(name) > 15:
        total_amount = total_amount + ((budget - total_amount) * 0.20)
        continue
    else:
        amount = float(input())

    total_amount += float(amount)

    if total_amount > budget:
        print(f"We need {total_amount - budget:.2f} leva for our actors.")
        break
