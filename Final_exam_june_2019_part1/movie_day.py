day_time = int(input())
numbers_project = int(input())
time_projects1 = int(input())

full_day_time = day_time * 0.85
needed_time = numbers_project * time_projects1

if full_day_time >= needed_time:
    print(f"You managed to finish the movie on time! You have {round(full_day_time - needed_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(needed_time - full_day_time)} minutes.")
