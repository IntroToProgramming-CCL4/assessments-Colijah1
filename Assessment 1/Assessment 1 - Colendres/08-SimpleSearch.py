#Exercise 8: Simple Search
names_group = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"] #List is a collection of data. This list is a group of names.
name = "Sam" #The variable name is assigned to Sam.
if name in names_group: #Lines 4-7 is used to check if Sam is in the list, otherwise, will display that the name is not in the list.
    print(f"{name} is found in the list.")
else: 
    print(f"{name} is not found in the list.")

#Optional Requirements
names_group2 = ["Jake","Zac", "Ian", "Ron", "Sam", "Dave"] 
name_input=input("Enter name: ").lower() #Asks for the input of the user.
if name_input.lower() in (name1.lower() for name1 in names_group2): #The system checks if the entered name is in the list regardless if it's upper or lowercase.
    print(f"{name_input} is found in the list.") #If the name entered is in the list, it will display that the entered name is in the list.
else: 
    print(f"{name_input} not found in the list.") #This code will display that the name entered is not on the list/