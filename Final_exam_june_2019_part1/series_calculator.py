from math import floor

serial = input()
seasons = int(input())
episodes = int(input())
time_cost = float(input())

time_per_episode = time_cost + (0.20 * time_cost)
final_episode = time_per_episode + 10

total_time_needed = (time_per_episode * (episodes - 1) + final_episode) * seasons

print(f"Total time needed to watch the {serial} series is {floor(total_time_needed)} minutes.")
