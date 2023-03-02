movies = []
movie_tickets = []
total_movie_sits = []

total_tickets = 0
standard = 0
kid = 0
student = 0
tickets_per_movie = 0
total_movies = 0

while True:
    movie = input()
    movies.append(movie)
    if movie == "Finish":
        break
    total_movies += 1
    n = int(input())
    total_movie_sits.append(n)

    while True:
        type_ticket = input()
        if type_ticket == "standard":
            standard += 1
            tickets_per_movie += 1
        elif type_ticket == "student":
            student += 1
            tickets_per_movie += 1
        elif type_ticket == "kid":
            kid += 1
            tickets_per_movie += 1

        if (type_ticket == "End") or (tickets_per_movie == n):
            movie_tickets.append(tickets_per_movie)
            tickets_per_movie = 0
            break

total_tickets = student + standard + kid

for i in range(0, total_movies):
    print(f"{movies[i]} - {(movie_tickets[i] / total_movie_sits[i]) * 100:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid / total_tickets) * 100:.2f}% kids tickets.")
