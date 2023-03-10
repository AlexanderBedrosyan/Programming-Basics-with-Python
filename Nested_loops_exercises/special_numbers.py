N = int(input())

numbers_list = []

for i in range(1111, 10000):
    check = [*map(int, str(i))]
    if 0 in check:
        continue
    elif N % check[0] == 0 and N % check[1] == 0 and N % check[2] == 0 and N % check[3] == 0:
        numbers_list.append(i)

print(*numbers_list)
