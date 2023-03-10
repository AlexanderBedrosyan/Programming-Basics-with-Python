n = int(input())
z = int(input())

list_of_numbers = []

for i in range(n, z + 1):
    odd_sum = 0
    even_sum = 0
    for digits, index in enumerate(str(i)):
        if digits % 2 != 0:
            odd_sum += int(index)
        else:
            even_sum += int(index)

    if even_sum == odd_sum:
        list_of_numbers.append(i)

print(*list_of_numbers)
