# from flask import Flask, jsonify, request
# import json
# import pymysql as p
# # creating a Flask app
#
# # fdata = open('data.json', 'r')
# # jsondata = json.load(fdata)
# # fdata.close()
# #
# # print(jsondata)
#
#
# # def extractDBdata(cnt):
# #     mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
# #     mycursor = mydb.cursor()
# #
# #     queries = 'select count(*) from city where countrycode = "' + str(cnt) + '";'
# #
# #     mycursor.execute(queries)
# #     res = mycursor.fetchall()
# #
# #     mydb.close()
# #     return res
#
# def getweatherdata(cnt):
#     mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
#     mycursor = mydb.cursor()
#
#     queries = 'select temperature from weather where country = "' + str(cnt) + '";'
#
#     mycursor.execute(queries)
#     res = mycursor.fetchall()
#     print(res)
#     mydb.close()
#     return res
#
#
#
# app = Flask(__name__)
#
#
#
# # @app.route('/', methods=['GET', 'POST'])
# # def home():
# #     if (request.method == 'GET'):
# #         mobilenum = "8220522238"
# #         return jsonify({'Mobile Number': mobilenum,
# #                         'companyname':'ABCD'})
# #
# # @app.route('/stock', methods=['GET', 'POST'])
# # def stock():
# #     if (request.method == 'GET'):
# #         return jsonify({'icici': 1000,
# #                         'hdfc':1200,
# #                         'yes' : 12})
#
#
#
# # @app.route('/home/<int:num>', methods=['GET'])
# # def disp(num):
# #     print(type(num))
# #     ''' extrat the data from json file'''
# #     return jsonify({'DB data =  ': jsondata[str(num)]})
# #
# # @app.route('/getdbdata/<string:cnt>', methods=['GET'])
# # def dbdata(cnt):
# #     print(cnt , type(cnt))
# #     ''' extrat the data from json file'''
# #     res = extractDBdata(cnt)
# #     return jsonify({'DB data =  ': res})

# from flask import Flask, jsonify, request
# import json
# import pymysql as p
#
# @app.route('/weather', methods=['GET'])
# def weatherdata(cnt):
#     print(cnt)
#     ''' extrat the data from database file'''
#     res = getweatherdata(cnt)
#     return jsonify({'DB data =  ': res})
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
# def getweatherdata(cnt):
#     mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
#     mycursor = mydb.cursor()
#
#     queries = 'select temperature from weather where country = "' + str(cnt) + '";'
#
#     mycursor.execute(queries)
#     res = mycursor.fetchall()
#     print(res)
#     mydb.close()
#     return res
#
#
#
# app = Flask(__name__)
# @app.route('/weather', methods=['GET'])
# def weatherdata(cnt):
#     print(cnt)
#     ''' extrat the data from database file'''
#     res = getweatherdata(cnt)
#     return jsonify({'DB data =  ': res})
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify, request
import pymysql as p

app = Flask(__name__)


def getweatherdata(cnt):
    try:
        mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
        mycursor = mydb.cursor()

        # Using a parameterized query to prevent SQL injection
        query = 'SELECT temperature FROM weather WHERE country = %s'
        mycursor.execute(query, (cnt,))

        res = mycursor.fetchall()
        mydb.close()

        if res:
            return {'temperature_data': res}
        else:
            return {'message': 'No data found for the specified country.'}

    except p.MySQLError as e:
        print(f"Error: {e}")
        return {'error': 'Database error occurred'}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {'error': 'An unexpected error occurred'}


@app.route('/weather', methods=['GET'])
def weatherdata():
    cnt = request.args.get('cnt')  # Get 'cnt' from query parameters
    if not cnt:
        return jsonify({'error': 'Country code is required'}), 400

    print(cnt)  # Debug print
    res = getweatherdata(cnt)
    return jsonify({'DB data': res})


if __name__ == '__main__':
    app.run(debug=True)
