#Exercise 3: Biography (ADVANCED)
name_input=input("Enter name: ") #The use of input allows the user to enter data that will be stored in a variable.
hometown_input=input("Enter hometown: ")
age_input=input("Enter age: ")
dictionary_1={"Name":name_input,"Hometown":hometown_input,"Age":age_input} #Dictionaries are groups of data that are stored in key values.
print (f'{dictionary_1["Name"]}\n{dictionary_1["Hometown"]}\n{dictionary_1["Age"]}')#These keys are groups that have variables known as values.
#Line 6 is a single line of code that displays the inputed name, hometown, and age, in separate line by \n.
