import random
def Play_game():
    choices = ('scissors', 'paper', 'rock')
    user_choice = input("Enter your choice (scissors, paper, rock): ")
    computer_choice = random.choice(choices)
    
    print("Computer chose:", computer_choice)
    
    if user_choice == computer_choice:
        print("It's a tie!")
    # elif (user_choice == 'scissors' and computer_choice == 'paper') or \
    #      (user_choice == 'paper' and computer_choice == 'rock') or \
    #      (user_choice == 'rock' and computer_choice == 'scissors'):
    #     print("You win!")
    # else:
        #print("Computer wins!")
