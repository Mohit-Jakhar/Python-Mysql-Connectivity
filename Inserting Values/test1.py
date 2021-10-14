import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',psswd='12345',database='school')
cursor=db.cursor()
cursor.execute("INSERT INTO stud VALUES(1001,'Ankush',’XII’,’A’,'Madras',7845965324)")
cursor.execute("INSERT INTO stud VALUES(1002, 'Ritik', 'XII' ,’B’ ,’Chennai’,7984321568)")
db.commit()
print("RECORDS ADDED")
