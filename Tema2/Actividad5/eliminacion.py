import pymysql
from pymysql import MySQLError

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
    
    # Actualiza la edad del actor con nombre 'Iván'
    cursor.execute("DELETE from actores WHERE nombre = 'Iván';")

    conexion.commit()

    print(cursor.rowcount, "registro(s) actualizado(s)")
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")
