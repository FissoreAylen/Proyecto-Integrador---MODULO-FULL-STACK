import mysql.connector # Con MariaDB

class Connect:
    
    def __init__(self) -> None:
        try:
            self.conn = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = 'root',
                db = 'mi_base'
            )
        except mysql.connector.Error as e:
            print("No se pudo conectar!", e)

# CRUD: CREATE.

    def InsertarValor(self,nombre, direccion, mail):
        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta = f"""INSERT INTO mi_base (nombre, direccion, mail) VALUES('{nombre}','{direccion}','{mail}')"""
                cursor.execute(consulta)
                
                self.conn.commit()
                self.conn.close()

            except:
                print("Ocurrio un error!")
   
# CRUD: READ.

    def BuscarObjeto(self):
#     def BuscarObjeto(self, nombre):
        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta= f"""SELECT * FROM mi_base"""
#                 consulta= f"""SELECT * FROM mi_base WHERE nombre = '{nombre}';"""
                cursor.execute(consulta)
                resultSet = cursor.fetchall()
                
                self.conn.close()
                return resultSet

            except:
                print("Ocurrio un error!")
               
# CRUD: UPDATE.

    def ActualizarDatosNombre(self, identificador, nombre):

        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta = f"""UPDATE mi_base SET nombre = '{nombre}' WHERE id = {identificador}"""
                cursor.execute(consulta)

                self.conn.commit()                
                self.conn.close()
            
            except:
                print("Ocurrio un error!")
                
    def ActualizarDatosDireccion(self, identificador, direccion):

        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta = f"""UPDATE mi_base SET direccion = '{direccion}' WHERE id = {identificador}"""
                cursor.execute(consulta)

                self.conn.commit()
                self.conn.close()
            
            except:
                print("Ocurrio un error!")
                
    def ActualizarDatosMail(self, identificador, mail):

        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta = f"""UPDATE mi_base SET mail = '{mail}' WHERE id = {identificador}"""
                cursor.execute(consulta)

                self.conn.commit()
                self.conn.close()
                
            except:
                print("Ocurrio un error!")
                
# CRUD: DELETE.
                
    def EliminarObjeto(self,ID):
        if self.conn.is_connected():
            try:
                cursor = self.conn.cursor()
                consulta = f"""DELETE FROM mi_base WHERE id = {ID}"""
                cursor.execute(consulta)

                self.conn.commit()
                self.conn.close()
                
            except:
                print("Ocurrio un error!")
            
while True:
    print('QUE OPERACION DECEA REALIZAR?\n')
    print('Ingrese "1" para leer')
    print('Ingrese "2" para agregar')
    print('Ingrese "3" para actualizar')
    print('Ingrese "4" para borrar')
    print('Ingrese "5" para salir\n')
    operacion = input('Operación N: ')
    if operacion == '1':
        
        
#         nombre = input('Ingrese su nombre: ')
#         objeto = Connect().BuscarObjeto(nombre)
        objeto = Connect().BuscarObjeto()
        for obj in objeto:
            print('\nID________: ' + str(obj[0]))
            print('Nombre____: ' + obj[1])
            print('Dirección_: ' + obj[2])
            print('Mail______: ' + obj[3]+'\n')
            
            
    elif operacion == '2':
        nombre = input('Ingrese su nombre: ')
        direccion = input('Ingrese su direccion: ')
        mail = input('Ingrese su mail: ')
        Connect().InsertarValor(nombre, direccion, mail)
    elif operacion == '3':
        try:
            columna = input('Que columna decea actualizar? nombre o direccion o mail o s para salir: ')
            if columna == 'nombre':
                if columna == 's':
                    break
                nombre = input('Ingrese el nuevo nombre: ')
                identificador = int(input('Ingrese el ID: '))
                Connect().ActualizarDatosNombre(identificador, nombre)
            elif columna == 'direccion':
                if columna == 's':
                    break
                direccion = input('Ingrese la nueva dirección: ')
                identificador = int(input('Ingrese el ID: '))
                Connect().ActualizarDatosDireccion(identificador, direccion)
            elif columna == 'mail':
                if columna == 's':
                    break
                mail = input('Ingrese el nuevo mail: ')
                identificador = int(input('Ingrese el ID: '))
                Connect().ActualizarDatosMail(identificador, mail)
            else:
                continue
        except ValueError as e:
                print("Error de Datos!", e)
    elif operacion == '4':
        id = int(input('Ingrese el ID'))
        Connect().EliminarObjeto(id)
    else:
        break

