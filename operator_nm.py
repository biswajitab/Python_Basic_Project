# var="mithun"
# print("my name is" + " " +var)

# varrr=int(input("put some number:"))
# for i in range(1,varrr+1):
#     print('*' * i)
# for i in range(varrr, 0, -1):
#     print('*' * i)
########nested loop#######
# varrr=int(input("put some number:"))
# for i in range(1,varrr+1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
# for k in range(varrr - 1,0,-1):
#     for m in range(1,k+1):
#         print('*',end=' ')
#     print()

#######number print######
# varrr=int(input("put some number:"))
# for i in range(1,varrr+1):
#     # print("*" * i)
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# ######dimond print in ###
# var=int(input("put the numbere :"))
# for i in range(1,var+1):
#     print(" " * (var - i), end='')
#     for j in range(1,i+1):
#         print("*",end=' ')
#     print()
# for k in range(var-1,0,-1):
#     print(" " * (var-k),end='')
#     for m in range(1,k + 1):
#         print("*",end=" ")
#     print()



############### index operator and index range operators
# var = "python is easy"
# ####### print(var)
# ###print(var[2])
# ###print(var[-2])
# ##print(var[0:3])
# print(var[3:6])
# print(var[-6:])
# print(var[:3])
# print(var[::-5])
########print(var[::2])

############ concatenation operator
# a = "santhosh"
# b = "123"
# var=a + str(b)
# print(var)


####### * - Duplication operator
# var="india"
# res=var * 5
# print(res)

######## range function
# nums = [1,2,3,4,5,6,7,8,9,10]
# for x in range(1,11):
#     print(x)

# for x in range(1,6):
#      print("Pathmesh")

# for x in range(1,11):
#      print("%" * x )
############pattern
# subcnt = 0
# for x in range(1,11):
#     temp = x
#     if(x > 5):
#         subcnt +=2
#
#     print("#" * temp)

######### Converts the first letter of variable in upper rest all lower

# var = "pYThoN iS eSAy"
# # res = var.capitalize()
# # print("capitalize format = " , res)
# #
# # ####converts all the words first letter in upper rest all lower
# res=var.title()
# print(res)
# #
# # #####"lower format=",
# res=var.lower()
# print(res)

# # #####"upper format=",
# res=var.upper()
# print(res)

# import math
# hye=3.5
# abc=math.sqrt(hye)
# print(abc)

# import math
# hye=3.5
# abc=math.ceil(hye)
# print(abc)

# import math
# hye=3.5
# abc=math.floor(hye)
# print(abc)

# import math
# hye=3.5
# abc=math.pow(hye,2)
# print(abc)

####"swapcase format = " ,
# var = "pYThoN iS eSAy"
# res = var.swapcase()
# print(res)

# var = "there was a netWOrk issue in servers"
# res = "NETWORK" in var.upper()
# print(res)

# log = """
# sdkcndsvmsdvnasv1
# sddjchds;vcmds1
# ;skdjch'skdvjdsv1
# sdcjsdklcnklvnsdkd;v
# we have network ERRor reported yest
# kdhcds
# bsdv1vdfv1sdv
# a.csdklskdv;svjf
# """
# res='error' in log.lower()
# print(res)
# if(res == True):
#     print("send email")
# else:
#     print("no rrror occured")

#######ASCII max value
# var = "pYThoN iS eSAyY"
# res=min(var)
# print(res)

## gives how many chars present in variable
# var = "pYThoN iS eSAy"
# res = len(var)
# print(res)

# while(True):
#
#     pwd = str(input("enter the pwd = "))
#
#     if(len(pwd)>= 8):
#         print("valid")
#         break
#     else:
#         print("invalid")

# user = "santhosh"
# pwd = "san@123"
# success = 0
#
# for x in range(3):
#     username = str(input("enter the user name = "))
#     password = str(input("enter the  password = "))
#
#     if(username == user and password == pwd):
#         print("welcome to home page ")
#         break
#     else:
#         print("Wrong cred try again")
#
# if(success == 0):
#     print("account locked")

# var = "#######santhosh############kumar########"
# res=var.rstrip('#')
# print("right strip ",res)
# #ans------#######santhosh############kumar

# var = "#######santhosh############kumar########"
# res=var.strip('#')
# print("left right strip ",res)
# ans-left right strip  santhosh############kumar

# var = "#######santhosh############kumar########"
# res = var.replace('#', '')
# print(res)
# ans-santhoshkumar

# pwd = 'santhosh123'
# print(pwd)
# res = pwd.strip(' ')
# print(res)


# var = """
# santhosh teaches python
# santhosh name is 2nd in the blogger list
# my parents kept my name as santhosh bcoz i will be happy
# """
# res = var.replace('santhosh', 'priya')
# print(res)

# var = "india is 4th largest Economy"

# res = var.startswith('india')
# print(res)

# res = var.lower().endswith('economy')
# print(res)

# email = "sandy@yahoo.com"
# res = email.endswith('@yaho.com')
# print(res)


# var = "santhosh 560100 bangalore 9986019197"
# res = var.split()
# print(res)

# var = "santhosh560100bangalore9986019197"
# res = " "
# indx = 0
# for x in var:
#      res = res + x
#      indx += 1
#      if(indx == 8):
#          res = res + " "
#      elif(indx == 14):
#          res = res + " "
#      elif(indx == 23):
#          res = res + " "
# print(res)

# email = "sandy@gmail.com"
# res = email.split('@')
# print(res)

# data = ['a','b','c','d','e']
# res = "____________".join(data)
# print(res)

# dates = ['2024','7', '26']
# res = '-'.join(dates)
# print(res)

# data = ['santhosh', 'kumar', 'yadav']
# fullname = " ".join(data)
# print(fullname)

var = "hi SAn hello sAn bye San"
# print(len(var))
# res = var.lower().count('san')
# print(res)

import re
res = re.findall('san', var,re.I)
print(res)

# var = "today we have python class"
# res = var.index('python')
# print(res)

# log = """parse1 Network error: db conn failed
# innstances port is not active
# asjkhasck';lcv;ad
# favfvlkdfvvdfjkvhfvgdsjvh
# hjcashckljadckl;sdkvl;4
# aakcshaslkcjasl;cjas
# """
# # errpos = log.index('error')
# # print(errpos)
# errmsg = log[errpos:errpos+50]
# print(errmsg)

# # var = "SANTOSHAfgh OOKUMAR"
# res = var.isalpha()
# print(res)

# var = "00cb0"
# # res = var.isdigit()
# res = var.isalnum()
# print(res)

