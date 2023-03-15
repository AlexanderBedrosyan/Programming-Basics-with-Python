n1 = int(input())
n2 = int(input())
magic_number = int(input())
counter = 0
result = 0

for i in range(n1, n2 + 1):
    if result != 0:
        break
    for c in range(n1, n2 + 1):
        counter += 1
        if i + c == magic_number:
            result = f"({i} + {c} = {magic_number})"
            break

if result != 0:
    print(f"Combination N:{counter} {result}")
else:
    print(f"{counter} combinations - neither equals {magic_number}")
