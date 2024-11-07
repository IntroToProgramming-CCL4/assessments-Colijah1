#Exercise 4: Primitive Quiz 
import sys #Import sys is a module that provides the user new functions for Python to use.

#This is a program used to ask the user geographical questions, depending on the answer will continue to the next question or end the program.
question_1=input("What is the capital of France?\n").lower() #This structure of code used is the foundation of asking an input from the user.
if question_1!="paris": #.lower() is a code that makes the data lowercase, this allows case sensitivity to not be a problem.
    print("\nThe correct capital of France is Paris.\n") #Line 4 uses if to conditionalize certain factors to influence the outcome of the code. 
    sys.exit() #sys.exit() is used to terminate the program. Only if the user enters the wrong answer.
else:
    print ("\nCorrect! Next Question.\n") #If the input is correct it will move on to the next question
question_2=input("What is the capital of Germany?\n").lower()
if question_2!="berlin":
    print("\nThe correct capital of Germany is Berlin.\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_3=input("What is the capital of Italy?\n").lower()
if question_3!="rome":
    print("\nThe correct capital of Italy is Rome.\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_4=input("What is the capital of Spain?\n").lower()
if question_4!="madrid":
    print("\nThe correct capital of Spain is Madrid.!\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_5=input("What is the capital of Greece?\n").lower()
if question_5!="athens":
    print("\nThe correct capital of Greece is Athens.\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_6=input("What is the capital of Georgia?\n").lower()
if question_6!="tbilisi":
    print("The correct capital of Georgia is Tbilisi.")
    sys.exit()
else:
    print ("Correct! Next Question.")
question_7=input("What is the capital of Ireland?\n").lower()
if question_7!="dublin":
    print("The correct capital of Ireland is Dublin.")
    sys.exit()
else:
    print ("Correct! Next Question.")
question_8=input("\nWhat is the capital of Finland?\n").lower()
if question_8!="helsinki":
    print("\nThe correct capital of Finland is Helsinki.\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_9=input("What is the capital of Serbia?\n").lower()
if question_9!="belgrade":
    print("\nThe correct capital of Serbia is Belgrade.\n")
    sys.exit()
else:
    print ("\nCorrect! Next Question.\n")
question_10=input("What is the capital of Malta? ").lower()
if question_10!="valletta":
    print("\nThe correct capital of Malta is Valletta.\n")
    sys.exit()
else:
    print ("Good job!")
    sys.exit()