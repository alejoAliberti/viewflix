# **Documentación de las Clases `MediaContent`, `Movie`, `Episode` y `Series`**

## **Clase `MediaContent`**

La clase `MediaContent` representa un contenido multimedia general, como una película o serie, e incluye detalles sobre su categoría, su elenco, duración, vistas y calificaciones.

### **Propiedades**
- **`name`**:
  - **Tipo**: `str`
  - **Descripción**: Nombre del contenido (película o serie).
  
- **`category`**:
  - **Tipo**: `str`
  - **Descripción**: Categoría del contenido (por ejemplo, `'acción'`, `'drama'`).
  
- **`id`**:
  - **Tipo**: `int`
  - **Descripción**: Identificador único del contenido.
  
- **`watched_date`**:
  - **Tipo**: `datetime`
  - **Descripción**: Fecha en que se visualizó por primera vez el contenido. Se establece automáticamente al momento de la creación.

- **`_ratings`**:
  - **Tipo**: `List[float]`
  - **Descripción**: Lista que almacena las puntuaciones individuales dadas al contenido.
  
- **`rating`**:
  - **Tipo**: `float`
  - **Descripción**: Promedio de las puntuaciones del contenido. Se actualiza automáticamente cuando se agrega una nueva puntuación.

- **`views`**:
  - **Tipo**: `int`
  - **Descripción**: Número de vistas que tiene el contenido.

- **`cast`**:
  - **Tipo**: `List[str]`
  - **Descripción**: Lista de actores o personajes principales del contenido.

- **`duration`**:
  - **Tipo**: `int`
  - **Descripción**: Duración del contenido en minutos (en el caso de una película).

---

### **Métodos**

#### **`__init__(self, name: str, category: str, id: int, cast: List[str] = [], duration: int = 0)`**
- **Descripción**: Constructor que inicializa un nuevo contenido multimedia con nombre, categoría, ID, elenco, duración y valores predeterminados para vistas y calificación.
- **Parámetros**:
  - `name`: Nombre del contenido.
  - `category`: Categoría del contenido.
  - `id`: Identificador único del contenido.
  - `cast` (opcional): Lista de actores o personajes principales.
  - `duration` (opcional): Duración del contenido (solo aplicable a películas).
  
---

#### **`__lt__(self, other) -> bool`**
- **Descripción**: Sobrecarga del operador `<`, compara dos contenidos utilizando el número de vistas como criterio.
- **Parámetros**:
  - `other`: Otro objeto de tipo `MediaContent` para comparar.
- **Resultado**: Retorna `True` si el contenido tiene menos vistas que el otro contenido, `False` en caso contrario.

---

#### **`__gt__(self, other) -> bool`**
- **Descripción**: Sobrecarga del operador `>`, compara dos contenidos utilizando el número de vistas como criterio.
- **Parámetros**:
  - `other`: Otro objeto de tipo `MediaContent` para comparar.
- **Resultado**: Retorna `True` si el contenido tiene más vistas que el otro contenido, `False` en caso contrario.

---

#### **`__eq__(self, other) -> bool`**
- **Descripción**: Sobrecarga del operador `==`, compara dos contenidos utilizando el nombre o el ID como criterio de igualdad.
- **Parámetros**:
  - `other`: Otro objeto de tipo `MediaContent` para comparar.
- **Resultado**: Retorna `True` si los contenidos tienen el mismo nombre o ID, `False` en caso contrario.

---

#### **`add_view(self) -> None`**
- **Descripción**: Añade una vista al contenido, incrementando el número de vistas.
- **Resultado**: Incrementa el valor de `views` en 1.

---

#### **`get_views(self) -> int`**
- **Descripción**: Retorna el número total de vistas del contenido.
- **Resultado**: El número total de vistas (`views`).

---

#### **`add_rating(self, score: float) -> None`**
- **Descripción**: Añade una nueva puntuación (entre 0 y 5) y actualiza la calificación promedio del contenido.
- **Parámetros**:
  - `score`: Puntuación entre 0 y 5 a agregar.
- **Resultado**: La puntuación se añade a la lista de calificaciones y el promedio (`rating`) se actualiza.

---

## **Clase `Movie`**

La clase `Movie` hereda de `MediaContent` y representa una película, añadiendo un campo para la duración.

### **Propiedades**
- **`duration`**:
  - **Tipo**: `int`
  - **Descripción**: Duración de la película en minutos.

- **`type`**:
  - **Tipo**: `str`
  - **Descripción**: Tipo de contenido, que siempre será `'movie'` para esta clase.

---

#### **`__init__(self, name: str, category: str, duration: int, id: int)`**
- **Descripción**: Constructor que inicializa una película con nombre, categoría, duración y ID.
- **Parámetros**:
  - `name`: Nombre de la película.
  - `category`: Categoría de la película.
  - `duration`: Duración de la película en minutos.
  - `id`: Identificador único de la película.

---

## **Clase `Episode`**

La clase `Episode` representa un episodio dentro de una serie, incluyendo su nombre, duración y número de episodio.

### **Propiedades**
- **`name`**:
  - **Tipo**: `str`
  - **Descripción**: Nombre del episodio.

- **`duration`**:
  - **Tipo**: `int`
  - **Descripción**: Duración del episodio en minutos.

- **`episode_number`**:
  - **Tipo**: `int`
  - **Descripción**: Número del episodio dentro de la serie (por ejemplo, episodio 1, episodio 2).

- **`watched_date`**:
  - **Tipo**: `datetime`
  - **Descripción**: Fecha en que el episodio fue visualizado.

---

#### **`__init__(self, name: str, duration: int, episode_number: int)`**
- **Descripción**: Constructor que inicializa un nuevo episodio con nombre, duración y número de episodio.
- **Parámetros**:
  - `name`: Nombre del episodio.
  - `duration`: Duración del episodio en minutos.
  - `episode_number`: Número del episodio dentro de la serie.

---

## **Clase `Series`**

La clase `Series` hereda de `MediaContent` y representa una serie, permitiendo agregar temporadas y episodios.

### **Propiedades**
- **`type`**:
  - **Tipo**: `str`
  - **Descripción**: Tipo de contenido, que siempre será `'series'` para esta clase.

- **`seasons`**:
  - **Tipo**: `List[List[Episode]]`
  - **Descripción**: Lista de temporadas, donde cada temporada es una lista de objetos `Episode`.

---

#### **`__init__(self, name: str, category: str, id: int)`**
- **Descripción**: Constructor que inicializa una serie con nombre, categoría y ID.
- **Parámetros**:
  - `name`: Nombre de la serie.
  - `category`: Categoría de la serie.
  - `id`: Identificador único de la serie.

---

#### **`add_season(self, episodes: List[Episode]) -> None`**
- **Descripción**: Añade una nueva temporada con sus episodios a la serie.
- **Parámetros**:
  - `episodes`: Lista de objetos `Episode` que corresponden a los episodios de la temporada.

---

#### **`get_season(self, season_number: int) -> List[Episode]`**
- **Descripción**: Obtiene los episodios de una temporada específica de la serie.
- **Parámetros**:
  - `season_number`: Número de la temporada (por ejemplo, 1 para la primera temporada).
- **Resultado**: Retorna la lista de episodios de la temporada especificada.

---

#### **`add_episode(self, season_number: int, episode: Episode) -> None`**
- **Descripción**: Añade un episodio a una temporada específica de la serie.
- **Parámetros**:
  - `season_number`: Número de la temporada a la que se añadirá el episodio.
  - `episode`: Objeto `Episode` a añadir a la temporada.
- **Resultado**: El episodio se agrega a la temporada correspondiente. Si la temporada no existe, se crea una nueva.

---
