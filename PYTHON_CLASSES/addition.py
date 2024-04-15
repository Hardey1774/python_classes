'''# program for addition table
addition = 0
for i in range(1, 101):
    if str(i).endswith("8")  or str(i).endswith("5"):
        addition += i 

print(addition)
'''

#or 

'''
    # program for addition table
addition = 0
for i in range(8, 101, 10):
        addition += i 

print(addition)
'''

#* Write a program that generates 50 random numbers from 1 through 9. Print out all 50 numbers on the
# same line. Then print out how many fives are generated​.


'''from random import randint
count_of_fives = 0
for i in range(50):
    generated_number = randint(1, 9)
    if generated_number == 5:
        count_of_fives += 1

    print(generated_number, end=",")
print()
print("numbers of times 5 is generated is", count_of_fives)
'''

#* Write a program that randomly generates 10 numbers from 1 to 10 and asks the user to guess each
#number. For each guess print out whether it is right, wrong, or close (within in 1 of the right answer).
# Also keep score, where players score 5 for a correct guess, 2 for a close guess, and -1 for a wrong
# guess. Print the accumulated score after each guess.

'''
from random import randint

score = 0
for i in range(10):
    
    generated_number = randint(1, 10)
    print("Generated number is: ", generated_number)
    guessed_number = int(input("Guess the number: "))

    if generated_number == guessed_number:
        score += 5
        print("You are correct") 
        
   
    elif (guessed_number + 1 == generated_number) or (guessed_number -1 == generated_number): 
        score += 2 
        print("You are close")

    else:
        score -= 1
        print("You are wrong")

    print("Accumulated score = " , score)
    
'''
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










    