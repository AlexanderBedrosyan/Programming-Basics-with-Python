best_movie = 0
best_movie_name = ""
counter_smaller = 0
counter_upper = 0
movies_counter = 0

while True:
    movie = input()
    if movie == "STOP":
        break

    movies_counter += 1
    total_movie = 0

    for index, digit in enumerate(str(movie)):
        if 65 <= ord(digit) <= 90:
            counter_upper += 1
            total_movie += ord(digit)
        elif 97 <= ord(digit) <= 122:
            counter_smaller += 1
            total_movie += ord(digit)
        else:
            total_movie += ord(digit)

    total_movie -= (((2 * len(movie)) * counter_smaller) + (len(movie) * counter_upper))

    counter_upper = 0
    counter_smaller = 0

    if total_movie > best_movie:
        best_movie = total_movie
        best_movie_name = movie
    if movies_counter == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {best_movie_name} with {best_movie} ASCII sum.")
