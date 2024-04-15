'''
#Write a program that adds up all the numbers from 1 through 100 and prints the result​
for i in randint (0, 100, 1):
    i += 1
    print( i  )
'''

# program for addition table
addition = 0
for i in range(1, 101):
    addition += i 


    print(addition)

    
'''
#  Write a program that generates 50 random numbers from 1 through 9. Print out all 50 numbers on the
# same line. Then print out how many fives are generated​.

from random import randint
choices = (1, 2, 3, 4, 5, 6, 7, 8, 9)
computer_choice = choices.count(51)

print( computer_choice)

    
if user_choice == computer_choice:
        print("It's a tie!")
     elif (user_choice == 5 and computer_choice == 5) or \
          (user_choice == 'paper' and computer_choice == 'rock') or \
          (user_choice == 'rock' and computer_choice == 'scissors'):
         print("You win!")
     else:
        print("Computer wins!")
'''

# Generate 50 random numbers from 1 through 9
import random
random_numbers = [random.randint(1, 9) for _ in range(50)]
# Count the number of occurrences of 5
count_of_fives = random_numbers.count(5)

# Print all 50 numbers on the same line
print(" ".join(map(str, random_numbers)))
print("5 appears in: ", count_of_fives)



    
