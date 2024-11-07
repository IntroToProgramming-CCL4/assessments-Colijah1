#Exercise 5: Days of the Month
Month_Dictionary={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #This dictionary stores the month number, and how many days in each month.
month_number=int(input("Enter month number: ")) #Using input for the user to enter a number, and converting the input in to an integer data type.
if month_number in Month_Dictionary: #These lines of codes determine how many days there are in a month.
    if month_number == 2: #Lines 5-12 is used when February is selected and, will ask the user if the year is a leap year or not.
        Yes_No=input("Is the year a leap year? ").lower()
        if Yes_No == "yes":
            print(f"The month {month_number} has 29 days.") #Line 8 displays the number of days in February in a normal year
        elif Yes_No =="no":
            print(f"The month {month_number} has 28 days.") #Line 10 displays the number of days in February in a leap year
        else:
            print("Invalid input. Enter yes or no.") #Line 12 is a line of code used to remind the user to input yes or no.
    else:
        print(f"The month {month_number} has {Month_Dictionary[month_number]} days. ") #Line 14 displays the number month and its days apart from February (2).
else:
    print("Invalid number input. Enter a number between 1-12.") #Line 16 is displayed when the user inputs an invalid month number.