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
        cursor.execute("CREATE TABLE tabla1(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text)")
        cursor.execute("CREATE TABLE nombreslista(id integer PRIMARY KEY, nombre text, tabla text)")
        cursor.execute("INSERT INTO nombreslista (nombre, tabla) VALUES('Meses en Inglés (ejemplo)', 'tabla1')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('January', 'Enero', 'Primer mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('February', 'Febrero', 'Segundo mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('March', 'Marzo', 'Tercer mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('April', 'Abril', 'Cuarto mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('May', 'Mayo', 'Quinto mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('June', 'Junio', 'Sexto mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('July', 'Julio', 'Séptimo mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('August', 'Agosto', 'Octavo mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('September', 'Septiembre', 'Noveno mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('October', 'Octubre', 'Décimo mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('November', 'Noviembre', 'Onceavo mes')")
        cursor.execute("INSERT INTO tabla1 (palabra1, palabra2, descripcion) VALUES('December', 'Diciembre', 'Doceavo mes')")
        cursor.execute("CREATE TABLE tabla2(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text)")
        cursor.execute("INSERT INTO nombreslista (nombre, tabla) VALUES('Colores en Inglés (ejemplo)', 'tabla2')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Azul', 'Blue', 'Color del cielo')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Rojo', 'Red', 'Color de las manzanas')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Verde', 'Green', 'Color de las plantas')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Café', 'Brown', 'Color de la tierra')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Morado', 'Purple', 'Color de las Uvas')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Rosa', 'Pink', 'Color del ajolote')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Negro', 'Black', 'Color de la oscuridad')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Blanco', 'White', 'Color de las nubes')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Amarillo', 'Yellow', 'Color del platano')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Naranja', 'Orange', 'Color de... la naranja')")
        cursor.execute("INSERT INTO tabla2 (palabra1, palabra2, descripcion) VALUES('Gris', 'Grey', 'Color del humo')")
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

def obtenerUltimaTabla():
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE tabla1(id integer PRIMARY KEY, palabra1 text, palabra2 text, descripcion text)")

def objetosTabla(tabla):
    con = db.connect("perfil.db")
    cursor = con.cursor()
    cursor.execute("SELECT palabra1, palabra2 FROM {}".format(tabla))
    objetos = cursor.fetchall()
    return objetos

def generarLista():
    listaCompleta = campoDatos.get("1.0",tk.END)
    listaArray = []
    try:
        listaDividida = listaCompleta.split("\n")
        for i in listaDividida:
            if i != "" and "=" in i and len(i.split("=")) == 2:
                listaArray.append(i.split("="))

        print(listaArray)
    except Exception as e:
        print(e)

def pantallaInicio():
    global paginaInicio, lista, campoDatos

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

        iniciarBoton.config(state = "normal", command = lambda x = idVar: iniciarPag(x))


def iniciarPag(idVar, numPreguntas = 10):

    global paginaTest, contador, resultadoLista #numPreguntasGlobal
    #numPreguntasGlobal = numPreguntas
    objetosArray = objetosTabla(obtenerTabla(idVar))
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
    avanceLabel.place(x = 800, y = 100)
    def iniciarTest(respuesta = 0):
        global contador

        if contador == numPreguntas:
            regresar()

        
        opciones = []
        numerosGenerados = []

        testInterfazFrame = tk.Frame(paginaTest, bg = colorFondoTest)
        testInterfazFrame.pack()
        randomPregunta = random.randint(0, len(objetosArray)-1)

        palabraPrincipal = objetosArray[randomPregunta][0]
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
                iniciarTest()
                if x == lugarRespuesta:
                    resultadoLista = resultadoLista + "O {0} = {1} \n".format(palabraPrincipal, opciones[x])
                    resultadosLabel.config(text= resultadoLista)
                else:
                    resultadoLista = resultadoLista + "X {0} = {1} -> O {2} = {3} \n".format(palabraPrincipal, opciones[x], palabraPrincipal, opciones[lugarRespuesta])
                    resultadosLabel.config(text= resultadoLista)
            except Exception as e: 
                print(e)
    # def verificarRespuesta():

    iniciarTest()

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
    list = paginaTest.winfo_children()
    for l in list:
        l.destroy()
    paginaTest.destroy()

pantallaInicio()
window.mainloop()
