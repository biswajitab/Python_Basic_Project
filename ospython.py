import os, shutil
# print(dir(os),'/n')

# 1.access func check for file or folder existance

# res = os.access(r'xyz.txt',os.F_OK)
# print(res)


# os.F_OK , os.R_OK , os.X_OK , os.W_OK


#2. delete the file

# os.remove(r'sandyy.txt')


#3. mkdir ( create folder )
# os.mkdir(r'RCBB.txt')

#4.
# os.rmdir(r'RCBB.txt')


# 5
# shutil.rmtree(r'RCBB.txt')



# 7. rename


# os.rename(r'vijay.txt',r'ajay.txt')



# 8. : gets the current folder path

# res = os.getcwd()
# print(res)




# # 10
# res = os.listdir(r'RCBB.txt')
# print(res)

# print(os.getcwd())


# 9.
# print("before shifting my path = "  , os.getcwd())
# print(os.listdir())

# os.chdir(r'D:\SANTHOSH\Batches\Batch106')
#
# print("after shifting my path = "  , os.getcwd())
# print(os.listdir())


### sample prog to check the file exisatance

# res = os.access(r'D:\SANTHOSH\Work\capgemini\CG_Backup\abcd.txt', os.F_OK)
# print(res)
#
# if (res == True):
#     print("success email sent")
# else:
#     print("failure email sent")






# 11. only files

# shutil.copy(r'amar.txt' , r'./RCB/amar.txt')


# 12. files & Folders

# moving file
# shutil.move(r'RCBB.txt/amar.txt' , r'demo.txt')



# moving folder
# os.mkdir(r'virat.txt')
# shutil.move(r'virat.txt', r'RCBB.txt')


#13. copying the folder

# shutil.copytree(r'RCBB.txt',r'.mithun')
# os.mkdir(r'mithun')

#14 gets all environment variable data

res = os.environ

# for x,y in res.items():
#    print(x  , "===>" , y)



# # 15.
#
# res = os.getenv('SYSTEMDRIVE')
# print(res)
# res = os.getenv('apwd')
# print(res)


# # 16.

# res  = os.system('ipconfig')
# print(res)

# res = os.system(r'type NUL > D:\SANTHOSH\BBB\rahul.txt')


# res = os.system('pip3.10 install bob')
# print(res)

#######################




#17  get the file stats

# res = os.stat(r'List-Tuple-Dictionary.xlsx')
# print(res)
# print(list(res))


# res = os.path.getsize(r'List-Tuple-Dictionary.xlsx')
# print(res)

