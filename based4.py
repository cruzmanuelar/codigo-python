import mysql.connector
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="basedatos"
)
mycursor = mydb.cursor()

def query_data():

    try:
        insert_row = 1
        while insert_row == 1 or insert_row == "1":

            print('-----Insertar nuevo registro-----')
            name        = input('Inserte el nombre: ')
            last_name   = input('Inserte el apellido: ')
            age         = int(input('Inserte la edad: '))        

            sql = "INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)"
            val = (name, last_name, age)

            mycursor.execute(sql, val)
            mydb.commit()
            clear()
            print(f"**Se ha insertado {mycursor.rowcount} registro correctamente**")
            insert_row = input("\nInserte '1' para insertar otro registro: ")

    except ValueError:
        print('Ha ocurrido un error con el tipo de dato ingresado')
    except Exception as err:
        print(err)
        print('Ha ocurrido un error al ejecutar el programa')
    
query_data()