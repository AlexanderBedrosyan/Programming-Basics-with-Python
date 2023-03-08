name1 = input()
name2 = input()

points1 = 0
points2 = 0

while True:
    card_one = input()
    if card_one == "End of game":
        print(f"{name1} has {points1} points")
        print(f"{name2} has {points2} points")
        break
    else:
        card_one = int(card_one)
    card_two = int(input())

    if card_one > card_two:
        points1 += (card_one - card_two)
    elif card_two > card_one:
        points2 += (card_two - card_one)
    elif card_one == card_two:
        print(f"Number wars!")
        player1_war = int(input())
        player2_war = int(input())
        if player1_war > player2_war:
            print(f"{name1} is winner with {points1} points")
            break
        elif player2_war > player1_war:
            print(f"{name2} is winner with {points2} points")
            break
