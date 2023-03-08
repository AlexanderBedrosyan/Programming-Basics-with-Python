win = 0
lost = 0

while True:
    name = input()

    if name == "End of tournaments":
        print(f"{(win / (win + lost)) * 100:.2f}% matches win")
        print(f"{(lost / (win + lost)) * 100:.2f}% matches lost")
        exit()

    n = int(input())

    for i in range(1, n + 1):
        desi_team = int(input())
        enemy = int(input())

        if desi_team > enemy:
            win += 1
            print(f"Game {i} of tournament {name}: win with {desi_team - enemy} points.")
        if desi_team < enemy:
            print(f"Game {i} of tournament {name}: lost with {enemy - desi_team} points.")
            lost += 1
