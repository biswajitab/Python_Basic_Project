from flask import Flask, jsonify, request
import json
import pymysql as p
import pandas as pd

# creating a Flask app

# def getexceldata():
#     global newnames
#     df = pd.read_excel('sudeep.xlsx')
#     names = list(df['name'])
#     newnames = ','.join(names)
#     print(newnames)

#
# pincodes = list(df['pincode'])
# pincodestemp = [str(x) for x in pincodes]
# newpincodes = ','.join(pincodestemp)

# fdata = open('data.json', 'r')
# jsondata = json.load(fdata)
# fdata.close()
#
# def getdbdata():
#     dbc = p.connect(host='localhost',user='root',password='root',database='santhosh')
#     print("connected ")
#     mycursor = dbc.cursor()
#     query = 'select * from stockprices'
#     mycursor.execute(query)
#     result = mycursor.fetchall()
#
#     sharepricesinfo = {}
#     for x in result:
#         sharepricesinfo[x[1]] = x[0]
#
#     dbc.close()
#     return sharepricesinfo






# create one constantly runnung process
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if (request.method == 'GET'):
        mobilenum = "9080037252"
        return jsonify({'Mobile Number': mobilenum,
                        'companyname':'TechMahindra',
                        'username':'Purushotham',
                        'password':'Psh@123'})


# @app.route('/mypersinfo', methods=['GET', 'POST'])
# def mypersinfo():
#     return jsonify({'Name': 'santhosh',
#                     'companyname': 'Cerner',
#                     'username': 'sandy123',
#                     'password': 'san@123',
#                     'city': 'Blr',
#                     'salary': '6300000'
#                     })
#
#
# @app.route('/stock', methods=['GET', 'POST'])
# def stock():
#     if (request.method == 'GET'):
#         return jsonify({'icici': 1000,
#                         'hdfc':1200,
#                         'sbi' : 1600})
#
#
#
# @app.route('/getshareprice', methods=['GET', 'POST'])
# def getshareprice():
#     result = getdbdata()
#     return jsonify((result))
#
# @app.route('/biodata', methods=["GET"])
# def biodata():
#     if (request.method == 'GET'):
#         return jsonify({'Name': 'Vaishnavi',
#                         'age': 21,
#                         'place' : 'bangalore',
#                         'education' : 'BE',
#                         'Working' : 'trying',
#                         'mobilenum' : 'speak t o my dad',
#                         'height' : 'shutup',
#                         'weight' : 'u can lift me for sure'})
#
#
#
# @app.route('/metals', methods=['GET', 'POST'])
# def metals():
#     if (request.method == 'GET'):
#         return jsonify({'gold': 58000,
#                         'siler':67000,
#                         'daimond' : 80000})
#
#
#
# @app.route('/electronics', methods=['GET', 'POST'])
# def electronics():
#     if (request.method == 'GET'):
#         return jsonify({'TV': {'price' : 50000,'comp':'SAMSUNG'},
#                         'Fridge': {'price' : 50000,'comp':'LG'},
#                         'Hometheatre' : {'price' : 23000,'comp':'SONY'}})
#
#
# @app.route('/getnames', methods=['GET', 'POST'])
# def getnames():
#     if (request.method == 'GET'):
#         getexceldata()
#         return jsonify({'names' : newnames})
#
#
# @app.route('/getpincode', methods=['GET', 'POST'])
# def getpincode():
#     if (request.method == 'GET'):
#         return jsonify({'pincodes' : newpincodes})


#
# @app.route('/home/<int:num>', methods=['GET'])
# def disp(num):
#     print(type(num))
#     ''' extrat the data from json file'''
#     return jsonify({'DB data =  ': jsondata[str(num)]})



if __name__ == '__main__':
    app.run(debug=True)