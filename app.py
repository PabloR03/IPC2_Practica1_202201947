from lista_colores import lista_colores
mi_tablero=lista_colores()



def configuracion_tablero():
  print("")
  print("")
  print("---------------------------TABLERO---------------------------")
  filas=input("Ingrese el número de filas: ")
  columnas=input("Ingrese el número de columnas: ")
  # Creo todas las piezas de mi tablero
  mi_tablero.inicializar_tablero(int(filas),int(columnas))
  mi_tablero.filas=int(filas)
  mi_tablero.columnas=int(columnas)
  # Verificamos que mi tablero se haya creado correctamente
  mi_tablero.recorrer_e_imprimir_lista()

  # Sentinela de agregar nueva pieza
  print("---------------------------PIEZAS---------------------------")
  nueva_pieza=True
  while nueva_pieza:
    fila=input("Ingrese la fila de la pieza: ")
    columna=input("Ingrese la columna de la pieza: ")
    color=input("Ingrese el color de la pieza: ")
    if (color=="Red" or color=="Blue" or color=="Green" or color=="Orange" or color=="Purple"):
      print("El color es correcto")
      print("recuerde el color debe ser Rojo, Azul, Verde, Naranja o Morado")
    else:
      print("El color es incorrecto")
      color=input("Ingrese el color de la pieza: ")
    mi_tablero.actualizar_pieza(int(fila),int(columna),color)
    print("")
    print("")
    mi_tablero.imprimir_tablero_en_consola()
    # Preguntamos si desea agregar otra pieza
    respuesta=input("Desea agregar otra pieza (si o no) S/N: ")
    print("")
    print("")
    if respuesta=="N" or respuesta=="n":
      nueva_pieza=False
  print("-----------------------------finalizo de colocar sus piezas-----------------------------")
  mi_tablero.imprimir_tablero_en_consola()
  print("-----------------------------finalizo de colocar su tablero-----------------------------")
  print("")
  print("")
  # Deberiamos graficar
  mi_tablero.graficar()
      



def mostrar_menu():
  print("")
  print("")
  print("*******************-Menú-*******************")
  print("1. Configurar tablero")
  print("2. Salir")
  opcion =input("Ingrese una opción válida del menú: ")
  while True:
    if opcion=="1":
      print("")
      configuracion_tablero()
      break
    elif opcion=="2":
      print("Gracias por jugar")
      break
    else:
      print("su opcion es incorrecta, intente de nuevo")


mostrar_menu()
