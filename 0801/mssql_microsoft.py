import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC960;DATABASE=app1;UID=app1user;PWD=student')

print("Pripojeno.")

connection.close()
