# In this problem you need to calculate the total amount of an electric bill. Given an integer value representing the number of kilowatt-hours used, calculate the total amount owed using the following rates:
# 7.633 cents for the first 1000 hours used
# 9.259 cents for any hours used over 1000 hours.

RATE_FIRST_1000 = 0.07633
RATE_OVER_1000 = 0.09259
THRESHOLD = 1000

while True:
    try:
        kwh = int(input(" Enter the KW hours used: "))
        if kwh > 0:
            break
        print("Please enter a number greater than 0")
    except ValueError:
            print(" Please enter a whole number ")

if kwh <= THRESHOLD:
    total =kwh * RATE_FIRST_1000
else:
    total = THRESHOLD * RATE_FIRST_1000 + (kwh - THRESHOLD) * RATE_OVER_1000
print(" Amount owed is ${}".format(total))
