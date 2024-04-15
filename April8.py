# * Write a program that asks the user to enter a string. The program should then print the following:

# (a) The total number of characters in the string

# (b) The string repeated 10 times

# (c) The first character of the string (remember that string indices start at 0)

# (d) The first three characters of the string

# (e) The last three characters of the string

# (f) The string backwards

# (g) The string with its first and last characters removed

# (h) The string in all caps

# (i) The string with every a replaced with an e 

# * Write a program that checks if a word is a palindrome, irrespective of the case (uppercase or lowercase)

name = (input("Enter anything: "))

length_of_characters = len(name)

print( "Total number of characters: ", "=", length_of_characters )

print("Repeat 10 times: ", length_of_characters* 10)

print("The first character of the string is: ", name[0])


'''
Input_string = input("Enter anything : ")
Number_of_character = len(Input_string)

print(Input_string)

print( "Total number of characters: ", "=", Number_of_character )

print("Repeat 10 times: ", Number_of_character * 10)

print("The first character of the string: ", "=", Input_string[0] )

print("The first 3 characters of the string are: ", Input_string[ :3] )

print("The last 3 characters of the string are: ", Input_string[ -3:] )

print("The string backwards is: ", Input_string[: : -1])

print("The string with its first and last characters removed: ", Input_string[1:-1: ])

print("The string in all caps: ", Input_string.upper())

print("The string with every a replaced with an e : ", Input_string.replace("a", "e"))

# a program that checks if a word is a palindrome, irrespective of the case (uppercase or lowercase)
if Input_string == Input_string[::-1]:
    print("The word is a palindrome.")
else:
    print("The word is not a palindrome.")
'''    

#check if a certain number is divisible by another number

# numerator  = int(input("Enter a certain number : "))

# denominator = int(input("Enter a second number: "))

# correct = False if denominator <= 0 else True

# if correct == True:
#     print(numerator/denominator)


#print(correct)

#print(5/0)

# for i in range(1, 101):
    # print(i, 'Adeoye Adeyinka')

#for i in range(1, 50):12

    # print(i*2, "Adeoye Adeyinka" )






