import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',passwd='12345',database='school')
cursor=db.cursor()
cursor.execute("SELECT * FROM  STUD")
result=cursor.fetchall()
for x in result:
  print(x)
