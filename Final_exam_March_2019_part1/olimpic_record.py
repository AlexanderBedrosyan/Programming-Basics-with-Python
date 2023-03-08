minutes_record = int(input())
seconds_control = int(input())
meters = float(input())
seconds_meters = int(input())

record_seconds = minutes_record * 60 + seconds_control
discount = (meters / 120) * 2.5
distance_seconds = (meters / 100) * seconds_meters
total_time = distance_seconds - discount

if total_time <= record_seconds:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(record_seconds - total_time):.3f} second slower.")
