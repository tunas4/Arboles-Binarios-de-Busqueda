class Nodo:
    def __init__(self, dato=None, padre=None):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.padre = padre
