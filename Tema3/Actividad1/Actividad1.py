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

# Función para mostrar el contenido de la tabla
def mostrar_tabla():
    peliculas = Peliculas.select()  # Selecciona todos los registros de la tabla
    for pelicula in peliculas:
        print(f"Id: {pelicula.id_pelicula}, Nombre: {pelicula.nombre}, Género: {pelicula.genero}, Director: {pelicula.director}, Valoración: {pelicula.valoracion}")

# Elimina la tabla 'peliculas' si existe en la base de datos
def eliminar_tabla():
    Peliculas.drop_table()  # Elimina la tabla usando las funcionalidades de Peewee
    print("Tabla eliminada con éxito\n")

# Función para crear la tabla
def crear_tabla():
    Peliculas.create_table()  # Crea la tabla automáticamente en base al modelo Peliculas
    print("Tabla creada con éxito\n")

# Función para insertar datos en la tabla
# Inserta una nueva película en la tabla con los valores proporcionados
def insertar_pelicula(nombre, genero, director, valoracion):
    Peliculas.create(nombre=nombre, genero=genero, director=director, valoracion=valoracion)  # Inserta una nueva fila
    print("Película insertada con éxito")

# Eliminar la tabla
eliminar_tabla()

# Crea la tabla 'peliculas' según la estructura definida en la clase Peliculas
crear_tabla()

# Insertar 5 películas
insertar_pelicula("El Padrino", "Crimen", "Francis Ford Coppola", 10)
insertar_pelicula("Interestelar", "Ciencia ficción", "Christopher Nolan", 9)
insertar_pelicula("Titanic", "Romance", "James Cameron", 8)
insertar_pelicula("Inception", "Acción", "Christopher Nolan", 9)
insertar_pelicula("Matrix", "Ciencia ficción", "The Wachowskis", 10)
print("\n")

# Mostrar las películas
mostrar_tabla()
