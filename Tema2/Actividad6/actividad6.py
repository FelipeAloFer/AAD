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
    
    cursor.execute("SELECT * FROM actores;")

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print("\n")

    cursor.execute("SELECT * FROM actores;")

    print("SEGUNDO CURSOR")
    print("\n")

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())

    conexion.commit()

except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")