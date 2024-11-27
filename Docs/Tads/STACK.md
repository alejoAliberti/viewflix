# **Documentación de la Clase `Stack`**

La clase `Stack` implementa una estructura de datos de pila (LIFO - Last In, First Out), donde el último elemento insertado es el primero en ser removido.

---

## **Métodos**

### **`__init__(self)`**
- **Descripción**: Constructor que inicializa una pila vacía.
- **Resultado**: Crea una instancia de `Stack` con una lista vacía para almacenar elementos.

---

### **`push(self, item)`**
- **Descripción**: Añade un elemento al tope de la pila.
- **Parámetros**:
  - `item`: Elemento a agregar.
- **Resultado**: El elemento se coloca en la parte superior de la pila.

---

### **`pop(self)`**
- **Descripción**: Remueve y retorna el elemento del tope de la pila.
- **Resultado**: Retorna el último elemento agregado a la pila.
- **Errores**: Lanza `IndexError` si la pila está vacía.

---

### **`peek(self)`**
- **Descripción**: Retorna el elemento del tope sin removerlo.
- **Resultado**: Retorna el último elemento agregado a la pila.
- **Errores**: Lanza `IndexError` si la pila está vacía.

---

### **`is_empty(self)`**
- **Descripción**: Verifica si la pila está vacía.
- **Resultado**: Retorna `True` si la pila no contiene elementos, de lo contrario `False`.

---

### **`size(self)`**
- **Descripción**: Retorna el número de elementos en la pila.
- **Resultado**: Un entero representando la cantidad de elementos en la pila.

---

### **`clear(self)`**
- **Descripción**: Elimina todos los elementos de la pila.
- **Resultado**: La pila queda vacía.

