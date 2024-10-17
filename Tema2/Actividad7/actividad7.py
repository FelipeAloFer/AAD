import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL usando el conector oficial
conexion = None
try:
    # Conectar a la base de datos
    conexion = mysql.connector.connect(
    host="localhost",
    user="usuario", # tu usuario MySQL
    password="usuario", # tu contraseña MySQL
    database="Felipe2DAM" # la base de datos donde está la tabla Peliculas
    )
    
    if conexion.is_connected():
        # Crear un cursor
        cursor = conexion.cursor()
        
        # Iniciar la transacción
        print("Iniciando transacción...")
        
        # Insertar un nuevo registro en la tabla Peliculas
        sql_insert = """
        INSERT INTO peliculas (nombre, genero, director, valoracion) 
        VALUES (%s, %s, %s, %s)
        """

        datos_pelicula = ("", "", "", "8a")

        cursor.execute(sql_insert, datos_pelicula)

        # Hacer commit si todo va bien
        conexion.commit()
        print("Transacción exitosa: Registro insertado correctamente.")

except Error as e:
    # Si ocurre un error, hacer rollback
    print(f"Error en la transacción: {e}")
    if conexion:
        conexion.rollback()
        print("Se realizó rollback.")
finally:
    # Cerrar el cursor y la conexión si están abiertos
    if conexion and conexion.is_connected():
        cursor.close()
        conexion.close()
        print("Conexión cerrada.")