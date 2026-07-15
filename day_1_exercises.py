# Day 1 Python Practice
# Exercise 1: Print your name, city, and goal

print("Name: Rao Muhammad Noman")
print("City: Lahore")
print("Goal: Become a Python Backend Developer")


# Exercise 2: Take a name as input and print a greeting

user_name = input("Enter your name: ")
print("Welcome,", user_name)

# Exercise 3: Take two numbers and print their sum

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

total = first_number + second_number

print("Sum:", total)

# Exercise 4: Calculate age for the next year

current_age = int(input("Enter your current age: "))
next_year_age = current_age + 1

print("Your age next year:", next_year_age)

# Exercise 5: Take subject marks and print the total

english_marks = float(input("Enter English marks: "))
math_marks = float(input("Enter Math marks: "))
computer_marks = float(input("Enter Computer marks: "))

total_marks = english_marks + math_marks + computer_marks

print("Total marks:", total_marks)

# Exercise 6: Calculate total bill using product price and quantity

product_price = float(input("Enter product price: "))
product_quantity = int(input("Enter product quantity: "))

total_bill = product_price * product_quantity

print("Total bill:", total_bill)

# Exercise 7: Convert Celsius temperature to Fahrenheit

celsius_temperature = float(input("Enter temperature in Celsius: "))

fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit_temperature)

# Exercise 8: Calculate the area of a rectangle

rectangle_length = float(input("Enter rectangle length: "))
rectangle_width = float(input("Enter rectangle width: "))

rectangle_area = rectangle_length * rectangle_width

print("Rectangle area:", rectangle_area)

# Exercise 9: Calculate monthly and yearly salary

monthly_salary = float(input("Enter your monthly salary: "))

yearly_salary = monthly_salary * 12

print("Monthly salary:", monthly_salary)
print("Yearly salary:", yearly_salary)

# Exercise 10: Calculate the average of three numbers

average_number_one = float(input("Enter first average number: "))
average_number_two = float(input("Enter second average number: "))
average_number_three = float(input("Enter third average number: "))

average_total = (
    average_number_one
    + average_number_two
    + average_number_three
)

average_result = average_total / 3

print("Average total:", average_total)
print("Average result:", average_result)

# Exercise 11: Calculate marks percentage

obtained_marks = float(input("Enter obtained marks: "))
maximum_marks = float(input("Enter maximum marks: "))

marks_percentage = (obtained_marks / maximum_marks) * 100

print("Marks percentage:", marks_percentage)

# Exercise 12: Calculate discount amount and final price

original_price = float(input("Enter original product price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount_amount = original_price * discount_percentage / 100
final_price = original_price - discount_amount

print("Discount amount:", discount_amount)
print("Final price:", final_price)

# Exercise 13: Calculate simple interest and final amount

principal_amount = float(input("Enter principal amount: "))
annual_interest_rate = float(input("Enter annual interest rate: "))
time_in_years = float(input("Enter time in years: "))

simple_interest = (
    principal_amount
    * annual_interest_rate
    * time_in_years
    / 100
)

final_amount = principal_amount + simple_interest

print("Simple interest:", simple_interest)
print("Final amount:", final_amount)

# Exercise 14: Convert hours into minutes and seconds

hours = float(input("Enter number of hours: "))

minutes = hours * 60
seconds = hours * 3600

print("Minutes:", minutes)
print("Seconds:", seconds)

# Exercise 15: Calculate distance using speed and time

travel_speed = float(input("Enter travel speed in km/h: "))
travel_time = float(input("Enter travel time in hours: "))

travel_distance = travel_speed * travel_time

print("Travel distance in kilometers:", travel_distance)