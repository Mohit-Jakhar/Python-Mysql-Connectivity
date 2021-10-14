import mysql.connector
db=mysql.connector.connect(host='localhost',user='root',password='12345',database='school')
cur = db.cursor()
cur.execute("insert into stud values('1011','Ritu','XI','A', 'Gurgaon', '9999210223')")
cur.execute("insert into stud values('1003', 'Pihu', 'XII', 'B', 'Palam, '9876210223')")
cur.execute("insert into stud values('1008','Neha','XI', 'B', 'Delhi', '9998752221')")
db.commit()
