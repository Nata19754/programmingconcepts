#In this problem you must create functions to solve each criterion.

#The first criteria is to solve the area of a circle.
# The function will have the parameter of radius and the function will calculate the area of the circle with the radius and Pi.
# Then it will return the area of the circle.
# Return the value, not a print statement.
# Parameters for the function will be pi and radius.


#Function 1 to calculate the area of a circle and rounds 2 decimal places

def areaOfCircle(radius,pi=3.1416):
    area = pi * radius ** 2
    area = round(area,2)
    return area

print("Test Data - Area of Circle")
area1=areaOfCircle(10, 3.1416)
area2=areaOfCircle(6,3.1416)
area3=areaOfCircle(24,3.1416)
area4=areaOfCircle(2,3.1416)
area5=areaOfCircle(1,3.1416)

print(area1)
print(area2)
print(area3)
print(area4)
print(area5)

#Function 2 to calculate total money due with taxes included

def totalMoneyDue(money,taxRate):
    taxRate = taxRate / 100
    total = money +(money * taxRate)
    return total

print("Test Data- Taxes")
total1=totalMoneyDue(20,taxRate=6)
total2=totalMoneyDue(54,taxRate=4)
total3=totalMoneyDue(68,taxRate=8)

print(total1)
print(total2)
print(total3)

#Function 3 converts Fahrenheit to Celsius

def fahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit -32) * (5/9)
    celsius = round(celsius,4)
    return celsius

print("Test Data- Temperature")
temp1=fahrenheitToCelsius(32)
temp2=fahrenheitToCelsius(80)
temp3=fahrenheitToCelsius(73)
temp4=fahrenheitToCelsius(42)

print(temp1)
print(temp2)
print(temp3)
print(temp4)



