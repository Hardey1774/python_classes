# Write a program that checks if a number exists in a set of numbers. You will take inputs for the number to find and the numbers to find it from.

# main_variable = input("Enter some numbers: ")
# a = input("Number to check: ")

# print(a in main_variable)
'''---------------------------------------------------------------------------
# number_of_seconds = int(input("Enter number of second: "))
# number_of_minutes = (number_of_seconds//60)
# number_remain = (number_of_seconds % 60)
# print(number_of_minutes,"minutes", number_remain, "seconds" )
'''
'''
# Write a program that takes height in inches and prints how many feet and how many inches we have in the inputted inches. There are 12 inches in one foot.

# height = int(input("What is your height in inches: "))
# height_feet = height // 12
# remaining_inches = height_feet % 12

# print("Your height is", height_feet, "feet and", remaining_inches, "inches")
'''
'''
#Create a program that calculates the area of a rectangle given its length and width in inches.

# a = int(input('Enter the length of the rectangle in inches: '))
# b = int(input('Enter the width of the rectangle inches: '))
# area = a * b
# print("Total area = ", area,"inches Square")
'''

#Create a program to convert a given distance in miles to kilometers. 
#Hint: 1 mile is equal to 1.60934 kilometers)
miles = int(input("Enter value in miles: ")) 
kilometre = miles * 1.60934

print(kilometre,"Km")

#Write a program to calculate the total cost of a meal at a restaurant including tax and tip, given the base cost of the meal
cost_of_meal = int(input("Enter the cost of the meal: "))
tax = 0.05 * cost_of_meal
tip = int(input("Enter the value of tips given: "))
print('N',cost_of_meal + tax + tip)
