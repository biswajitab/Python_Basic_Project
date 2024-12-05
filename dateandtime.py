# from datetime import date,datetime,timedelta, timezone
# import time
#
#
# current_datetime = datetime.now()
# print(current_datetime)

# time.sleep(15)
#
# print("year = " ,current_datetime.year)
# print("month = ", current_datetime.month)
# print("day = ", current_datetime.day)
# print("hour = " , current_datetime.hour)
# print("minute = " , current_datetime.minute)
# print("second = " , current_datetime.second)
# print("micro second = " , current_datetime.microsecond)




##### all() any() funcs
# a = 10
# b = 20
# c = 30
#
# res1 = a<10
# res2 = b == 20
# res3 = c < 25
#
# print(res1,res2,res3)
#
# if(res1 == True and res2 == True and res3 == True):
#     print("Happy")
# else:
#     print("Not happy")


# USING all() and any()


# a = 10
# b = 20
# c = 30
#
# res =[a<10, b==20 , c<25]
# print(res)
#
# op = any(res)
# print("any op = " , op)
#
# op = all(res)
# print("all op = " , op)




# Example for any and all

# username = str(input("enter the usrname = "))
# passwd = str(input("enter the password = "))
# otp = str(input("enter the otp = "))
#
# res = [username.lower()=="santhosh",passwd=="San@123",otp=='1234']
# print(res)
#
# op = all(res)
# print(op)



### Lambda ###########

# def test(x,y,z):
#     res = x + y + z
#     return res
#
# res = test(20,5,2)
# print(res)

# formula
# # variable = lambda parameters : return result

# myfunc = lambda x,y,z : x + y + z
#
# res = myfunc(10,5,3)
# print(res)
#
# res = myfunc(100,300,200)
# print(res)



# another example

# def incr(x):
#     return x + 10
#
# res = incr(50)
# print(res)

# # variable = lambda parameters : return result

# fincr = lambda x : x + 10
# op = fincr(300)
# print(op)


# def test(a,b):
#     res = a * b
#     return res
#
# op = test(10,30)
# print(op)
#
#
# var = lambda a,b : a * b
# op = var(7,8)
# print(op)

# import math
# def sqrtt(x):
#     return math.sqrt(x)
# data=[2,4,2,8]
# dataa=[]
# for ind in data:
#     xx = dataa.append(ind)
# pnt=map(sqrtt,data)
# for dt,kk in zip(pnt,dataa):
#     print(f"print sqrt of {dt}{dt}")