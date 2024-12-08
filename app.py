import tkinter as tk
from tkinter import messagebox
from arbol_binario_busqueda import ArbolBinarioBusqueda

# Instancia global del árbol binario
arbol = ArbolBinarioBusqueda()

def solo_numeros(entrada):
    """Valida que la entrada contenga solo números (positivos o negativos)."""
    if entrada == "" or entrada == "-" or (entrada[0] == "-" and entrada[1:].isdigit()) or entrada.isdigit():
        return True
    return False

def inicializar_arbol():
    """Inicializa o borra el árbol binario."""
    arbol.liberar(arbol.raiz)
    arbol.raiz = None
    messagebox.showinfo("Operación exitosa", "Árbol inicializado/borrado.")

def mostrar_recorrido(ventana):
    """Muestra los recorridos del árbol en una nueva ventana."""
    if arbol.raiz is None:
        messagebox.showwarning("Error", "El árbol está vacío.")
        return

    def mostrar(tipo):
        if tipo == "PreOrder":
            recorrido = arbol.PreOrder(arbol.raiz)
        elif tipo == "InOrder":
            recorrido = arbol.InOrder(arbol.raiz)
        elif tipo == "PostOrder":
            recorrido = arbol.PostOrder(arbol.raiz)
        else:
            recorrido = []
        salida = " -> ".join(map(str, recorrido)) if recorrido else "El recorrido está vacío."
        label_resultado.config(text=f"{tipo}: {salida}")

    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Recorridos del Árbol")
    tk.Label(nueva_ventana, text="Seleccione el tipo de recorrido").pack(pady=5)

    tk.Button(nueva_ventana, text="PreOrder", command=lambda: mostrar("PreOrder")).pack(pady=5)
    tk.Button(nueva_ventana, text="InOrder", command=lambda: mostrar("InOrder")).pack(pady=5)
    tk.Button(nueva_ventana, text="PostOrder", command=lambda: mostrar("PostOrder")).pack(pady=5)

    label_resultado = tk.Label(nueva_ventana, text="", wraplength=300, justify="left")
    label_resultado.pack(pady=10)

def buscar_dato():
    """Busca un dato en el árbol."""
    def buscar():
        try:
            dato = int(entry.get())
            nodo, nivel = arbol.buscar(arbol.raiz, dato)
            if nodo:
                messagebox.showinfo("Resultado", f"Dato encontrado en el nivel {nivel}.")
            else:
                messagebox.showwarning("Error", "El dato no está en el árbol.")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Ingrese un número válido.")

    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Buscar Dato")
    tk.Label(nueva_ventana, text="Ingrese el dato a buscar:").pack(pady=5)

    vcmd = nueva_ventana.register(solo_numeros)
    entry = tk.Entry(nueva_ventana, validate="key", validatecommand=(vcmd, "%P"))
    entry.pack(pady=5)

    tk.Button(nueva_ventana, text="Buscar", command=buscar).pack(pady=10)

def insertar_dato():
    """Inserta un dato en el árbol."""
    def insertar():
        try:
            dato = int(entry.get())
            arbol.insertar(arbol.raiz, dato)
            messagebox.showinfo("Operación exitosa", "Dato insertado.")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Ingrese un número válido.")

    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Insertar Dato")
    tk.Label(nueva_ventana, text="Ingrese el dato a insertar:").pack(pady=5)

    vcmd = nueva_ventana.register(solo_numeros)
    entry = tk.Entry(nueva_ventana, validate="key", validatecommand=(vcmd, "%P"))
    entry.pack(pady=5)

    tk.Button(nueva_ventana, text="Insertar", command=insertar).pack(pady=10)

def eliminar_dato():
    """Elimina un dato del árbol."""
    def eliminar():
        try:
            dato = int(entry.get())
            nodo_eliminado = arbol.eliminar(dato)
            if nodo_eliminado:
                messagebox.showinfo("Operación exitosa", f"Dato {dato} eliminado.")
            else:
                messagebox.showwarning("Error", "El dato no se encontró en el árbol.")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Ingrese un número válido.")

    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Eliminar Dato")
    tk.Label(nueva_ventana, text="Ingrese el dato a eliminar:").pack(pady=5)

    vcmd = nueva_ventana.register(solo_numeros)
    entry = tk.Entry(nueva_ventana, validate="key", validatecommand=(vcmd, "%P"))
    entry.pack(pady=5)

    tk.Button(nueva_ventana, text="Eliminar", command=eliminar).pack(pady=10)

def modificar_dato():
    """Modifica un dato del árbol."""
    def modificar():
        try:
            dato = int(entry_dato.get())
            nuevo_dato = int(entry_nuevo.get())
            nodo, _ = arbol.buscar(arbol.raiz, dato)
            if nodo:
                arbol.eliminar(dato)
                arbol.insertar(arbol.raiz, nuevo_dato)
                messagebox.showinfo("Operación exitosa", f"Dato {dato} modificado a {nuevo_dato}.")
            else:
                messagebox.showwarning("Error", "El dato no está en el árbol.")
        except ValueError:
            messagebox.showerror("Entrada inválida", "Ingrese números válidos.")

    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Modificar Dato")
    tk.Label(nueva_ventana, text="Ingrese el dato a modificar:").pack(pady=5)

    vcmd = nueva_ventana.register(solo_numeros)
    entry_dato = tk.Entry(nueva_ventana, validate="key", validatecommand=(vcmd, "%P"))
    entry_dato.pack(pady=5)

    tk.Label(nueva_ventana, text="Ingrese el nuevo dato:").pack(pady=5)
    entry_nuevo = tk.Entry(nueva_ventana, validate="key", validatecommand=(vcmd, "%P"))
    entry_nuevo.pack(pady=5)

    tk.Button(nueva_ventana, text="Modificar", command=modificar).pack(pady=10)

def mostrar_creditos():
    """Muestra los créditos del programa."""
    messagebox.showinfo("Créditos", "Programa desarrollado por:\n- Tu Nombre\nEstructura de Datos")

def main():
    ventana = tk.Tk()
    ventana.title("Gestión de Árbol Binario")
    ventana.geometry("400x500")

    tk.Button(ventana, text="Inicializar/Borrar Árbol", command=inicializar_arbol).pack(pady=10)
    tk.Button(ventana, text="Mostrar Árbol", command=lambda: mostrar_recorrido(ventana)).pack(pady=10)
    tk.Button(ventana, text="Buscar Dato", command=buscar_dato).pack(pady=10)
    tk.Button(ventana, text="Insertar Dato", command=insertar_dato).pack(pady=10)
    tk.Button(ventana, text="Eliminar Dato", command=eliminar_dato).pack(pady=10)
    tk.Button(ventana, text="Modificar Dato", command=modificar_dato).pack(pady=10)
    tk.Button(ventana, text="Créditos", command=mostrar_creditos).pack(pady=10)
    tk.Button(ventana, text="Salir", command=ventana.quit).pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
