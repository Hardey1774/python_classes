#Guess game
'''
# To generate our random number, we need to import a randint function from a file/module called Random

 from random import randint
 generated_number = randint(1, 20)
 print(generated_number)
 user = int(input("Guess a number between 1 and 20: "))
 if generated_number == user:
     print("you are correct")
 else:
     print("you are wrong")
'''
import random
choices = ("scissors", "paper", "rock")
computer_generated_choice =random.choice(choices)
print("computer choose:",  computer_generated_choice, )
user = input("Make a choice from these 3 objects (scissors, paper and rock): ")
if computer_generated_choice == user:
    print("you are correct")
else:
    print("you are wrong")