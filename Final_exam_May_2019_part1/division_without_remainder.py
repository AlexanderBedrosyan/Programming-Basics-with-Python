n = int(input())

p1 = 0
p2 = 0
p3 = 0

for i in range(0, n):
    number = int(input())

    if number % 2 == 0:
        p1 += 1
    if number % 3 == 0:
        p2 += 1
    if number % 4 == 0:
        p3 += 1

print(f"{(p1 / n) * 100:.2f}%\n"
      f"{(p2 / n) * 100:.2f}%\n"
      f"{(p3 / n) * 100:.2f}%")
