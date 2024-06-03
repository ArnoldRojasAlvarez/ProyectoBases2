import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys

# Asegúrate de que la ruta del archivo Proyecto_BD_II.py está en el path de Python
sys.path.append(r'C:\Users\Yorleny\Desktop\code\ProyectoBases2')
from Proyecto_BD_II import (
    watchMembershipProc, insertMembershipProc, updateMembershipProc, deleteMembershipProc,
    watchClassProc, insertClassProc, updateClassProc, deleteclaseProc,
    watchClientProc, insertClientProc, updateClientProc, deleteclientProc, 
    watchPFProc, insertPFProc, updatePFProc, deletePFProc,     #agregar mañana esta funcionalidad
    watchEmployeeProc, insertEmployeeProc, updateEmployeeProc, deletePFProc,
    watchCityProc, InsertCiudad, updateCityProc, deleteCityProc,
    watchGymProc, insertGym, updateGymProc, deleteGymProc,
    watchWorkingProc, insertWorking, updateWorkingProc, deleteWorkingProc,
    watchEquipProc, insertEquip, updateEquipProc, deleteEquipProc,
    watchProductProc, insertProductProc, updateProductProc, deleteProductProc,
    watchSaleProc, insertSaleProc, updateSaleProc, deleteSaleProc,
    watchInscriptionProc, insertInscriptionProc, updateInscriptionProc, deleteInscriptionProc
)

def show_membership_data():
    try:
        result = watchMembershipProc()

        # Crear una ventana emergente
        popup = tk.Toplevel()
        popup.title("Membership Data")

        # Crear un árbol para mostrar los datos
        tree = ttk.Treeview(popup)
        tree["columns"] = ("ID", "Tipo", "Costo", "Estado")
        tree.heading("#0", text="Info Membre")
        tree.column("#0", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("ID", text="ID")
        tree.column("ID", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Tipo", text="Tipo")
        tree.column("Tipo", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Costo", text="Costo")
        tree.column("Costo", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Estado", text="Estado")
        tree.column("Estado", minwidth=0, width=100, stretch=tk.NO)

        # Insertar datos en la tabla
        for row in result:
            tree.insert("", tk.END, values=row)

        # Añadir scrollbars
        y_scroll = ttk.Scrollbar(popup, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_membership():
    id = id_entry.get()
    tipo = tipo_entry.get()
    costo = float(costo_entry.get())
    estado = estado_entry.get()
    try:
        insertMembershipProc(id, tipo, costo, estado)
        messagebox.showinfo("Success", "Membership inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_membership():
    id = id_entry.get()
    tipo = tipo_entry.get()
    costo = float(costo_entry.get())
    estado = estado_entry.get()
    try:
        updateMembershipProc(id, tipo, costo, estado)
        messagebox.showinfo("Success", "Membership updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_membership():
    id = id_entry.get()
    try:
        deleteMembershipProc(id)
        messagebox.showinfo("Success", "Membership deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Define funciones para operaciones de clase
def show_class_data():
    try:
        result = watchClassProc()

        # Crear una ventana emergente
        popup = tk.Toplevel()
        popup.title("Class Data")

        # Crear un árbol para mostrar los datos
        tree = ttk.Treeview(popup)
        tree["columns"] = ("ID", "Funcionario", "Nombre", "Capacidad Máxima")
        tree.heading("#0", text="Info Clase")
        tree.column("#0", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("ID", text="ID")
        tree.column("ID", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Funcionario", text="Funcionario")
        tree.column("Funcionario", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Nombre", text="Nombre")
        tree.column("Nombre", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Capacidad Máxima", text="Capacidad Máxima")
        tree.column("Capacidad Máxima", minwidth=0, width=100, stretch=tk.NO)

        # Insertar datos en la tabla
        for row in result:
            tree.insert("", tk.END, values=row)

        # Añadir scrollbars
        y_scroll = ttk.Scrollbar(popup, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_class():
    id = id_entry.get()
    id_funcionario = id_funcionario_entry.get()
    nombre = nombre_entry.get()
    capacidad_maxima = int(capacidad_maxima_entry.get())
    try:
        insertClassProc(id, id_funcionario, nombre, capacidad_maxima)
        messagebox.showinfo("Success", "Class inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_class():
    id = id_entry.get()
    id_funcionario = id_funcionario_entry.get()
    nombre = nombre_entry.get()
    capacidad_maxima = int(capacidad_maxima_entry.get())
    try:
        updateClassProc(id, id_funcionario, nombre, capacidad_maxima)
        messagebox.showinfo("Success", "Class updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_class():
    id = id_entry.get()
    try:
        deleteclaseProc(id)
        messagebox.showinfo("Success", "Class deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))
# Funciones de operaciones de cliente
def show_client_data():
    try:
        result = watchClientProc()

        popup = tk.Toplevel()
        popup.title("Client Data")

        tree = ttk.Treeview(popup)
        tree["columns"] = ("ID", "Membresía", "Nombre", "Apellido1", "Apellido2", "Correo", "Teléfono")
        tree.heading("#0", text="Info Cliente")
        tree.column("#0", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("ID", text="ID")
        tree.column("ID", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Membresía", text="Membresía")
        tree.column("Membresía", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Nombre", text="Nombre")
        tree.column("Nombre", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Apellido1", text="Apellido1")
        tree.column("Apellido1", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Apellido2", text="Apellido2")
        tree.column("Apellido2", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Correo", text="Correo")
        tree.column("Correo", minwidth=0, width=100, stretch=tk.NO)
        tree.heading("Teléfono", text="Teléfono")
        tree.column("Teléfono", minwidth=0, width=100, stretch=tk.NO)

        for row in result:
            tree.insert("", tk.END, values=row)

        y_scroll = ttk.Scrollbar(popup, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=y_scroll.set)
        y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill=tk.BOTH, expand=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_client():
    id = id_entry.get()
    id_membresia = id_membresia_entry.get()
    nombre = nombre_entry.get()
    apellido1 = apellido1_entry.get()
    apellido2 = apellido2_entry.get()
    correo = correo_entry.get()
    telefono = telefono_entry.get()
    try:
        insertClientProc(id, id_membresia, nombre, apellido1, apellido2, correo, telefono)
        messagebox.showinfo("Success", "Client inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_client():
    id = id_entry.get()
    id_membresia = id_membresia_entry.get()
    nombre = nombre_entry.get()
    apellido1 = apellido1_entry.get()
    apellido2 = apellido2_entry.get()
    correo = correo_entry.get()
    telefono = telefono_entry.get()
    try:
        updateClientProc(id, id_membresia, nombre, apellido1, apellido2, correo, telefono)
        messagebox.showinfo("Success", "Client updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_client():
    id = id_entry.get()
    try:
        deleteclientProc(id)
        messagebox.showinfo("Success", "Client deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def show_employee_data():
    try:
        result = watchEmployeeProc()
        display_data("Employee Data", result, ["ID", "Puesto", "Nombre", "Apellido1", "Apellido2", "Teléfono"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_employee():
    id = id_entry.get()
    puesto = puesto_entry.get()
    nombre = nombre_entry.get()
    apellido1 = apellido1_entry.get()
    apellido2 = apellido2_entry.get()
    telefono = telefono_entry.get()
    try:
        insertEmployeeProc(id, puesto, nombre, apellido1, apellido2, telefono)
        messagebox.showinfo("Success", "Employee inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_employee():
    id = id_entry.get()
    puesto = puesto_entry.get()
    nombre = nombre_entry.get()
    apellido1 = apellido1_entry.get()
    apellido2 = apellido2_entry.get()
    telefono = telefono_entry.get()
    try:
        updateEmployeeProc(id, puesto, nombre, apellido1, apellido2, telefono)
        messagebox.showinfo("Success", "Employee updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_employee():
    id = id_entry.get()
    try:
        deletePFProc(id)
        messagebox.showinfo("Success", "Employee deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Funciones para gestionar ciudades
def show_city_data():
    try:
        result = watchCityProc()
        display_data("City Data", result, ["ID", "Nombre"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_city():
    id = id_entry.get()
    nombre = nombre_entry.get()
    try:
        InsertCiudad(id, nombre)
        messagebox.showinfo("Success", "City inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_city():
    id = id_entry.get()
    nombre = nombre_entry.get()
    try:
        updateCityProc(id, nombre)
        messagebox.showinfo("Success", "City updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))
def show_gym_data():
    try:
        result = watchGymProc()
        display_data("Gym Data", result, ["ID Gimnasio", "ID Ciudad", "Nombre", "Dirección", "Teléfono"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_gym():
    id_gym = id_gym_entry.get()
    id_city = id_city_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    try:
        insertGym(id_gym, id_city, name, address, phone)
        messagebox.showinfo("Success", "Gym inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_gym():
    id_gym = id_gym_entry.get()
    id_city = id_city_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    try:
        updateGymProc(id_gym, id_city, name, address, phone)
        messagebox.showinfo("Success", "Gym updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_gym():
    id_gym = id_gym_entry.get()
    try:
        deleteGymProc(id_gym)
        messagebox.showinfo("Success", "Gym deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_working_data():
    try:
        result = watchWorkingProc()
        display_data("Working Data", result, ["ID Gimnasio", "ID Funcionario"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_working():
    id_gym = id_gym_entry.get()
    id_func = id_func_entry.get()
    try:
        insertWorking(id_gym, id_func)
        messagebox.showinfo("Success", "Funcionario asignado a gimnasio")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_working():
    id_gym = id_gym_entry.get()
    id_func = id_func_entry.get()
    try:
        updateWorkingProc(id_gym, id_func)
        messagebox.showinfo("Success", "Funcionario asignado a gimnasio actualizado")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_working():
    id_gym = id_gym_entry.get()
    id_func = id_func_entry.get()
    try:
        deleteWorkingProc(id_gym, id_func)
        messagebox.showinfo("Success", "Funcionario asignado a gimnasio eliminado")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_city():
    id = id_entry.get()
    try:
        deleteCityProc(id)
        messagebox.showinfo("Success", "City deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_equip_data():
    try:
        result = watchEquipProc()
        display_data("Equip Data", result, ["Código Equipo", "Código Gimnasio", "Nombre", "Estado", "Fecha Adquisición"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_equip():
    cod_equip = cod_equip_entry.get()
    cod_gym = cod_gym_entry.get()
    name = name_entry.get()
    status = status_entry.get()
    acquisition_date = acquisition_date_entry.get()
    try:
        insertEquip(cod_equip, cod_gym, name, status, acquisition_date)
        messagebox.showinfo("Success", "Equipo insertado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_equip():
    cod_equip = cod_equip_entry.get()
    cod_gym = cod_gym_entry.get()
    name = name_entry.get()
    status = status_entry.get()
    acquisition_date = acquisition_date_entry.get()
    try:
        updateEquipProc(cod_equip, cod_gym, name, status, acquisition_date)
        messagebox.showinfo("Success", "Equipo actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_equip():
    cod_equip = cod_equip_entry.get()
    try:
        deleteEquipProc(cod_equip)
        messagebox.showinfo("Success", "Equipo eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_product_data():
    try:
        result = watchProductProc()
        display_data("Product Data", result, ["ID Producto", "Nombre", "Descripción", "Costo"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_product():
    id_product = id_product_entry.get()
    name = name_entry.get()
    description = description_entry.get()
    cost = cost_entry.get()
    try:
        insertProductProc(id_product, name, description, cost)
        messagebox.showinfo("Success", "Producto insertado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_product():
    id_product = id_product_entry.get()
    name = name_entry.get()
    description = description_entry.get()
    cost = cost_entry.get()
    try:
        updateProductProc(id_product, name, description, cost)
        messagebox.showinfo("Success", "Producto actualizado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_product():
    id_product = id_product_entry.get()
    try:
        deleteProductProc(id_product)
        messagebox.showinfo("Success", "Producto eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_sale_data():
    try:
        result = watchSaleProc()
        display_data("Sale Data", result, ["Número Transacción", "ID Cliente", "ID Producto", "Fecha Adquisición", "Monto", "Cantidad"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_sale():
    trans_number = trans_number_entry.get()
    id_client = id_client_entry.get()
    id_product = id_product_entry.get()
    acquisition_date = acquisition_date_entry.get()
    amount = amount_entry.get()
    quantity = quantity_entry.get()
    try:
        insertSaleProc(trans_number, id_client, id_product, acquisition_date, amount, quantity)
        messagebox.showinfo("Success", "Venta ingresada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_sale():
    trans_number = trans_number_entry.get()
    id_client = id_client_entry.get()
    id_product = id_product_entry.get()
    acquisition_date = acquisition_date_entry.get()
    amount = amount_entry.get()
    quantity = quantity_entry.get()
    try:
        updateSaleProc(trans_number, id_client, id_product, acquisition_date, amount, quantity)
        messagebox.showinfo("Success", "Venta actualizada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_sale():
    trans_number = trans_number_entry.get()
    try:
        deleteSaleProc(trans_number)
        messagebox.showinfo("Success", "Venta eliminada correctamente")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_inscription_data():
    try:
        result = watchInscriptionProc()
        display_data("Inscription Data", result, ["Inscription Code", "Class ID", "Client ID"])
    except Exception as e:
        messagebox.showerror("Error", str(e))

def insert_inscription():
    inscription_code = inscription_code_entry.get()
    class_id = class_id_entry.get()
    client_id = client_id_entry.get()
    try:
        insertInscriptionProc(inscription_code, class_id, client_id)
        messagebox.showinfo("Success", "Inscription successfully inserted")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_inscription():
    inscription_code = inscription_code_entry.get()
    class_id = class_id_entry.get()
    client_id = client_id_entry.get()
    try:
        updateInscriptionProc(inscription_code, class_id, client_id)
        messagebox.showinfo("Success", "Inscription successfully updated")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_inscription():
    inscription_code = inscription_code_entry.get()
    try:
        deleteInscriptionProc(inscription_code)
        messagebox.showinfo("Success", "Inscription successfully deleted")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_menu():
    clear_frame()
    global menu_frame
    menu_frame = tk.Frame(frame)
    menu_frame.pack(fill="both", expand=True)

    container = ttk.Frame(menu_frame)
    canvas = tk.Canvas(container)
    scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    for text, command in buttons:
        button = ttk.Button(scrollable_frame, text=text, command=command, width=30)
        button.pack(pady=5, padx=10, fill='x')

    container.pack(fill="both", expand=True)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def create_membership_interface():
    clear_frame()

    global id_entry, tipo_entry, costo_entry, estado_entry

    id_label = tk.Label(frame, text="ID Membresía")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    tipo_label = tk.Label(frame, text="Tipo")
    tipo_label.pack(pady=5)
    tipo_entry = tk.Entry(frame)
    tipo_entry.pack(pady=5)

    costo_label = tk.Label(frame, text="Costo")
    costo_label.pack(pady=5)
    costo_entry = tk.Entry(frame)
    costo_entry.pack(pady=5)

    estado_label = tk.Label(frame, text="Estado")
    estado_label.pack(pady=5)
    estado_entry = tk.Entry(frame)
    estado_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Membership", command=insert_membership, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Membership", command=update_membership, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Membership", command=delete_membership, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_class_interface():
    clear_frame()

    global id_entry, id_funcionario_entry, nombre_entry, capacidad_maxima_entry

    id_label = tk.Label(frame, text="ID Clase")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    id_funcionario_label = tk.Label(frame, text="ID Funcionario")
    id_funcionario_label.pack(pady=5)
    id_funcionario_entry = tk.Entry(frame)
    id_funcionario_entry.pack(pady=5)

    nombre_label = tk.Label(frame, text="Nombre")
    nombre_label.pack(pady=5)
    nombre_entry = tk.Entry(frame)
    nombre_entry.pack(pady=5)

    capacidad_maxima_label = tk.Label(frame, text="Capacidad Máxima")
    capacidad_maxima_label.pack(pady=5)
    capacidad_maxima_entry = tk.Entry(frame)
    capacidad_maxima_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Class", command=insert_class, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Class", command=update_class, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Class", command=delete_class, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)
def create_client_interface():
    clear_frame()

    global id_entry, id_membresia_entry, nombre_entry, apellido1_entry, apellido2_entry, correo_entry, telefono_entry

    id_label = tk.Label(frame, text="ID Cliente")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    id_membresia_label = tk.Label(frame, text="ID Membresía")
    id_membresia_label.pack(pady=5)
    id_membresia_entry = tk.Entry(frame)
    id_membresia_entry.pack(pady=5)

    nombre_label = tk.Label(frame, text="Nombre")
    nombre_label.pack(pady=5)
    nombre_entry = tk.Entry(frame)
    nombre_entry.pack(pady=5)

    apellido1_label = tk.Label(frame, text="Apellido1")
    apellido1_label.pack(pady=5)
    apellido1_entry = tk.Entry(frame)
    apellido1_entry.pack(pady=5)

    apellido2_label = tk.Label(frame, text="Apellido2")
    apellido2_label.pack(pady=5)
    apellido2_entry = tk.Entry(frame)
    apellido2_entry.pack(pady=5)

    correo_label = tk.Label(frame, text="Correo")
    correo_label.pack(pady=5)
    correo_entry = tk.Entry(frame)
    correo_entry.pack(pady=5)

    telefono_label = tk.Label(frame, text="Teléfono")
    telefono_label.pack(pady=5)
    telefono_entry = tk.Entry(frame)
    telefono_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Client", command=insert_client, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Client", command=update_client, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Client", command=delete_client, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)


def create_employee_interface():
    clear_frame()

    global id_entry, puesto_entry, nombre_entry, apellido1_entry, apellido2_entry, telefono_entry

    id_label = tk.Label(frame, text="ID Empleado")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    puesto_label = tk.Label(frame, text="Puesto")
    puesto_label.pack(pady=5)
    puesto_entry = tk.Entry(frame)
    puesto_entry.pack(pady=5)

    nombre_label = tk.Label(frame, text="Nombre")
    nombre_label.pack(pady=5)
    nombre_entry = tk.Entry(frame)
    nombre_entry.pack(pady=5)

    apellido1_label = tk.Label(frame, text="Apellido1")
    apellido1_label.pack(pady=5)
    apellido1_entry = tk.Entry(frame)
    apellido1_entry.pack(pady=5)

    apellido2_label = tk.Label(frame, text="Apellido2")
    apellido2_label.pack(pady=5)
    apellido2_entry = tk.Entry(frame)
    apellido2_entry.pack(pady=5)

    telefono_label = tk.Label(frame, text="Teléfono")
    telefono_label.pack(pady=5)
    telefono_entry = tk.Entry(frame)
    telefono_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Employee", command=insert_employee, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Employee", command=update_employee, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Employee", command=delete_employee, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_city_interface():
    clear_frame()

    global id_entry, nombre_entry

    id_label = tk.Label(frame, text="ID Ciudad")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    nombre_label = tk.Label(frame, text="Nombre")
    nombre_label.pack(pady=5)
    nombre_entry = tk.Entry(frame)
    nombre_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert City", command=insert_city, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update City", command=update_city, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete City", command=delete_city, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)
def create_gym_interface():
    clear_frame()

    global id_gym_entry, id_city_entry, name_entry, address_entry, phone_entry

    id_gym_label = tk.Label(frame, text="ID Gimnasio")
    id_gym_label.pack(pady=5)
    id_gym_entry = tk.Entry(frame)
    id_gym_entry.pack(pady=5)

    id_city_label = tk.Label(frame, text="ID Ciudad")
    id_city_label.pack(pady=5)
    id_city_entry = tk.Entry(frame)
    id_city_entry.pack(pady=5)

    name_label = tk.Label(frame, text="Nombre")
    name_label.pack(pady=5)
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    address_label = tk.Label(frame, text="Dirección")
    address_label.pack(pady=5)
    address_entry = tk.Entry(frame)
    address_entry.pack(pady=5)

    phone_label = tk.Label(frame, text="Teléfono")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(frame)
    phone_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Gym", command=insert_gym, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Gym", command=update_gym, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Gym", command=delete_gym, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_working_interface():
    clear_frame()

    global id_gym_entry, id_func_entry

    id_gym_label = tk.Label(frame, text="ID Gimnasio")
    id_gym_label.pack(pady=5)
    id_gym_entry = tk.Entry(frame)
    id_gym_entry.pack(pady=5)

    id_func_label = tk.Label(frame, text="ID Funcionario")
    id_func_label.pack(pady=5)
    id_func_entry = tk.Entry(frame)
    id_func_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Working", command=insert_working, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Working", command=update_working, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Working", command=delete_working, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def display_data(title, result, columns):
    popup = tk.Toplevel()
    popup.title(title)

    tree = ttk.Treeview(popup)
    tree["columns"] = columns
    tree.heading("#0", text="Info")
    tree.column("#0", minwidth=0, width=100, stretch=tk.NO)

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, minwidth=0, width=100, stretch=tk.NO)

    for row in result:
        tree.insert("", tk.END, values=row)

    y_scroll = ttk.Scrollbar(popup, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=y_scroll.set)
    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    tree.pack(fill=tk.BOTH, expand=True)

def create_equip_interface():
    clear_frame()

    global cod_equip_entry, cod_gym_entry, name_entry, status_entry, acquisition_date_entry

    cod_equip_label = tk.Label(frame, text="Código Equipo")
    cod_equip_label.pack(pady=5)
    cod_equip_entry = tk.Entry(frame)
    cod_equip_entry.pack(pady=5)

    cod_gym_label = tk.Label(frame, text="Código Gimnasio")
    cod_gym_label.pack(pady=5)
    cod_gym_entry = tk.Entry(frame)
    cod_gym_entry.pack(pady=5)

    name_label = tk.Label(frame, text="Nombre")
    name_label.pack(pady=5)
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    status_label = tk.Label(frame, text="Estado")
    status_label.pack(pady=5)
    status_entry = tk.Entry(frame)
    status_entry.pack(pady=5)

    acquisition_date_label = tk.Label(frame, text="Fecha Adquisición")
    acquisition_date_label.pack(pady=5)
    acquisition_date_entry = tk.Entry(frame)
    acquisition_date_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Equip", command=insert_equip, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Equip", command=update_equip, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Equip", command=delete_equip, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_product_interface():
    clear_frame()

    global id_product_entry, name_entry, description_entry, cost_entry

    id_product_label = tk.Label(frame, text="ID Producto")
    id_product_label.pack(pady=5)
    id_product_entry = tk.Entry(frame)
    id_product_entry.pack(pady=5)

    name_label = tk.Label(frame, text="Nombre")
    name_label.pack(pady=5)
    name_entry = tk.Entry(frame)
    name_entry.pack(pady=5)

    description_label = tk.Label(frame, text="Descripción")
    description_label.pack(pady=5)
    description_entry = tk.Entry(frame)
    description_entry.pack(pady=5)

    cost_label = tk.Label(frame, text="Costo")
    cost_label.pack(pady=5)
    cost_entry = tk.Entry(frame)
    cost_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Product", command=insert_product, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Product", command=update_product, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Product", command=delete_product, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_sale_interface():
    clear_frame()

    global trans_number_entry, id_client_entry, id_product_entry, acquisition_date_entry, amount_entry, quantity_entry

    trans_number_label = tk.Label(frame, text="Número Transacción")
    trans_number_label.pack(pady=5)
    trans_number_entry = tk.Entry(frame)
    trans_number_entry.pack(pady=5)

    id_client_label = tk.Label(frame, text="ID Cliente")
    id_client_label.pack(pady=5)
    id_client_entry = tk.Entry(frame)
    id_client_entry.pack(pady=5)

    id_product_label = tk.Label(frame, text="ID Producto")
    id_product_label.pack(pady=5)
    id_product_entry = tk.Entry(frame)
    id_product_entry.pack(pady=5)

    acquisition_date_label = tk.Label(frame, text="Fecha Adquisición")
    acquisition_date_label.pack(pady=5)
    acquisition_date_entry = tk.Entry(frame)
    acquisition_date_entry.pack(pady=5)

    amount_label = tk.Label(frame, text="Monto")
    amount_label.pack(pady=5)
    amount_entry = tk.Entry(frame)
    amount_entry.pack(pady=5)

    quantity_label = tk.Label(frame, text="Cantidad")
    quantity_label.pack(pady=5)
    quantity_entry = tk.Entry(frame)
    quantity_entry.pack(pady=5)
    
    insert_button = tk.Button(frame, text="Insert Sale", command=insert_sale, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Sale", command=update_sale, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Sale", command=delete_sale, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

def create_inscription_interface():
    clear_frame()

    global inscription_code_entry, class_id_entry, client_id_entry

    inscription_code_label = tk.Label(frame, text="Inscription Code")
    inscription_code_label.pack(pady=5)
    inscription_code_entry = tk.Entry(frame)
    inscription_code_entry.pack(pady=5)

    class_id_label = tk.Label(frame, text="Class ID")
    class_id_label.pack(pady=5)
    class_id_entry = tk.Entry(frame)
    class_id_entry.pack(pady=5)

    client_id_label = tk.Label(frame, text="Client ID")
    client_id_label.pack(pady=5)
    client_id_entry = tk.Entry(frame)
    client_id_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Inscription", command=insert_inscription, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Inscription", command=update_inscription, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Inscription", command=delete_inscription, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)
def show_pf_data():
     try:
         result = watchPFProc()

         popup = tk.Toplevel()
         popup.title("Puesto Funcionario Data")

         tree = ttk.Treeview(popup)
         tree["columns"] = ("ID", "Puesto")
         tree.heading("#0", text="Info Puesto")
         tree.column("#0", minwidth=0, width=100, stretch=tk.NO)
         tree.heading("ID", text="ID")
         tree.column("ID", minwidth=0, width=100, stretch=tk.NO)
         tree.heading("Puesto", text="Puesto")
         tree.column("Puesto", minwidth=0, width=100, stretch=tk.NO)

         for row in result:
             tree.insert("", tk.END, values=row)

         y_scroll = ttk.Scrollbar(popup, orient=tk.VERTICAL, command=tree.yview)
         tree.configure(yscroll=y_scroll.set)
         y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
         tree.pack(fill=tk.BOTH, expand=True)
     except Exception as e:
         messagebox.showerror("Error", str(e))

def insert_pf():
    id = id_entry.get()
    puesto = puesto_entry.get()
    try:
        insertPFProc(id, puesto)
        messagebox.showinfo("Success", "Puesto Funcionario inserted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_pf():
    id = id_entry.get()
    puesto = puesto_entry.get()
    try:
        updatePFProc(id, puesto)
        messagebox.showinfo("Success", "Puesto Funcionario updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_pf():
    id = id_entry.get()
    try:
        deletePFProc(id)
        messagebox.showinfo("Success", "Puesto Funcionario deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def create_pf_interface():
    clear_frame()

    global id_entry, puesto_entry

    id_label = tk.Label(frame, text="ID Puesto")
    id_label.pack(pady=5)
    id_entry = tk.Entry(frame)
    id_entry.pack(pady=5)

    puesto_label = tk.Label(frame, text="Puesto")
    puesto_label.pack(pady=5)
    puesto_entry = tk.Entry(frame)
    puesto_entry.pack(pady=5)

    insert_button = tk.Button(frame, text="Insert Puesto Funcionario", command=insert_pf, width=30)
    insert_button.pack(pady=5)

    update_button = tk.Button(frame, text="Update Puesto Funcionario", command=update_pf, width=30)
    update_button.pack(pady=5)

    delete_button = tk.Button(frame, text="Delete Puesto Funcionario", command=delete_pf, width=30)
    delete_button.pack(pady=5)

    back_button = tk.Button(frame, text="Back", command=show_menu, width=30)
    back_button.pack(pady=5)

# Crear la ventana principal
root = tk.Tk()
root.title("Gym Management System")

# Crear el frame principal
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Inicializar el frame para el menú
menu_frame = tk.Frame(frame)

# Crear botones del menú inicial
buttons = [
    ("Watch Membership Data", show_membership_data),
    ("Membership Operations", create_membership_interface),
    ("Watch Class Data", show_class_data),  # Agregar botón para ver datos de clase
    ("Class Operations", create_class_interface),  # Agregar botón para operaciones de clase
    ("Watch Client Data", show_client_data),  # Agregar botón para ver datos de cliente
    ("Client Operations", create_client_interface),  # Agregar botón para operaciones de cliente
    ("Watch Puesto Funcionario Data", show_pf_data),  # Agregar botón para ver datos de puesto de funcionario
    ("Watch Employee Data", show_employee_data),  # Agregar botón para ver datos de empleado
    ("Employee Operations", create_employee_interface),  # Agregar botón para operaciones de empleado
    ("Watch City Data", show_city_data),  # Agregar botón para ver datos de ciudad
    ("City Operations", create_city_interface),  # Agregar botón para operaciones de ciudad
    ("Watch Gym Data", show_gym_data),  # Agregar botón para ver datos de gimnasio
    ("Gym Operations", create_gym_interface),  # Agregar botón para operaciones de gimnasio
    ("Watch Working Data", show_working_data),  # Agregar botón para ver datos de funcionario asignado a gimnasio
    ("Working Operations", create_working_interface),  # Agregar botón para operaciones de funcionario asignado a gimnasio
    ("Watch Equip Data", show_equip_data),  # Agregar botón para ver datos de equipo
    ("Equip Operations", create_equip_interface),  # Agregar botón para operaciones de equipo
    ("Watch Product Data", show_product_data),  # Agregar botón para ver datos de producto
    ("Product Operations", create_product_interface),  # Agregar botón para operaciones de producto
    ("Watch Sale Data", show_sale_data),  # Agregar botón para ver datos de venta
    ("Sale Operations", create_sale_interface),  # Agregar botón para operaciones de venta
    ("Watch Inscription Data", show_inscription_data),  # Agregar botón para ver datos de inscripción
    ("Inscription Operations", create_inscription_interface),  # Agregar botón para operaciones de inscripción
    ("Puesto Funcionario Operations", create_pf_interface)  # Agregar botón para operaciones de puesto de funcionario
]
# Mostrar el menú inicial
show_menu()
root.mainloop()