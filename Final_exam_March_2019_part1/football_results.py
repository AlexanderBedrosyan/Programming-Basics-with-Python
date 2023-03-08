results = []

results.append(input())
results.append(input())
results.append(input())

w = 0
d = 0
l = 0

for i in range(0, 3):
    index = results[i]
    if index[0] > index[2]:
        w += 1
    elif index[0] == index[2]:
        d += 1
    elif index[0] < index[2]:
        l += 1

print(f"Team won {w} games.\nTeam lost {l} games.\nDrawn games: {d}")
