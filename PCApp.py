import tkinter as tk 
import sqlite3 as db
import os.path as fs
import random


window = tk.Tk()
window.geometry("1200x700")

colorFondoTest = "black"
colorLetraTest = "white"

def conexionBaseDatos():
    if fs.exists("perfil.db"):
        con = db.connect("perfil.db")
        cursor = con.cursor()
        #cursor.execute("SELECT name FROM sqlite_master where type= 'table'")
        cursor.execute("SELECT id, nombre FROM nombreslista")
        rows = cursor.fetchall()

        con.close()
        return rows
    else:
        con = db.connect("perfil.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE meses(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text)")
        cursor.execute("CREATE TABLE nombreslista(id integer PRIMARY KEY, nombre text, tabla text)")
        cursor.execute("INSERT INTO nombreslista (nombre, tabla) VALUES('Meses en Inglés', 'meses')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('January', 'Enero', 'Primer mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('February', 'Febrero', 'Segundo mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('March', 'Marzo', 'Tercer mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('April', 'Abril', 'Cuarto mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('May', 'Mayo', 'Quinto mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('June', 'Junio', 'Sexto mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('July', 'Julio', 'Séptimo mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('August', 'Agosto', 'Octavo mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('September', 'Septiembre', 'Noveno mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('October', 'Octubre', 'Décimo mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('November', 'Noviembre', 'Onceavo mes')")
        cursor.execute("INSERT INTO meses (palabra1, palabra2, descripcion) VALUES('December', 'Diciembre', 'Doceavo mes')")
        con.commit()
        #cursor.execute("SELECT name FROM sqlite_master where type= 'table'")
        cursor.execute("SELECT id, nombre FROM nombreslista")
        rows = cursor.fetchall()
        # cursor.execute("select last_insert_rowid()")
        # ids = cursor.fetchall()
        # print(ids)
        con.close()

        return rows

def obtenerTabla(idVar):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT tabla FROM nombreslista WHERE id = ?", [idVar])
    tabla = cursor.fetchall()
    return tabla[0][0]

def objetosTabla(tabla):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT palabra1, palabra2 FROM {}".format(tabla))
    objetos = cursor.fetchall()
    return objetos

def pantallaInicio():
    global paginaInicio, lista

    idArray = []
    nombreArray = []
    paginaInicio = tk.Frame(window)
    paginaInicio.pack(fill = "both", expand = True)
    camposFrame = tk.Frame(paginaInicio)
    camposFrame.pack()
    campoDatos = tk.Text(camposFrame, bg = "azure")
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

    rows = conexionBaseDatos()

    for nombreLista in rows:
        idArray.append(nombreLista[0])
        nombreArray.append(nombreLista[1])
        lista.insert(tk.END, nombreLista[1])


    miListaBoton = tk.Button(paginaInicio, text = "Cargar lista seleccionada", width = 32, font = ("Arial ", 15), command = lambda : mostrar())
    miListaBoton.place(x = 12, y = 660)

    labelCargado =tk.Label(paginaInicio, text = "Lista: ")
    labelCargado.place(x = 400, y = 500)
    campoCargado = tk.Text(paginaInicio, width = 30, height = 1, state = "disabled")
    campoCargado.place(x = 450, y = 500)

    iniciarBoton = tk.Button(paginaInicio, text = "Iniciar", width = 15, font = ("Arial ", 20), state = "disabled")
    iniciarBoton.place(x = 900, y = 500)


    def mostrar():
        idVar = idArray[lista.curselection()[0]]
        campoCargado.config(state = "normal")
        campoCargado.delete('1.0',tk.END)
        campoCargado.insert(tk.END, nombreArray[lista.curselection()[0]])
        campoCargado.config(state = "disabled")

        iniciarBoton.config(state = "normal", command = lambda x = idVar: iniciar(x))


def iniciar(idVar):
    objetosArray = objetosTabla(obtenerTabla(idVar))
    global paginaTest
    opciones = []
    numerosGenerados = []
    paginaInicio.pack_forget()
    paginaTest = tk.Frame(window, bg = colorFondoTest)
    paginaTest.pack(expand = True, fill = "both")

    palabraPrincipalLabel = tk.Label(paginaTest, text = objetosArray[random.randint(0, len(objetosArray)-1)][0], bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 40))
    palabraPrincipalLabel.pack(pady = 90)
    for i in range(5):
        while True:
            numeroRandom = random.randint(0, len(objetosArray)-1)
            print(numeroRandom)
            if numeroRandom not in numerosGenerados:
                numerosGenerados.append(numeroRandom)
                break
        opciones.append(objetosArray[numeroRandom][1])

    
    anchoBotonArr = []

    for i in opciones:
        anchoBotonArr.append(len(i))

    anchoBotonArr.sort()
    anchoBoton = anchoBotonArr[-1] + 2

    for i in range(len(opciones)):

        


        opcionBoton = tk.Button(paginaTest, text = opciones[i], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25))
        opcionBoton.pack(pady = 10)


def regresar():
    paginaInicio.pack()
    paginaTest.pack_forget()

def mostrar():
    print(lista.curselection())
conexionBaseDatos()
pantallaInicio()
window.mainloop()