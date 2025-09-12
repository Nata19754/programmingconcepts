# In this problem you need to calculate the total amount of an electric bill. Given an integer value representing the number of kilowatt-hours used, calculate the total amount owed using the following rates:
# 7.633 cents for the first 1000 hours used
# 9.259 cents for any hours used over 1000 hours.
from selectors import SelectSelector

#Prompts users for number of kilowatt-hours used
kwh= int(input("Enter the KW hours used:"))
#If kwh is less than or equal to 1000 then multiply kwh amount entered by 0.07633
if  kwh <= 1000:
    amount = kwh * 0.07633
    print(f"Amount owed is ${amount}")
#Else pring
else:
    amount = 1000 * 0.07633 + (kwh - 1000) * 0.09259
    print(f"Amount owed is ${amount}")
