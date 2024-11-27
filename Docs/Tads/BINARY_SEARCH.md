# **Documentación de la Clase `BinarySearchTree` y la Clase `Node`**

## **Clase Node**

La clase `Node` representa un nodo en un árbol binario de búsqueda. Cada nodo contiene un valor y referencias a sus hijos izquierdo y derecho.

### **Propiedades**

- **`data`**: 
  - **Tipo**: `int`, `float`, `str`, etc. (dependiendo de los valores que maneje el árbol).
  - **Descripción**: El valor almacenado en el nodo.

- **`left`**:
  - **Tipo**: `Node` o `None`
  - **Descripción**: Referencia al hijo izquierdo. Es `None` si no tiene hijo izquierdo.

- **`right`**:
  - **Tipo**: `Node` o `None`
  - **Descripción**: Referencia al hijo derecho. Es `None` si no tiene hijo derecho.

### **Método `__init__(self, data)`**

- **Descripción**: Constructor que inicializa un nodo con un valor y establece ambos hijos como `None`.
- **Parámetros**:
  1. `data`: Valor que se almacenará en el nodo.

---

## **Clase BinarySearchTree**

La clase `BinarySearchTree` representa un árbol binario de búsqueda (BST), que organiza los valores de forma que los valores menores están en el subárbol izquierdo y los mayores en el derecho.

### **Propiedades**

1. **`root`**:
   - **Tipo**: `Node` o `None`
   - **Descripción**: Nodo raíz del árbol. Es `None` si el árbol está vacío.

---

### **Métodos**

#### **`__init__(self)`**
- **Descripción**: Constructor que inicializa un árbol binario de búsqueda vacío.
- **Resultado**: Crea un árbol sin nodos.

---

#### **`insert(self, data)`**
- **Descripción**: Inserta un nuevo valor en el árbol.
- **Parámetros**:
  - `data`: Valor a insertar en el árbol.
- **Detalles**: Si el árbol está vacío, el valor se convierte en la raíz. De lo contrario, utiliza el método recursivo `_insert_recursive`.

---

#### **`_insert_recursive(self, node, data)`**
- **Descripción**: Método auxiliar recursivo para insertar un valor en el lugar adecuado.
- **Parámetros**:
  - `node`: Nodo actual durante la búsqueda del lugar de inserción.
  - `data`: Valor a insertar.
- **Detalles**: Coloca el valor en el subárbol izquierdo si es menor, o en el derecho si es mayor.

---

#### **`search(self, data)`**
- **Descripción**: Busca un valor en el árbol.
- **Parámetros**:
  - `data`: Valor a buscar.
- **Resultado**: Retorna el nodo que contiene el valor, o `None` si no se encuentra.

---

#### **`_search_recursive(self, node, data)`**
- **Descripción**: Método auxiliar recursivo para buscar un valor.
- **Parámetros**:
  - `node`: Nodo actual durante la búsqueda.
  - `data`: Valor a buscar.
- **Detalles**: Retorna el nodo si lo encuentra o `None` si no está en el árbol.

---

#### **`delete(self, data)`**
- **Descripción**: Elimina un valor del árbol.
- **Parámetros**:
  - `data`: Valor a eliminar.
- **Detalles**: Usa el método recursivo `_delete_recursive`.

---

#### **`_delete_recursive(self, node, data)`**
- **Descripción**: Método auxiliar recursivo para eliminar un nodo.
- **Parámetros**:
  - `node`: Nodo actual durante la búsqueda del nodo a eliminar.
  - `data`: Valor a eliminar.
- **Detalles**:
  - Si el nodo tiene un solo hijo o ninguno, se reorganiza el árbol.
  - Si tiene dos hijos, reemplaza el valor con el menor nodo del subárbol derecho.

---

#### **`_min_value_node(self, node)`**
- **Descripción**: Encuentra el nodo con el valor mínimo en un subárbol.
- **Parámetros**:
  - `node`: Nodo raíz del subárbol.
- **Resultado**: Retorna el nodo con el menor valor.

---

#### **`clear(self)`**
- **Descripción**: Elimina todos los nodos del árbol, dejándolo vacío.
- **Resultado**: Establece la raíz en `None`.

---
