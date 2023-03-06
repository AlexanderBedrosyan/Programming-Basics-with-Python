period = int(input())
hours = int(input())

total = 0
day = 0

for i in range(1, period + 1):
    for h in range(1, hours + 1):
        if i % 2 == 0 and h % 2 != 0:
            total += 2.50
            day += 2.50
        elif i % 2 != 0 and h % 2 == 0:
            total += 1.25
            day += 1.25
        else:
            total += 1
            day += 1

        if h == hours and i != period:
            print(f"Day: {i} - {day:.2f} leva")
            day = 0
        elif h == hours and i == period:
            print(f"Day: {i} - {day:.2f} leva")
            print(f"Total: {total:.2f} leva")
