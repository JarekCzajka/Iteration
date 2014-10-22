#Jaroslaw Czajka
#21-10-2014
#Python_Iteration_Class Exercise_Revision exercises_Task 3



#Write a program that asks the user to enter how many numbers are to be averaged,
#then enter this number of numbers, calculating the average. The program should
#display the average

number=int(input("Please enter the amount of numbers to be averaged:"))
for count in range(number):
    count=int(input("Please enter a number:"))
total=count

average=count/number
