from arbol_binario_busqueda import ArbolBinarioBusqueda
from nodo import Nodo

def menu():
    arbol = ArbolBinarioBusqueda()

    while True:
        print("\nMenú:")
        print("1. Inicializar / Borrar Árbol")
        print("2. Mostrar Árbol")
        print("3. Buscar")
        print("4. Insertar")
        print("5. Eliminar")
        print("6. Modificar")
        print("7. Créditos")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        # Inicializar / Borrar
        if opcion == "1":
            arbol.liberar(arbol.raiz)
            arbol.raiz = None
            print("Árbol inicializado/borrado.")

        # Mostrar
        elif opcion == "2":
            if arbol.raiz is None:
                print("El árbol está vacío.")
            else:
                print("1. PreOrder")
                print("2. InOrder")
                print("3. PostOrder")
                recorrido = input("Seleccione el tipo de recorrido: ")
                if recorrido == "1":
                    print("Recorrido PreOrder:")
                    arbol.PreOrder(arbol.raiz)
                elif recorrido == "2":
                    print("Recorrido InOrder:")
                    arbol.InOrder(arbol.raiz)
                elif recorrido == "3":
                    print("Recorrido PostOrder:")
                    arbol.PostOrder(arbol.raiz)
                else:
                    print("Opción no válida.")
                print()

        # Buscar
        elif opcion == "3":
            dato = input("Ingrese el dato a buscar: ")
            try:
                dato = int(dato)
                nodo, nivel = arbol.buscar(arbol.raiz, dato)
                if nodo:
                    print(f"Dato encontrado en el nivel {nivel}.")
                else:
                    print("El dato no está en el árbol.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        # Insertar
        elif opcion == "4":
            dato = input("Ingrese el dato a insertar (números positivos o negativos): ")
            try:
                dato = int(dato)
                arbol.insertar(arbol.raiz, dato)
                print("Dato insertado.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese solo números enteros.")

        # Eliminar
        elif opcion == "5":
            dato = input("Ingrese el dato a eliminar: ")
            try:
                dato = int(dato)
                nodo_eliminado = arbol.eliminar(dato)
                if nodo_eliminado:
                    print(f"Dato {dato} eliminado.")
                else:
                    print("El dato no se encontró en el árbol.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        # Modificar
        elif opcion == "6":
            dato = input("Ingrese el dato a modificar: ")
            try:
                dato = int(dato)
                nuevo_dato = input("Ingrese el nuevo dato: ")
                try:
                    nuevo_dato = int(nuevo_dato)
                    nodo, _ = arbol.buscar(arbol.raiz, dato)
                    if nodo:
                        arbol.eliminar(dato)
                        arbol.insertar(arbol.raiz, nuevo_dato)
                        print(f"Dato {dato} modificado a {nuevo_dato}.")
                    else:
                        print("El dato no está en el árbol.")
                except ValueError:
                    print("Entrada no válida. El nuevo dato debe ser un número.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        # Créditos
        elif opcion == "7":
            print("Créditos:")
            print("Programa realizado por:")
            print("Noé Abel Vergas López - 23170106")
            print("Jonathan Iván Castro Saenz - 23170132")
            print("Juan Alfredo Gómez González - 23170006")

        # Salir
        elif opcion == "8":
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
