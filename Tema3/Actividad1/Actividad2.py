from peewee import MySQLDatabase, CharField, IntegerField, Model, PrimaryKeyField

# Configuración de la base de datos
db = MySQLDatabase(
    '1dam',  # Nombre de la base de datos
    user='usuario',  # Nombre de usuario para la base de datos
    password='usuario',  # Contraseña del usuario
    host='localhost',  # Servidor de la base de datos
    port=3306  # Puerto donde escucha MySQL (3306 es el predeterminado)
)

# Conectarse a la base de datos
db.connect()
print("Conexión exitosa a la base de datos\n")

# La clase Peliculas define cómo será la estructura de la tabla en la base de datos
class Peliculas(Model):
    id_pelicula = PrimaryKeyField()  # Clave primaria que se auto-incrementa
    nombre = CharField()  # Campo de tipo cadena
    genero = CharField()  # Campo de tipo cadena
    director = CharField()  # Campo de tipo cadena
    valoracion = IntegerField()  # Campo de tipo entero para la valoración (0-10)

    class Meta:
        database = db
        db_table = 'peliculas'  # Nombre de la tabla en la base de datos

def tarea1():
    print("Tarea 1\n")
    print("Peliculas con valoracion 10\n")
    peliculas_valoracion10 = Peliculas.select().where(Peliculas.valoracion == 10)
    for pelicula in peliculas_valoracion10:
        print(f"Id: {pelicula.id_pelicula}, Nombre: {pelicula.nombre}, Valoración: {pelicula.valoracion}")

def tarea2():
    print("Tarea 2\n")

    peliculas = Peliculas.select()
    for pelicula in peliculas:
        print(f"Id: {pelicula.id_pelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Director: {pelicula.director}, Valoración: {pelicula.valoracion}")

    pelicula_inception = Peliculas.delete().where((Peliculas.genero == 'Acción') & (Peliculas.valoracion == 9))
    pelicula_eliminada = pelicula_inception.execute()
    print("\nPelicula con genero = 'Acción' y valoracion = '9' eliminada con exito\n")

    peliculas = Peliculas.select()
    for pelicula in peliculas:
        print(f"Id: {pelicula.id_pelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Director: {pelicula.director}, Valoración: {pelicula.valoracion}")

def tarea3():
    print("Tarea 3\n")
    peliculas_valoracion10 = Peliculas.delete().where(Peliculas.valoracion == 10)
    peliculas_eliminada = peliculas_valoracion10.execute()
    print("Peliculas con valoracion 10 eliminadas con exito\n")

    peliculas = Peliculas.select()
    for pelicula in peliculas:
        print(f"Id: {pelicula.id_pelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Director: {pelicula.director}, Valoración: {pelicula.valoracion}")


tarea1()
print("\n")
tarea2()
print("\n")
tarea3()