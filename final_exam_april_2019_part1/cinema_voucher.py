voucher_amount = int(input())

rest_amount = voucher_amount
movie_amount = 0
tickets = 0
other_stuffs = 0

while True:
    movie = input()
    movie_list = list(movie)

    if movie == "End":
        break

    if len(movie) > 8:
        movie_amount = int(ord(movie_list[0])) + int(ord(movie_list[1]))
        if movie_amount <= rest_amount:
            tickets += 1
        else:
            break
    elif len(movie) <= 8:
        movie_amount = ord(movie_list[0])
        if movie_amount <= rest_amount:
            other_stuffs += 1
        else:
            break

    rest_amount -= movie_amount

print(tickets)
print(other_stuffs)
