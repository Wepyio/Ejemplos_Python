import psycopg2, psycopg2.extras
conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')

cur = conn.cursor()
cur.execute("SELECT * FROM estudiante")
cur.execute("ALTER TABLE calcu\nRENAME COLUMN numero1 to n1;")
#rows=cur.fetchall()
#print rows
conn.commit()
conn.close()