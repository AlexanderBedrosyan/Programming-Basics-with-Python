from math import floor

tournaments = int(input())
points = int(input())
starting_points = 0

winning_counter = 0

for i in range(1, tournaments + 1):
    stage = input()

    if stage == "W":
        starting_points += 2000
        winning_counter += 1
    elif stage == "F":
        starting_points += 1200
    elif stage == "SF":
        starting_points += 720

print(f"Final points: {starting_points + points}")
print(f"Average points: {floor(starting_points / tournaments)}")
print(f"{(winning_counter / tournaments) * 100:.2f}%")
