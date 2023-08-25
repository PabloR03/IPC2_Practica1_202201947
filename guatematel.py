from graphviz import Digraph
#clases
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def obtener_valor(self, fila, columna):
        actual = self.cabeza
        fila_actual = 0
        while actual is not None and fila_actual < fila:
            actual = actual.siguiente
            fila_actual += 1

        if actual is None:
            return None

        nodo_fila = actual.valor
        columna_actual = 0
        nodo_actual = nodo_fila
        while nodo_actual is not None and columna_actual < columna:
            nodo_actual = nodo_actual.siguiente
            columna_actual += 1

        if nodo_actual is None:
            return None

        return nodo_actual.valor


    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual is not None:
            print(actual.valor, end="\t")
            actual = actual.siguiente
            #valor = actual.valor
            #if valor == 1:
            #    print("A", end="\t")
            #elif valor == 2:
            #    print("R", end="\t")
            #elif valor == 3:
            #    print("V", end="\t")
            #elif valor == 4:
            #    print("P", end="\t")
            #elif valor == 5:
            #    print("N", end="\t")
            #elif valor == 6:
            #    print(" ", end="\t")
            #else:
            #    print(valor, end="\t")
            #actual = actual.siguiente
        print()

#APP
print("BIENVENIDO AL JUEGO GUATEMATEL - COLOREALO - ")
while True:
    print("Menu de opciones: ")
    print("1. Crear tablero")
    print("2. Datos del estudiante")
    print("3. Salir")
    opcion = int(input("Ingrese una opcion: "))
    if opcion < 1 or opcion > 3:
        print("Opcion invalida, ingrese una opcion valida")

    if opcion == 1:
        print("Creando tablero...")
        print("...")
        print("...")
        print("Ingrese el numero de filas: ")
        filas = int(input())
        print("Ingrese el numero de columnas: ")
        columnas = int(input())
        while filas < 1 or columnas < 1:
            print("Ingrese un numero valido")
            print("Ingrese el numero de filas: ")
            filas = int(input())
            print("Ingrese el numero de columnas: ")
            columnas = int(input())
        print("Creando tablero de " + str(filas) + "x" + str(columnas) + "...")
        matriz = ListaEnlazada()
        print("A CONTINUACION SE SOLICITARA QUE INGRESE LOS NUMEROS CORRESPONDIENTES AL COLOR QUE ELIJA:")
        print("1. Azul")
        print("2. Rojo")
        print("3. Verde")
        print("4. Purpura")
        print("5. Naranja")
        print("6. Vacio")
        for i in range(filas):
            fila = ListaEnlazada()
            for j in range(columnas):
                valor = int(input(f"Ingrese el valor para la posición ({i}, {j}): "))
                fila.agregar(valor)
            matriz.agregar(fila)
        print("La matriz ingresada es:")
        actual = matriz.cabeza
        while actual is not None:
            actual.valor.mostrar()
            actual = actual.siguiente

        print("Creando Diagrama ...")
        grafo = Digraph(format='png')  # Puedes cambiar 'png' por otros formatos como 'pdf', 'svg', etc.
        # Agregar nodos al grafo
        for i in range(filas):
            for j in range(columnas):
                valor = matriz.obtener_valor(i, j)  # Asumiendo que tienes un método obtener_valor en la clase ListaEnlazada
                grafo.node(f'({i},{j})', label=str(valor))  # Agrega un nodo con las coordenadas y el valor

        # Agregar arcos al grafo
        for i in range(filas):
            for j in range(columnas):
                if i + 1 < filas:
                    grafo.edge(f'({i},{j})', f'({i+1},{j})')  # Agrega un arco hacia abajo
                if j + 1 < columnas:
                    grafo.edge(f'({i},{j})', f'({i},{j+1})')  # Agrega un arco hacia la derecha

        # Guardar el grafo en un archivo y generar la imagen
        grafo.render('matriz_grafo', view=True)  # Esto generará 'matriz_grafo.png'



    elif opcion == 2:
        print("")
        print("")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("\t \t Datos del estudiante: ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Nombre: PABLO ANDRES RODRIGUEZ LIMA")
        print("Carnet: 202201947")
        print("Curso: Introduccion a la Programacion y Computacion 2 - 2do Semestre")
        print("Seccion: D")
        print("")
        print("")
    elif opcion == 3:
        print("Saliendo del juego...")
        break





