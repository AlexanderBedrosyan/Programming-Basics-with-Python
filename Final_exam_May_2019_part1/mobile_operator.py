one_year = [9.98, 18.99, 25.98, 35.99]
two_year = [8.58, 17.09, 23.59, 31.79]
package = ["Small", "Middle", "Large", "ExtraLarge"]

amount = 0

period = input()
type_package = input()
add_net = input()
months = int(input())

if period == "one":
    for i in range(0, len(package)):
        if package[i] == type_package:
            amount = one_year[i]
        else:
            continue
elif period == "two":
    for i in range(0, len(package)):
        if package[i] == type_package:
            amount = two_year[i]
        else:
            continue

if add_net == "yes":
    if amount <= 10:
        amount += 5.50
    elif 10 < amount <= 30:
        amount += 4.35
    else:
        amount += 3.85

total_amount = amount * months

if period == "two":
    total_amount *= 0.9625

print(f"{total_amount:.2f} lv.")
