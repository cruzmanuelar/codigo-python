import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basedatos"
)
mycursor = mydb.cursor()

def query_data():

    try:
        print('-----Insertar nuevo registro-----')
        name        = input('Inserte el nombre: ')
        last_name   = input('Inserte el apellido: ')
        age         = int(input('Inserte la edad: '))        

        sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
        val = (name, last_name, age)

        mycursor.execute(sql, val)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    except ValueError:
        print('Ha ocurrido un error con el tipo de dato ingresado')
    except Exception as err:
        print(err)
        print('Ha ocurrido un error al ejecutar el programa')
    
query_data()