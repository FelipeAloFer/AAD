import pymysql
import time
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
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS actores (
    id_actor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT NOT NULL,
    nombre_pelicula VARCHAR(50),
    CONSTRAINT fk_nombre_pelicula FOREIGN KEY (nombre_pelicula) REFERENCES peliculas(nombre)
    );""")

    cursor.execute("""INSERT INTO actores (nombre, apellido, edad, nombre_pelicula) VALUES ('Dani', 'Rovira', 40, 'Ocho apellidos vascos');""")

    cursor.execute("""INSERT INTO actores (nombre, apellido, edad, nombre_pelicula) VALUES ('Clara', 'Lago', 33, 'Ocho apellidos vascos');""")

    cursor.execute("""INSERT INTO actores (nombre, apellido, edad, nombre_pelicula) VALUES ('Iván', 'Massagué', 47, 'El hoyo');""")

    cursor.execute("""INSERT INTO actores (nombre, apellido, edad, nombre_pelicula) VALUES ('Marlon', 'Brando', 47, 'El Padrino');""")

    cursor.execute("""INSERT INTO actores (nombre, apellido, edad, nombre_pelicula) VALUES ('Leonardo', 'DiCaprio', 49, 'Titanic');""")

    conexion.commit()
except MySQLError as e:
    print(f"Error de conexión: {e}")
finally:
    if conexion.open:
        conexion.close()
        print("Conexión cerrada")
