budget = float(input())
number_series = int(input())

names_list = ["Thrones", "Lucifer", "Protector", "TotalDrama", "Area"]
discount_list = [0.50, 0.60, 0.70, 0.80, 0.90]

total_sum = 0

for i in range(1, number_series + 1):
    name = input()
    sum = float(input())

    for m in range(0, len(names_list)):
        if name == names_list[m]:
            sum *= discount_list[m]

    total_sum += sum

if total_sum <= budget:
    print(f"You bought all the series and left with {budget - total_sum:.2f} lv.")
else:
    print(f"You need {total_sum - budget:.2f} lv. more to buy the series!")
