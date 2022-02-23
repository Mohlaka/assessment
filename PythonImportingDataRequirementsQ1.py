# SOLUTION FOR Python Importing Data Requirements: 1.1
# Lookup table using Pandas module (OOP Model)

import sys
sys.path.append("/")
from config import *
from PythonImportingDataRequirementsQ2 import IncomeVsExpense, pd  # For new expenses and datafile

class MyLookupTable:
    # Constructor method
    def __init__(self, csvFile, key=None):
        self.csvFile = csvFile
        self.key = key
    
    # Lookup table function
    def createLookupTable(self):
        self.lookupTable = pd.read_csv(self.csvFile, header=None, skiprows=1, index_col=0, squeeze=True).to_dict()

        # Remove duplicates if any
        uniqueLookupTable = {}
        for key, val in self.lookupTable.items():
            if val not in uniqueLookupTable:
                uniqueLookupTable[key] = val

                # Add payslip item codes to database if connection is successfull
                if cursor != "":
                    cursor.execute('INSERT INTO PayslipItemCodes (PayslipItemCode) SELECT ? WHERE NOT EXISTS (SELECT PayslipItemCode FROM PayslipItemCodes WHERE PayslipItemCode = ?)',(key, key))
                    cnxn.commit()
        
        return uniqueLookupTable

    # Display lookup table
    def displayLookupTable(self):
        if self.key != None:
            print(self.createLookupTable()[self.key])
        else:
            print(self.createLookupTable())

    # Code for displaying with new expenses

    def displayWithNewExpenses(self, Expensefile, key=None):
        newLookup = obj.createLookupTable()

        newClass = IncomeVsExpense(Expensefile, self.csvFile)
        newExp = newClass.createNewExpenses()
        TableWithNewExpenses = {**newLookup, **newExp}
        if key != None:
            print(TableWithNewExpenses[key])
        else:
            print(TableWithNewExpenses)



# Lookup table for 38 from PayslipItemCodeTypes.csv
obj = MyLookupTable('PayslipItemCodeTypes.csv') # Optional key argument
obj.displayLookupTable()


# Uncomment below for Lookup table With more rows rom datafile(Python Developer Assessment v1.csv)
#obj = MyLookupTable('PayslipItemCodeTypes.csv')
#obj.displayWithNewExpenses('Python Developer Assessment v1.csv') # Optional key argument 