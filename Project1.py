# Weather Severity Project
# Natally Chaves
# The program will use a sentinel controlled loop (Do not use break). The program will count the number of days entered, and that count is included in the output.
# The program will output the average rain, and average wind.  It will also output the number of days for which data were entered, and the weather severity.


rain_total = 0
wind_total = 0
count = 0

while True:
    # read a whole line, split into parts
    data = input().split()

    # sentinel check
    if len(data) == 1 and data[0] == "-1.0":
        break

    # convert rain and wind to numbers
    rain = float(data[0])
    wind = float(data[1])

    # add to totals
    rain_total += rain
    wind_total += wind
    count += 1

# avoid division error if no data
if count > 0:
    avg_rain = rain_total / count
    avg_wind = wind_total / count
else:
    avg_rain = 0
    avg_wind = 0

# weather severity formula
severity = (avg_rain * 10) + avg_wind

# print results
print(f"The average rain is {avg_rain:.1f} inches")
print(f"The average wind is {avg_wind:.1f} mph")
print(f"The weather severity for these {count} readings is: {severity:.1f}")
