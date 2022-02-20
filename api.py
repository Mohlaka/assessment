from textwrap import wrap
from flask import Flask, make_response, request
from flask_restful import Api, Resource, abort
import pyodbc
from config import *
from PythonImportingDataRequirementsQ2 import IncomeVsExpense

# Initializing Flask and wrap out app with Api
app = Flask(__name__)
api = Api(app)

# Create a class object wich will allow us access external class methods
newClass = IncomeVsExpense('Python Developer Assessment v1.csv', 'PayslipItemCodeTypes.csv')

def auth_required(f):
    @wrap(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'username' and auth.password == 'password':
            return f(**args, **kwargs)
        return make_response('Could not verify your login!', 404, {'WWW-Authentication': 'Basic realm="Login Reguired"'})
    return decorated

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

if __name__ == '__main__':
    app.run(debug=True)