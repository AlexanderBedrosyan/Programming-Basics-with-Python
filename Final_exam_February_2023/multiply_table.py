number = int(input())

m = 0
middle = 0
last = 0

for index, digit in enumerate(str(number)):
    if index == 2:
        m = int(digit)
    if index == 1:
        middle = int(digit)
    if index == 0:
        last = int(digit)

for i in range(1, m + 1):
    for s in range(1, middle + 1):
        for z in range(1, last + 1):
            print(f"{i} * {s} * {z} = {i * s * z};")
