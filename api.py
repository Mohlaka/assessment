from textwrap import wrap
from flask import Flask, make_response, request, jsonify
from flask_restful import Api, Resource, abort
import pyodbc
from config import *
from PythonImportingDataRequirementsQ2 import IncomeVsExpense
import jwt
import datetime
from functools import wraps

# Initializing Flask and wrap out app with Api
app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'THIS IS THE SECRET KEY'

# Create a class object wich will allow us access external class methods
newClass = IncomeVsExpense('Python Developer Assessment v1.csv', 'PayslipItemCodeTypes.csv')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message' : 'Token is missing.'}), 403

        try :
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message' : 'Token is invalid.'}), 403

        return f(*args, **kwargs)

    return decorated


class ExpenseTypes(Resource):
    def get(self):
        return newClass.createNewExpenses()

class IncomeTypes(Resource): 
    def get(self):
        inccomeListValues = []       
        keys = newClass.GetIncomes()
        for val in keys:
            inccomeListValues.append("TRUE")  
        incomeDictionary = dict(zip(keys, inccomeListValues))
        return incomeDictionary

class ExpenseTypes(Resource):
    def get(self):
        return newClass.createNewExpenses()

class Eployees(Resource):
    def post(self, EmployeeNumber):
        data = []
        rows = cursor.execute("SELECT * FROM employeeDetails WHERE EmployeeNumber = ? FOR JSON PATH, ROOT('Employees');", (EmployeeNumber)).fetchall()
        for row in rows:
            data.append(list(row))
        return data

api.add_resource(IncomeTypes, "/income-types")
api.add_resource(ExpenseTypes, "/expense-types")
api.add_resource(Eployees, "/employees/<int:EmployeeNumber>")


# Authorization using JSON web tokens 
app.route('/login')
def login():
    auth = request.authorization

    if auth == 'admin' and password == 'password':
        token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token' : token.decode('UTF-8')})

    return make_response('Could not verify!', 401, {'WWW-Autheticate' : 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run(debug=True)