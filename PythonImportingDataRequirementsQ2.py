# SOLUTION FOR Python Importing Data Requirements: 1.2
# Import the payslip items into income vs expense table (OOP Model)

import pandas as pd
from config import *

class IncomeVsExpense:
    def __init__(self, expenseFile, incomeFile, updatedb=False):
        self.expenseFile = expenseFile
        self.incomeFile = incomeFile
        self.updatedb = updatedb
        self.oldExpenses = pd.read_csv(self.incomeFile, header=None, index_col=0, squeeze=True).to_dict()

    # Get expense list from the datafile(Python Developer Assessment v1.csv)
    def getExpensesFromDataFile(self):
        expensesFromDataFile = []
        with open(self.expenseFile, 'r') as file:
            next(file)
            for line in file.readlines():
                EmployerID, EmployeeNumber, EmployeeLastName, EmployeeFirstName, EmployeeDoB, PayslipItemCode, PayslipItemDescription, PayslipItemAmount, EmployeeTerminated = line.rstrip().split('|')
                expensesFromDataFile.append(PayslipItemCode)

                # Add payslip item codes to database if connection is successfull
                if cursor != "" and self.updatedb == True:
                    cursor.execute("INSERT INTO employeeDetails (EmployerID, EmployeeNumber, EmployeeLastName, EmployeeFirstName, EmployeeDoB, PayslipItemCode, PayslipItemDescription, PayslipItemAmount, EmployeeTerminated) SELECT ?,?,?,?,?,?,?,?,? WHERE NOT EXISTS (SELECT * FROM employeeDetails WHERE CONCAT_WS('',EmployeeNumber,PayslipItemCode) = 'PK_Employee')",(EmployerID, EmployeeNumber, EmployeeLastName, EmployeeFirstName, EmployeeDoB, PayslipItemCode, PayslipItemDescription, PayslipItemAmount, EmployeeTerminated))
                    cnxn.commit()

            # Remove duplicates
            expensesFromDataFile = list(dict.fromkeys(expensesFromDataFile))
            return expensesFromDataFile


    # Create new expenses for the lookup table using ExpensesFromDataFile
    def createNewExpenses(self):

        # Remove duplicates if any
        newExpenses = {}
        for expense in self.getExpensesFromDataFile():
            if expense not in self.oldExpenses.keys():
                newExpenses[expense] = 'New'

        return newExpenses


    # Get income list from PayslipItemCodeTypes.csv
    def GetIncomes(self):
        newIncomes = []
        for key, value in self.oldExpenses.items():
            if value == 'TRUE':
                newIncomes.append(key)
        return newIncomes


    # Display the income vs expense table
    def displayIncomeVsExpenseTable(self):
        df = pd.DataFrame({'Income' : pd.Series(self.GetIncomes()), 'Expense' : pd.Series(list(self.createNewExpenses().keys()))})
        print(df)


obj = IncomeVsExpense('Python Developer Assessment v1.csv', 'PayslipItemCodeTypes.csv') # With optional argument to update DB

# Uncomment below to see results
#obj.displayIncomeVsExpenseTable()