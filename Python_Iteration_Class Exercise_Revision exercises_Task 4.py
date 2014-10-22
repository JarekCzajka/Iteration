#Jaroslaw Czajka
#21-10-2014
#Python_Iteration_Class Exercise_Revision exercises_Task 4
 
#Task
 
#Write a program that asks a user for a number between 10 and 20 inclusive.
#The program should give the user a message if the number input is outside 
#this range and ask for another number until the number input is within range.
 
number=int(input("Please enter and number between 10-20:"))
if 10<=number<=20:
           print("Your number is correct!")
while 20>=number<=10:
    number=int(input("Please enter and number between 10-20:"))
    print("Your number is correct")


#The program carried out the task set
    
