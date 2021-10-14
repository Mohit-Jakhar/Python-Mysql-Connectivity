import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',psswd='12345',database='school')
cursor=db.cursor()
s=("UPDATE STUD set contact_no=9754863250 where name='Ankush' ")
cursor.execute(s)
print("RECORD UPDATED")
db.commit()  
