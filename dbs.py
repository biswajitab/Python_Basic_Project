# # Step 1 : import module
from optparse import Values
from tkinter.constants import INSERT

import pymysql as p
# # # # # #cx_Oracle
#
#
#
# # # # Step 2 : connect to database
santhoshdb = p.connect(host = 'localhost', user = 'root', password = 'TRIGER', db = 'biswajit')
print("connected successfully")

#
# # # # # # # Step3  : create cursor
mypage = santhoshdb.cursor()
#
#
# # # # # # # # #### selelect query ....
# # # # # # Step 4 : Prepare the query
q1 = [
        'select * from mithun;',
        'select count(*) from mithun;',
        # 'select * from mithun where id in (120,121,122);',
        # 'select * from mithun where name = "virat";',
        # 'select name,email from login;',
        # 'select * from login where id=3;',
        # 'select * from login where name = "jeeva";'
        ############ "INSERT INTO biswajit.mithun(id, name, age,city) VALUES (130, 'kkkkkkkkkkkk','22','bnglr');",

      ]
for query in q1:
    # Step 5 : execute the query
    mypage.execute(query)

    # Step 6 : fetch all result
    res = mypage.fetchall()
    print("\n", res, "\n")



# Step7 : close DB
santhoshdb.close()

#
#
#
#
#
# ###################################################################################
#
#
#
#
#
#
#
#
#
# ### dml statements
#
#
#
#
#
# # # step 1
# import pymysql as p
#
#
# # Step 2 : connect to database
# db = p.connect(host = 'localhost', user = 'root', password = 'TRIGER', db = 'biswajit')
#
# print("connected successfully")
#
#
# # Step3  : create cursor
# mypage = db.cursor()
#
#
#
# ##### insert query
#
# # Step 4 : insert the data
# q1 = [
#     "INSERT INTO biswajit.mithun (id, name, age,city) VALUES (130, 'Anu','22','bnglr');",
#     "INSERT INTO biswajit.mithun (id, name, age,city) VALUES (131, 'Raja','23','chennai');",
#     """CREATE TABLE biswajit.Shweta (
#         PersonID int,
#         LastName varchar(255),
#         FirstName varchar(255),
#         Address varchar(255),
#         City varchar(255)
#     );""",
#     # 'drop table projects'
#
# ]
#
#
#
# # Step 5 : execute the query
# for x in q1:
#     try:
#         mypage.execute(x)
#     except Exception as err:
#         print("error msg was = ", err)
#
# # Step 6 : commit
# db.commit()
#
# # Step 7 : Close DB
# db.close()
#
# print("successfully inserted ")


# import pymysql as kk
# das=kk.connect(host='localhost',user='root',password='TRIGER',db='biswajit')
# # db = p.connect(host = 'localhost', user = 'root', password = 'TRIGER', db = 'biswajit')
# crsr=das.cursor()
# s = "UPDATE mithun SET city = 'odisha' WHERE name = 'virat';"
# try:
#     crsr.execute(s)
# except Exception as err:
#     print("error msg was = ", err)
# das.commit()
# das.close()