#try - except


#############################################################

# print("simple prog with out Exception Handlng")

# var = "today we are learning EH  in python"
# res = var.index('python')
# print("the position of python = " , res)

# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")







## example with exception handling




# print("simple prog with out Exception Handlng")
#
# var = "today we are learning EH  in python"
# try:
#     res = var.index('java')
# except Exception as err:
#     print("its ok we can ignore this error ")
#     res = "Not Found"
# print("the position of python = " , res)

#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")











# File Example with out EH

# print("opening file ")

# try:
#     fvar = open(r'sandy.txt' , 'r')
# except Exception as err:
#     fvar = open(r'sandy.txt', 'w')
#     print("created the file")
# fvar.close()

# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")







#####################################################################

#EH Example with File concept with data inside
#
print("opening file ")

# try:
#     fvar = opn(r'sandy.txt' , 'r')

# except Exception as err:
#     print("creating the file sandy.txt")
#     fvar = open(r'sandy.txt', 'w')

# fvar.close()

# a = 400
# b = 90
# c = 1000
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")
#


# EH Example with File concept

# print("EH Example with File concept")
#
# try:
#     fvar = open('sand.txt','r')
#
# except FileNotFoundError as err:
#     print("\n =============== Exception FNFE Block ========= \n")
#     print("Hey boss its ok lets create file ")
#     fvar = open('sand.txt' , 'w')
#     print("created file successfully")
#     print("\n =============== Exception Block ========= \n")
#
# except NameError as err:
#     print("\n =============== NAME ERR Block ========= \n")
#     print("Hey boss lets correct the name ")
#     fvar = open('sand.txt' , 'r')
#     print("\n =============== Exception Block ========= \n")
#
# finally:
#     print("Finally block executed")
#
#
# fvar.close()
# print("complete")


# print("lets start exceptcion handling")
# try:
#     mithun=ope('sand.txt','r')
# except NameError as err:
#     print("name error")
#     mithun=open('sand.txt','r')
# except FileNotFoundError as err:
#     print("file type error")
#     mithun=open('sand.txt','w')
#     print("new file created")
# finally:
#     print("exceptcion cpmpleted")
# mithun.close()
# print("completed")







############################ creating errors ##############################

# assert and raise



## assert statement example to create error
# assert condition , message


# simple example

# mobnum  = str(input("enter the mobile number = "))
# res1 = len(mobnum)
# res2 = mobnum.isdigit()
# # assert condition , message
# assert res1==10 and res2 == True, "hey guys give correct number "
# print("Valid Mobile number")

# age = int(input("enter the age = "))
# assert  str(age) >= 22 and str(age) <= 35 , "Invaid age"
# print("Valid age")
#
# print("complete")

# age = int(input("Enter the age: "))
# assert 22 <= age <= 35, "Invalid age"
# print("Valid age")
# print("Complete")


# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")
#












#  using raise statement

# mobnum  = str(input("enter the mobile number = "))

# res1 = len(mobnum)
# res2 = mobnum.isdigit()

# # raise category("error msg")

# if res1 != 10 or res2 != True:
#     raise ValueError("Pallavi, enter correct data")
# else:
#     print("Valid mobile number")

# print("Complete")


# data=int(input("put a number="))
# if data>5 and data<10:
#     raise ValueError("invalid number")
# data = int(input("put a number="))
# if data < 5 or data < 10:
#     raise ValueError("invalid number")  # Correct comment syntax

#
#
# a = 20
# b = 40
# c = 60
# res = a + b + c
# print("addition res = " , res)
#
# print("complete")











### assert


# username = "santhosh"
# password = "Krishna@123"
# otp = 3428
#
# userin = str(input("enter the user name = "))
# assert userin == username , "invalid username"
# print("valid user name proceed next ")
#
# pwdin = str(input("enter the password = "))
# assert pwdin == password , "invalid password"
# print("valid password  proceed next ")
#
# otpin = int(input("enter the otp = "))
# assert otpin == otp , "invalid otp"
# print("valid otp  proceed next ")
#
#
# print("welcome to home page")





### raise
### if(cond):
#### raise Ecategory("msg")

# username = "santhosh"
# password = "Krishna@123"
# otp = 3428
#
# userin = str(input("enter the user name = "))
# if(username != userin):
#     raise ValueError("invalid username")
# print("valid user name proceed next ")
#
#
# pwdin = str(input("enter the password = "))
# if(pwdin != password):
#     raise ValueError("invalid password")
# print("valid password  proceed next ")
#
#
# otpin = int(input("enter the otp = "))
# if(otpin != otp):
#     raise ValueError("invalid otp")
# print("valid otp  proceed next ")
#
#
#
# print("welcome to home page")


#
#
#
#
#
#
#





#assert userin == username and pwdin == password and otpin == otp , "Invalid cread try agaian"



# % >= 60
# back logs == 0
# end duration == 4
# interview == cleared

# perc = int(input("enter the perc = "))
# assert perc >= 60 , "Sorry you dont have enough perc"
# print("percentage is validated")
#
# backlogs = int(input("enter the backlogs = "))
# assert backlogs == 0 , "Sorry you have backlogs"
# print("backlogs is validated")
#
# duration = int(input("enter the eng duration = "))
# assert duration == 4 , "Sorry you dont have enough duration for the course"
# print("duration is validated")
#
# interview = str(input("did u clear the interview = "))
# assert interview == 'yes' , "Sorry  dint clear interview"
# print("interview is validated")
#
# print("welcome to the company XYZ")
#
#
#
#
#
