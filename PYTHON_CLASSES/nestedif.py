# nested if
age = int(input("How old are you: "))
if age > 0:
    if age <= 18:
        print("You are a minor.")
    elif age <= 40:
        print("You are a yound adult.")
    elif age <= 50:
        print("You are getting old.")
    else:
        print("You are an octogenerian.")
else:
    print("Your input is invalid.")
    

