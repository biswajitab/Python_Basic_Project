#############how to read a file######
# f = open("demo.txt","r")
# data=f.read()
# print(data)
# f.close()

# #######how to execute line by line file######
# f = open("demo.txt","r")
# data1=f.readline()
# print(data1)
#
# data2=f.readline()
# print(data2)
# f.close()

# ############how to writing a file , existing is showing fst then showing new######
# f = open("demo.txt","r")
# data=f.write("\n i am not happy")
# readdd=f.read()
# print(readdd)
# f.close()

# ############if file is not existing then create a new file using a,w ######
# create=open('mithun.txt','w')
# create.write("hello ! mr.biswajit")
# create.close()

# # ############ r+ first show new data then show existing data######
# f = open("demo.txt","r+")
# f.write("biswajit das mithun")
# print(f.read())
# f.close()

###### as use for alias(name change)###########
# with open("demo.txt","r") as m:
#     data=m.read()
#     print(data)

####or

# hye=open('demo.txt','r')
# hy=hye.read()
# print(hy)
# import os

# os.remove("mithun.txt")

##########print the number in which line of the file######
# def biswajit_das():
#     kkk="happy"
#     dataa=True
#     lineno=1
#     with open("demo.txt","r") as m:
#         while dataa:
#             data=m.readline()
#             # if data.find(kkk):
#             if kkk in data:
#                 lineno += 1
#                 print(lineno)
#                 # return
# biswajit_das()

# i=1
# k=100
# for m in range(k):
#     if m>=100:
#         i += 1
#         print(i)
#
# for i in range(1, 101):
#     print(i)



### creating the json file it comntains only dictionary data
# import json
# info = {
#     'name' : 'biswajit',
#     'place' : 'bhubaneswar',
#     'country' : 'indian',
#     'salary' : 1000
# }
#
# fvar = open(r'prosnal.json', 'w')
# json.dump(info,fvar)
# fvar.close()


# #################### read data from json file ####################
# import json
# fvar = open(r'prosnal.json', 'r')
# myinfo = json.load(fvar)
# fvar.close()
# print(myinfo)

# import copy

# # Original list with nested list
# original_list = [1, 2, [3, 4]]

# # Deep copy of the original list
# deep_copy_list = copy.deepcopy(original_list)

# # Modify the nested list in the deep copy
# # deep_copy_list[2][0] = 'X'
# deep_copy_list.insert(2, [1,'x'])

# print("Original List:", original_list)     # Output: [1, 2, [3, 4]]
# print("Deep Copy List:", deep_copy_list)   # Output: [1, 2, ['X', 4]]
