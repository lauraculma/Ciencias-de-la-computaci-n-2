class Grafo:
    """
    Clase para representar un grafo y generar sus diferentes formas computacionales.
    No requiere ninguna librería externa.
    """
    def __init__(self, vertices, aristas):
        """
        Inicializa el grafo.
        
        Args:
            vertices (int): El número de vértices en el grafo (nombrados de 0 a V-1).
            aristas (list): Una lista de tuplas, donde cada tupla representa una arista (u, v).
        """
        self.V = vertices
        self.aristas = aristas
        self.E = len(aristas)
        self.mapa_vertices = list(range(vertices))

    def generar_matriz_adyacencia(self):
        """
        Genera la matriz de adyacencia usando listas de listas.
        """
        # Crea una matriz de V x V llena de ceros
        matriz = [[0 for _ in range(self.V)] for _ in range(self.V)]
        
        for u, v in self.aristas:
            matriz[u][v] = 1
            matriz[v][u] = 1
            
        return matriz

    def generar_matriz_incidencia(self):
        """
        Genera la matriz de incidencia usando listas de listas.
        """
        # Crea una matriz de V x E llena de ceros
        matriz = [[0 for _ in range(self.E)] for _ in range(self.V)]
        
        for idx_arista, (u, v) in enumerate(self.aristas):
            matriz[u][idx_arista] = 1
            matriz[v][idx_arista] = 1
            
        return matriz

    def generar_lista_adyacencia(self):
        """
        Genera la lista de adyacencia del grafo.
        """
        lista = {v: [] for v in self.mapa_vertices}
        
        for u, v in self.aristas:
            lista[u].append(v)
            lista[v].append(u)
            
        return lista

    def generar_lista_incidencia(self):
        """
        Genera la lista de incidencia del grafo.
        """
        lista = {v: [] for v in self.mapa_vertices}
        
        for idx_arista, (u, v) in enumerate(self.aristas):
            lista[u].append(idx_arista)
            lista[v].append(idx_arista)
            
        return lista

    def mostrar_representaciones(self):
        """
        Imprime todas las representaciones del grafo de forma clara.
        """
        print("\n" + "="*40)
        print("    REPRESENTACIONES COMPUTACIONALES DEL GRAFO")
        print("="*40)
        print(f"Grafo con {self.V} vértices y {self.E} aristas.")
        print("Aristas:", self.aristas)
        
        # --- Matriz de Adyacencia ---
        print("\n" + "-"*40)
        print("1. Matriz de Adyacencia")
        print("-" * 40)
        matriz_ady = self.generar_matriz_adyacencia()
        for fila in matriz_ady:
            print(f"  {fila}")
        
        # --- Matriz de Incidencia ---
        print("\n" + "-"*40)
        print("2. Matriz de Incidencia")
        print("-" * 40)
        matriz_inc = self.generar_matriz_incidencia()
        for fila in matriz_inc:
            print(f"  {fila}")
            
        # --- Lista de Adyacencia ---
        print("\n" + "-"*40)
        print("3. Lista de Adyacencia")
        print("-" * 40)
        lista_ady = self.generar_lista_adyacencia()
        for vertice, vecinos in lista_ady.items():
            print(f"  Vértice {vertice}: {vecinos}")
            
        # --- Lista de Incidencia ---
        print("\n" + "-"*40)
        print("4. Lista de Incidencia")
        print("-" * 40)
        lista_inc = self.generar_lista_incidencia()
        for vertice, aristas_incidentes in lista_inc.items():
            print(f"  Vértice {vertice}: {aristas_incidentes}")
        print("="*40)

def obtener_datos_usuario():
    """
    Función para interactuar con el usuario y obtener la estructura del grafo.
    """
    print(" Creador de Representaciones de Grafos ".center(50, "="))
    
    while True:
        try:
            num_vertices = int(input("Ingrese el número total de vértices: "))
            if num_vertices > 0:
                break
            print("Error: El número de vértices debe ser mayor que 0.")
        except ValueError:
            print("Error: Ingrese un número entero válido.")
            
    print(f"Perfecto. Los vértices se nombrarán de 0 a {num_vertices - 1}.")
    
    aristas = []
    print("\nAhora ingrese las aristas una por una (ej: '0 1').")
    print("Escriba 'fin' cuando haya terminado.")

    idx = 0
    while True:
        arista_str = input(f"  Arista {idx}: ")
        if arista_str.lower() == 'fin':
            break
        
        try:
            partes = arista_str.split()
            if len(partes) != 2:
                raise ValueError("Debe ingresar exactamente dos vértices.")
                
            u, v = int(partes[0]), int(partes[1])
            
            if not (0 <= u < num_vertices and 0 <= v < num_vertices):
                print(f"Error: Los vértices deben estar en el rango [0, {num_vertices - 1}]")
                continue
            
            if u == v:
                print("Error: No se permiten bucles.")
                continue

            arista_ordenada = tuple(sorted((u, v)))
            if arista_ordenada in aristas:
                print("Error: Esa arista ya fue ingresada.")
                continue
            
            aristas.append(arista_ordenada)
            idx += 1

        except ValueError as e:
            print(f"Error de formato: '{e}'. Intente de nuevo (ej: '0 1').")

    return num_vertices, aristas

# --- Ejecución Principal ---
if __name__ == "__main__":
    V, E_list = obtener_datos_usuario()
    mi_grafo = Grafo(V, E_list)
    mi_grafo.mostrar_representaciones()