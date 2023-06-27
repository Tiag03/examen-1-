import tkinter as tk

# Función para agregar elementos al arreglo
def agregar_elemento():
    elemento = int(entry.get())
    if elemento != 0:
        arreglo.append(elemento)
        entry.delete(0, tk.END)
        label3.config(text="Elemento agregado: " + str(elemento))
    else:
        ordenar_arreglo()

# Función para ordenar el arreglo utilizando el ordenamiento burbuja
def ordenar_arreglo():
    n = len(arreglo)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]
    mostrar_resultados()

# Función para mostrar el tamaño del arreglo, el elemento de mayor valor y el elemento de menor valor
def mostrar_resultados():
    size = len(arreglo)
    max_element = max(arreglo) if size > 0 else None
    min_element = min(arreglo) if size > 0 else None
    label4.config(text="Tamaño del arreglo: " + str(size))
    label5.config(text="Elemento de mayor valor: " + str(max_element))
    label6.config(text="Elemento de menor valor: " + str(min_element))

# Crear una ventana en tkinter
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Ordenamiento burbuja")

label1 = tk.Label(ventana, text="Ingrese un elemento al arreglo:")
label1.pack()

entry = tk.Entry(ventana)
entry.pack()

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack()

label2 = tk.Label(ventana, text="Resultados:")
label2.pack()

label3 = tk.Label(ventana, text="")
label3.pack()

label4 = tk.Label(ventana, text="")
label4.pack()

label5 = tk.Label(ventana, text="")
label5.pack()

label6 = tk.Label(ventana, text="")
label6.pack()

# Declarar el arreglo vacío
arreglo = []

ventana.mainloop()
