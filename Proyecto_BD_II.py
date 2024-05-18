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
    print("37 Salir")

    opcion = int(input("Seleccione una opción: "))
    return opcion

def main():
    opcion = menu()
    while opcion != 37:
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
        opcion = menu()
    print("Saliendo...")
main()
