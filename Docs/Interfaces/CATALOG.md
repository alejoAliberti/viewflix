# **Documentación de la Clase `Catalog`**

La clase `Catalog` organiza y gestiona contenido multimedia (películas y series). Implementa diversas estructuras de datos, como listas enlazadas, árboles generales, árboles binarios de búsqueda y grafos, para ofrecer funcionalidades como búsquedas rápidas, recomendaciones y jerarquías de contenido.

---

## **Atributos**

- **`movies`** (`LinkedList`): Lista enlazada que almacena películas.
- **`series`** (`GeneralTree`): Árbol general que organiza las series por temporadas y episodios.
- **`most_popular`** (`BinarySearchTree`): Árbol binario de búsqueda que almacena el contenido más popular.
- **`most_popular_movie`** (`BinarySearchTree`): Árbol binario de búsqueda que almacena las películas más populares.
- **`most_popular_series`** (`BinarySearchTree`): Árbol binario de búsqueda que almacena las series más populares.
- **`recommendations_graph`** (`Graph`): Grafo que gestiona las recomendaciones basadas en similitudes entre contenidos.

---

## **Métodos**

### **`__init__(self)`**
- **Descripción**: Constructor que inicializa un catálogo vacío con las estructuras de datos necesarias.

---

### **`add_most_popular(self)`**
- **Descripción**: Añade todo el contenido al árbol de los más populares (películas y series).

---

### **`add_most_popular_movies(self)`**
- **Descripción**: Añade todas las películas al árbol de las películas más populares.

---

### **`add_most_popular_series(self)`**
- **Descripción**: Añade todas las series al árbol de las series más populares.

---

### **`set_serie(self, serie: Serie)`**
- **Descripción**: Agrega una serie al árbol general, organizándola jerárquicamente por temporadas y episodios.
- **Parámetros**:
  - `serie` (`Serie`): Serie a añadir.

---

### **`set_movies(self, movie: Movie)`**
- **Descripción**: Agrega una película a la lista enlazada.
- **Parámetros**:
  - `movie` (`Movie`): Película a añadir.

---

### **`search_content(self, name: str, preferences: List[str] = None) -> MediaContent`**
- **Descripción**: Busca contenido (película o serie) por su nombre.
- **Parámetros**:
  - `name` (`str`): Nombre del contenido a buscar.
  - `preferences` (`List[str]`): Lista de preferencias para ordenar los resultados.
- **Resultado**: Retorna el contenido que coincida con el nombre o `None` si no se encuentra.

---

### **`update_recommendations_graph(self)`**
- **Descripción**: Actualiza el grafo de recomendaciones creando conexiones entre contenidos similares.

---

### **`get_recommendations(self, content, limit=5)`**
- **Descripción**: Obtiene recomendaciones basadas en el contenido proporcionado.
- **Parámetros**:
  - `content`: Contenido base para las recomendaciones.
  - `limit` (`int`): Máximo número de recomendaciones a retornar.
- **Resultado**: Lista de contenidos recomendados.

---

### **`get_recommendations_by_type(self, content, recommendation_type='bfs', limit=5)`**
- **Descripción**: Obtiene recomendaciones según el tipo de recorrido (BFS o DFS) especificado.
- **Parámetros**:
  - `content`: Contenido base para las recomendaciones.
  - `recommendation_type` (`str`): Tipo de recorrido (`'bfs'` o `'dfs'`).
  - `limit` (`int`): Máximo número de recomendaciones a retornar.
- **Resultado**: Lista de contenidos recomendados.
