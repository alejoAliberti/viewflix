# **Documentación de la Clase `GeneralTree` y la Clase `Node`**

## **Clase `Node`**

La clase `Node` representa un nodo en un árbol general. Cada nodo contiene un valor y una lista de referencias a sus nodos hijos.

### **Propiedades**
- **`data`**:
  - **Tipo**: `Any`
  - **Descripción**: El valor almacenado en el nodo.
  
- **`children`**:
  - **Tipo**: `List[Node]`
  - **Descripción**: Lista de nodos hijos de este nodo. Vacía si no tiene hijos.

### **Método `__init__(self, data: Any)`**
- **Descripción**: Constructor que inicializa un nodo con un valor y una lista vacía de hijos.
- **Parámetros**:
  1. `data`: Valor que se almacenará en el nodo.

---

## **Clase `GeneralTree`**

La clase `GeneralTree` representa un árbol general, donde cada nodo puede tener un número arbitrario de hijos.

### **Propiedades**
1. **`root`**:
   - **Tipo**: `Node` o `None`
   - **Descripción**: Nodo raíz del árbol. Es `None` si el árbol está vacío.

---

### **Métodos**

#### **`__init__(self)`**
- **Descripción**: Constructor que inicializa un árbol general vacío.
- **Resultado**: Crea un árbol sin nodos.

---

#### **`is_empty(self)`**
- **Descripción**: Verifica si el árbol está vacío.
- **Resultado**: Retorna `True` si el árbol no tiene nodos, de lo contrario `False`.

---

#### **`add_root(self, data: Any)`**
- **Descripción**: Añade la raíz al árbol si está vacío.
- **Parámetros**:
  - `data`: Valor que se asignará a la raíz.
- **Excepciones**: Lanza un `ValueError` si el árbol ya tiene una raíz.

---

#### **`add_child(self, parent: Node, data)`**
- **Descripción**: Añade un hijo al nodo padre especificado.
- **Parámetros**:
  - `parent`: Nodo al que se añadirá el hijo.
  - `data`: Valor del nuevo nodo hijo.
- **Excepciones**: Lanza un `ValueError` si el nodo padre es `None`.

---

#### **`find_node(self, data = None, node: Node = None) -> Node`**
- **Descripción**: Busca un nodo en el árbol basado en el valor proporcionado.
- **Parámetros**:
  - `data`: Valor del nodo a buscar.
  - `node`: Nodo desde donde iniciar la búsqueda (opcional, por defecto la raíz).
- **Resultado**: Retorna el nodo encontrado o `None` si no existe.

---

#### **`find_nodes_by_name(self, name: str, node: Node = None, results: list = None) -> list`**
- **Descripción**: Busca nodos cuyo atributo `name` coincida parcialmente con la subcadena proporcionada.
- **Parámetros**:
  - `name`: Subcadena para buscar dentro del atributo `name` de los nodos.
  - `node`: Nodo desde donde comenzar la búsqueda (opcional, por defecto la raíz).
  - `results`: Lista acumulativa de nodos coincidentes (opcional).
- **Resultado**: Retorna una lista de nodos cuyos nombres coinciden parcialmente con la subcadena.

---

#### **`clear(self)`**
- **Descripción**: Elimina todos los nodos del árbol, dejándolo vacío.
- **Resultado**: Establece la raíz como `None`.

---

#### **`dfs_traverse(self, node: Node = None)`**
- **Descripción**: Recorre el árbol en profundidad (DFS).
- **Parámetros**:
  - `node`: Nodo desde donde iniciar el recorrido (opcional, por defecto la raíz).
- **Resultado**: Generador que produce nodos en orden DFS.

---

#### **`bfs_traverse(self)`**
- **Descripción**: Recorre el árbol en anchura (BFS).
- **Resultado**: Generador que produce nodos en orden BFS.

---

#### **`bfs_traverse_with_depth(self, max_depth: int = 1)`**
- **Descripción**: Recorre el árbol en anchura, pero limitado a una profundidad máxima.
- **Parámetros**:
  - `max_depth`: Profundidad máxima a recorrer (0 incluye solo la raíz, 1 incluye los hijos directos, etc.).
- **Resultado**: Generador que produce nodos en orden BFS hasta la profundidad máxima.


