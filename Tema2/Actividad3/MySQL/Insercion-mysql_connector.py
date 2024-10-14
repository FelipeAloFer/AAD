import mysql.connector
import time
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(             # Conexión a la base de datos con PyMySQL
    host='localhost',
    user='usuario',
    password='usuario',
    database='prueba_pymysql'
)
    
    start_time = time.time()

    if conexion.is_connected():
        print("Conexión a la base de datos exitosa")

    cursor = conexion.cursor()
    sql = "INSERT INTO peliculas (nombre, genero, director, valoracion) values ('Torrente 4','Accion, Comedia', 'Santiago Segura', 8);"
    
    for i in range(10000):
        cursor.execute(sql)
        print("Insercion ", i)
except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

end_time = time.time()
print(f"Tiempo de inserción con mysql-connector: {end_time - start_time} segundos")
