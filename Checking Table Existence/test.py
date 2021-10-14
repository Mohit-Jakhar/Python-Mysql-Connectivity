import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="12345",database="railyatri")
mycursor = mydb.cursor()
mycursor.execute("Show Tables")
for x in mycursor:
         print(x)

