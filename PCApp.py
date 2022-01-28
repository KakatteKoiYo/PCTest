

import tkinter as tk 

window = tk.Tk()
window.geometry("1200x700")
def pantallaInicio():
    paginaInicio = tk.Frame(window)
    paginaInicio.pack(fill = "both", expand = True)
    camposFrame = tk.Frame(paginaInicio)
    camposFrame.pack()
    campoDatos = tk.Text(camposFrame)
    campoDatos.pack(side = tk.LEFT)
    campoEjemplo = tk.Text(camposFrame, width = 70)
    campoEjemplo.insert(tk.INSERT, """
EXPLICACIÓN:
En el campo de la izquierda debe haber una lista obedeciendo
el siguiente formato: Que contenga en cada linea una palabra, 
letra, frase o número seguido de espacio y signo de igualdad (=)
después de un espacio debe haber algo que represente 
alguna relación con lo primero.
Ejemplo de formato:

Have they been charting me? = ¿Me han estado rastreando?
Ag = Plata
IV = Cuatro
1001 = 9

Todo lo que haya del lado izquierdo del signo de igualdad es
considerado lo principal y lo del lado derecho el significado.

Se recomienda crear la lista con más de 10 objetos. 
""")
    campoEjemplo.config(state = "disabled")
    campoEjemplo.pack(side = tk.LEFT)

    cargarFrame = tk.Frame(paginaInicio)
    cargarFrame.pack(fill = "x")
    botonCrear = tk.Button(cargarFrame, text = "Crear lista", width = 58 , font = ("Arial ", 15))
    botonCrear.pack(side = tk.LEFT )

    listaLabel = tk.Label(paginaInicio, text = "Seleccionar lista", font = ("Arial ", 20))
    listaLabel.place(x = 10, y = 450)

    lista = tk.Listbox(paginaInicio, width = 60)
    lista.place(x = 10, y = 500)
    # miListaBoton = tk.Button(paginaInicio, text = "Cargar lista", font = ("Arial ", 20))
    # miListaBoton.place(x = 10, y = 500)

    iniciarBoton = tk.Button(paginaInicio, text = "Iniciar", width = 15, font = ("Arial ", 20))
    iniciarBoton.place(x = 300, y = 500)



pantallaInicio()
window.mainloop()