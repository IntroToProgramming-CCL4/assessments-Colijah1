#Exercise 6: Brute Force Attack
Correct_PIN="12345" #Assigns the correct PIN to 12345.
Tries=5 #Is a variable that sets the limit to only 5 tries.
Attemps=0 #Is a variable that represents the current amount of tries.
while Attemps < Tries: #Lines 5-16 are lines of code used to check if the password entered is correct.
    PIN=input("Enter your PIN: ")
    if PIN == Correct_PIN: #Lines 6-9 displays "Correct PIN entered" if 12345 is entered and will end the code.
        print("Correct PIN entered.")
        break
    else:
        Attemps = Attemps + 1 #Lines 11-16 displays the ammount of tries the user has before authorities will be alerted if the user entered the wrong password.
        Attemps_Left = Tries - Attemps
        if Attemps_Left > 0:
            print (f"Incorrect password entered. {Attemps_Left} attemp(s) left.")
        else: 
            print("Maximum attemps reached. Authorities have been alerted.")