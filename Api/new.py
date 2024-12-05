# from flask import Flask,jsonify
# app = Flask(__name__)
#
# @app.route('/')
# def biswajit():
#     return 'hello,world'
#
# def getweatherdata(cnt):
#     try:
#         mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
#         mycursor = mydb.cursor()
#
#         # Using parameterized query to prevent SQL injection
#         query = 'SELECT temperature FROM weather WHERE country = %s'
#         mycursor.execute(query, (cnt,))
#
#         res = mycursor.fetchall()
#         mydb.close()
#
#         if res:
#             return {'temperature_data': res}
#         else:
#             return {'message': 'No data found for the specified country.'}
#
#     except p.MySQLError as e:
#         print(f"Error: {e}")
#         return {'error': 'Database error occurred'}
#     except Exception as e:
#         print(f"Unexpected error: {e}")
#         return {'error': 'An unexpected error occurred'}
#
#
# @app.route('/weather/<string:cnt>', methods=['GET'])
# def weatherdata(cnt):
#     print(cnt, type(cnt))
#     res = getweatherdata(cnt)
#     return jsonify(res)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify
import pymysql as p

app = Flask(__name__)

@app.route('/')
def biswajit():
    return 'hello, world'

def getweatherdata(cnt):
    try:
        # Connect to the database
        mydb = p.connect(host='localhost', user='root', password='TRIGER', db='biswajit')
        mycursor = mydb.cursor()

        # Use a parameterized query to prevent SQL injection
        query = 'SELECT temperature FROM weather WHERE country = %s'
        mycursor.execute(query, (cnt,))

        # Fetch all results
        res = mycursor.fetchall()
        mydb.close()

        # Format the result for JSON response
        if res:
            return {'temperature_data': [row[0] for row in res]}  # Convert tuple to list
        else:
            return {'message': 'No data found for the specified country.'}

    except p.MySQLError as e:
        print(f"Database Error: {e}")
        return {'error': 'Database error occurred'}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {'error': 'An unexpected error occurred'}

@app.route('/weather/<string:cnt>', methods=['GET'])
def weatherdata(cnt):
    res = getweatherdata(cnt)
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
