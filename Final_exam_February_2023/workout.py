from math import ceil

n = int(input())
first_day = float(input())
total_range = first_day

for i in range(1, n + 1):
    growing = int(input())
    new_range = first_day * (1 + growing / 100)
    first_day = new_range

    total_range += new_range

if total_range >= 1000:
    print(f"You've done a great job running {ceil(total_range - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_range)} more kilometers")
