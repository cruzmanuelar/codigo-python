import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="",
    password="",
    database="basedatos"
)
mycursor = mydb.cursor()

def query_data():

    try:
        print('Seleccione la accion a realizar:')
        print('1. Buscar por nombre')
        print('2. Buscar por apellido')
        option = int(input('->'))
        value = ''

        if(option == 1):
            sql = "SELECT * FROM personas WHERE nombre = %s" 
            value = input('Ingrese el nombre: ')
        elif(option == 2):
            sql = "SELECT * FROM personas WHERE apellido = %s" 
            value = input('Ingrese el apellido:')
        else:
            print('Opcion no valida')
            return
        
        values = (value, )
        mycursor.execute(sql, values)

        data = mycursor.fetchall()

        if(data):
            print('--------Registros encontrados--------')
            for dat in data:
                print(f'Nombre: {dat[1]}')
                print(f'Apellido: {dat[2]}')
                print(f'Edad: {dat[3]}')
                print('---------------------------')
        else:
            print('No se encontraron registros')
    except ValueError:
        print('Ha ocurrido un error con el tipo de dato ingresado')
    except Exception as err:
        print('Ha ocurrido un error al ejecutar el programa')
    
query_data()