#* Write a program that asks the user to enter a string. If the string is at least five characters long, then
#create a new string that consists of the first five characters of the string along with three asterisks at
# the end. Otherwise add enough exclamation points (!) to the end of the string in order to get the
# length up to five.

input_character = str(input("Enter a character: "))
a = 5 - len(input_character)
if len(input_character) >= 5:
   print("The new string is: ", input_character[ :5] + ("***"))
elif len(input_character ) < 5:
   print("New string is: ", input_character + (("!")*a))
