import nodo

class arbol_binario_busqueda:
    def __init__(self):
        self.raiz = None

    def PreOrder (self, nodo):
        if (nodo != None):
            print (nodo.dato)
            self.PreOrder(nodo.izquierda)
            self.PreOrder(nodo.derecha)

    def InOrder (self, nodo):
        if (nodo != None):
            self.InOrder(nodo.izquierda)
            print (nodo.dato)
            self.InOrder(nodo.derecha)

    def PostOrder (self, nodo):
        if (nodo != None):
            self.PostOrder(nodo.izquierda)
            self.PostOrder(nodo.derecha)
            print (nodo.dato)

    def insertar(self, nodo, dato):
        if (nodo == None):
            q = nodo.Nodo()
            q.dato = dato
            self.raiz = q
        else:
            if (dato <= nodo.dato):
                if nodo.izquierda == None:
                    q = nodo.Nodo()
                    q.dato = dato
                    nodo.izquierda = q
                else:
                    self.insertar(nodo.izquierda, dato)
            else:
                if nodo.derecha == None:
                    q = nodo.Nodo()
                    q.dato = dato
                    nodo.derecha = q
                else:
                    self.insertar(nodo.derecha, dato)

    def buscar(self, nodo, dato):
        if (nodo == None):
            return None
        elif (nodo.dato == dato):
            return nodo
        elif (dato < nodo.dato):
            return self.buscar(nodo.izquierda, dato)
        return self.buscar(nodo.derecha, dato)

    def eliminar(self, dato):
        res = self.buscar(self.raiz, dato)
        if (res != None):
            return None
        
        hijos = 0
        a = nodo.Nodo()

        if (res.derecha != None):
            hijos += 1
            a = res.izquierda
        
        if (res.izquierda != None):
            hijos += 1
            a = res.derecha

        if (hijos == 0):
            if res.padre == None:
                r = None
            else:
                p = res.padre
                if (p.izquierda == res):
                    p.izquierda = None
                else:
                    p.derecha = None
                res.padre = None
            return res
        
        elif (hijos == 1):
            if res.padre == None:
                self.raiz = a
                a.padre = None
                if res.izquierda == a:
                    res.izquierda = None
            else:
                p = res.padre
                if (p.izquierda == res):
                    p.izquierda = a
                else:
                    p.derecha = a
                a.padre = p 
                res.padre = None
                if res.izquierda == a:
                    res.izquierda = None
                else:
                    res.derecha = None
            return res
    
        elif (hijos == 2):
            t = a
            while (t.derecha != None):
                t = t.derecha
            res.dato = t.dato
            t.dato = dato
            if a == t:
                res.izquierda = a.izquierda
                a.padre = None
                a.izquierda = None
                if res.izquierda != None:
                    res.izquierda.padre = res
            else:
                q = t.padre
                q.derecha = t.izquierda
                t.padre = None
                t.izquierda = None
                if q.derecha != None:
                    q.derecha.padre = q
            return t
        
    def liberar(self, nodo):
        if (nodo != None):
            self.liberar(nodo.izquierda)
            self.liberar(nodo.derecha)
            nodo.izquierda = nodo.derecha = nodo.padre = None

    