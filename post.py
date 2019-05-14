import pg

conn = pg.connect(dbname = 'postgres', user = 'postgres', passwd = 'proyectos')

consulta = 'select * from table;'

resultado = conn.query(consulta)

conn.close()

print resultado
