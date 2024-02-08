import pyodbc
conn= pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Lekcje\ACCESS\ZamowieniaPrzyklad.accdb;')
cursor=conn.cursor()
cursor.execute('SELECT * FROM pracownicy')

for row in cursor.fetchall():
    print(row)
