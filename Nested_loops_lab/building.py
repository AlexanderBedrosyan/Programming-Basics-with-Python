n = int(input())
m = int(input())
result = 0

for i in range(n, 0, -1):
    for z in range(0, m):
        number = i * 10 + z
        if i == n:
            result = f"L{number}"
        elif i % 2 != 0:
            result = f"A{number}"
        else:
            result = f"O{number}"

        if z == m - 1:
            print(result)
            result = 0
            continue

        print(result, end=" ")

    if i == 1:
        break
