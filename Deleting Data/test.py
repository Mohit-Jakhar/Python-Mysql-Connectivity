import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",passwd="12345",database="school")
cursor=db.cursor()
s=("DELETE FROM STUDENT WHERE NAME='Ankush' ")
cursor.execute(s)
print("RECORD DELETED")
db.commit()
