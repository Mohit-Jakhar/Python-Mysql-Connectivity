import mysql.connector
mydb=mysql.connector.connect(host=”localhost”,user=”root”,passwd=”12345”)
mycursor=mydb.cursor()
mycursor.execute(“Show Databases”)
for x in mycursor:
	print(x)
