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

# Función para ordenar el arreglo por selección
def ordenar_arreglo():
    n = len(arreglo)
    for i in range(n-1):
        max_index = i
        for j in range(i+1, n):
            if arreglo[j] > arreglo[max_index]:
                max_index = j
        arreglo[i], arreglo[max_index] = arreglo[max_index], arreglo[i]
    mostrar_resultados()

# Función para mostrar el tamaño del arreglo, el promedio y la suma de los elementos
def mostrar_resultados():
    size = len(arreglo)
    average = sum(arreglo) / size if size > 0 else 0
    total_sum = sum(arreglo)
    label4.config(text="Tamaño del arreglo: " + str(size))
    label5.config(text="Promedio del arreglo: " + str(average))
    label6.config(text="Suma de los elementos: " + str(total_sum))

# Crear una ventana en tkinter
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Ordenamiento por selección")

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
