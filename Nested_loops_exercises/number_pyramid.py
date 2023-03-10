n = int(input())
counter = 0


for i in range(1, n + 1):
    for z in range(1, i + 1):
        counter += 1
        if counter == n:
            print(f"{counter}")
            exit()
        if z == i:
            print(f"{counter}")
            break

        print(f"{counter}", end=" ")
