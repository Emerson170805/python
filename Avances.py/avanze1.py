import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector

# Función para conectar a MySQL
def connect_db():
    return mysql.connector.connect(
        host="192.168.0.18",
        user="emerson",
        password="shadow.2005.SHADOW",
        database="emerson"
    )

# Función para insertar datos en la base de datos
def agregar_producto():
    nombre = entry_nombre.get()
    id_categoria = entry_id_categoria.get()
    precio = entry_precio.get()
    id_marca = entry_id_marca.get()
    descripcion = entry_descripcion.get("1.0", tk.END).strip()
    cantidad = entry_cantidad.get()
    
    if not (nombre and id_categoria and precio and id_marca and cantidad):
        messagebox.showerror("Error", "Todos los campos obligatorios deben llenarse.")
        return
    
    imagen_data = None
    if imagen_path:
        with open(imagen_path, "rb") as file:
            imagen_data = file.read()
    
    try:
        with connect_db() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO productos (nombre, id_categoria, precio, id_marca, descripcion, cantidad, imagen)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (nombre, id_categoria, precio, id_marca, descripcion, cantidad, imagen_data))
            conn.commit()
        messagebox.showinfo("Éxito", "Producto agregado correctamente")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error en la base de datos: {err}")

# Función para seleccionar imagen
def seleccionar_imagen():
    global imagen_path
    imagen_path = filedialog.askopenfilename(filetypes=[("Imágenes", "*.jpg;*.jpeg;*.png;*.gif")])
    if imagen_path:
        label_imagen.config(text=f"Imagen seleccionada: {imagen_path}")

# Crear la ventana principal
root = tk.Tk()
root.title("Agregar Producto")
root.geometry("400x500")

# Campos del formulario
tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

tk.Label(root, text="ID Categoría:").pack()
entry_id_categoria = tk.Entry(root)
entry_id_categoria.pack()

tk.Label(root, text="Precio:").pack()
entry_precio = tk.Entry(root)
entry_precio.pack()

tk.Label(root, text="ID Marca:").pack()
entry_id_marca = tk.Entry(root)
entry_id_marca.pack()

tk.Label(root, text="Descripción:").pack()
entry_descripcion = tk.Text(root, height=3, width=30)
entry_descripcion.pack()

tk.Label(root, text="Cantidad:").pack()
entry_cantidad = tk.Entry(root)
entry_cantidad.pack()

# Botón para seleccionar imagen
imagen_path = None
tk.Button(root, text="Seleccionar Imagen", command=seleccionar_imagen).pack()
label_imagen = tk.Label(root, text="No se ha seleccionado ninguna imagen")
label_imagen.pack()

# Botón para agregar producto
tk.Button(root, text="Agregar Producto", command=agregar_producto).pack()

# Ejecutar la aplicación
root.mainloop()