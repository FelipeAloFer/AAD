import pymysql
import time
from pymysql import MySQLError

start_time = time.time()

try:
    conexion = pymysql.connect(       # Conexión a la base de datos
        host='localhost',
        user='usuario',
        password='usuario',
        database='prueba_pymysql'
    )
    
    if conexion.open:
        print("Conexión a la base de datos exitosa")
    
    cursor = conexion.cursor()
    sql = "INSERT INTO peliculas (nombre, genero, director, valoracion) values ('Torrente 4','Accion, Comedia', 'Santiago Segura', 8);"
    
    for i in range(10000):
        cursor.execute(sql)
        print("Insercion ", i)
    

except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")

end_time = time.time()
print(f"Tiempo de inserción con pymysql: {end_time - start_time} segundos")
