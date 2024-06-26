import mysql.connector
from mysql.connector import errorcode
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout

config = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'proyecto1',
  'raise_on_warnings': True
}

def watchMembershipProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verMembresias')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
        return sales_data

def insertMembershipProc(IDMembresiaParam ,tipoParam ,costoParam, estadoParam):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDMembresiaParam ,tipoParam ,costoParam, estadoParam)
        cursorObject.callproc('InsertarMembresia', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Membresia insertada")

def updateMembershipProc(IDMembresiaParam ,tipoParam ,costoParam, estadoParam):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDMembresiaParam ,tipoParam ,costoParam, estadoParam)
        cursorObject.callproc('ActualizarMembresia', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Membresia actualizada")

def deleteMembershipProc(IDMembresiaParam):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDMembresiaParam,)
        cursorObject.callproc('EliminarMembresia', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Membresia eliminada")
   
def watchClassProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verClases')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data

def insertClassProc(IDClase, IDFuncionario, nombre, capacidadMaxima):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDClase, IDFuncionario, nombre, capacidadMaxima)
        cursorObject.callproc('InsertarClase', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Clase insertada")

def updateClassProc(IDClase ,IDFuncionario ,nombre, capacidadMaxima):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDClase ,IDFuncionario ,nombre, capacidadMaxima)
        cursorObject.callproc('ActualizarClase', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Clase actualizada")     

def deleteclaseProc(IDClase):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDClase,)
        cursorObject.callproc('EliminarClase', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Clase eliminada")

def watchClientProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verClientes')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertClientProc(IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
        cursorObject.callproc('InsertarCliente', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Cliente insertado")
def updateClientProc(IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
        cursorObject.callproc('ActualizarCliente', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Cliente actualizado")   

def deleteclientProc(IDCliente):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCliente,)
        cursorObject.callproc('EliminarCliente', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Cliente eliminado")
        
def insertClientProc(IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        try:
            cursorObject = cnx.cursor()
            params = (IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
            cursorObject.callproc('InsertarCliente', params)
            cnx.commit()
            print("Cliente insertado")
        except mysql.connector.errors.DatabaseError as err:
            # Verifica si el mensaje de error contiene "El formato del correo electrónico no es válido."
            if "El formato del correo electrónico no es válido." in str(err):
                print("Error: El formato del correo electrónico no es válido.")
            else:
                print(f"Database error: {err}")
        finally:
            cursorObject.close()
            cnx.close()

def watchPFProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verPuestosFuncionario')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertPFProc(IDPuesto, puesto):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDPuesto, puesto)
        cursorObject.callproc('InsertarPuestoFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Nuevo puesto insertado")

def updatePFProc(IDPuesto, puesto):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDPuesto, puesto)
        cursorObject.callproc('ActualizarPuestoFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Puesto actualizado")

def deletePFProc(IDPuesto):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDPuesto,)
        cursorObject.callproc('EliminarPuestoFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Puesto eliminado")

def watchEmployeeProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verFuncionarios')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertEmployeeProc(IDFuncionario,
puesto ,
nombre ,
apellidol ,
apellido2 ,
NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDFuncionario,
puesto ,
nombre ,
apellidol ,
apellido2 ,
NumeroTelefono)
        cursorObject.callproc('InsertarFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Nuevo funcionario ingresado") 

def updateEmployeeProc(IDFuncionario,
puesto ,
nombre ,
apellidol ,
apellido2 ,
NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDFuncionario,
puesto ,
nombre ,
apellidol ,
apellido2 ,
NumeroTelefono)
        cursorObject.callproc('ActualizarFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Funcionario actualizado")     

def deletePFProc(IDFuncionario):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDFuncionario,)
        cursorObject.callproc('EliminarFuncionario', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Funcionario eliminado")

def watchCityProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verCiudades')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def InsertCiudad(IDCiudad, nombre):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCiudad, nombre)
        cursorObject.callproc('InsertarCiudad', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Ciudad insertada")

def updateCityProc(IDCiudad, nombre):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCiudad, nombre)
        cursorObject.callproc('ActualizarCiudad', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Ciudad actualizada")   

def deleteCityProc(IDCiudad):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDCiudad,)
        cursorObject.callproc('EliminarCiudad', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Ciudad eliminada")

def watchGymProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verGimnasios')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertGym(IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono)
        cursorObject.callproc('InsertarGimnasio', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Gimnasio insertado")

def updateGymProc(IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono)
        cursorObject.callproc('ActualizarGimnasio', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Gimnasio actualizado") 

def deleteGymProc(IDGimnasio):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio,)
        cursorObject.callproc('EliminarGimnasio', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Gimnasio eliminado") 

def watchWorkingProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verTrabajos')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertWorking(IDGimnasio, IDFuncionario):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio, IDFuncionario)
        cursorObject.callproc('InsertarTrabaja', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Funcionario asignado a gimnasio")

def updateWorkingProc(IDGimnasio, IDFuncionario):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio, IDFuncionario)
        cursorObject.callproc('ActualizarTrabaja', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Funcionaroi asignado a gimnasio actualizado") 

def deleteWorkingProc(IDGimnasio, IDFuncionario):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDGimnasio, IDFuncionario)
        cursorObject.callproc('EliminarTrabaja', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Funcionario asignado a gimnasio eliminado")

def watchEquipProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verEquipos')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertEquip(CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
        cursorObject.callproc('InsertarEquipo', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Equipo insertado")

def updateEquipProc(CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
        cursorObject.callproc('ActualizarEquipo', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Equipo actualizado")

def deleteEquipProc(CodigoEquipo):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (CodigoEquipo,)
        cursorObject.callproc('EliminarEquipo', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Equipo eliminado")

def watchProductProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verProductos')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertProductProc(IDProducto, nombre, descripcion, costo):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDProducto, nombre, descripcion, costo)
        cursorObject.callproc('InsertarProducto', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Nuevo producto insertado")

def updateProductProc(IDProducto, nombre, descripcion, costo):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDProducto, nombre, descripcion, costo)
        cursorObject.callproc('ActualizarProducto', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Producto actualizado")
def deleteProductProc(IDProducto):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDProducto,)
        cursorObject.callproc('EliminarProducto', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Producto eliminado")

def watchSaleProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verVentas')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)
    return sales_data
def insertSaleProc(NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad)
        cursorObject.callproc('InsertarVenta', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Nueva venta ingresada")

def updateSaleProc(NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad)
        cursorObject.callproc('ActualizarVenta', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Venta actualizada")

def deleteSaleProc(NumeroTransaccion):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (NumeroTransaccion,)
        cursorObject.callproc('EliminarVenta', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Venta eliminada")

def watchInscriptionProc():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        cursorObject.callproc('verInscripciones')
        
        sales_data = []
        
        for result in cursorObject.stored_results():
            sales_data.extend(result.fetchall())
        
        cursorObject.close()
        cnx.close()
        
        # Mostrar la información en la consola
        for row in sales_data:
            print(row)  
    return sales_data
def insertInscriptionProc(IDClase, IDCliente):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (IDClase, IDCliente)
        cursorObject.callproc('InsertarInscripcion', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Inscripción realizada")

def updateInscriptionProc(codigoInscripcion,IDClase, IDCliente):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (codigoInscripcion, IDClase, IDCliente)
        cursorObject.callproc('ActualizarInscribirse', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Inscripción actualizada")


def deleteInscriptionProc(codigoInscripcion):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursorObject = cnx.cursor()
        params = (codigoInscripcion)
        cursorObject.callproc('EliminarInscripcion', params)
        cnx.commit()
        cursorObject.close()
        cnx.close()
        print("Inscripción eliminada")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def execute_query(query):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cursor = cnx.cursor()
        try:
            cursor.execute(query)
            cnx.commit()
            print("Query executed successfully")
        except mysql.connector.Error as err:
            print("Error executing query:", err)
        finally:
            cursor.close()
            cnx.close()


def crear_trigger_verificar_stock_before_venta():
    query = """
        CREATE TRIGGER verificar_stock_before_venta
        BEFORE INSERT ON Venta
        FOR EACH ROW
        BEGIN
            DECLARE disponible INT;
            
            SELECT Stock INTO disponible
            FROM Producto
            WHERE IDProducto = NEW.IDProducto;
            
            IF disponible < NEW.Cantidad THEN
                SIGNAL SQLSTATE '55000'
                SET MESSAGE_TEXT = 'No hay suficiente stock disponible para realizar la venta';
            END IF;
        END;
    """
    execute_query(query)

def crear_trigger_actualizar_stock_after_crear_venta():
    query ="""
        CREATE TRIGGER actualizar_stock_after_crear_venta
        AFTER INSERT ON Venta
        FOR EACH ROW
        BEGIN
            DECLARE cantidad_vendida INT;
            SELECT NEW.Cantidad INTO cantidad_vendida;
            
        

            UPDATE PRODUCTO
            SET Stock = Stock - cantidad_vendida
            WHERE IDProducto = NEW.IDProducto;
        END;
        """
    execute_query(query) 

def crear_trigger_actualizar_stock_after_eliminar_venta():
       query = """
        CREATE TRIGGER actualizar_stock_after_delete_venta
        BEFORE DELETE ON Venta
        FOR EACH ROW
        BEGIN
            DECLARE cantidad_devuelta INT;
            -- Obtener la cantidad devuelta del producto
            SELECT OLD.Cantidad INTO cantidad_devuelta
            FROM Venta
            WHERE NumeroTransaccion = OLD.NumeroTransaccion;
            
            -- Actualizar el stock del producto
            UPDATE Producto
            SET Stock = Stock + cantidad_devuelta
            WHERE IDProducto = OLD.IDProducto;
        END;
        """
       execute_query(query) 


def crear_trigger_actualizar_monto_venta_despues_actualizacion():
    query = """
    CREATE TRIGGER actualizar_monto_venta_despues_actualizacion
    BEFORE UPDATE ON Venta
    FOR EACH ROW
    BEGIN
        -- Calcula el nuevo monto basado en la nueva cantidad de productos y el precio unitario
        DECLARE nuevo_monto DECIMAL(9, 2);
        SET nuevo_monto = NEW.cantidad * (SELECT costo FROM Producto WHERE IDProducto = NEW.IDProducto);
        
        -- Actualiza el monto en una variable local
        SET NEW.monto = nuevo_monto;
    END;
    """
    execute_query(query) 

def crear_trigger_validar_correo_cliente_before_insert():
    query = """
    CREATE TRIGGER validar_correo_cliente_before_insert
    BEFORE INSERT ON Cliente
    FOR EACH ROW
    BEGIN
        IF NEW.correoElectronico NOT LIKE '%@%.%' THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El formato del correo electrónico no es válido.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_actualizar_correo_cliente():
    query = """
    CREATE TRIGGER crear_trigger_actualizar_correo_cliente
    BEFORE UPDATE ON Cliente
    FOR EACH ROW
    BEGIN
        IF NEW.correoElectronico NOT LIKE '%@%.%' THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'El formato del correo electrónico no es válido.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_eliminar_cliente():
    query = """  
    CREATE TRIGGER before_delete_cliente
    BEFORE DELETE ON Cliente
    FOR EACH ROW
    BEGIN
        DECLARE inscripciones_count INT;

        -- Contamos cuántas inscripciones tiene el cliente que se va a eliminar
        SELECT COUNT(*) INTO inscripciones_count FROM Inscribirse WHERE IDCliente = OLD.IDCliente;

        -- Si el cliente tiene inscripciones, evitamos la eliminación y mostramos un mensaje de error
        IF inscripciones_count > 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar el cliente porque está inscrito en una o más clases.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_insertar_equipo():
    query = """
    CREATE TRIGGER before_insert_equipo
    BEFORE INSERT ON Equipo
    FOR EACH ROW
    BEGIN
        IF NEW.fechaAdquisicion IS NULL THEN
            SET NEW.fechaAdquisicion = CURDATE();
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_eliminar_equipo():
    query = """
    CREATE TRIGGER before_delete_equipo
    BEFORE DELETE ON Equipo
    FOR EACH ROW
    BEGIN
        -- Verificamos si el equipo que se va a eliminar está marcado como activo
        IF OLD.estado = 'D' THEN
            -- Si el equipo está activo, generamos un error y evitamos la eliminación
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar un equipo disponible.';
        END IF;
    END;
    """
    execute_query(query)

def crear_trigger_actualizar_equipo():
    query = """
    CREATE TRIGGER before_update_equipo
    BEFORE UPDATE ON Equipo
    FOR EACH ROW
    BEGIN
        -- Verificamos si la fecha de adquisición está siendo modificada
        IF OLD.fechaAdquisicion <> NEW.fechaAdquisicion THEN
            -- Si la fecha de adquisición está cambiando, generamos un error y revertimos la actualización
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede modificar la fecha de adquisición de un equipo.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_eliminar_gim():
    query = """
    CREATE TRIGGER before_delete_gimn
    BEFORE DELETE ON Gimnasio
    FOR EACH ROW
    BEGIN
        DECLARE trabajos_count INT;

        -- Contamos cuántos registros existen en la tabla Trabaja que hacen referencia al gimnasio que se va a eliminar
        SELECT COUNT(*) INTO trabajos_count FROM Trabaja WHERE IDGimnasio = OLD.IDGimnasio;

        -- Si existen registros en la tabla Trabaja que dependen del gimnasio, evitamos la eliminación y mostramos un mensaje de error
        IF trabajos_count > 0 THEN
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede eliminar el gimnasio porque hay funcionarios asignados a él.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_insertar_gim():
    query = """
    CREATE TRIGGER before_insert_update_gimnasio
    BEFORE INSERT ON Gimnasio
    FOR EACH ROW
    BEGIN
        -- Verifica si la ciudad especificada existe en la tabla Ciudad
        DECLARE ciudad_count INT;
        SELECT COUNT(*) INTO ciudad_count FROM Ciudad WHERE IDCiudad = NEW.IDCiudad;
        IF ciudad_count = 0 THEN
            -- Si la ciudad no existe, genera un error y cancela la inserción/actualización
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'La ciudad especificada no existe en la tabla Ciudad.';
        END IF;
    END;
    """
    execute_query(query) 

def crear_trigger_actualizar_gim():
    query = """
    CREATE TRIGGER before_update_gimnasio
    BEFORE UPDATE ON Gimnasio
    FOR EACH ROW
    BEGIN
        -- Verifica si el ID de la ciudad está siendo modificado
        IF OLD.IDCiudad <> NEW.IDCiudad THEN
            -- Si la ciudad está cambiando, genera un error y revierte la actualización
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'No se puede modificar la ciudad de un gimnasio.';
        END IF;
    END;
    """
    execute_query(query) 

def crearVistaInformacionFuncionarios():
    query = """
    CREATE VIEW Vista_Funcionario_Puesto_Gimnasio AS
    SELECT 
        f.IDFuncionario,
        f.nombre AS NombreFuncionario,
        f.apellidol AS Apellido1Funcionario,
        f.apellido2 AS Apellido2Funcionario,
        f.NumeroTelefono AS TelefonoFuncionario,
        p.puesto AS NombrePuesto,
        g.nombre AS NombreGimnasio,
        g.direccionExacta AS DireccionGimnasio,
        g.NumeroTelefono AS TelefonoGimnasio
    FROM Funcionario f 
    JOIN PuestoFuncionario p ON f.puesto = p.IDPuesto
    JOIN Trabaja t ON f.IDFuncionario = t.IDFuncionario
    JOIN Gimnasio g ON t.IDGimnasio = g.IDGimnasio;"""

    execute_query(query) 

def crearVistaInformacionFuncionarios():
    query = """
    CREATE VIEW Vista_Funcionario_Puesto_Gimnasio AS
    SELECT 
        f.IDFuncionario,
        f.nombre AS NombreFuncionario,
        f.apellidol AS Apellido1Funcionario,
        f.apellido2 AS Apellido2Funcionario,
        f.NumeroTelefono AS TelefonoFuncionario,
        p.puesto AS NombrePuesto,
        g.nombre AS NombreGimnasio,
        g.direccionExacta AS DireccionGimnasio,
        g.NumeroTelefono AS TelefonoGimnasio
    FROM Funcionario f 
    JOIN PuestoFuncionario p ON f.puesto = p.IDPuesto
    JOIN Trabaja t ON f.IDFuncionario = t.IDFuncionario
    JOIN Gimnasio g ON t.IDGimnasio = g.IDGimnasio;"""

    execute_query(query) 

def crearVistaInformacionCliente():
    query = """
    CREATE VIEW Vista_Cliente_Membresia AS
    SELECT 
    c.IDCliente,
    c.nombre AS NombreCliente,
    c.apellidol AS Apellido1Cliente,
    c.apellido2 AS Apellido2Cliente,
    c.correoElectronico AS CorreoCliente,
    c.NumeroTelefono AS TelefonoCliente,
    m.tipo AS TipoMembresia,
    m.costo AS CostoMembresia,
    m.estado AS EstadoMembresia
    FROM Cliente c
    JOIN Membresia m ON c.IDMembresia = m.IDMembresia;"""


    execute_query(query) 

def crearVistaClaseInstructor():
    query = """
    CREATE VIEW Vista_Clases_Instructores AS
    SELECT 
    cl.IDClase,
    cl.nombre AS NombreClase,
    cl.capacidadMaxima AS CapacidadMaximaClase,
    f.nombre AS NombreInstructor,
    f.apellidol AS Apellido1Instructor,
    f.apellido2 AS Apellido2Instructor,
    g.nombre AS NombreGimnasio,
    g.direccionExacta AS DireccionGimnasio
    FROM Clase cl
    JOIN Funcionario f ON cl.IDFuncionario = f.IDFuncionario
    JOIN Trabaja t ON f.IDFuncionario = t.IDFuncionario
    JOIN Gimnasio g ON t.IDGimnasio = g.IDGimnasio;
    """
    execute_query(query) 

def crearVistaVentaProductos():
    query = """
    CREATE VIEW Vista_Ventas_Productos AS
    SELECT 
    v.NumeroTransaccion,
    v.fechaAdquisicion,
    v.monto,
    v.cantidad,
    c.IDCliente,
    c.nombre AS NombreCliente,
    c.apellidol AS Apellido1Cliente,
    c.apellido2 AS Apellido2Cliente,
    p.IDProducto,
    p.nombre AS NombreProducto,
    p.costo AS CostoProducto
    FROM Venta v
    JOIN Cliente c ON v.IDCliente = c.IDCliente
    JOIN Producto p ON v.IDProducto = p.IDProducto;
    """
    execute_query(query) 


def crearVistaEquipoGimnasio():
     query = """
     CREATE VIEW Vista_Equipos_Gimnasios AS
     SELECT 
    e.CodigoEquipo,
    e.nombre AS NombreEquipo,
    e.estado AS EstadoEquipo,
    e.fechaAdquisicion AS FechaAdquisicionEquipo,
    g.IDGimnasio,
    g.nombre AS NombreGimnasio,
    g.direccionExacta AS DireccionGimnasio,
    g.NumeroTelefono AS TelefonoGimnasio,
    c.IDCiudad,
    c.nombre AS NombreCiudad
    FROM Equipo e
    JOIN Gimnasio g ON e.CodigoGimnasio = g.IDGimnasio
    JOIN Ciudad c ON g.IDCiudad = c.IDCiudad;
     """
     execute_query(query) 

def CrearCursorGimnasioEquipo():
    query = """
    CREATE PROCEDURE cursorGimnasio(
    IN gimnasio_id char(9)
    )
    BEGIN
    DECLARE done int default 0;
    DECLARE nombre_equipo_temp varchar(50);
    DECLARE cursor_gimnasio CURSOR FOR


    SELECT nombre FROM Equipo WHERE CodigoGimnasio = gimnasio_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cursor_gimnasio;
    gimnasio_loop: LOOP
    Fetch cursor_gimnasio into nombre_equipo_temp;
    if done = 1 THEN
       LEAVE gimnasio_loop;
    end if;
    SELECT nombre_equipo_temp;
   END LOOP;


    CLOSE cursor_gimnasio;

    END;

    """
    execute_query(query) 


def LlamarCursorGimnasioEquipo(gimnasio_id):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return  # Salir de la función si hay un error en la conexión

    cursor = cnx.cursor()

    cursor.callproc("cursorGimnasio", (gimnasio_id,))

    for result in cursor.stored_results():
        rows = result.fetchall()
        print(f"Filas recuperadas: {len(rows)}")
        for row in rows:
            ciudad = row[0]
            print(f"El gimnasio con ID {gimnasio_id} tiene la máquina de {ciudad}")

    cursor.close()
    cnx.close()

def CrearCursorContarFuncionarios():
    query = """
    CREATE PROCEDURE cursorContarFuncionarios (
    IN gimnasio_id char(9)
    )
    BEGIN
    DECLARE total INT DEFAULT 0;
    DECLARE done INT DEFAULT 0;
    DECLARE vacliente char(9);


    DECLARE cursor_funcionarios CURSOR FOR
    SELECT IDFuncionario FROM trabaja WHERE IDGimnasio = gimnasio_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cursor_funcionarios;
    funcionarios_loop: LOOP
    FETCH cursor_funcionarios INTO vacliente;
    IF done THEN
    LEAVE funcionarios_loop;
    END IF;
    SET total = total + 1;
    END LOOP;
    CLOSE cursor_funcionarios;
    SELECT total;
    END 

    """
    execute_query(query) 


def LlamarCursorContarFuncionarios(gimnasio_id):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return  # Salir de la función si hay un error en la conexión

    cursor = cnx.cursor()

    cursor.callproc("cursorContarFuncionarios", (gimnasio_id,))
     # Recuperar el resultado del procedimiento almacenado
    for result in cursor.stored_results():
        for row in result.fetchall():
            print("Total de funcionarios:", row[0])

    cursor.close()
    cnx.close()

def CrearCursorContarClientesClase():
    query = """
    CREATE PROCEDURE cursorContarClientesClase (
    IN clase_id char(9)
    )
    BEGIN
    DECLARE total INT DEFAULT 0;
    DECLARE done INT DEFAULT 0;
    DECLARE vacliente char(11);


    DECLARE cursor_clientes CURSOR FOR
    SELECT IDCliente FROM inscribirse WHERE IDClase = clase_id;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN cursor_clientes;
    clientes_loop: LOOP
    FETCH cursor_clientes INTO vacliente;
    IF done THEN
    LEAVE clientes_loop;
    END IF;
    SET total = total + 1;
    END LOOP;
    CLOSE cursor_clientes;
    SELECT total;
    END 

    """
    execute_query(query) 


def LlamarCursorContarFuncionarios(clase_id):
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return  # Salir de la función si hay un error en la conexión

    cursor = cnx.cursor()

    cursor.callproc("cursorContarClientesClase", (clase_id,))
     # Recuperar el resultado del procedimiento almacenado
    for result in cursor.stored_results():
        for row in result.fetchall():
            print("Total de clientes:", row[0])

    cursor.close()
    cnx.close()

def menu():
    print("1. Insertar membresia")
    print("2. Actualizar membresia")
    print("3. Eliminar membresia")
    print("4. Insertar clase")
    print("5. Actualizar clase")
    print("6. Eliminar clase")
    print("7. Insertar Cliente")
    print("8. Actualizar Cliente")
    print("9. Eliminar Cliente")
    print("10. Ingresar nuevo puesto de funcionario")
    print("11. Actualizar puesto de funcionario")
    print("12. Eliminar puesto de funcionario")
    print("13. Insertar nuevo funcionario")
    print("14. Actualizar funcionario")
    print("15. Eliminar funcionario")
    print("16. Insertar ciudad")
    print("17. Actualizar ciudad")
    print("18. Eliminar ciudad")
    print("19. Insertar gimnasio")
    print("20. Actualizar gimnasio")
    print("21. Eliminar gimnasio")
    print("22. Asignar funcionario a gimnasio")
    print("23. Actualizar asignación de funcionario a gimnasio")
    print("24. Eliminar asignación de funcionario a gimnasio")
    print("25. Insertar equipo")
    print("26. Actualizar equipo")
    print("27. Eliminar equipo")
    print("28. Insertar producto")
    print("29. Actualizar producto")
    print("30. Eliminar producto")
    print("31. Insertar venta")
    print("32. Actualizar venta")
    print("33. Eliminar venta")
    print("34. Insertar inscripción")
    print("35. Actualizar inscripción")
    print("36. Eliminar inscripción")
    print("37. Ver productos")
    print("38. Ver ventas")
    print("39. Ver inscripciones")
    print("40. ver información de funcionarios")
    print("41. ver información de clientes")
    print("42. ver clases")
    print("43. ver ciudades con gimnasios")
    print("44. ver equipo")
    print("45. ver información de gimnasios")
    print("46. ver información de trabajos de los funcionarios")
    print("47. ver información de los puestos de los funcionarios")
    print("48 Salir")

    opcion = int(input("Seleccione una opción: "))
    return opcion

def main():
    opcion = menu()
    while opcion != 48:
        if opcion == 1:
            IDMembresia = input("Ingrese el ID de la membresia: ")
            tipo = input("Ingrese el tipo de membresia: ")
            costo = float(input("Ingrese el costo de la membresia: "))
            estado = input("Ingrese el estado de la membresia: ")
            insertMembershipProc(IDMembresia, tipo, costo, estado)
        elif opcion == 2:
            IDMembresia = input("Ingrese el ID de la membresia a actualizar: ")
            tipo = input("Ingrese el nuevo tipo de membresia: ")
            costo = float(input("Ingrese el nuevo costo de la membresia: "))
            estado = input("Ingrese el nuevo estado de la membresia: ")
            updateMembershipProc(IDMembresia, tipo, costo, estado)
        elif opcion == 3:
            IDMembresia = input("Ingrese el ID de la membresia a eliminar: ")
            deleteMembershipProc(IDMembresia)
        elif opcion == 4:
            IDClase = str(input("Ingrese el ID de la clase: "))
            IDFuncionario = str(input("Ingrese el ID del funcionario: "))
            nombre = str(input("Ingrese el nombre de la clase: "))
            capacidadMaxima = int(input("Ingrese la capacidad máxima de la clase: "))
            insertClassProc(IDClase, IDFuncionario, nombre, capacidadMaxima)
        elif opcion == 5:
            IDClase = str(input("Ingrese el ID de la clase a actualizar: "))
            IDFuncionario = str(input("Ingrese el nuevo ID del funcionario: "))
            nombre = str(input("Ingrese el nuevo nombre de la clase: "))
            capacidadMaxima = int(input("Ingrese la nueva capacidad máxima de la clase: "))
            updateClassProc(IDClase, IDFuncionario, nombre, capacidadMaxima)
        elif opcion == 6:
            IDClase = str(input("Ingrese el ID de la clase a eliminar: "))
            deleteclaseProc(IDClase)
        elif opcion == 7:
            IDCliente = str(input("Ingrese el ID del cliente: "))
            IDMembresia = str(input("Ingrese el ID de la membresia: "))
            nombre = str(input("Ingrese el nombre del cliente: "))
            apellidol = str(input("Ingrese el primer apellido del cliente: "))
            apellido2 = str(input("Ingrese el segundo apellido del cliente: "))
            correoElectronico = str(input("Ingrese el correo electrónico del cliente: "))
            NumeroTelefono = str(input("Ingrese el número de teléfono del cliente: "))
            insertClientProc(IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
        elif opcion == 8:
            IDCliente = str(input("Ingrese el ID del cliente a actualizar: "))
            IDMembresia = str(input("Ingrese el nuevo ID de la membresia: "))
            nombre = str(input("Ingrese el nuevo nombre del cliente: "))
            apellidol = str(input("Ingrese el nuevo primer apellido del cliente: "))
            apellido2 = str(input("Ingrese el nuevo segundo apellido del cliente: "))
            correoElectronico = str(input("Ingrese el nuevo correo electrónico del cliente: "))
            NumeroTelefono = str(input("Ingrese el nuevo número de teléfono del cliente: "))
            updateClientProc(IDCliente, IDMembresia, nombre, apellidol, apellido2, correoElectronico, NumeroTelefono)
        elif opcion == 9:
            IDCliente = str(input("Ingrese el ID del cliente a eliminar: "))
            deleteclientProc(IDCliente)
        elif opcion ==  10:
            IDPuesto = str(input("Ingrese el ID del puesto: "))
            puesto = str(input("Ingrese el nombre del puesto: "))
            insertPFProc(IDPuesto, puesto)
        elif opcion == 11:
            IDPuesto = str(input("Ingrese el ID del puesto a actualizar: "))
            puesto = str(input("Ingrese el nuevo nombre del puesto: "))
            updatePFProc(IDPuesto, puesto)
        elif opcion == 12:
            IDPuesto = str(input("Ingrese el ID del puesto a eliminar: "))
            deletePFProc(IDPuesto)
        elif opcion == 13:
            IDFuncionario = str(input("Ingrese el ID del funcionario: "))
            puesto = str(input("Ingrese el puesto del funcionario: "))
            nombre = str(input("Ingrese el nombre del funcionario: "))
            apellidol = str(input("Ingrese el primer apellido del funcionario: "))
            apellido2 = str(input("Ingrese el segundo apellido del funcionario: "))
            NumeroTelefono = str(input("Ingrese el número de teléfono del funcionario: "))
            insertEmployeeProc(IDFuncionario, puesto, nombre, apellidol, apellido2, NumeroTelefono)
        elif opcion == 14:
            IDFuncionario = str(input("Ingrese el ID del funcionario a actualizar: "))
            puesto = str(input("Ingrese el nuevo puesto del funcionario: "))
            nombre = str(input("Ingrese el nuevo nombre del funcionario: "))
            apellidol = str(input("Ingrese el nuevo primer apellido del funcionario: "))
            apellido2 = str(input("Ingrese el nuevo segundo apellido del funcionario: "))
            NumeroTelefono = str(input("Ingrese el nuevo número de teléfono del funcionario: "))
            updateEmployeeProc(IDFuncionario, puesto, nombre, apellidol, apellido2, NumeroTelefono)
        elif opcion == 15:
            IDFuncionario = str(input("Ingrese el ID del funcionario a eliminar: "))
            deletePFProc(IDFuncionario)
        elif opcion == 16:
            IDCiudad = str(input("Ingrese el ID de la ciudad: "))
            nombre = str(input("Ingrese el nombre de la ciudad: "))
            InsertCiudad(IDCiudad, nombre)
        elif opcion == 17:
            IDCiudad = str(input("Ingrese el ID de la ciudad a actualizar: "))
            nombre = str(input("Ingrese el nuevo nombre de la ciudad: "))
            updateCityProc(IDCiudad, nombre)
        elif opcion == 18:
            IDCiudad = str(input("Ingrese el ID de la ciudad a eliminar: "))
            deleteCityProc(IDCiudad)
        elif opcion == 19:
            IDGimnasio = str(input("Ingrese el ID del gimnasio: "))
            IDCiudad = str(input("Ingrese el ID de la ciudad: "))
            nombre = str(input("Ingrese el nombre del gimnasio: "))
            direccionExacta = str(input("Ingrese la dirección exacta del gimnasio: "))
            NumeroTelefono = str(input("Ingrese el número de teléfono del gimnasio: "))
            insertGym(IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono)
        elif opcion == 20: 
            IDGimnasio = str(input("Ingrese el ID del gimnasio a actualizar: "))
            IDCiudad = str(input("Ingrese el nuevo ID de la ciudad: "))
            nombre = str(input("Ingrese el nuevo nombre del gimnasio: "))
            direccionExacta = str(input("Ingrese la nueva dirección exacta del gimnasio: "))
            NumeroTelefono = str(input("Ingrese el nuevo número de teléfono del gimnasio: "))
            updateGymProc(IDGimnasio, IDCiudad, nombre, direccionExacta, NumeroTelefono)
        elif opcion == 21:
            IDGimnasio = str(input("Ingrese el ID del gimnasio a eliminar: "))
            deleteGymProc(IDGimnasio)
        elif opcion == 22:
            IDGimnasio = str(input("Ingrese el ID del gimnasio: "))
            IDFuncionario = str(input("Ingrese el ID del funcionario: "))
            insertWorking(IDGimnasio, IDFuncionario)
        elif opcion == 23:
            IDGimnasio = str(input("Ingrese el ID del gimnasio a actualizar: "))
            IDFuncionario = str(input("Ingrese el nuevo ID del funcionario: "))
            updateWorkingProc(IDGimnasio, IDFuncionario)
        elif opcion == 24: 
            IDGimnasio = str(input("Ingrese el ID del gimnasio: "))
            IDFuncionario = str(input("Ingrese el ID del funcionario: "))
            deleteWorkingProc(IDGimnasio, IDFuncionario)
        elif opcion == 25:
            CodigoEquipo = str(input("Ingrese el código del equipo: "))
            CodigoGimnasio = str(input("Ingrese el código del gimnasio: "))
            nombre = str(input("Ingrese el nombre del equipo: "))
            estado = str(input("Ingrese el estado del equipo: "))
            fechaAdquisicion = str(input("Ingrese la fecha de adquisición del equipo: "))
            insertEquip(CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
        elif opcion == 26:
            CodigoEquipo = str(input("Ingrese el código del equipo a actualizar: "))
            CodigoGimnasio = str(input("Ingrese el nuevo código del gimnasio: "))
            nombre = str(input("Ingrese el nuevo nombre del equipo: "))
            estado = str(input("Ingrese el nuevo estado del equipo: "))
            fechaAdquisicion = str(input("Ingrese la nueva fecha de adquisición del equipo: "))
            updateEquipProc(CodigoEquipo, CodigoGimnasio, nombre, estado, fechaAdquisicion)
        elif opcion == 27:
            CodigoEquipo = str(input("Ingrese el código del equipo a eliminar: "))
            deleteEquipProc(CodigoEquipo)
        elif opcion == 28:
            IDProducto = str(input("Ingrese el ID del producto: "))
            nombre = str(input("Ingrese el nombre del producto: "))
            descripcion = str(input("Ingrese la descripción del producto: "))
            costo = float(input("Ingrese el costo del producto: "))
            insertProductProc(IDProducto, nombre, descripcion, costo)
        elif opcion == 29:
            IDProducto = str(input("Ingrese el ID del producto a actualizar: "))
            nombre = str(input("Ingrese el nuevo nombre del producto: "))
            descripcion = str(input("Ingrese la nueva descripción del producto: "))
            costo = float(input("Ingrese el nuevo costo del producto: "))
            updateProductProc(IDProducto, nombre, descripcion, costo)
        elif opcion == 30:
            IDProducto = str(input("Ingrese el ID del producto a eliminar: "))
            deleteProductProc(IDProducto)
        elif opcion == 31:
            NumeroTransaccion = str(input("Ingrese el número de transacción: "))
            IDCliente = str(input("Ingrese el ID del cliente: "))
            IDProducto = str(input("Ingrese el ID del producto: "))
            fechaAdquisicion = str(input("Ingrese la fecha de adquisición: "))
            monto = float(input("Ingrese el monto: "))
            cantidad = int(input("Ingrese la cantidad: "))
            insertSaleProc(NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad)
        elif opcion == 32:
            NumeroTransaccion = str(input("Ingrese el número de transacción a actualizar: "))
            IDCliente = str(input("Ingrese el nuevo ID del cliente: "))
            IDProducto = str(input("Ingrese el nuevo ID del producto: "))
            fechaAdquisicion = str(input("Ingrese la nueva fecha de adquisición: "))
            monto = float(input("Ingrese el nuevo monto: "))
            cantidad = int(input("Ingrese la nueva cantidad: "))
            updateSaleProc(NumeroTransaccion, IDCliente, IDProducto, fechaAdquisicion, monto, cantidad)
        elif opcion == 33:
            NumeroTransaccion = str(input("Ingrese el número de transacción a eliminar: "))
            deleteSaleProc(NumeroTransaccion)
        elif opcion == 34:
            IDClase = str(input("Ingrese el ID de la clase: "))
            IDCliente = str(input("Ingrese el ID del cliente: "))
            insertInscriptionProc(IDClase, IDCliente)
        elif opcion == 35:
            codigoInscripcion = str(input("Ingrese el ID de la inscripción a actualizar: "))
            IDClase = str(input("Ingrese el ID de la clase a actualizar: "))
            IDCliente = str(input("Ingrese el nuevo ID del cliente: "))
            updateInscriptionProc(IDClase, IDCliente)
        elif opcion == 36:
            codigoInscripcion = str(input("Ingrese el ID de la inscripción a eliminar: "))
            deleteInscriptionProc(codigoInscripcion)
        elif opcion == 37:
            watchProductProc()
        elif opcion == 38:
            watchSaleProc()
        elif opcion == 39:
            watchInscriptionProc()
        elif opcion == 40:
            watchEmployeeProc()
        elif opcion == 41:
            watchClientProc()
        elif opcion == 42:
            watchClassProc()
        elif opcion == 43:
            watchCityProc()
        elif opcion == 44:
            watchEquipProc()
        elif opcion == 45:
            watchGymProc()
        elif opcion == 46:
            watchWorkingProc()
        elif opcion == 47:
            watchPFProc()
        opcion = menu()
    print("Saliendo...")
#llamar la funcion ver membresia

#main()

CrearCursorGimnasioEquipo()

CrearCursorContarFuncionarios()

CrearCursorContarClientesClase()



crearVistaClaseInstructor()
crearVistaEquipoGimnasio()
crearVistaInformacionCliente()
crearVistaInformacionFuncionarios()
crearVistaVentaProductos()


crear_trigger_verificar_stock_before_venta()
crear_trigger_actualizar_stock_after_eliminar_venta()
crear_trigger_actualizar_stock_after_crear_venta()
crear_trigger_actualizar_monto_venta_despues_actualizacion()

crear_trigger_validar_correo_cliente_before_insert()  
crear_trigger_actualizar_correo_cliente()
crear_trigger_insertar_equipo()
crear_trigger_eliminar_gim()
crear_trigger_eliminar_cliente()

crear_trigger_eliminar_equipo()
crear_trigger_actualizar_equipo()
crear_trigger_insertar_gim()
crear_trigger_actualizar_gim()