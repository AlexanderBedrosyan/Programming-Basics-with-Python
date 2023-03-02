points = 0
winner_word = ""
checking_string = "aeiouyAEIOUY"

total_points = 0

while True:
    word = input()

    if word == "End of words":
        break

    for i in range(0, len(word)):
        points += ord(word[i])

        if i == (len(word) - 1) and (word[0] not in checking_string):
            points /= len(word)
            if total_points <= points:
                total_points = points
                winner_word = word
                points = 0
            else:
                points = 0
        elif i == (len(word) - 1) and (word[0] in checking_string):
            points *= len(word)
            if total_points <= points:
                total_points = points
                winner_word = word
                points = 0
            else:
                points = 0

print(f"The most powerful word is {winner_word} - {round(total_points)}")
