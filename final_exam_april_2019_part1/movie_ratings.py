import sys

n = int(input())

common_rating = 0
max_rating = -sys.maxsize
movie_max_rating = 0
min_rating = sys.maxsize
movie_min_rating = 0

for i in range(1, n + 1):
    movie = input()
    rating = float(input())
    common_rating += rating

    if rating >= max_rating:
        max_rating = rating
        movie_max_rating = movie
    if rating <= min_rating:
        min_rating = rating
        movie_min_rating = movie

print(f"{movie_max_rating} is with highest rating: {max_rating:.1f}")
print(f"{movie_min_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {common_rating / n:.1f}")
