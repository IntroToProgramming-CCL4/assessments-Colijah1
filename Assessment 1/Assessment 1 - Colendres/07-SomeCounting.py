#Exercise 7: Some Counting

print("0-50 count up: ") #Lines 3-6 displays a looping statement that goes from 0-50 in increments of 1.
for count_1 in range(0,51,1): #The application of for loops allow the coder to set a range of numbers to be printed by the coder.
    print(count_1) #Displaying the range using print.
    print("\r") #Allows room for space per increment/decrement in range.

print("50-0 count down: ") #The same lines of code are replicated with different ranges and steps to complete the task.
for count_2 in range(50,-1,-1):
    print(count_2)
    print("\r")

print("30-50 count up: ")
for count_3 in range(30,51,1):
    print(count_3)
    print("\r")

print("50-10 in 2 decrements: ")
for count_4 in range(50,9,-2):
    print(count_4)
    print("\r")

print("100-200 in 5 increments: ")
for count_5 in range(100,201,5):
    print(count_5)
    print("\r")
