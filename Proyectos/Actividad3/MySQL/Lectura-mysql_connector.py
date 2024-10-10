import mysql.connector
import time
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(         # Conexión a la base de datos
    host='localhost',
    user='usuario',
    password='usuario',
    database='Felipe2DAM'
)
    
    start_time = time.time()

    if conexion.is_connected():
        print("Conexión a la base de datos exitosa")

    cursor = conexion.cursor()
    sql = "SELECT * FROM peliculas"
    
    for i in range(10000):
        cursor.execute(sql)
        result = cursor.fetchall()
        print("Lectura ", i)

except Error as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")

end_time = time.time()
print(f"Tiempo de lectura con mysql-connector (4 registros): {end_time - start_time} segundos")
