budget = float(input())

counter = 0
total_amount = 0

while True:
    product = input()
    if product == "Stop":
        print(f"You bought {counter} products for {total_amount:.2f} leva.")
        break

    price = float(input())

    counter += 1

    if counter % 3 == 0:
        price *= 0.50

    total_amount += price

    if total_amount > budget:
        print(f"You don't have enough money!\nYou need {total_amount - budget:.2f} leva!")
        break
