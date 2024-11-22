import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk



def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    if carpeta:
        entrada_carpeta.set(carpeta)

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if archivo:
        entrada_archivo.set(archivo)

def aceptar():
    ruta_carpeta = entrada_carpeta.get()
    ruta_archivo = entrada_archivo.get()
    modo = combo_tipo.get()
    
    # Verificar si todos los campos están completos
    if not ruta_carpeta or not ruta_archivo or not modo:
        messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos antes de continuar.")
        return
    
    # Aquí iría tu proceso
    amistad = 5+5
    try:
        Proceso
        # Simular un error para mostrar un ejemplo
        raise ValueError("Texto ejemplo del error en el proceso.")
    except Exception as e:
        messagebox.showerror("Error en el proceso", f"Se produjo un error: {str(e)}")
        return
    
    # Notificar éxito
    messagebox.showinfo("Proceso finalizado", "El proceso ha terminado exitosamente.")
    ventana.destroy()

def cancelar():
    ventana.destroy()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Básica con Tkinter")
ventana.geometry("600x400")
ventana.resizable(False, False)

# Cargar y redimensionar la imagen
encabezado_original = Image.open(r"C:\Users\carlo\Downloads\encabezado.png")
encabezado_redimensionado = encabezado_original.resize((600, 100))  # Ajusta el tamaño (ancho, alto)
encabezado = ImageTk.PhotoImage(encabezado_redimensionado)



# Encabezad0
imagen_label = tk.Label(ventana, image=encabezado)
imagen_label.pack(pady=10)

titulo = tk.Label(ventana, text="Gestor de Archivos", font=("Arial", 18, "bold"))
titulo.pack(pady=5)

# Variables
entrada_carpeta = tk.StringVar()
entrada_archivo = tk.StringVar()

# Selección de carpeta
label_carpeta = tk.Label(ventana, text="Seleccionar carpeta:")
label_carpeta.pack(anchor="w", padx=20)
frame_carpeta = tk.Frame(ventana)
frame_carpeta.pack(fill="x", padx=20, pady=5)
campo_carpeta = tk.Entry(frame_carpeta, textvariable=entrada_carpeta, state="readonly", width=50)
campo_carpeta.pack(side="left", expand=True, fill="x")
boton_carpeta = tk.Button(frame_carpeta, text="Buscar", command=seleccionar_carpeta)
boton_carpeta.pack(side="right", padx=5)

# Selección de archivo
label_archivo = tk.Label(ventana, text="Seleccionar archivo PDF:")
label_archivo.pack(anchor="w", padx=20)
frame_archivo = tk.Frame(ventana)
frame_archivo.pack(fill="x", padx=20, pady=5)
campo_archivo = tk.Entry(frame_archivo, textvariable=entrada_archivo, state="readonly", width=50)
campo_archivo.pack(side="left", expand=True, fill="x")
boton_archivo = tk.Button(frame_archivo, text="Buscar", command=seleccionar_archivo)
boton_archivo.pack(side="right", padx=5)

# ComboBox para el tipo
label_tipo = tk.Label(ventana, text="Seleccionar tipo:")
label_tipo.pack(anchor="w", padx=20, pady=5)
combo_tipo = ttk.Combobox(ventana, values=["Editar", "Eliminar", "Agregar"], state="readonly")
combo_tipo.pack(fill="x", padx=20)

# Botones Aceptar y Cancelar
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=20)

boton_aceptar = tk.Button(frame_botones, text="Aceptar", command=aceptar)
boton_aceptar.pack(side="left", padx=10)

boton_cancelar = tk.Button(frame_botones, text="Cancelar", command=cancelar)
boton_cancelar.pack(side="right", padx=10)

# Iniciar el bucle principal
ventana.mainloop()
