import psycopg2, psycopg2.extras

n1 = 0.1
n2 = 0.2
ope = '+'
answer = 0.3
conn = psycopg2.connect(database='test',user='postgres',password='samuel', host='localhost')

cur = conn.cursor()
cur.execute("CREATE TABLE Calculadora(n1 character varying(20), operador character, n2 character varying(20), answer character varying)")
#cur.execute("WITH(\nOIDS=FALSE)")
cur.execute("ALTER TABLE Calculadora OWNER TO postgres")

cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
cur.execute("INSERT INTO Calculadora (n1, operador, n2, answer) VALUES ('"+str(n1)+"', '"+str(ope)+"', '"+str(n2)+"', '"+str(answer)+"')")
#rows=cur.fetchall()
#print rows
conn.close()