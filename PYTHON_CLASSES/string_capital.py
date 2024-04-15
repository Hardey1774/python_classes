# * Write a program that asks the user to enter a string. Print out whether the string contains more capital
# 'A' than capital 'B', the same amount, or more capital 'B'.

user_input = input("Enter a letter: ")

if user_input.count("A") > user_input.count("B"):
    print("Capital A is more than Capital B")
elif user_input.count("A") == user_input.count("B"):
    print("Capital A is equal Capital B")
else:
    print("Capital A is less than Capital B")