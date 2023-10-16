import tkinter as tk
from tkinter import ttk



# Crea una instancia de la ventana principal
ventana = tk.Tk()

# Opcional: Configura el título de la ventana
ventana.title("Mi Ventana Tkinter")

# Opcional: Configura las dimensiones de la ventana (ancho x alto)
ventana.geometry("400x300")


download_button = tk.Button(text="Download")
download_button.pack()


# Opcional: Agrega widgets (como etiquetas, botones, etc.) a la ventana
cuadro_texto = tk.Entry(ventana)
cuadro_texto.pack()



etiqueta = tk.Label(ventana, text="Downloader")
etiqueta.pack()  # Coloca el widget en la ventana
#etiqueta.pack_forget()
# Opcional: Define funciones para responder a eventos


# Porgress bar
progressbar = ttk.Progressbar()
progressbar.place(x=30, y=60, width=200)
progressbar.step(50)
ventana.geometry("300x200")

# Muestra la ventana y entra en el bucle principal
ventana.mainloop()