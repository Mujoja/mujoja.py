import sqlite3

conn = sqlite3.connect('test.db')
print("Successfully")

conn.execute("INSERT INTO TEACHERS VALUES(1,'James','Martin',45,560000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(2,'Dawn','Lucian',55,660000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(3,'Nicky','Grey',35,760000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(4,'Ricky','Gregory',25,860000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(6,'Dicky','Luis',49,960000.00)")
conn.execute("INSERT INTO TEACHERS VALUES(7,'Alice','Wonderland',45,1060000.00)")

conn.commit()
print("Successfully")
conn.close()