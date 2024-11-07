#Exercise 10 - Is It Even?
def even_odd_checker(number): #Lines 2-6 checks if the number entered is an odd or even number.
    if number % 2 == 0: #If the number has a remainder of 0.
        return f"{number} is an even number" #If the number has a remainder of 0 it is even.
    else:
        return f"{number} is an odd number" #If the number does not have a remainder of 0 it is odd.
    
def math():
    input_value = int(input("Enter a number: ")) #User is asked to enter a number.
    result = even_odd_checker(input_value) #After the number is entered will run through the even or odd function.
    print (result) #The number will be displayed if the number is even or odd.

if __name__ == "__main__":
    math()