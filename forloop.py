# print & count only those nums which are greater than 25
# nums = [10,20,30,40,50]
# count = 0
# for x in nums:
#     if x > 28:
#         count += 1
#     # print(x)
# print("count=", count)
from itertools import count

# converting earlier example to real time scenario
# nums = [60, 42, 30, 40, 50,44,72,80,39,12,55,95,67,88,76,99]
# passs = 0
# firstclass = 0
# distinct=0
# for x in nums:
#     if x > 30 and x < 60:
#         passs += 1
#         # print("Total count =",x)
#     elif(x>60 and x<80):
#       firstclass +=1
#       # print("firstclass student total=",x)
#     elif(x>80 and x<100):
#       distinct +=100
#       # print("distint total student=",distinct)
# print(passs)
# print(firstclass)
# print(distinct)

###### While loop or conditional loop ########
#print number 1 to 10 #
# num=0
# while(num <=10):
#     print(num)
#     num=num+1

# print all nums which are divisible by 2 and 3 between 1 to 50
# number=50
# count=0
# while (number>0):
#     if (number % 2 == 0 and number % 3==0):
#         if number == 30:
#             number = number - 1
#             continue
#         count += 1
#         print(number)
#     number=number-1
# print("total count=",count)


# number=[10,20,30,40,50,60,70,80] ##
# for x in number:
#     # if x == 40:
#     if x in (50,30,70):
#         continue
#     print(x)

