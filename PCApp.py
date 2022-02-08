from cgitb import text
import tkinter as tk 
import sqlite3 as db
import os.path as fs
import random, time


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
    cursor.execute("SELECT palabra1, palabra2, descripcion, disponible, nivel, id  FROM {}".format(tabla))
    objetos = cursor.fetchall()
    con.close()
    return objetos

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
    if nivel < 0:
        nivel = 0
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("UPDATE {} SET nivel = ? where id = ?".format(tabla), (nivel, idItem))
    con.commit()
    con.close()
    #return "Se actualizó la base de datos"


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
    try:
        listaDividida = [x for x in listaCompleta.split("\n") if x]
        listaCompleta = len(listaDividida)
        print(listaCompleta)
        for i in listaDividida:
            if i != "" and "=" in i and len(i.split("=")) == 2:
                listaArray.append(i.split("="))

        
        formNuevaLista(listaArray)
        
    except Exception as e:
        print(e)

def pantallaInicio():
    global paginaInicio, lista, campoDatos, campoEjemplo, camposFrame
    
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
considerado texto principal y lo del lado derecho el significado.
Recuerda, sólo debe haber un signo de igualdad (=) por linea,
cualquier linea que no cumpla con texto1 = texto2 será ignorada.
El texto de cualquier lado puede llevar espacios o signos 
que sean diferentes al signo de igualdad (=).
Se recomienda crear la lista con más de 10 objetos. 
""")
    campoEjemplo.config(state = "disabled")
    campoEjemplo.pack(side = tk.LEFT)

    cargarFrame = tk.Frame(paginaInicio)
    cargarFrame.pack(fill = "x")
    botonCrear = tk.Button(cargarFrame, text = "Crear lista", width = 58 , font = ("Arial ", 15), command = generarLista)
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


    miListaBoton = tk.Button(paginaInicio, text = "Cargar lista seleccionada", width = 32, font = ("Arial ", 15), command = lambda : cargar())
    miListaBoton.place(x = 12, y = 660)

    labelCargado =tk.Label(paginaInicio, text = "Lista: ")
    labelCargado.place(x = 400, y = 500)
    campoCargado = tk.Text(paginaInicio, width = 30, height = 1, state = "disabled")
    campoCargado.place(x = 450, y = 500)

    verListaBoton = tk.Button(paginaInicio, text = "Ver lista", font = ("Arial ", 10), state = "disabled" )
    verListaBoton.place(x = 400, y = 550)
    iniciarBoton = tk.Button(paginaInicio, text = "Iniciar", width = 15, font = ("Arial ", 20), state = "disabled")
    iniciarBoton.place(x = 900, y = 500)


    def cargar():
        idVar = idArray[lista.curselection()[0]]
        campoCargado.config(state = "normal")
        campoCargado.delete('1.0',tk.END)
        campoCargado.insert(tk.END, nombreArray[lista.curselection()[0]])
        campoCargado.config(state = "disabled")

        verListaBoton.config(state = "normal", command = lambda x = idVar: verLista(x))
        iniciarBoton.config(state = "normal", command = lambda x = idVar: iniciarPag(x))

def verLista(idVar):
    destruirInicio()
    def mayus(e):
        return e.upper()
    def mostrarDetalles(e):

        datosArray = listaAlfabetica[listaObjetos.curselection()[0]].split("/#IDINVISIBLE#/")[1]
        detalleTexto = listaAlfabetica[listaObjetos.curselection()[0]].split("/#IDINVISIBLE#/")[0].split("=")[0]
        detalleDefinicion = listaAlfabetica[listaObjetos.curselection()[0]].split("/#IDINVISIBLE#/")[0].split("=")[1]
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

    objetosArray = []
    objetosArray = objetosTabla(obtenerTabla(idVar))

    
    verListaFrame = tk.Frame(window)
    verListaFrame.pack(fill = "both", expand = True)


    listaObjetos = tk.Listbox(verListaFrame, width= 100, height = 40)
    listaObjetos.pack(side = tk.LEFT)

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

    btnEnTest = tk.Button(botonesFrame, text = "Desactivar en test" , state ="disabled", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial ", 17))
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
    
def iniciarPag(idVar, numPreguntas = 10):
    
    global paginaTest, contador, resultadoLista #numPreguntasGlobal
    #numPreguntasGlobal = numPreguntas
    tablaActual = obtenerTabla(idVar)
    objetosArray = objetosTabla(tablaActual)
    resultadoLista = ""

    paginaInicio.pack_forget()
    #destruirInicio()
    paginaTest = tk.Frame(window, bg = colorFondoTest)
    paginaTest.pack(expand = True, fill = "both")

    contador = 0
    # botontest = tk.Button(paginaTest, text = "press", command = lambda : iniciarTest())
    # botontest.place(x = 0,y = 30)
    resultadosLabel = tk.Label(paginaTest, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 10), justify = "left")
    resultadosLabel.place(x= 20, y = 10)

    avanceLabel = tk.Label(paginaTest, text = "{}/{}".format(contador,numPreguntas), bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 20))
    avanceLabel.place(x = 1000, y = 50)
    def iniciarTest(respuesta = 0):
        global contador
        if contador == numPreguntas:
            mostrarPaginaResultado()
            #regresar()

        
        opciones = []
        numerosGenerados = []

        testInterfazFrame = tk.Frame(paginaTest, bg = colorFondoTest)
        testInterfazFrame.pack()
        randomPregunta = random.randint(0, len(objetosArray)-1)

        palabraPrincipal = objetosArray[randomPregunta][0]
        nivelPrincipal = int(objetosArray[randomPregunta][4])
        idPrincipal = objetosArray[randomPregunta][5]
        palabraPrincipalAncho = len(palabraPrincipal)
        palabraPrincipalLabel = tk.Label(testInterfazFrame, text = palabraPrincipal, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial bold", 40), width = palabraPrincipalAncho)
        palabraPrincipalLabel.pack(pady = 90)

        contador += 1
        print(contador)
        lugarRespuesta = random.randint(0, 4)
        for i in range(5):
            while True:

                numeroRandom = random.randint(0, len(objetosArray)-1)
                #print(numeroRandom)
                if numeroRandom not in numerosGenerados and numeroRandom != randomPregunta:
                    numerosGenerados.append(numeroRandom)
                    break
            if i == lugarRespuesta:
                opciones.append(objetosArray[randomPregunta][1])
            else:
                opciones.append(objetosArray[numeroRandom][1])

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
            global resultadoLista       
            try: 
                avanceLabel.config(text = "{}/{}".format(contador, numPreguntas))
                list = testInterfazFrame.winfo_children()
                for l in list:
                    l.destroy()
                testInterfazFrame.destroy()
                
                if x == lugarRespuesta:
                    resultadoLista = resultadoLista + "O {0} = {1} \n".format(palabraPrincipal, opciones[x])
                    resultadosLabel.config(text= resultadoLista)
                    nivelar(nivelPrincipal, tablaActual, 1, idPrincipal)
                else:
                    resultadoLista = resultadoLista + "X {0} = {1} -> O {2} = {3} \n".format(palabraPrincipal, opciones[x], palabraPrincipal, opciones[lugarRespuesta])
                    resultadosLabel.config(text= resultadoLista)
                    nivelar(nivelPrincipal, tablaActual, 0, idPrincipal)
                iniciarTest()
            except Exception as e: 
                print(e)
    # def verificarRespuesta():
    iniciarTest()

def mostrarPaginaResultado():
    destruirTestInicio()
    resultadoFrame = tk.Frame(window)
    resultadoFrame.pack(fill = "both", expand = True)

    resultadoPalabra1 = tk.Label(resultadoFrame, text = "HOLA", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    resultadoPalabra1.pack()
    resultadoPalabra2 = tk.Label(resultadoFrame, text = "ADIOS", bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    resultadoPalabra2.pack()

    # listaCorrectas = tk.Listbox(resultadoFrame, bg = colorFondoTest, fg = colorLetraTest, font = ("Arial", 20))
    # listaCorrectas.pack()

def generarNombreTabla():
    numeroUltimaTabla = int(obtenerUltimaTabla().split("tabla")[1])
    nombreNuevoTabla = "tabla" + str(numeroUltimaTabla + 1)
    return nombreNuevoTabla

def formNuevaLista(listaArray):
    
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
    paginaTest.pack_forget()
    paginaInicio.pack(fill = "both", expand = True)
    # destruirTestInicio()
    # pantallaInicio()
def mostrar():
    print(lista.curselection())

def destruirInicio():
    list = paginaInicio.winfo_children()
    for l in list:
        l.destroy()
    paginaInicio.destroy()

def destruirTestInicio():
    paginaTest.pack_forget()
    # print("inicio")
    # list = paginaTest.winfo_children()
    # for l in list:
    #     l.destroy()
    # paginaTest.destroy()
    # print("final")
    #paginaTest.destroy()


pantallaInicio()
window.mainloop()
