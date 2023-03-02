points = 0
winner_name = ""

total_points = 0

while True:
    name = input()

    if name == "Stop":
        break

    for i in range(0, len(name)):
        n = int(input())
        if i == 0:
            points = 0
        if ord(name[i]) == n:
            points += 10
        else:
            points += 2

        if total_points <= points:
            total_points = points
            winner_name = name

print(f"The winner is {winner_name} with {total_points} points!")
