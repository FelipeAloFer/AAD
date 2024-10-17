import mysql.connector
try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="usuario", # tu usuario MySQL
    password="usuario", # tu contraseña MySQL
    database="Felipe2DAM" # la base de datos
)
    with conexion.cursor() as cursor:
        cursor.callproc('contar_peliculas_y_mayores_que', [8])
        for resultado in cursor.stored_results():
            print(resultado.fetchall())
except mysql.connector.Error as e:
    print(f'Error {e}')