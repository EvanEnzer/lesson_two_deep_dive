# 1.1

'''You are provided with a Python script that 
uses conditional statements to tell if a number is 
positive, negative, or zero, 
but it has some errors. Identify and fix them.'''

'''
number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number = 0:
    print("The number is zero.")
else number < 0:
    print("The number is negative.")
    
'''
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else: # could also use elif
    print("The number is negative.")

# 2.1

'''You are provided with a Python script that uses if-else structures 
for a story branching mechanism. There are some errors in the code. 
Identify and correct them.'''

'''choice = input("Do you choose the path to the left or right? ")

if choice = "left":
    print("You find a treasure chest!")
elif choice = "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")'''

choice = input("Do you choose the path to the left or right? (Choose right or left)")

if choice == "left":
    print("You find a treasure chest!")
elif choice == "right":
    print("You encounter a dragon!")
else:
    print("Invalid choice!")

# 3.1 and 3.2 

'''Write a Python program 
that prompts the user to enter three numbers. 
The program should then identify and print out the largest number 
among the three.
Extend your progam to identify the smallest number
Enhance to identify if two or more numbers are equal. 
'''

first_number = int(input("please enter your first number."))
second_number = int(input("please enter your second number."))
third_number = int(input("please enter your third number."))

# for the first task I used a much more simple if, else, elis structure.
# when needing to take equals into account it became a much longer code

if first_number == second_number and first_number == third_number:
    print("the three numbers are equal")
elif first_number != second_number and first_number == third_number and first_number > second_number:
    print(first_number)
    print("the first and third are equal and are the largest")
    print(second_number)
    print("the second number is the smallest")
elif first_number != second_number and first_number == third_number and first_number < second_number:
    print(first_number)
    print("the first and third are equal and are the smallest")
    print(second_number)
    print("the second number is the biggest")
elif first_number == second_number and first_number != third_number and first_number > third_number:
    print(first_number)
    print("the first and second are equal and are the biggest")
    print(third_number)
    print("the third number is the smallest")
elif first_number == second_number and first_number != third_number and first_number < third_number:
    print(first_number)
    print(" the first and second are equal and are the smallest")
    print(third_number)
    print("the third number is the biggest")
elif first_number != second_number and second_number == third_number and second_number > first_number:
    print(second_number)
    print("the second and third are equal and are the biggest")
    print(first_number)
    print("the first number is the smallest")
elif first_number != second_number and second_number == third_number and second_number < first_number:
    print(second_number)   
    print("the second and third are equal and are the smallest")
    print(first_number)
    print("the first number is the biggest")
elif first_number > second_number and first_number > third_number and third_number < second_number:
    print(first_number)
    print("the first number is the biggest")
    print(third_number)
    print("the third number is the smallest")
elif first_number > second_number and first_number > third_number and third_number > second_number:
    print(first_number)
    print("the first number is the biggest")
    print(second_number)
    print("the second number is the smallest")
elif second_number > first_number and second_number > third_number and first_number > third_number:
   print(second_number)
   print("the second number is the biggest")
   print(third_number)
   print("the third number is the smallest")
elif second_number > first_number and second_number > third_number and first_number < third_number:
   print(second_number)
   print("the second number is the biggest")
   print(first_number)
   print("the first number is the smallest")
elif third_number > second_number and third_number > first_number and first_number > second_number: 
    print(third_number) 
    print("the third number is the biggest")
    print(second_number) 
    print("the second number is the smallest")
elif third_number > second_number and third_number > first_number and first_number < second_number: 
    print(third_number) 
    print("the third number is the biggest")
    print(first_number) 
    print("the first number is the smallest")

#4.1, 4.2, 4.3
'''Write a Python program that prompts the user to input a year.
 The program should determine if the given year is a leap year or not 
 and then display an appropriate message.
 
 Add functionality to your program from Task 1 to inform the user if 
 the entered year is a century year (e.g., 1900, 2000) regardless of 
 whether it's a leap year or not.
 
 Enhance your program to indicate if the provided year is in the 
 future, past, or is the current year, compared to the system's 
 current year. You might find Python's 
 datetime module helpful for this task.'''

year=int(input("enter a year"))
if year % 4 == 0:
    print("this is a leap year")
else:
    print("this is not a leap year")
if year % 100 == 0:
    print("this is a century year")
else:
    print("this is not a century year")
import datetime
current_year = datetime.datetime.now().year
if current_year == year:
    print("the year provided is the same as this year!")
elif current_year > year:
    print("the year provided is in the past!")
elif current_year < year:
    print("the year provided is in the future!")