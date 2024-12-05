from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pymysql as p
import pandas as pd

app = Flask(__name__)
CORS(app)


# def createdictdata():
#     dbc = p.connect(host='localhost', user='root', password='root', db='santhosh')
#     mycursor = dbc.cursor()
#     q1 = 'select * from studentsdata';
#     mycursor.execute(q1)
#     finalop = []
#     res = mycursor.fetchall()
#     for x in range(len(res)):
#         name = res[x][0]
#         email = res[x][1]
#         phone = res[x][2]
#         course = res[x][3]
#         id = x+1
#         createdat = ''
#         updatedat = ''
#
#         mycred = {'name': name, 'id': id, 'email':email, 'phone':phone, 'course':course,'createdat':createdat,'updatedat':updatedat}
#         finalop.append(mycred)
#     dbc.close()
#
#     lastfinalop = {'status' : 200,
#                 'students' : finalop}
#     return lastfinalop
#
# @app.route('/', methods=['GET', 'POST'])
# def saninfo():
#     if (request.method == 'GET'):
#         mobilenum = "9986019197"
#         return jsonify({'Mobile Number': mobilenum,
#                         'companyname':'CG',
#                         'username':'santhoh',
#                         'password':'San@123'})

@app.route('/students_back', methods=['GET', 'POST'])
def studentsinfo_back():
    if (request.method == 'GET'):
        return jsonify({
            'status' : 200,
            'students' : [{
                'id' : 1,
                'name' : 'santhosh',
                'email' : 'santhosh@gmail.com',
                'phone' : '7411694426',
                'createdat' : '',
                'updatedat' : '',
                'course' : 'React'
            },

                {
                    'id': 2,
                    'name': 'Gayathri',
                    'email': 'gayathri@gmail.com',
                    'phone': '7826373688',
                    'createdat': '',
                    'updatedat': '',
                    'course': 'Python'
                },

                {
                    'id': 3,
                    'name': 'Pallavi',
                    'email': 'pallavi@gmail.com',
                    'phone': '5237388390',
                    'createdat': '',
                    'updatedat': '',
                    'course': 'Frontend'
                },

                {
                    'id': 4,
                    'name': 'Salina',
                    'email': 'salina@gmail.com',
                    'phone': '9374746447',
                    'createdat': '',
                    'updatedat': '',
                    'course': 'Frontend'
                }

            ]
        })


# @app.route('/students', methods=['GET', 'POST'])
# def studentsinfo():
#     if (request.method == 'GET'):
#         result = createdictdata()
#         return jsonify(result)
#
#
# @app.route('/savestudents', methods=["POST"])
# def add_guide():
#     name = request.json['name']
#     email = request.json['email']
#     phone = request.json['phone']
#     course = request.json['course']
#     print(name,email,phone,course)
#
#     #inserting the data in to database
#
#     db = p.connect(host='localhost', user='root', password='root', db='santhosh')
#     print("connected successfully")
#     mypage = db.cursor()
#
#     sqlq = "INSERT INTO studentsdata (name, email, phone , course) VALUES (%s,%s,%s,%s)"
#     val = (name, email, phone, course)
#     mypage.execute(sqlq, val)
#     db.commit()
#     db.close()
#
#     return "success"
#
#
# @app.route('/prajwal', methods=['GET','POST'])
# def prajwalinfo():
#     return jsonify({'name':'Prjwal raj',
#                     'married':'no',
#                     'age':'25',
#                     'email':'prajwal@gmail.com'})
#
#
# @app.route('/gayathriwebsite', methods=['GET','POST'])
# def gayathriwebsite():
#     return jsonify({'name':'Apple Iphone',
#                     'price':150000,
#                     'model':'2627AD',
#                     'color':'black'})
#
#
#
# @app.route('/getdbdata', methods=['GET','POST'])
# def getcount():
#     dbc = p.connect(host = 'localhost', user = 'root', password = 'root', db = 'santhosh')
#     mycursor = dbc.cursor()
#     q1 = 'select * from login where id in (1,5,9);'
#     mycursor.execute(q1)
#     res = mycursor.fetchall()
#     # print(res)
#     # count = res[0][0]
#     dbc.close()
#     return jsonify({'reccount' : res})
#
#
# @app.route('/getcred/<int:num>', methods=['GET'])
# def getcred(num):
#     dbc = p.connect(host='localhost', user='root', password='root', db='santhosh')
#     mycursor = dbc.cursor()
#     q1 = 'select * from login where id = ' + str(num) + ';'
#     mycursor.execute(q1)
#     res = mycursor.fetchall()
#     print(res)
#     username = res[0][2]
#     password = res[0][3]
#     mycred = {'user':username, 'password': password}
#     dbc.close()
#     return jsonify({
#                     'username = ': username,
#                     'password = ': password
#                     })
if __name__ == '__main__':
    app.run(debug=True)
