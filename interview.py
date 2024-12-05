# ##### how to count without using built in function a string
# name="Biswajit"
# count=0
# for i in name:
#     count +=1
# print(count)



# ###write a fabonacci series
# n=int(input("enter a number:"))
# a=0
# b=1
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for m in range(1,n+1):
#         c=a+b
#         a=b
#         b=c
#         print(c)



#####chech both string are anagram or not
# def anagatam_String(str1,str2):
#     mm=str1.replace("","").lower()
#     kk=str2.replace("","").lower()
#     return sorted(mm)==sorted(kk)
# str="listne"
# srr="silent"
# if anagatam_String(srr,str):
#     print(f" '{str}' and '{srr}' are anagaram")
# else:
#     print(f" '{str}' and '{srr}' are not anagram")

###########how to convert a costumer input 32 to three tow in chaqtacter python code
# inp=int(input("enter a number:"))
# def digitWord(numberr):
#     digits={
#         '0':"one",'2':"two",'3':"three",'4':"four",'5':"five",
#         '6':"six",'7':"seven",'8':"eight",'9':"nive"
#     }
#     return ' ' .join(digits[digit] for digit in str(numberr) )
# # number=56   
# result=digitWord(inp)
# print(result)


    
#############Checking if 153 is a Perfect Square
# import math
# inp=int(input("enter a sqrt number:"))
# def sqareroot(enter):
#     sqrtt=math.sqrt(enter)
#     return sqrtt.is_integer()
# if sqareroot(inp):
#     print(f"the {inp} number is sqrt.")
# else:
#     print(f"the {inp} number is not sqrt.") 

# import math

# def is_perfect_square(number):
#     sqrt_value = math.sqrt(number)
#     return sqrt_value.is_integer()

# # Check for 152
# number = 152
# if is_perfect_square(number):
#     print(f"{number} is a perfect square.")
# else:
#     print(f"{number} is not a perfect square.")


########### the input number is palendrom or not and sum of the number 
num=int(input("the enter number is:"))
def palindrome(number):
    number1=str(number)
    number2=number1[::-1]
    if number1==number2:
         print(f"the {number} is palindrome")
    else:
        print(f"the {number} is not palindrome")    
def summ(number):
    return sum(int(digit) for digit in str(number))
summm=summ(num)
print(f"the {num} of sum is {summm} ")
palindrome(num)


       
            

