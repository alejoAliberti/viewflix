# **Documentación de la Clase `LinkedList` y la Clase `Node`**

## **Clase `Node`**

La clase `Node` representa un nodo en una lista enlazada. Contiene un valor y una referencia al siguiente nodo en la lista.

### **Propiedades**
- **`data`**:
  - **Tipo**: `Any`
  - **Descripción**: El valor almacenado en el nodo.
  
- **`next`**:
  - **Tipo**: `Node` o `None`
  - **Descripción**: Referencia al siguiente nodo en la lista. Es `None` si es el último nodo.

### **Método `__init__(self, data)`**
- **Descripción**: Constructor que inicializa un nodo con un valor y establece la referencia `next` como `None`.
- **Parámetros**:
  1. `data`: Valor que se almacenará en el nodo.

---

## **Clase `LinkedList`**

La clase `LinkedList` representa una lista enlazada simple. Es una estructura lineal en la que cada nodo apunta al siguiente.

### **Propiedades**
1. **`head`**:
   - **Tipo**: `Node` o `None`
   - **Descripción**: Nodo inicial de la lista. Es `None` si la lista está vacía.

2. **`size`**:
   - **Tipo**: `int`
   - **Descripción**: Número de nodos en la lista.

---

### **Métodos**

#### **`__init__(self)`**
- **Descripción**: Constructor que inicializa una lista enlazada vacía.
- **Resultado**: Establece `head` como `None` y `size` como 0.

---

#### **`is_empty(self)`**
- **Descripción**: Verifica si la lista está vacía.
- **Resultado**: Retorna `True` si la lista no contiene elementos, de lo contrario `False`.

---

#### **`append(self, data)`**
- **Descripción**: Añade un nodo al final de la lista.
- **Parámetros**:
  - `data`: Valor del nuevo nodo.
- **Resultado**: Incrementa el tamaño de la lista.

---

#### **`prepend(self, data)`**
- **Descripción**: Añade un nodo al inicio de la lista.
- **Parámetros**:
  - `data`: Valor del nuevo nodo.
- **Resultado**: Incrementa el tamaño de la lista.

---

#### **`delete(self, data)`**
- **Descripción**: Elimina la primera ocurrencia del nodo con el valor especificado.
- **Parámetros**:
  - `data`: Valor del nodo a eliminar.
- **Resultado**: Retorna `True` si se eliminó un nodo, de lo contrario `False`.

---

#### **`get_size(self)`**
- **Descripción**: Retorna el tamaño de la lista.
- **Resultado**: Devuelve el número total de nodos.

---

#### **`search(self, data=None, name=None, node=None)`**
- **Descripción**: Busca un elemento en la lista de forma recursiva.
- **Parámetros**:
  - `data`: Valor del nodo a buscar (opcional).
  - `name`: Criterio alternativo de búsqueda basado en un atributo `name` (opcional).
  - `node`: Nodo desde donde iniciar la búsqueda (opcional).
- **Resultado**: Retorna `True` si encuentra el nodo, de lo contrario `False`.

---

#### **`search_by_name(self, name: str, node=None, results=None)`**
- **Descripción**: Busca nodos cuyo atributo `name` coincida parcialmente con el valor proporcionado.
- **Parámetros**:
  - `name`: Subcadena para buscar en el atributo `name` de los nodos.
  - `node`: Nodo desde donde comenzar la búsqueda (opcional).
  - `results`: Lista acumulativa de nodos coincidentes (opcional).
- **Resultado**: Retorna una lista de nodos que cumplen con el criterio.

---

#### **`clear(self)`**
- **Descripción**: Elimina todos los elementos de la lista, dejándola vacía.
- **Resultado**: Establece `head` como `None` y `size` como 0.

---

#### **`get_all(self)`**
- **Descripción**: Retorna todos los valores almacenados en la lista como una lista de Python.
- **Resultado**: Lista de valores.

---