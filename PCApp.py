import tkinter as tk 
import sqlite3 as db
import os.path as fs
import random, time, os, sys
from tkinter import messagebox

colorFondoTest = "black"
colorLetraTest = "white"


window = tk.Tk()
window.geometry("1200x700")
window.resizable(False, False)
window.title("CustomTest App")



# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except:
#         base_path = os.path.abspath(".")

#     return os.path.join(base_path, relative_path)

# window.iconbitmap(resource_path("testIcon.ico"))

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
        #Si no existe perfil.db lo crea y agrega una lista por default
        con = db.connect("perfil.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE tabla1(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text DEFAULT 'Descripción no disponible', disponible integer DEFAULT 1 NOT NULL, nivel integer DEFAULT 0 NOT NULL)")
        cursor.execute("CREATE TABLE nombreslista(id integer PRIMARY KEY, nombre text, tabla text)")
        cursor.execute("INSERT INTO nombreslista (nombre, tabla) VALUES('Animales en Inglés (ejemplo)', 'tabla1')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Bull', 'Toro')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Cow', 'Vaca')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Chicken', 'Pollo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Hen', 'Gallina')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Rooster/Cock', 'Gallo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Donkey', 'Burro')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Goat', 'Cabra')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Horse', 'Caballo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Pig', 'Cerdo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Rabbit', 'Conejo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Sheep', 'Oveja')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Turkey', 'Pavo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Goose', 'Ganso')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Shrimp', 'Camarón')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Crab', 'Cangrejo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Dolphin', 'Delfín')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Shark', 'Tiburón')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Eel', 'Anguila')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Whale', 'Ballena')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Killer whale', 'Orca')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Jellyfish', 'Medusa')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Lobster', 'Langosta')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Octopus', 'Pulpo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Oyster', 'Ostra')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Clam', 'Almeja')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Seal', 'Foca')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Squid', 'Calamar')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Cuttlefish', 'Sepia')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Boar', 'Jabalí')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Deer', 'Ciervo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Mouse', 'Ratón')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Racoon', 'Mapache')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Skunk', 'Mofeta')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Squirrel', 'Ardilla')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Bat', 'Murciélago')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Bear', 'Oso')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Weasel', 'Comadreja')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Moose', 'Alce')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Falcon', 'Halcón')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Eagle', 'Águila')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Vulture', 'Buitre')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Hummingbird', 'Colibrí')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Crow', 'Cuervo')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Owl', 'Búho')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Stork', 'Cigüeña')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Duck', 'Pato')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Cat', 'Gato')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2) VALUES('Dog', 'Perro')")
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
    con.close()
    return tabla[0][0]

def obtenerUltimaTabla():
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT tabla FROM nombreslista ORDER BY tabla DESC LIMIT 1;")
    ultimaTabla = cursor.fetchall()
    con.close()
    return ultimaTabla[0][0]

def objetosTabla(tabla):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT palabra1, palabra2, descripcion, disponible, nivel, id  FROM {} WHERE disponible = 1".format(tabla))
    objetos = cursor.fetchall()
    con.close()
    return objetos

def todosObjetosTabla(tabla):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT palabra1, palabra2, descripcion, disponible, nivel, id  FROM {}".format(tabla))
    objetos = cursor.fetchall()
    con.close()
    return objetos

def eliminarObjeto(tabla, idVar):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM {} WHERE id =  ?".format(tabla),[idVar])
    con.commit()
    con.close()
    return "Se eliminó con éxito"

def eliminarTabla(tabla, idVar):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("DROP TABLE {}".format(tabla))
    cursor.execute("DELETE FROM nombreslista WHERE id = ?", [idVar])
    con.commit()
    con.close()

# def obtenerItem(idItem, tabla):
#     con = db.connect("perfil.db")
#     cursor = con.cursor()
#     cursor.execute("SELECT palabra1, palabra2, descripcion, disponible, nivel FROM {} where id = ?".format(tabla), [idItem])
#     objetoEspecifico = cursor.fetchall()
#     con.close()
#     return objetoEspecifico

def nivelar(nivel, tabla, opcion, idItem):
    if opcion == 1:
        nivel = nivel + 1
    if opcion == 0:
        nivel = nivel - 1
    if nivel > 10:
        nivel = 10
    if nivel < 1:
        nivel = 1
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("UPDATE {} SET nivel = ? where id = ?".format(tabla), (nivel, idItem))
    con.commit()
    con.close()
    #return "Se actualizó la base de datos"

def activarDesactivarSQL(tabla, valor, idVar):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("UPDATE {} SET disponible = ? WHERE id = ?".format(tabla), (valor, idVar))
    con.commit()
    con.close()

def agregarNuevosElementosSQL(tabla, array ):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    for palabra1, palabra2 in array:
        cursor.execute("INSERT INTO {} (palabra1, palabra2) VALUES(?,?)".format(tabla), (palabra1, palabra2))
    con.commit()
    con.close()

def crearListaSQL(nombreTabla, nombreLista, listaObjetos):
    try:
        con = db.connect("perfil.db")
        cursor = con.cursor()
        cursor.execute("CREATE TABLE {}(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text DEFAULT 'Descripción no disponible', disponible integer DEFAULT 1 NOT NULL, nivel integer DEFAULT 0 NOT NULL)".format(nombreTabla))
        for texto, significado in listaObjetos:
            cursor.execute("INSERT INTO {}(palabra1, palabra2) VALUES(?,?)".format(nombreTabla), (texto, significado))

        cursor.execute("INSERT INTO nombreslista (nombre, tabla) VALUES(?, ?)", (nombreLista, nombreTabla))
        con.commit()
        con.close()
        print("Lista creada")
        return "Lista creada"
    except:
        print("Ocurrió un error")
        return "Ocurrió un error"
    
def generarLista():
    listaCompleta = campoDatos.get("1.0",tk.END)
    listaArray = []
    listaRechazada = []
    try:
        listaDividida = [x for x in listaCompleta.split("\n") if x]
        listaCompleta = len(listaDividida)
        print(listaCompleta)
        for i in listaDividida:
            if i != "" and "=" in i and len(i.split("=")) == 2:
                listaArray.append(i.split("="))
            else:
                listaRechazada.append(i)

        if len(listaArray) < 10:
            messagebox.showinfo(title="Error", message="Debe haber más de diez objetos válidos en la lista")
        else:
            if listaCompleta == len(listaArray):
                formNuevaLista(listaArray)
            else:
                #diferencia = (listaCompleta - len(listaArray))
                #messagebox.showinfo(title = "Atención", message = "{} objetos no pudieron agregarse a la lista\n Los puede agregar más tarde a la lista creada".format(diferencia)) 
                formNuevaLista(listaArray, listaRechazada)

        
    except Exception as e:
        print(e)

def pantallaInicio(rechazadosArray = None):
    global paginaInicio, lista, campoDatos, campoEjemplo, camposFrame, valorNumPreg, valorModo
    # fondoPaginaInicial = "black"
    # "white"  = "white"
    
    idArray = []
    nombreArray = []

    def focus1(e):
        input2.configure(state = "disabled")
        labelPalabra2.configure(state = "disabled")
        labelPalabra1.configure(state = "normal")
        
    def backSpace(e):
        if input2.get() == "":
            input1.focus()




    def enter1(e):
        if input1.get().strip() == "":
            return
        input2.configure(state = "normal")
        input2.focus()
        labelPalabra1.configure(state = "disabled")
        labelPalabra2.configure(state = "normal")
        
    def enter2(e):
        if input2.get().strip() == "":
            return
        campoDatos.insert(tk.END, "{} = {}\n".format(input1.get().strip(), input2.get().strip()))
        
        input1.delete("0", tk.END)
        input2.delete("0", tk.END)
        input2.configure(state = "disabled")
        labelPalabra1.configure(state = "normal")
        labelPalabra2.configure(state = "disabled")
        input1.focus()

    paginaInicio = tk.Frame(window)
    paginaInicio.pack(fill = "both", expand = True)
    camposFrame = tk.Frame(paginaInicio)
    camposFrame.pack()


    inputFrame = tk.Frame(camposFrame, bg = "azure")
    inputFrame.pack(side = tk.LEFT)
    
    fastInputFrame = tk.Frame(inputFrame, bg = "azure")
    fastInputFrame.pack()
    labelPalabra1 = tk.Label(fastInputFrame, text= "ENTER ->", bg = "azure")
    labelPalabra1.grid(column = 0, row = 0)
    labelPalabra2 = tk.Label(fastInputFrame, text= "ENTER", bg = "azure", state = "disabled")
    labelPalabra2.grid(column = 2, row = 0)
    input1 = tk.Entry(fastInputFrame)
    input1.grid(column = 0, row = 1)
    input1.bind("<Return>", enter1)
    input1.bind("<FocusIn>", focus1)
    tk.Label(fastInputFrame, text= "=", bg = "azure").grid(column = 1, row = 1)
    input2 = tk.Entry(fastInputFrame, state = "disabled")
    input2.grid(column = 2, row = 1)
    input2.bind("<Return>", enter2)
    input2.bind("<BackSpace>", backSpace)



    campoDatos = tk.Text(inputFrame, bg = "antiquewhite", height = 21)
    campoDatos.pack()

 
    if rechazadosArray != None:
        campoDatos.insert(tk.END, "Los siguientes elementos no pudieron agregarse, No cumplen con el formato: \n")
        for rechazado in rechazadosArray:
            campoDatos.insert(tk.END, rechazado + "\n")

    ejemploFrame = tk.Frame(camposFrame)
    ejemploFrame.pack(side = tk.LEFT,expand = True, fill = "y")
    campoEjemplo = tk.Text(ejemploFrame, width = 70, bg = "lightgray")
    campoEjemplo.insert(tk.INSERT, """EXPLICACIÓN:
En el campo de la izquierda debe haber una lista obedeciendo
el siguiente formato: Que contenga en cada linea una palabra, 
letra, frase o número seguido de espacio y signo de igualdad (=)
después de un espacio debe haber algo que represente 
alguna relación con lo primero.
Puedes usar los campos de entrada para ingresar automáticamente
con el formato o utilizar el campo de texto para hacerlo manual.

Ejemplo de formato:

Have they been charting me? = ¿Me han estado rastreando?
Ag = Plata
IV = Cuatro
1001 = 9

Todo lo que haya del lado izquierdo del signo de igualdad es
considerado texto principal y lo del lado derecho el significado.
Recuerda, sólo debe haber un signo de igualdad (=) por linea,
cualquier linea que no cumpla con texto1 = texto2 será ignorada.
El texto de cualquier lado puede llevar espacios o signos 
que sean diferentes al signo de igualdad (=).
Se debe crear la lista con mínimo 10 objetos. 
""")
    campoEjemplo.config(state = "disabled")
    campoEjemplo.pack()

    cargarFrame = tk.Frame(paginaInicio)
    cargarFrame.pack(fill = "x")
    botonCrear = tk.Button(cargarFrame, text = "Crear lista", width = 58 , font = ("Arial ", 15), command = generarLista)
    botonCrear.pack(side = tk.LEFT )

    listaLabel = tk.Label(paginaInicio, text = "Seleccionar lista", font = ("Arial ", 20))
    listaLabel.place(x = 10, y = 450)

    lista = tk.Listbox(paginaInicio, width = 60, bg = "lightgray")
    lista.place(x = 10, y = 500)

    rows = conexionBaseDatos()

    for nombreLista in rows:
        idArray.append(nombreLista[0])
        nombreArray.append(nombreLista[1])
        lista.insert(tk.END, nombreLista[1])


    miListaBoton = tk.Button(paginaInicio, text = "Cargar lista seleccionada", width = 32, font = ("Arial ", 15), command = lambda : cargar())
    miListaBoton.place(x = 10, y = 660)

    labelCargado =tk.Label(paginaInicio, text = "Lista: ")
    labelCargado.place(x = 400, y = 500)
    campoCargado = tk.Text(paginaInicio, width = 30, height = 1, state = "disabled", bg = "lightgray")
    campoCargado.place(x = 450, y = 500)

    verListaBoton = tk.Button(paginaInicio, text = "Estudiar lista", font = ("Arial ", 10), state = "disabled" )
    verListaBoton.place(x = 400, y = 550)

    eliminarListaBoton = tk.Button(paginaInicio, text = "Eliminar lista", font = ("Arial ", 10), state = "disabled")
    eliminarListaBoton.place(x = 500, y = 550)
    

    radioNumFrame = tk.LabelFrame(paginaInicio)
    radioNumFrame.place(x = 870, y = 500)

    valorPregLabel = tk.Label(radioNumFrame, text = "Cantidad de preguntas", font = ("Arial ", 10))
    valorPregLabel.pack()

    valorNumPreg = tk.IntVar()
    
    rdNumPreg = tk.Radiobutton(radioNumFrame, text = "10", variable = valorNumPreg, font = ("Arial ", 10), borderwidth = 10,
                        value = 10)
    rdNumPreg.pack(side = tk.LEFT)
    rdNumPreg.select()

    rdNumPreg2 = tk.Radiobutton(radioNumFrame, text = "20", variable = valorNumPreg, font = ("Arial ", 10),
                        value = 20)
    rdNumPreg2.pack(side = tk.LEFT)

    rdNumPreg3 = tk.Radiobutton(radioNumFrame, text = "30", variable = valorNumPreg, font = ("Arial ", 10),
                        value = 30)
    rdNumPreg3.pack(side = tk.LEFT)

    radioModoFrame = tk.LabelFrame(paginaInicio)
    radioModoFrame.place(x = 1040, y = 465)

    valorModo = tk.IntVar()
    
    modoLabel = tk.Label(radioModoFrame, text ="Pregunta principal", font = ("Arial ", 10))
    modoLabel.pack()

    rdModo = tk.Radiobutton(radioModoFrame, text = "Ambos", variable = valorModo, font = ("Arial ", 10), 
                       value = 0)
    rdModo.pack(anchor=tk.W)
    rdModo.select()
    

    rdModo2 = tk.Radiobutton(radioModoFrame, text = "Texto", variable = valorModo, font = ("Arial ", 10),
                        value = 1)
    rdModo2.pack(anchor=tk.W)

    rdModo3 = tk.Radiobutton(radioModoFrame, text = "Definición", variable = valorModo, font = ("Arial ", 10),
                         value = 2)
    rdModo3.pack(anchor=tk.W)
    


    iniciarBoton = tk.Button(paginaInicio, text = "Iniciar", width = 15, font = ("Arial ", 20), state = "disabled"
    , bg = "indigo", fg = "white")
    iniciarBoton.place(x = 900, y = 600)


    def cargar():
        try: 
            idVar = idArray[lista.curselection()[0]]
            campoCargado.config(state = "normal")
            campoCargado.delete('1.0',tk.END)
            campoCargado.insert(tk.END, nombreArray[lista.curselection()[0]])
            campoCargado.config(state = "disabled")

            verListaBoton.config(state = "normal", command = lambda x = idVar: verLista(x))
            iniciarBoton.config(state = "normal", command = lambda x = idVar: iniciarTestInput(x, valorNumPreg.get(), valorModo.get()))#iniciarTestPreguntas(x, valorNumPreg.get(), valorModo.get()))
            eliminarListaBoton.config(state = "normal", command = lambda x = idVar: eliminarLista(x, campoCargado.get("1.0",tk.END)) )
        except:
            pass


def eliminarLista(idVar, nombre):
    respuesta = messagebox.askyesno(title = "Atención", message = "¿Seguro que desea eliminar la lista \n'{}'?".format(nombre.strip()))
    if respuesta == True:
        eliminarTabla(obtenerTabla(idVar), idVar)
        destruirInicio()
        pantallaInicio()

def verLista(idVar, seleccion = None):
    print(idVar)
    global verListaFrame
    tablaActual = obtenerTabla(idVar)
    paginaInicio.pack_forget()
    #destruirInicio()



    def mayus(e):
        return e.upper()
    def mostrarDetalles(e):

        seleccionID = listaObjetos.curselection()[0]
        def eliminar():
            respuesta = messagebox.askyesno("Cuidado", "¿Seguro que desea borrar este objeto?")
            if respuesta == True:
                eliminarObjeto(tablaActual, detalleID)
                salirLista()
                verLista(idVar)
            else:
                return

        def cambiarDisponible(valor):
            activarDesactivarSQL(tablaActual, valor, detalleID)
            salirLista()
            verLista(idVar, seleccionID)


        datosArray = listaAlfabetica[seleccionID].split("/#IDINVISIBLE#/")[1]
        detalleTexto = listaAlfabetica[seleccionID].split("/#IDINVISIBLE#/")[0].split("=")[0]
        detalleDefinicion = listaAlfabetica[seleccionID].split("/#IDINVISIBLE#/")[0].split("=")[1]
        detalleID = datosArray.split(",")[0]
        detalleDescripcion = datosArray.split(",")[1]
        detalleDisponible = int(datosArray.split(",")[2])
        detalleNivel = int(datosArray.split(",")[3])
        
        textoPrincipalLabel.config(text = detalleTexto)
        textoSignificadoLabel.config(text = detalleDefinicion)

        if detalleNivel == 0:
            nivelLabel.config(text = "Nivel: Indefinido")
        else:
            if detalleNivel == 1 or detalleNivel == 2:
                mensaje = "Nivel:" + " ■         | " +"Falta practicar"
            if detalleNivel == 3 or detalleNivel == 4:
                mensaje = "Nivel:" + " ■ ■       | " +"Regular" 
            if detalleNivel == 5 or detalleNivel == 6:
                mensaje = "Nivel:" + " ■ ■ ■     | " +"Bueno"
            if detalleNivel == 7 or detalleNivel == 8:
                mensaje = "Nivel:" + " ■ ■ ■ ■   | " +"Muy bien"
            if detalleNivel == 9:
                mensaje = "Nivel:" + " ■ ■ ■ ■ ■ | " +"Excelente"
            if detalleNivel == 10:
                mensaje = "Nivel:" + " ★ ★ ★ ★ ★| " + "Maestro"
                
            nivelLabel.config(text =  mensaje)


        campoDescripcion.config(state = "normal")
        campoDescripcion.delete('1.0',tk.END)
        campoDescripcion.insert(tk.INSERT, detalleDescripcion)
        campoDescripcion.config(state = "disabled")

        btnEnTest.config(state = "normal")
        btnEliminar.config(state = "normal")
        btnEditarDes.config(state = "normal")
        print(detalleDisponible)
        if detalleDisponible == 1:
            btnEnTest.config(text = "Desactivar en test", command = lambda: cambiarDisponible(0))
            
        if detalleDisponible == 0:
            btnEnTest.config(text = "Activar en test", command = lambda: cambiarDisponible(1))
            

        btnEliminar.config(command = eliminar)


    def mostrarAgregar():
        global agregarFrame, campoAgregar
        agregarFrame = tk.Frame(leftSide, bg = "azure")
        agregarFrame.place(x = 0, y = 30)

        campoAgregar = tk.Text(agregarFrame, bg = "lightgray", height = 10, width = 50)
        campoAgregar.pack(pady = 10, padx = 10)

        botonesAgregarFrame = tk.Frame(agregarFrame)
        botonesAgregarFrame.pack(fill = "both", expand = True)

        btnConfirmar = tk.Button(botonesAgregarFrame, text = "Agregar", command = agregarNuevo)
        btnConfirmar.pack(side = tk.LEFT, fill = "both", expand = True)

        btnCancelar = tk.Button(botonesAgregarFrame, text = "Cancelar", command = cerrarAgregar)
        btnCancelar.pack(side = tk.LEFT, fill = "both", expand = True)
        btnAgregarNuevos.config(state = "disabled")

    def cerrarAgregar():
        agregarFrame.destroy()
        btnAgregarNuevos.config(state = "normal")

    def agregarNuevo():
        listaCompleta = campoAgregar.get("1.0",tk.END)
        listaArray = []
        listaRechazada = []
   
        listaDividida = [x for x in listaCompleta.split("\n") if x]
        listaCompleta = len(listaDividida)
        print(listaCompleta)
        for i in listaDividida:
            if i != "" and "=" in i and len(i.split("=")) == 2:
                listaArray.append(i.split("="))
            else:
                listaRechazada.append(i)

        if len(listaArray) != 0 and listaCompleta == len(listaArray):
            agregarNuevosElementosSQL(tablaActual, listaArray)
            messagebox.showinfo(title = "", message = "Se agregarón con éxito") 
        else:
            #diferencia = listaCompleta - len(listaArray)
            messagebox.showinfo(title = "Atención", message = "Sólo se agregaron {} objetos de {}".format(len(listaArray), listaCompleta)) 
            if len(listaArray) != 0:
                agregarNuevosElementosSQL(tablaActual, listaArray)
               
        cerrarAgregar()
        salirLista()
        verLista(idVar)

    objetosArray = []
    objetosArray = todosObjetosTabla(tablaActual)

    
    verListaFrame = tk.Frame(window)
    verListaFrame.pack(fill = "both", expand = True)

    leftSide = tk.Frame(verListaFrame)
    leftSide.pack(side = tk.LEFT)

    btnAgregarNuevos = tk.Button(leftSide, text = "Agregar nuevos elementos", command = mostrarAgregar)
    btnAgregarNuevos.pack(fill = "both")


    listaObjetos = tk.Listbox(leftSide, width= 55, height = 27, bg = "lightgray", font= ("Arial", 15))
    listaObjetos.pack()

    


    btnSalir = tk.Button(leftSide, text = "Salir", font= ("Arial", 15), command = salirLista)
    btnSalir.pack(fill = "both")

    listaObjetos.bind("<<ListboxSelect>>", mostrarDetalles)

    detallesFrame = tk.Frame(verListaFrame, bg = "black")
    detallesFrame.pack(side = tk.LEFT, fill = "both", expand = True)

    textoPrincipalLabel = tk.Label(detallesFrame, text = "", bg = colorFondoTest, fg = "white", font = ("Arial ", 25))
    textoPrincipalLabel.pack(pady = 15, fill = "x", expand = True)

    textoSignificadoLabel = tk.Label(detallesFrame, text = "", bg = colorFondoTest, fg = "grey", font = ("Arial ", 20))
    textoSignificadoLabel.pack(pady = 30, fill = "x", expand = True)

    nivelLabel = tk.Label(detallesFrame, text = "", bg = colorFondoTest, fg = "white", font = ("Arial ", 18))
    nivelLabel.pack(pady = 10)

    botonesFrame = tk.Frame(detallesFrame, bg = colorFondoTest)
    botonesFrame.pack()

    btnEnTest = tk.Button(botonesFrame, text = "Desactivar en test" , width = 15, state ="disabled", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial ", 17))
    btnEnTest.grid(column = 0, row = 0)

    btnEliminar = tk.Button(botonesFrame, text = "Eliminar de lista" , state ="disabled", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial ", 17))
    btnEliminar.grid(column = 1, row = 0, padx = 5)

    btnEditarDes = tk.Button(botonesFrame, text = "Editar descripción" , state ="disabled", bg = colorFondoTest, fg = colorLetraTest,font = ("Arial ", 17))
    btnEditarDes.grid(column = 2, row = 0)

    descripcionFrame = tk.Frame(detallesFrame)
    descripcionFrame.pack()

    descripcionLabel = tk.Label(descripcionFrame, text = "Descripción", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial ", 15))
    descripcionLabel.pack(fill = "both")
    campoDescripcion = tk.Text(descripcionFrame, height= 10, state ="disabled", bg = colorFondoTest, fg = colorLetraTest)
    campoDescripcion.pack()

    btnGuardar = tk.Button(detallesFrame, text = "Guardar", state = "disabled", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial ", 15))
    btnGuardar.pack(fill = "both")

    listaAlfabetica = []

    for texto, significado, descripcion, disponible, nivel, idItem in objetosArray:
        
        listaAlfabetica.append("{} = {}/#IDINVISIBLE#/{}, {}, {}, {}".format(texto, significado, idItem, descripcion, disponible, nivel))
        
    listaAlfabetica.sort(key = mayus)
    for elemento in listaAlfabetica:
        nivelSimbol = "|" + ("·"*int(elemento.split("/#IDINVISIBLE#/")[1].split(",")[3])) + "|" if int(elemento.split("/#IDINVISIBLE#/")[1].split(",")[3]) > 0 else ""
        listaObjetos.insert(tk.END, elemento.split("/#IDINVISIBLE#/")[0] + " " + nivelSimbol)
    
    if seleccion != None:
        listaObjetos.selection_set(seleccion)
        listaObjetos.activate(seleccion)
        mostrarDetalles("<<ListboxSelect>>")
    listaObjetos.focus()

def iniciarTestInput(idVar, numPreguntas, modoPreguntas):
    global contadorInput, resultadoListaInput, resultadoListaInputArray, numeroCorrectasInput
    paginaInicio.pack_forget()
    #destruirInicio()
    paginaInputFrame = tk.Frame(window, bg = colorFondoTest)
    paginaInputFrame.pack(expand = True, fill = "both")

    tablaActual = obtenerTabla(idVar)
    objetosArray = objetosTabla(tablaActual)

    contadorInput = 0
    numeroCorrectasInput = 0

    resultadoListaInput = ""
    resultadoListaInputArray = []

    avanceLabelInput = tk.Label(paginaInputFrame, text = "{}/{}".format(contadorInput,numPreguntas), bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 20))
    avanceLabelInput.place(x = 1050, y = 30)

    resultadosLabelInput = tk.Label(paginaInputFrame, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 10), justify = "left")
    resultadosLabelInput.place(x= 20, y = 70)

    botonInputSalir = tk.Button(paginaInputFrame, text = "Abortar", borderwidth=0, bg = colorFondoTest, fg = "grey", font = ("Arial bold", 15)
    , command = lambda : regresar())

    botonInputSalir.place(x = 100,y = 20)

    def iniciarTest(respuesta = 0):
        global contadorInput
        if contadorInput == numPreguntas:
            porcentaje = (numeroCorrectasInput/numPreguntas)*100
            mostrarPaginaResultado(porcentaje, resultadoListaInputArray, idVar)
            return
        
       
        
        
        testInterfazInputFrame = tk.Frame(paginaInputFrame, bg = colorFondoTest)
        testInterfazInputFrame.pack()
        randomPregunta = random.randint(0, len(objetosArray)-1)

        if modoPreguntas == 0:
            p = random.randint(0, 1)
            if p == 0:
                r = 1
            else:
                r = 0
        if modoPreguntas == 1:
            p = 0
            r = 1
        if modoPreguntas == 2:
            p = 1
            r = 0


        palabraPrincipal = objetosArray[randomPregunta][p]
        respuestaCorrecta = objetosArray[randomPregunta][r]
        nivelPrincipal = int(objetosArray[randomPregunta][4])
        idPrincipal = objetosArray[randomPregunta][5]
        palabraPrincipalAncho = len(palabraPrincipal)
        palabraPrincipalLabel = tk.Label(testInterfazInputFrame, text = palabraPrincipal, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 40), width = palabraPrincipalAncho)
        palabraPrincipalLabel.pack(pady = 90)

        respuestaInput = tk.Entry(testInterfazInputFrame,  font = ("Arial bold",30), justify='center')
        respuestaInput.pack()
        respuestaInput.focus()

        respuestaInput.bind("<Return>", lambda e = "<Return>": verificarRespuesta(e))

        btnVerificar = tk.Button(testInterfazInputFrame, text = "ENTER", bg = "dimgrey", fg = "white",
        command = lambda  : verificarRespuesta())
        btnVerificar.pack(fill = "x")

        # btnPista = tk.Button(testInterfazInputFrame, text = "Pista")
        # btnPista.pack(side = tk.LEFT)

        contadorInput += 1


        #print(contadorInput)
        # lugarRespuesta = random.randint(0, 4)
        # for i in range(5):
        #     while True:

        #         numeroRandom = random.randint(0, len(objetosArray)-1)
        #         #print(numeroRandom)
        #         if numeroRandom not in numerosGenerados and numeroRandom != randomPregunta:
        #             numerosGenerados.append(numeroRandom)
        #             break
        #     if i == lugarRespuesta:
        #         opciones.append(objetosArray[randomPregunta][r])
        #     else:
        #         opciones.append(objetosArray[numeroRandom][r])

        # numerosGenerados = []

        # anchoBotonArr = []

        # for i in opciones:
        #     anchoBotonArr.append(len(i))

        # anchoBotonArr.sort()
        # anchoBoton = anchoBotonArr[-1] + 2

        # if anchoBoton < 20:
        #     anchoBoton = 20


        # opcionBoton1 = tk.Button(testInterfazInputFrame, text = opciones[0], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        # command = lambda : verificarRespuesta(0))
        # opcionBoton1.pack(pady = 10)

        # opcionBoton2 = tk.Button(testInterfazInputFrame, text = opciones[1], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        # command = lambda : verificarRespuesta(1))
        # opcionBoton2.pack(pady = 10)
        # opcionBoton3 = tk.Button(testInterfazInputFrame, text = opciones[2], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        # command = lambda : verificarRespuesta(2))
        # opcionBoton3.pack(pady = 10)
        # opcionBoton4 = tk.Button(testInterfazInputFrame, text = opciones[3], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        # command = lambda : verificarRespuesta(3))
        # opcionBoton4.pack(pady = 10)
        # opcionBoton5 = tk.Button(testInterfazInputFrame, text = opciones[4], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        # command = lambda : verificarRespuesta(4))
        # opcionBoton5.pack(pady = 10)

        def verificarRespuesta(e = "<Return>"):
            global resultadoListaInput, numeroCorrectasInput

            respuestaUsuario = respuestaInput.get()
            try: 
                avanceLabelInput.config(text = "{}/{}".format(contadorInput, numPreguntas))
                list = testInterfazInputFrame.winfo_children()
                for l in list:
                    l.destroy()
                testInterfazInputFrame.destroy()
                
                if sim(respuestaUsuario) == sim(respuestaCorrecta):
                    numeroCorrectasInput = numeroCorrectasInput + 1
                    resultadoListaInputArray.append(("[O] {} = {}".format(palabraPrincipal, respuestaCorrecta),1, palabraPrincipal, respuestaCorrecta))
                    resultadoListaInput = resultadoListaInput + "O {0} = {1} \n".format(palabraPrincipal, respuestaCorrecta)
                    resultadosLabelInput.config(text= resultadoListaInput)
                    nivelar(nivelPrincipal, tablaActual, 1, idPrincipal)
                else:
                    resultadoListaInputArray.append(("[X] {} ≠ {}".format(palabraPrincipal, respuestaUsuario),0,palabraPrincipal, respuestaCorrecta))
                    resultadoListaInput = resultadoListaInput + "X {0} ≠ {1} -> O {2} = {3} \n".format(palabraPrincipal, respuestaUsuario, palabraPrincipal, respuestaCorrecta)
                    resultadosLabelInput.config(text= resultadoListaInput)
                    nivelar(nivelPrincipal, tablaActual, 0, idPrincipal)
                iniciarTest()
            except Exception as e: 
                print(e)
    # def verificarRespuesta():
    iniciarTest()

def iniciarTestPreguntas(idVar, numPreguntas, modoPreguntas):
    
    global paginaTest, contador, resultadoLista, numeroCorrectas #numPreguntasGlobal
    print(valorNumPreg.get())
    #numPreguntasGlobal = numPreguntas
    tablaActual = obtenerTabla(idVar)
    objetosArray = objetosTabla(tablaActual)
    if len(objetosArray) < 10:
         messagebox.showinfo(title = "Atención", message = "Se necesitan más de 10 elementos para iniciar el test\n Verifica que no engas elementos desactivados en test")
         return

    resultadoLista = ""
    resultadoListaArray = []
    paginaInicio.pack_forget()
    #destruirInicio()
    paginaTest = tk.Frame(window, bg = colorFondoTest)
    paginaTest.pack(expand = True, fill = "both")

    contador = 0
    numeroCorrectas = 0
    botontest = tk.Button(paginaTest, text = "Abortar", borderwidth=0, bg = colorFondoTest, fg = "grey", font = ("Arial bold", 15)
    , command = lambda : regresar())

    botontest.place(x = 100,y = 20)
    resultadosLabel = tk.Label(paginaTest, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 10), justify = "left")
    resultadosLabel.place(x= 20, y = 70)

    avanceLabel = tk.Label(paginaTest, text = "{}/{}".format(contador,numPreguntas), bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 20))
    avanceLabel.place(x = 1050, y = 30)
    def iniciarTest(respuesta = 0):
        global contador
        if contador == numPreguntas:
            porcentaje = (numeroCorrectas/numPreguntas)*100
            mostrarPaginaResultado(porcentaje, resultadoListaArray, idVar)
            return
        
        opciones = []
        numerosGenerados = []
        
        testInterfazFrame = tk.Frame(paginaTest, bg = colorFondoTest)
        testInterfazFrame.pack()
        randomPregunta = random.randint(0, len(objetosArray)-1)

        if modoPreguntas == 0:
            p = random.randint(0, 1)
            if p == 0:
                r = 1
            else:
                r = 0
        if modoPreguntas == 1:
            p = 0
            r = 1
        if modoPreguntas == 2:
            p = 1
            r = 0


        palabraPrincipal = objetosArray[randomPregunta][p]
        nivelPrincipal = int(objetosArray[randomPregunta][4])
        idPrincipal = objetosArray[randomPregunta][5]
        palabraPrincipalAncho = len(palabraPrincipal)
        palabraPrincipalLabel = tk.Label(testInterfazFrame, text = palabraPrincipal, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 40), width = palabraPrincipalAncho)
        palabraPrincipalLabel.pack(pady = 90)

        contador += 1
        #print(contador)
        lugarRespuesta = random.randint(0, 4)
        for i in range(5):
            while True:

                numeroRandom = random.randint(0, len(objetosArray)-1)
                #print(numeroRandom)
                if numeroRandom not in numerosGenerados and numeroRandom != randomPregunta:
                    numerosGenerados.append(numeroRandom)
                    break
            if i == lugarRespuesta:
                opciones.append(objetosArray[randomPregunta][r])
            else:
                opciones.append(objetosArray[numeroRandom][r])

        numerosGenerados = []

        anchoBotonArr = []

        for i in opciones:
            anchoBotonArr.append(len(i))

        anchoBotonArr.sort()
        anchoBoton = anchoBotonArr[-1] + 2

        if anchoBoton < 20:
            anchoBoton = 20


        opcionBoton1 = tk.Button(testInterfazFrame, text = opciones[0], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        command = lambda : verificarRespuesta(0))
        opcionBoton1.pack(pady = 10)

        opcionBoton2 = tk.Button(testInterfazFrame, text = opciones[1], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        command = lambda : verificarRespuesta(1))
        opcionBoton2.pack(pady = 10)
        opcionBoton3 = tk.Button(testInterfazFrame, text = opciones[2], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        command = lambda : verificarRespuesta(2))
        opcionBoton3.pack(pady = 10)
        opcionBoton4 = tk.Button(testInterfazFrame, text = opciones[3], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        command = lambda : verificarRespuesta(3))
        opcionBoton4.pack(pady = 10)
        opcionBoton5 = tk.Button(testInterfazFrame, text = opciones[4], width = anchoBoton, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 25), 
        command = lambda : verificarRespuesta(4))
        opcionBoton5.pack(pady = 10)

        def verificarRespuesta(x):
            global resultadoLista, numeroCorrectas
            try: 
                avanceLabel.config(text = "{}/{}".format(contador, numPreguntas))
                list = testInterfazFrame.winfo_children()
                for l in list:
                    l.destroy()
                testInterfazFrame.destroy()
                
                if x == lugarRespuesta:
                    numeroCorrectas = numeroCorrectas + 1
                    resultadoListaArray.append(("[O] {} = {}".format(palabraPrincipal, opciones[x]),1, palabraPrincipal, opciones[x]))
                    resultadoLista = resultadoLista + "O {0} = {1} \n".format(palabraPrincipal, opciones[x])
                    resultadosLabel.config(text= resultadoLista)
                    nivelar(nivelPrincipal, tablaActual, 1, idPrincipal)
                else:
                    resultadoListaArray.append(("[X] {} ≠ {}".format(palabraPrincipal, tachar(opciones[x])),0,palabraPrincipal, opciones[lugarRespuesta]))
                    resultadoLista = resultadoLista + "X {0} ≠ {1} -> O {2} = {3} \n".format(palabraPrincipal, opciones[x], palabraPrincipal, opciones[lugarRespuesta])
                    resultadosLabel.config(text= resultadoLista)
                    nivelar(nivelPrincipal, tablaActual, 0, idPrincipal)
                iniciarTest()
            except Exception as e: 
                print(e)
    # def verificarRespuesta():
    iniciarTest()

def mostrarPaginaResultado(porcentaje, resultadoArray, idVar):
    global resultadoFrame
    destruirTestInicio()
    
    def seleccionRes(e):
       objeto = resultadoArray[listaResultadoFinal.curselection()[0]]
       resultadoPalabra1.config(text = objeto[2])
       resultadoPalabra2.config(text = objeto[3])

    colorPorcentaje = ""
    if porcentaje <= 100:
        colorPorcentaje = "green"
    if porcentaje < 80:
        colorPorcentaje = "yellow"
    if porcentaje < 50:
        colorPorcentaje = "red"


    resultadoFrame = tk.Frame(window, bg = colorFondoTest)
    resultadoFrame.pack(fill = "both", expand = True)

    resultadoPalabra1 = tk.Label(resultadoFrame, text = "", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    resultadoPalabra1.pack(fill = "both", expand = True)
    resultadoPalabra2 = tk.Label(resultadoFrame, text = "", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    resultadoPalabra2.pack(fill = "both", expand = True)

    listaResultadoFinal = tk.Listbox(resultadoFrame,  bg = colorFondoTest, height= 10, fg = colorLetraTest, font = ("Arial", 13))
    listaResultadoFinal.pack(fill = "both", expand = True)
    #index = 0
    #colorBG = ""
    for res in resultadoArray:
        #if res[1] == 1:
        #    colorBG = "green"
        #else:
        #    colorBG  ="red"

        listaResultadoFinal.insert(tk.END, res[0])
        #listaResultadoFinal.itemconfigure(index, bg = colorBG)
        #index = index + 1

    listaResultadoFinal.bind("<<ListboxSelect>>", seleccionRes)

    

    bottonFrame = tk.Frame(resultadoFrame, bg = colorFondoTest)
    bottonFrame.pack(fill = "x")
    btnSalir = tk.Button(bottonFrame, text = "Salir", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20)
    , command = lambda : destruirResultado())
    btnSalir.pack(side = tk.LEFT, fill = "both", expand = True)
    
    btnReiniciar = tk.Button(bottonFrame, text = "Test otra vez", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20)
    , command = lambda : destruirResultado(idVar, 0))
    btnReiniciar.pack(side = tk.LEFT, fill = "both", expand = True)
    


    precisionLabel = tk.Label(bottonFrame, text = "Precisión: ", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    precisionLabel.pack(side = tk.LEFT)
    porcentajeLabel = tk.Label(bottonFrame, text = str(round(porcentaje,1)) + "%", bg = colorFondoTest, fg = colorPorcentaje, font = ("Arial", 20))
    porcentajeLabel.pack(side = tk.LEFT)
    # listaCorrectas = tk.Listbox(resultadoFrame, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    # listaCorrectas.pack()

def generarNombreTabla():
    try:
        numeroUltimaTabla = int(obtenerUltimaTabla().split("tabla")[1])
        nombreNuevoTabla = "tabla" + str(numeroUltimaTabla + 1)
        return nombreNuevoTabla
    except: 
        return "tabla1"

def tachar(texto):
    result = ''
    for c in texto:
        result = result + c + '\u0336'
    return result

def sim(texto):
    textofinal = texto.lower().strip().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü", "u")
    return textofinal

def formNuevaLista(listaArray, rechazadosArray = None):
    
    def crear():
        
        nombreLista = nombreListaInput.get()
        if nombreLista.strip() == "":
            astericoLabel.config(text= "*")
            nombreListaInput.delete("0", tk.END)
        else:
            nombreTabla = generarNombreTabla()
            mensaje = crearListaSQL(nombreTabla, nombreLista, listaArray)
            print(mensaje)
            ventanaConfirmacion.destroy()
            destruirInicio()
            if rechazadosArray != None:
                pantallaInicio(rechazadosArray)
            else:
                pantallaInicio()
    
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    ventanaConfirmacion = tk.Toplevel(window, bg = "cyan")
    ventanaConfirmacion.geometry("%dx%d+%d+%d" % (500, 150, x + 400 , y + 100))
    ventanaConfirmacion.resizable(False, False)
    ventanaConfirmacion.overrideredirect(1)

    nombreLabel = tk.Label(ventanaConfirmacion, text= "Nombre de la lista: ", bg = "cyan" , font = ("arial bold", 15))
    nombreLabel.grid(column = 0, row = 0, pady = 15, padx = 15)

    nombreListaInput = tk.Entry(ventanaConfirmacion , font = ("arial bold", 15))
    nombreListaInput.grid(column = 1, row =0, pady = 15 )

    astericoLabel = tk.Label(ventanaConfirmacion, text= "", fg = "red",  bg = "cyan" , font = ("arial bold", 25))
    astericoLabel.grid(column =2, row = 0)

    btnCancelar = tk.Button(ventanaConfirmacion, text = "CANCELAR", bg = "red", font = ("arial bold", 15), width = 10, command = ventanaConfirmacion.destroy)
    btnCancelar.grid(column = 0, row = 1, pady = 15, padx = 15)

    btnCrear = tk.Button(ventanaConfirmacion, text = "CREAR", bg = "green", font = ("arial bold", 15), width = 10, command = crear)
    btnCrear.grid(column = 1, row = 1, pady = 15)

    ventanaConfirmacion.grab_set()

def regresar():
    destruirTestInicio()
    paginaInicio.pack(fill = "both", expand = True)
    # 
    # pantallaInicio()

def salirLista():
    list = verListaFrame.winfo_children()
    for l in list:
        l.destroy()
    verListaFrame.destroy()
    paginaInicio.pack(fill = "both", expand = True)
    
def mostrar():
    print(lista.curselection())

def destruirResultado(idVar = "", salir = 1):
    list = resultadoFrame.winfo_children()
    for l in list:
        l.destroy()
    resultadoFrame.destroy()
    if salir == 1:
        paginaInicio.pack(fill = "both", expand = True)
    else:
        iniciarTestPreguntas(idVar, valorNumPreg.get(), valorModo.get())

def destruirInicio():
    list = paginaInicio.winfo_children()
    for l in list:
        l.destroy()
    paginaInicio.destroy()

def destruirTestInicio():
    list = paginaTest.winfo_children()
    for l in list:
        l.destroy()
    paginaTest.destroy()
    paginaTest.destroy()

pantallaInicio()
window.mainloop()
