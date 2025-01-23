"""
Mod 2 Demo
Tristan Bickel
Date: 2025-01-20
"""
# Single line comment
"""multi line comment"""
FEDERAL_TAX_RATE = 0.05
PI = 3.1415967
absolute_value = abs(-12)

print('absolute value:', absolute_value)
print('Absolute value is:',abs(-15))

name = "mike" # str
age = 25 # int
celery = 67239.21 #float
is_employed = True #bool

print(type(name))
print(type(age))
print(type(float))
print(type(is_employed))

age = 25
current_salary = 67293.21
age_and_salary = age + current_salary
print(age_and_salary)
#Function embedded within another function. 
# print('absolute value:', abs(-15))
 
months_old = "11"
years_old = 25
age = float(years_old) + (float(months_old)/12)
print("age as a float:", age)

age = int(age)
print(age)

original_string = "hello, world!"
original_string = original_string.capitalize()
print(original_string)

width = 20
fill_character = "-"
centeredstring = original_string.center(width,fill_character)
cooktstring = original_string.center(35,'Z')
print(cooktstring)
print(centeredstring)

is_hello = original_string.startswith("Hello")
print(is_hello)
is_world = original_string.endswith("world!")
print(is_world)
is_cookt = original_string.__contains__("z")
print(is_cookt)

print(original_string)
upper_case = original_string.upper()
print(upper_case)

new_string = "hello world, hello python."
print(new_string)
replaced_string = new_string.replace("hello", 'hi')
print(replaced_string)
random_string = new_string.replace("python", "SCREAMING") +new_string.replace("world","unimaginable horrors")
print(random_string)