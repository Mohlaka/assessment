import pyodbc

# SQL Server connection
cursor = ""
try:
    server='psi-assessments.database.windows.net'
    database='charles_mohlaka'
    username='charles'
    password='x7zzB9ca=*CtW6-F'
    driver='ODBC Driver 17 for SQL Server'

    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
except:
    print("Database is not connected.")