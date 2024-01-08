import pyodbc

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC960;DATABASE=app1;UID=app1user;PWD=student')
cursor = connection.cursor()

SQLCommand = ("SELECT * FROM ovoce;")
cursor.execute(SQLCommand)
for row in cursor:
    print("row = %r" % (row,))
