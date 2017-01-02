sec_per_min = 60
min_per_hour = 60
hour_per_day = 24

seconds_per_hour = sec_per_min * min_per_hour
print(seconds_per_hour)
seconds_per_day = seconds_per_hour * hour_per_day
print(seconds_per_day)
print(seconds_per_day / seconds_per_hour)
print(seconds_per_day // seconds_per_hour)

if seconds_per_day // seconds_per_hour == seconds_per_day / seconds_per_hour:
    print('It`s equal')
else:
    print('Not equal')
