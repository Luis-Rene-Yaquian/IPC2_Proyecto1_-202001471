import xml.etree.ElementTree as ET
from os import system,startfile
import os
import graphviz
import copy
from PIL import Image


class lista():
    def __init__(self) -> None:
        self.inicio = None
        self.codigo = None
        self.size = 0
        self.id = None

    def agregar(self,nodoNuevo):
        tmp = self.inicio
        if tmp == None:
            self.inicio = nodoNuevo
        else:
            while tmp.siguiente != None:
                tmp = tmp.siguiente
            tmp.siguiente = nodoNuevo
            nodoNuevo.anterior = tmp
        self.size += 1

    def imprimirPisos(self):
        nodo_piso = self.inicio
        while nodo_piso != None:
            print("---------------------------------------------")
            print("Nombre :",nodo_piso.dato.nombre)
            print("R :",nodo_piso.dato.r)
            print("C :",nodo_piso.dato.c)
            print("F :",nodo_piso.dato.f)
            print("S :",nodo_piso.dato.s)
            listaListas = nodo_piso.dato.patrones #instancia de lista//contine nodos que contienen otras listas de caracteres
            ListaIndividual = listaListas.inicio
            contador = 1
            while ListaIndividual != None:
                print(f"********************lista #{contador}******************")
                tmp = ListaIndividual.dato.inicio
                if tmp != None:
                    print("\t\tCodigo :",tmp.nombre)
                while tmp != None:
                    print(">Azulejo color : ",tmp.dato)
                    tmp = tmp.siguiente
                ListaIndividual = ListaIndividual.siguiente
            nodo_piso = nodo_piso.siguiente
    
    def imprimirNombresPisos(self):
        nodo_piso = self.inicio
        contador = 1
        while nodo_piso != None:
            print(f"----------------------PISO #{contador}----------------------")
            contador += 1
            print(">Nombre :",nodo_piso.dato.nombre,"\n")
            nodo_piso = nodo_piso.siguiente
        
    def crearGrafos(self):
        nodo_piso = self.inicio
        while nodo_piso != None:

            listaListas = nodo_piso.dato.patrones #instancia de lista//contine nodos que contienen otras listas de caracteres
            ListaIndividual = listaListas.inicio
            while ListaIndividual != None:

                crearGrafo(ListaIndividual,nodo_piso.dato.r,nodo_piso.dato.c)
                ListaIndividual = ListaIndividual.siguiente
            nodo_piso = nodo_piso.siguiente

    def ordenarPisos(self):
        pass

    def retornarNodo(self,posicion):
        tmp = self.inicio
        while tmp is not None:
            if tmp.id == posicion:
                return tmp
            tmp = tmp.siguiente
        return None

    def bubbleSortPiso(self):
        n = self.size

        for i in range(n):

            for j in range(0, n-i-1):

                print("Comparando :",self.retornarNodo(j).dato.nombre,self.retornarNodo(j+1).dato.nombre,j,j+1)
                if self.retornarNodo(j).dato.nombre > self.retornarNodo(j+1).dato.nombre :
                    print("cambio")
                    nodoJ = self.retornarNodo(j).dato
                    nodoJ_2 = self.retornarNodo(j+1).dato
                    self.retornarNodo(j).dato = nodoJ_2
                    self.retornarNodo(j+1).dato = nodoJ

    def bubbleSortCodigos(self):
        print(self.size)
        n = self.size

        for i in range(n):

            for j in range(0, n-i-1):

                print("Comparando :",self.retornarNodo(j).dato.codigo,self.retornarNodo(j+1).dato.codigo,j,j+1)
                if self.retornarNodo(j).dato.codigo > self.retornarNodo(j+1).dato.codigo :
                    print("cambio")
                    nodoJ = self.retornarNodo(j).dato
                    nodoJ_2 = self.retornarNodo(j+1).dato
                    self.retornarNodo(j).dato = nodoJ_2
                    self.retornarNodo(j+1).dato = nodoJ

    def ordenarPatrones(self):
        tmp = self.inicio#nodo Piso
        while tmp != None:
            tmp.dato.patrones.bubbleSortCodigos()
            tmp = tmp.siguiente
        

tree = None
root = None
ruta = None
listaPisos = lista()

class nodo():
    def __init__(self,dato) -> None:
        self.siguiente = None
        self.anterior = None
        self.dato = dato
        self.nombre = None
        self.id = None

        self.fila = None
        self.columna = None

class piso():
    def __init__(self,nombre,r,c,f,s,patrones) -> None:
        self.nombre = nombre
        self.r = int(r)
        self.f = float(f)
        self.c = int(c)
        self.s = int(s)
        self.patrones = patrones # lista.
        
    def mostrarPatrones(self):
        listaListas = self.patrones #instancia de lista//contine nodos que contienen otras listas de caracteres
        ListaIndividual = listaListas.inicio
        contador = 1
        while ListaIndividual != None:# LIndiv es un nodo
            print(f"********************lista #{contador}******************")
            contador += 1
            tmp = ListaIndividual.dato.inicio
            if tmp != None:
                print("\t\tCodigo :",tmp.nombre)
            while tmp != None:
                print("\t\t\t>Azulejo color : ",tmp.dato)
                tmp = tmp.siguiente
            ListaIndividual = ListaIndividual.siguiente

class TextoCambio():
    def __init__(self) -> None:
        self.listaA = None
        self.listaB = None
        self.movimientos = "\n==========Movientos==========="
        self.contador = 1
        self.gasto = 0

def simulacion(piso,codigoA,codigoB):
    cambio(codigoA,codigoB,piso)

def cambio(codigoA,codigoB,pisoE):
    salida = TextoCambio()
    listA = copy.copy(retornarListaIndividual(pisoE.patrones,codigoA))#Patron actual
    listB = copy.copy(retornarListaIndividual(pisoE.patrones,codigoB))#Patron al que deseamos llegar.
    pivFilas = 0
    pivColumnas = 0
    azuActual = retornarNodo(listA,pivFilas,pivColumnas)
    azuDestino = retornarNodo(listB,pivFilas,pivColumnas)
    while azuActual is not None and azuDestino is not None:

        #azulejoActual voltear.
        if azuActual.dato != azuDestino.dato:
            salida.movimientos += f"\n{salida.contador}. Voltear el azulejo de la fila {azuActual.fila} y de la columna {azuActual.columna} . Costo Q. {pisoE.f}"
            salida.contador += 1
            salida.gasto += pisoE.f
        pivColumnas+= 1
        if pivColumnas == pisoE.c:
            pivColumnas = 0
            pivFilas += 1
        azuActual = retornarNodo(listA,pivFilas,pivColumnas)
        azuDestino = retornarNodo(listB,pivFilas,pivColumnas)
    print(f"\nGasto total: {salida.gasto}")
    print("Movimientos:")
    print(salida.movimientos)
    try:
        im = Image.open(f'Graficas//{codigoB}.png')
        im.show()
    except:
        print("No se pudo abrir/encontrar el grafo solicitado.")

def retornarPiso(nombre):
    global listaPisos
    tmp = listaPisos.inicio
    while tmp != None:
        if tmp.dato.nombre == nombre:
            return tmp
        tmp = tmp.siguiente
    return None

def retornarListaIndividual(patrones,codigo):
    listaListas = patrones #instancia de lista//contine nodos que contienen otras listas de caracteres
    ListaIndividual = listaListas.inicio
    while ListaIndividual != None:
        print(f"comparando el codigo : {codigo} con el codigo {ListaIndividual.dato.codigo}")
        if codigo == ListaIndividual.dato.codigo:
            print("Se encontro la lista con el codigo buscado\n")
            return ListaIndividual
        ListaIndividual = ListaIndividual.siguiente
    print("No se encontro la lista con el codigo buscado\n")
    return None

def retornarNodo(ListaIndividual,fila,columna):
    tmp = ListaIndividual.dato.inicio
    while tmp != None:
        if tmp.fila == fila and tmp.columna == columna:
            return tmp
        tmp = tmp.siguiente
    return None

def crearPisos():
    longitud = len(root)
    for i in range(longitud):
        leerPiso(i)

def leerPiso(posicion):

    nombre = root[posicion].attrib.get('nombre')
    r = root[posicion][0].text.strip()
    c = root[posicion][1].text.strip()
    f = root[posicion][2].text.strip()
    s = root[posicion][3].text.strip()
    lista_listaPatrones = lista() # lista donde se almacenan listas individuales.
    longitud = len(root[posicion][4])
    piv = 0
    for i in range(longitud):
        contador = 1
        patron = root[posicion][4][i].text.strip() 
        listTmp = lista() # LISTA DE NODOS DONDE TIENE COMO DATO CADA CARACTER B/W
        nombrePatron =  root[posicion][4][i].attrib.get('codigo')
        listTmp.codigo = nombrePatron
        fila = 0
        columna = 0
        for i in patron:# recorremos cada uno de los caracteres.
            nodotmp = nodo(i) 
            nodotmp.id = contador
            nodotmp.fila = fila
            nodotmp.columna = columna
            columna += 1
            if columna == int(c):
                columna = 0
                fila += 1
            contador += 1
            nodotmp.nombre = nombrePatron
            listTmp.agregar(nodotmp)
        nodoLista = nodo(listTmp)
        nodoLista.id = piv
        piv += 1
        lista_listaPatrones.agregar(nodoLista)
    nodoActual = nodo(piso(nombre,r,c,f,s,lista_listaPatrones))
    nodoActual.id = posicion
    listaPisos.agregar(nodoActual)


def crearGrafo(ListaIndividual,filas,columnas):
    tmp = ListaIndividual.dato.inicio
    base = '''digraph G {
    rankdir=LR
    node [shape=rectangle, color=blue]'''

    cadena = ""
    nodoPiv = tmp
    nodoInicio = None
    for i in range(filas):
        contenido = ""
        tmp = nodoPiv
        nodoInicio = tmp
        contador = 0
        for i in range(columnas):
            contador += 1
            if tmp.dato == 'W':
                contenido += f"\n{(tmp.id)} [label = \"{tmp.id} [{tmp.fila},{tmp.columna}]\",style=filled, fillcolor=white];"
            else:
                contenido += f"\n{(tmp.id)} [label = \"{tmp.id} [{tmp.fila},{tmp.columna}] \",style=filled, fillcolor=red];"
            nodoPiv = tmp
            tmp = tmp.siguiente
            if tmp != None:
                nodoPiv = tmp
        tmp = nodoInicio
        if tmp.siguiente != None:
            contenido += f"\n\"{(tmp.id)}\"" 
            tmp = tmp.siguiente
            tmpAux = tmp
            contador = 0
            for i in range(columnas-1):
                contador += 1
                contenido += f"->\"{(tmp.id)}\""
                tmpAux = tmp
                tmp = tmp.siguiente
            tmp = tmpAux
            # sale y tmp es el nodo final
            contenido += f"\n\"{(tmp.id)}\""
            tmp = tmp.anterior
            contador = 0
            for i in range(columnas-1):
                contador += 1
                contenido += f"->\"{(tmp.id)}\""
                tmp = tmp.anterior
        cadena = contenido + cadena
    cadena = base + cadena+ "\n}"
    tmp = ListaIndividual.dato.inicio
    ruta = "dot//"+str(tmp.nombre)+(".dot")
    ruta2 = "Graficas//"+str(tmp.nombre)+".png"
    generarGrafica(cadena,ruta,ruta2)

def obtenerTexto(tmp,ListaIndividual,columnas):
    contador = 0
    contenido = ""
    while tmp != None and contador < columnas:
        contador += 1
        if tmp.dato == 'W':
            contenido += f"\n{id(tmp)} [label = \"\",style=filled, fillcolor=white];"
        else:
            contenido += f"\n{id(tmp)} [label = \"\",style=filled, fillcolor=black];"
        tmp = tmp.siguiente
    tmp = ListaIndividual.dato.inicio
    if tmp.siguiente != None:
        contenido += f"\n\"{id(tmp)}\"" 
        tmp = tmp.siguiente
        tmpAux = tmp
        contador = 0
        while tmp != None and contador <columnas:
            contador += 1
            contenido += f"->\"{id(tmp)}\""
            tmpAux = tmp
            tmp = tmp.siguiente
        tmp = tmpAux
        contenido += f"\n\"{id(tmp)}\""
        tmp = tmp.anterior
        contador = 0
        while tmp != None and contador < columnas:
            contador += 1
            contenido += f"->\"{id(tmp)}\""
            tmp = tmp.anterior
        return contenido
    return ""
        
def generarGrafica(contenido,ruta,ruta2):
    try:
        miArchivo = open(ruta, 'w')
        miArchivo.write(contenido)
        miArchivo.close()

        rutaAbs = "\"" + os.path.abspath(ruta) + "\""
        rutaAbs2 = "\"" + os.path.abspath(ruta2) + "\""

        try:
            system('dot -Tpng ' + ruta + ' -o ' + ruta2)

        except:
            pass

    except:

        pass


def Menu():
    print("\n")
    print("1.Cargar archivo entrada")
    print("2.Ver pisos disponibles en el sistema")
    print("3.Eligir un piso.")
    print("4.Ordenar y mostrar Alfabeticamente.")
    print("Digite la opcion que desee")
    opcion = input(">")
    subMenu(opcion)

def subMenu(opcion):
    global listaPisos
    if opcion == "1":
        print("Ingrese la ruta del archivo:")
        entrada = input(">")
        op1(entrada)
    elif opcion == '2':
        try:
            listaPisos.imprimirNombresPisos()
        except:
            print("Algo salio mal, revisa que tengas datos cargados")
    elif opcion == "3":
  
            print("=================================PISOS DISPONIBLES=================================")
            listaPisos.imprimirNombresPisos()
            print("digite el nombre del piso")
            sel = input(">")
            op3(sel)
    elif opcion == "4":
        listaPisos.bubbleSortPiso()
        listaPisos.ordenarPatrones()
        listaPisos.imprimirPisos()


    Menu()


def op1(ruta2):
    global tree,root,ruta,listaPisos
    try:
        ruta = ruta2
        tree = ET.parse(ruta)
        root = tree.getroot()
        crearPisos()
        listaPisos.crearGrafos()
        print("\nExito!\n")
    except:
        print("Algo salio mal, intenta nuevamente.")

def op3(sel):
    pisoA = retornarPiso(sel).dato
    bandera = True
    if pisoA is not None:
        print(f"--------------------------Piso : {sel}--------------------------")
        print("Mostrando patrones...")
        pisoA.mostrarPatrones()
        print("\nOpciones:")
        print("1.Mostrar un patron")
        print("2.Pasar de un patron a otro")
        print("3.Regresar al menu principal.")
        print("Digite su opcion:")
        op = input(">")
        if op == "1":
            op3_1(sel)
        elif op == "2":
            op3_2(sel,pisoA)
        elif op == "3":
            bandera = False
        if bandera:
            print("Opcion incorrecta intenta nuevamente")
            op3(sel)

def op3_1(sel):
    print("Digite el codigo del patron que desee visualizar:")
    nombre = input(">")
    try:
        im = Image.open(f'Graficas//{nombre}.png')
        im.show()
    except:
        print("No se pudo abrir/encontrar el grafo solicitado.")

def op3_2(sel,pisoA):
    print("Digite el codigo del patron actual:")
    p1 = input(">")
    print("Digite el codigo del patron al que desea llegar:")
    p2 = input(">")
    try:
        simulacion(pisoA,p1,p2)
    except:
        print("Algo salio mal intenta nuevamente, revisa que tengas datos cargados.")


Menu()
