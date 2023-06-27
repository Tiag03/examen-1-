import tkinter as tk
from collections import deque

# Función para encolar un elemento
def encolar():
    elemento = int(entry.get())
    cola.append(elemento)
    label3.config(text="Elemento encolado: " + str(elemento))
    entry.delete(0, tk.END)

# Función para desencolar un elemento
def desencolar():
    if len(cola) > 0:
        elemento = cola.popleft()
        label3.config(text="Elemento desencolado: " + str(elemento))
    else:
        label3.config(text="La cola está vacía")

# Función para verificar si la cola está vacía
def verificar_vacia():
    if len(cola) == 0:
        label3.config(text="La cola está vacía")
    else:
        label3.config(text="La cola no está vacía")

# Crear una ventana en tkinter
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Operaciones con una cola")

label1 = tk.Label(ventana, text="Ingrese un elemento a la cola:")
label1.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_encolar = tk.Button(ventana, text="Encolar", command=encolar)
boton_encolar.pack()

boton_desencolar = tk.Button(ventana, text="Desencolar", command=desencolar)
boton_desencolar.pack()

boton_vacia = tk.Button(ventana, text="Verificar si está vacía", command=verificar_vacia)
boton_vacia.pack()

label2 = tk.Label(ventana, text="Operaciones:")
label2.pack()

label3 = tk.Label(ventana, text="")
label3.pack()

# Crear una cola vacía
cola = deque()

ventana.mainloop()
