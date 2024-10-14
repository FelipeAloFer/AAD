import pymysql
import time
from pymysql import MySQLError

start_time = time.time()

try:
    conexion = pymysql.connect(       # Conexión a la base de datos
        host='localhost',
        user='usuario',
        password='usuario',
        database='Felipe2DAM'
    )
    
    if conexion.open:
        print("Conexión a la base de datos exitosa")
    
    cursor = conexion.cursor()
    sql = "SELECT * FROM peliculas"
    
    for i in range(10000):
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Lectura ", i)
    

except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")

end_time = time.time()
print(f"Tiempo de lectura (4 registros) con pymysql: {end_time - start_time} segundos")
