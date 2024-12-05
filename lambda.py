# mithun=lambda x,y:x+y
# print(mithun(4,5))

# def appl(fx,value):
#     return 6 + fx(value)
# print(appl(cube,2))

# cube=lambda x:x * 6
# print(cube(4))
#
# def appl(fx, value):
#     return fx(value) + 7
#
# print(appl(cube, 3))


# number=[20,10,11,22,17,40,74,648,84,83,]
# var=[]
# def even(x):
#     for k in x:
#         if k % 2==0:
#             var.append(k)
# even(number)
# print(var)

number=[20,10,11,22,17,40,74,648,84,83,]
das=lambda x:[m for m in x if m % 2==0]
print(das(number))