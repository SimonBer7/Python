import pyodbc


def insert_into_db(ovoce):

    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=PC960;DATABASE=app1;UID=app1user;PWD=student')
    cursor = connection.cursor()

    SQLCommand = ("INSERT INTO ovoce (nazev) VALUES ('"+ovoce+"');")
    cursor.execute(SQLCommand)

    connection.commit()
    print("Data Successfully Inserted")
    connection.close()




ovoce = input("Zadej ovoce: ")
insert_into_db(ovoce)












