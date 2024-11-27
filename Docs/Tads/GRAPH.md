# **Documentación de la Clase `Graph` y la Clase `Edge`**

## **Clase Edge**

La clase `Edge` representa una arista en el grafo, que conecta dos vértices (contenidos) con un peso asociado que indica la similitud.

### **Propiedades**

- **`dest`**: 
  - **Tipo**: `str` o cualquier tipo que represente un contenido.
  - **Descripción**: El destino de la arista, que corresponde al contenido conectado por esta arista.

- **`weight`**:
  - **Tipo**: `float`
  - **Descripción**: El peso o similitud de la conexión entre el vértice origen y el destino. 
  - **Valor predeterminado**: `1.0`

### **Método `__init__(self, dest, weight=1.0)`**

- **Descripción**: Constructor que inicializa una arista con su destino y peso.
- **Parámetros**:
  1. `dest` (requerido): El contenido destino de la arista.
  2. `weight` (opcional): El peso de la arista.

---

## **Clase Graph**

La clase `Graph` modela un sistema de contenidos (como películas o series) y sus relaciones mediante un grafo.

### **Propiedades**

1. **`vertices`**:
   - **Tipo**: `dict`
   - **Estructura**: `{contenido: [lista de Edge]}`
   - **Descripción**: Diccionario que almacena los vértices (contenidos) y sus conexiones (aristas).

2. **`dependencies`**:
   - **Tipo**: `dict`
   - **Estructura**: `{content_before: [lista de content_after]}`
   - **Descripción**: Diccionario que almacena las dependencias entre contenidos para ordenarlos.

---

### **Métodos**

#### **`__init__(self)`**
- **Descripción**: Constructor que inicializa un grafo vacío.
- **Resultado**: Crea un grafo sin vértices ni dependencias.

---

#### **`add_vertex(self, content)`**
- **Descripción**: Añade un nuevo vértice al grafo.
- **Parámetros**:
  - `content`: El contenido (película o serie) a añadir.
- **Detalles**: Si el vértice ya existe, no realiza ninguna acción.

---

#### **`add_edge(self, content1, content2, similarity=1.0)`**
- **Descripción**: Añade una arista no dirigida entre dos contenidos con un peso de similitud.
- **Parámetros**:
  - `content1`: El contenido de origen.
  - `content2`: El contenido destino.
  - `similarity` (opcional): Peso de la conexión (predeterminado `1.0`).
- **Detalles**: Crea los vértices si no existen y conecta ambos en ambas direcciones.

---

#### **`calculate_similarity(self, content1, content2)`**
- **Descripción**: Calcula la similitud entre dos contenidos basado en género, calificación y reparto.
- **Parámetros**:
  - `content1`, `content2`: Contenidos a comparar.
- **Detalles**:
  - **Género**: +0.4 si coinciden.
  - **Rating**: +0.3 si la diferencia es ≤ 1.
  - **Reparto**: +0.1 por actor compartido (máximo +0.3).
- **Resultado**: Retorna un valor de similitud entre `0.0` y `1.0`.

---

#### **`get_recommendations(self, content, limit=5)`**
- **Descripción**: Genera recomendaciones de contenidos similares.
- **Parámetros**:
  - `content`: El contenido base.
  - `limit` (opcional): Número máximo de recomendaciones (predeterminado `5`).
- **Resultado**: Una lista ordenada por similitud descendente.

---

#### **`get_recommendations_dfs(self, content, limit=5, min_similarity=0.3)`**
- **Descripción**: Genera recomendaciones usando una búsqueda en profundidad (DFS).
- **Parámetros**:
  - `content`: El contenido base.
  - `limit`: Número máximo de recomendaciones.
  - `min_similarity`: Peso mínimo de similitud para considerar vecinos.
- **Resultado**: Una lista de recomendaciones limitadas por profundidad y peso mínimo.

---

#### **`get_recommendations_bfs(self, content, limit=5, min_similarity=0.3)`**
- **Descripción**: Genera recomendaciones usando una búsqueda por niveles (BFS).
- **Parámetros**:
  - `content`: El contenido base.
  - `limit`: Número máximo de recomendaciones.
  - `min_similarity`: Peso mínimo de similitud para considerar vecinos.
- **Resultado**: Una lista de recomendaciones explorando vecinos nivel por nivel.

---

#### **`add_dependency(self, content_before, content_after)`**
- **Descripción**: Registra que un contenido debe ser visto antes que otro.
- **Parámetros**:
  - `content_before`: Contenido previo.
  - `content_after`: Contenido dependiente.
- **Detalles**: Las dependencias se guardan en el diccionario `dependencies`.

---

#### **`get_content_order(self)`**
- **Descripción**: Determina el orden de visualización de los contenidos basado en las dependencias.
- **Detalles**:
  - Realiza un **ordenamiento topológico**.
  - Detecta ciclos e informa si no es posible resolver el orden.
- **Resultado**: Una lista con el orden sugerido para consumir los contenidos. 

### **Ejemplo de Uso**


