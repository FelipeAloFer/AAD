import pymysql
from pymysql import MySQLError

try:
    conexion = pymysql.connect(       # Conexión a la base de datos con PyMySQL
        host='localhost',
        user='usuario',
        password='usuario',
        database='Felipe2DAM'
    )
    
    if conexion.open:
        print("Conexión a la base de datos exitosa")
    
    cursor = conexion.cursor()
    sql = "SELECT * FROM peliculas"
    cursor.execute(sql)
    
    resultados = cursor.fetchall()     # El metodo fetchall() sirve para recoger los datos despues de hacer una consulta
    
    for fila in resultados:      # Imprimimos los resultados
        print(fila)
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")
