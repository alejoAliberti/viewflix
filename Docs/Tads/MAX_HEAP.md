# **Documentación de la Clase `MaxHeap` y la Clase `Node`**

## **Clase `Node`**

La clase `Node` representa un nodo en un montículo (heap). Contiene un valor y una prioridad que determina su posición en la estructura de datos.

### **Propiedades**
- **`content`**:
  - **Tipo**: `Any`
  - **Descripción**: El valor almacenado en el nodo.
  
- **`priority`**:
  - **Tipo**: `int`
  - **Descripción**: La prioridad del nodo. Los nodos con mayor prioridad se colocan en la parte superior del montículo.

### **Método `__init__(self, content, priority)`**
- **Descripción**: Constructor que inicializa un nodo con un contenido y una prioridad.
- **Parámetros**:
  1. `content`: Valor almacenado en el nodo.
  2. `priority`: Prioridad del nodo.

---

## **Clase `MaxHeap`**

La clase `MaxHeap` implementa un montículo máximo, donde cada nodo tiene una prioridad, y el nodo con la mayor prioridad está en la parte superior.

### **Propiedades**
1. **`heap`**:
   - **Tipo**: `list[Node]`
   - **Descripción**: Lista que almacena los nodos del montículo en un arreglo.

---

### **Métodos**

#### **`__init__(self)`**
- **Descripción**: Constructor que inicializa un montículo vacío.
- **Resultado**: Establece `heap` como una lista vacía.

---

#### **`is_empty(self) -> bool`**
- **Descripción**: Verifica si el montículo está vacío.
- **Resultado**: Retorna `True` si no contiene elementos, de lo contrario `False`.

---

#### **`insert(self, content, priority) -> None`**
- **Descripción**: Añade un nuevo nodo al montículo con un contenido y una prioridad.
- **Parámetros**:
  1. `content`: Valor del nodo a insertar.
  2. `priority`: Prioridad del nodo.
- **Resultado**: El montículo se reorganiza para mantener las propiedades del heap máximo.

---

#### **`extract_max(self)`**
- **Descripción**: Retorna y elimina el nodo con la mayor prioridad.
- **Resultado**: Retorna el contenido del nodo extraído.
- **Errores**: 
  - Lanza `IndexError` si el montículo está vacío.

---

#### **`get_max(self)`**
- **Descripción**: Retorna el nodo con la mayor prioridad sin eliminarlo.
- **Resultado**: Retorna el contenido del nodo con mayor prioridad.
- **Errores**: 
  - Lanza `IndexError` si el montículo está vacío.

---

### **Métodos Auxiliares**

#### **`_sift_up(self, index)`**
- **Descripción**: Reorganiza el montículo hacia arriba desde el índice dado para mantener las propiedades del heap máximo.
- **Parámetros**:
  - `index`: Índice del nodo que se verificará.
- **Resultado**: Actualiza el montículo.

---

#### **`_sift_down(self, index)`**
- **Descripción**: Reorganiza el montículo hacia abajo desde el índice dado para mantener las propiedades del heap máximo.
- **Parámetros**:
  - `index`: Índice del nodo que se verificará.
- **Resultado**: Actualiza el montículo.

