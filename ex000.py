# Lecture 4

# First commands
print('Hello, world!')
print('7' + '4')
print(7+4)

# Using variables
var = 7 + 4
print(var)

name = 'Gabriel'
age = 31
weight = 54
print(name, age, weight)

# Using interaction
name = input("What's your name?")
age = input("What's your age?")
weight = input("What's your weight?")
print(name, age, weight)

# Challenge 1 - Write a script that takes the username and shows a welcome message with it
username = input("What's your name?")
print('Welcome,', username, '!')

# Challenge 2 - Write a script that takes the day, month and year of birth of the username and shows a message with
# the formatted date
birth_day = input('What day were you born?')
birth_month = input('What month were you born?')
birth_year = input('What year were you born?')
print('Your date of birth is', birth_day, '/', birth_month, '/', birth_year)

# Challenge 3 - Write a script that takes two numbers and shows the sum of those numbers.
num_1 = float(input('Type the first number:'))
num_2 = float(input('Type the second number:'))
print(num_1 + num_2)
