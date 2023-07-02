# CONFIGURACION DE ACCESO A BASE DE DATOS
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="manuel",
    password="manuel",
    database="basedatos"
)

mycursor = mydb.cursor()

# CONSULTA PARA OBTENER Y MOSTRAR LAS TABLAS EN NUESTRA BASE DE DATOS
# *LA CONSULTA BUSCARÁ TABLAS EN LA BASE DE DATOS DEFINIDA EN LA LINEA 8
#mycursor.execute("SHOW TABLES")

#for table_name in mycursor:
#   print(table_name)


# CONSULTA PARA ELIMINAR LA TABLA "personas"
#mycursor.execute("DROP TABLE personas")

#CONSULTA PARA CREAR LA TABLA "personas" con 6 columnas
#mycursor.execute("CREATE TABLE personas(id INT(10) NOT NULL AUTO_INCREMENT, nombre VARCHAR(255) NOT NULL, apellido VARCHAR(255) NOT NULL , edad INT(10) NOT NULL ,  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (id))")

#CONSULTA PARA INSERTAR REGISTROS EN LA TABLA "personas"
query   = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
values  = [
    ("Maxi", "Herrera", 21),
    ("Juan", "Quevedo", 19),
    ("Ivan", "Ruiz", 26),
    ("Silvia", "Hernandez", 25),
    ("German", "Aguirre", 17)
]
mycursor.executemany(query, values)

mydb.commit()

print("Se intertaron ", mycursor.rowcount, " registros")

