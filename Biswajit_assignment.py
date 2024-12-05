####### 1. write a program for the basketball selection,
	# take height (float) as the input from the user and verify whethetr his height is 6.0 and above if yes
	# he is selected , if height is less that 6.0 please print not selected ##############
from array import array
from itertools import count, repeat

# height =int(input("enter your age ="))
# if height>=6:
#     print("selected")
# else:
#     print("not selected")


############# 2. Write a program for the school registry exmple
# please take total marks as input from user for max 600
# calculate the percentage of the total marks and verify if sthe student has passed in which grade #########

# total_marks = float(input("Enter the total marks out of 600: "))
#
# if 0 <= total_marks <= 600:
#     percentage = (total_marks / 600) * 100
#
#     print("Percentage:", percentage)
#
#     if 0 <= percentage < 35:
#         print("Result: FAIL")
#     elif 35 <= percentage < 50:
#         print("Result: Passed in third class")
#     elif 50 <= percentage < 60:
#         print("Result: Passed in second class")
#     elif 60 <= percentage < 85:
#         print("Result: Passed in first class")
#     elif 85 <= percentage <= 100:
#         print("Result: Distinction")
# else:
#     print("Invalid entry! Please enter total marks between 0 and 600.")
#

#########3. write a prog for calculator #####
# operation = input("Please select one of them (add, sub, mul, div): ")
# fst = float(input("Please put your 1st input: "))  # Convert input to a number (float for decimals)
# second = float(input("Please put your 2nd input: "))
#
# if operation == "add":
#     result = fst + second
#     print("Total =", result)
# elif operation == "sub":
#     result = fst - second
#     print("Total =", result)
# elif operation == "mul":
#     result = fst * second
#     print("Total =", result)
# elif operation == "div":
#     if second != 0:
#         result = fst / second
#         print("Total = " ,result)
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation selected!")

#######Write w program which prints how many even and odd numbers are there in the above list
# List =[ 50, 33 , 27 , -20 , 85 , 74 , 4,9,3,7]
# even_count=0
# odd_count=0
#
# for num in List:
#  if num % 2==0:
#     print("even_count",num)
#     even_count +=1
#  else:
#      print("odd_count",num)
#      odd_count +=1
# print("Even Count:",even_count)
# print("Odd Count:",odd_count)

########## 5.please print all the elements of the list which has word python present in it and count how many elements contsins python word
# L1 = ["python is good" , "Java is ok" , "i love python" , "c is mother lang" , "python rocks"]
# count = 0
# for num in L1:
#    if "python" in num:
#        print(num)
#        count +=1
# print("Number of elements containing the word python =",count )

########6.Write a program to take email I'd and pwd as input from user and compare the same with hardcoded email I'd and pwd if both are matching then you need to print welcome to the home page and exit the loop.
# If wrong credentials were given ask the email I'd and pwd again on a loop of 3 times.
# If all the three times the credentials were given wrong print account locked.

# Email = "das17908@gmail.com"
# Password = "Abcde12@"
# attempts = 3
# while attempts > 0:
#     email = input("Enter your email: ")
#     password = input("Enter your password: ")
#     if email ==Email and password == Password:
#         print("Welcome to the home page!")
#         break
#     else:
#         attempts -= 1
#         print("Wrong credentials! You have attempt left :",attempts)
#     if attempts == 0:
#         print("Account locked.")

########### 7.Take any number between 1 to 10 and save in a temp variable.
# Now ask user to guess the number between 1 to 10 and compare with the temp variable.
# If both are same print  you have guessed the number correctly and also print the number of attempts taken to guess correctly in a loop.

# import random
# temp = random.randint(1, 10)
# attempts = 0
# while True:
#     guess = int(input("Guess a number between 1 and 10: "))
#     attempts += 1
#     if guess == temp:
#         print("Congratulations! You've guessed the number correctly in {attempts} attempt.")
#         break
#     else:
#         print("Wrong guess. Try again!")

############8.names = ['A','B','C',D','E','F']
# write a program which takes names list and prints the first prize and second prize winners

# import random
#
# names = ['A', 'B', 'C', 'D', 'E', 'F']
#
# first_prize = random.choice(names)
# second_prize = random.choice([name for name in names if name != first_prize])
#
# print("First prize winner:", first_prize)
# print("Second prize winner:",second_prize)

###########9. write a program which takes five numbers as input from user and prints which is maximum value and which is minimum value without using max and min func?
# Input five numbers from the user
# num=int(input("Total time of input enter number:"))
# arra=[]
# for time in range(num):
#     number=int(input("enter number:"))
#     arra.append(number)
# max1=arra[0]
# min1=arra[0]
# for nums in arra:
#     if nums>max1:
#         max1=nums
#     if nums<min1:
#         min1=nums
#
# print("maximum value is:",max1)
# print("minimum value is:",min1)

