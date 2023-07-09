import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basedatos"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS personas"
mycursor.execute(sql) 

# CONSULTA PARA CREAR LA TABLA "personas" con 6 columnas
mycursor.execute("CREATE TABLE personas(id INT(10) NOT NULL AUTO_INCREMENT, nombre VARCHAR(255) NOT NULL, apellido VARCHAR(255) NOT NULL , edad INT(10) NOT NULL ,  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, PRIMARY KEY (id))")

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
