import pyodbc

# SQL Server connection
cursor = ""
try:
    cnxn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-A3FRRVK;"
    "Database=employeeDB;"
    "Trusted_Connection=yes;")
    cursor = cnxn.cursor()
except:
    print("Database is not connected.")