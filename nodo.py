class Nodo:
    def __init__(self, dato, padre=None):
        self.dato = dato
        self.padre = padre
        self.izquierda = None
        self.derecha = None
