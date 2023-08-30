import psycopg2 as sql

con = sql.connect(host='localhost', database='Almox Control',
user='postgres', password='z78e02xa', port='5432')
cur = con.cursor()
insert = "INSERT INTO colaboradores  VALUES (2,'Moises teste2','00002','Seco',false,false)"
cur.execute(insert)
con.commit()