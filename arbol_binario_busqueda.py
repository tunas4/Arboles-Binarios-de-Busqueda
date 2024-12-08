from nodo import Nodo

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, nodo, dato):
        if nodo is None:
            nuevo_nodo = Nodo(dato)
            if self.raiz is None:
                self.raiz = nuevo_nodo
            return nuevo_nodo
        else:
            if dato <= nodo.dato:
                if nodo.izquierda is None:
                    nodo.izquierda = Nodo(dato, nodo)
                else:
                    self.insertar(nodo.izquierda, dato)
            else:
                if nodo.derecha is None:
                    nodo.derecha = Nodo(dato, nodo)
                else:
                    self.insertar(nodo.derecha, dato)
        return self.raiz

    def buscar(self, nodo, dato, nivel=0):
        if nodo is None:
            return None, -1
        if nodo.dato == dato:
            return nodo, nivel
        elif dato < nodo.dato:
            return self.buscar(nodo.izquierda, dato, nivel + 1)
        else:
            return self.buscar(nodo.derecha, dato, nivel + 1)

    def eliminar(self, dato):
        nodo, _ = self.buscar(self.raiz, dato)
        if nodo is None:
            print("El dato no se encuentra en el árbol.")
            return None

        hijos = 0
        hijo = None

        if nodo.derecha is not None:
            hijos += 1
            hijo = nodo.derecha
        if nodo.izquierda is not None:
            hijos += 1
            hijo = nodo.izquierda

        # hoja
        if hijos == 0:
            if nodo == self.raiz:
                self.raiz = None
            else:
                padre = nodo.padre
                if padre.izquierda == nodo:
                    padre.izquierda = None
                else:
                    padre.derecha = None
            return nodo

        # un hijo
        elif hijos == 1:
            if nodo == self.raiz:
                self.raiz = hijo
                hijo.padre = None
            else:
                padre = nodo.padre
                if padre.izquierda == nodo:
                    padre.izquierda = hijo
                else:
                    padre.derecha = hijo
                hijo.padre = padre
            return nodo

        # dos hijos
        else:
            sucesor = nodo.derecha
            while sucesor.izquierda is not None:
                sucesor = sucesor.izquierda

            nodo.dato = sucesor.dato

            if sucesor.padre.izquierda == sucesor:
                sucesor.padre.izquierda = sucesor.derecha
            else:
                sucesor.padre.derecha = sucesor.derecha

            if sucesor.derecha is not None:
                sucesor.derecha.padre = sucesor.padre

            return nodo

    def PreOrder(self, nodo):
        resultado = []
        if nodo:
            resultado.append(nodo.dato)
            resultado.extend(self.PreOrder(nodo.izquierda))
            resultado.extend(self.PreOrder(nodo.derecha))
        return resultado

    def InOrder(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self.InOrder(nodo.izquierda))
            resultado.append(nodo.dato)
            resultado.extend(self.InOrder(nodo.derecha))
        return resultado

    def PostOrder(self, nodo):
        resultado = []
        if nodo:
            resultado.extend(self.PostOrder(nodo.izquierda))
            resultado.extend(self.PostOrder(nodo.derecha))
            resultado.append(nodo.dato)
        return resultado

    def liberar(self, nodo):
        if nodo is not None:
            self.liberar(nodo.izquierda)
            self.liberar(nodo.derecha)
            nodo.izquierda = nodo.derecha = nodo.padre = None
