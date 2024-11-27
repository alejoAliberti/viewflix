# **Documentación de la Clase `User`**

## **Clase `User`**

La clase `User` representa a un usuario dentro de una plataforma de contenidos multimedia (como películas y series). Esta clase gestiona las preferencias de género, el historial de contenidos vistos, los contenidos favoritos y la lista de seguimiento (watchlist).

### **Propiedades**
- **`favorites`**:
  - **Tipo**: `LinkedList`
  - **Descripción**: Lista enlazada que almacena los contenidos favoritos del usuario. Utiliza la clase `LinkedList` para gestionar los contenidos.
  
- **`name`**:
  - **Tipo**: `str`
  - **Descripción**: Nombre del usuario.
  
- **`age`**:
  - **Tipo**: `int`
  - **Descripción**: Edad del usuario.
  
- **`preferences`**:
  - **Tipo**: `List[str]`
  - **Descripción**: Lista de preferencias del usuario (por ejemplo, géneros de contenido como `'drama'`, `'acción'`, `'terror'`).

- **`history`**:
  - **Tipo**: `Stack`
  - **Descripción**: Pila que almacena el historial de contenidos vistos por el usuario, usando la clase `Stack` para gestionar los contenidos en orden de visualización.

- **`watchlist`**:
  - **Tipo**: `MaxHeap`
  - **Descripción**: Montículo máximo que organiza los contenidos que el usuario desea ver, priorizando aquellos con más vistas. Utiliza la clase `MaxHeap` para mantener el orden.

### **Métodos**

#### **`__init__(self, name: str, age: int, preferences: List[str])`**
- **Descripción**: Constructor que inicializa un nuevo objeto `User` con el nombre, la edad y las preferencias del usuario.
- **Parámetros**:
  - `name`: Nombre del usuario.
  - `age`: Edad del usuario.
  - `preferences`: Lista de géneros preferidos por el usuario (ejemplo: `['drama', 'acción']`).
- **Resultado**: Inicializa el usuario con las propiedades y estructuras de datos vacías (favoritos, historial y watchlist).

---

#### **`add_preference(self, preference: str)`**
- **Descripción**: Añade una nueva preferencia de género a la lista de preferencias del usuario.
- **Parámetros**:
  - `preference`: El género a añadir (por ejemplo, `'comedia'`, `'romántica'`).
- **Resultado**: La preferencia se agrega a la lista de preferencias del usuario.

---

#### **`add_to_history(self, content: MediaContent)`**
- **Descripción**: Añade un contenido al historial del usuario. El contenido se apila en la estructura `Stack`, manteniendo los contenidos más recientes en la parte superior.
- **Parámetros**:
  - `content`: El contenido (película o serie) que se está agregando al historial.
- **Resultado**: El contenido se añade al historial del usuario.

---

#### **`get_history(self) -> List[MediaContent]`**
- **Descripción**: Retorna el historial completo del usuario, ordenado por fecha de visualización (más reciente primero).
- **Resultado**: Retorna la lista de contenidos del historial, con los más recientes en la parte superior.

---

#### **`clear_history(self)`**
- **Descripción**: Elimina todos los elementos del historial del usuario.
- **Resultado**: El historial se vacía completamente.

---

#### **`add_to_favorites(self, content: MediaContent) -> bool`**
- **Descripción**: Añade un contenido a la lista de favoritos del usuario. Si el contenido ya está en favoritos, lanza un error.
- **Parámetros**:
  - `content`: El contenido (película o serie) a añadir a los favoritos.
- **Resultado**: Si el contenido no está en favoritos, se añade a la lista. Si ya está, se lanza un `ValueError`.

---

#### **`remove_from_favorites(self, content: MediaContent) -> bool`**
- **Descripción**: Elimina un contenido de la lista de favoritos del usuario.
- **Parámetros**:
  - `content`: El contenido (película o serie) que se desea eliminar de los favoritos.
- **Resultado**: El contenido se elimina de la lista de favoritos. Retorna `True` si se eliminó correctamente, `False` si no estaba en la lista.

---

#### **`get_favorites(self, content_type: str = None) -> Dict[str, List[MediaContent]]`**
- **Descripción**: Retorna la lista de favoritos del usuario. Si se especifica un tipo de contenido (`'movie'` o `'serie'`), retorna solo ese tipo de contenido.
- **Parámetros**:
  - `content_type` (opcional): Especifica si se desean los favoritos de tipo `'movie'` o `'serie'`.
- **Resultado**: Retorna un diccionario con las listas de favoritos por tipo (`'movie'`, `'serie'`), o todos los favoritos si no se especifica `content_type`.

---

#### **`is_favorite(self, content: MediaContent) -> bool`**
- **Descripción**: Verifica si un contenido está en la lista de favoritos del usuario.
- **Parámetros**:
  - `content`: El contenido (película o serie) a verificar.
- **Resultado**: Retorna `True` si el contenido está en favoritos, `False` si no lo está.

---

#### **`set_watchlist(self, content: MediaContent)`**
- **Descripción**: Añade un contenido a la lista de seguimiento (watchlist) del usuario, organizándolo en la estructura `MaxHeap` según su número de vistas.
- **Parámetros**:
  - `content`: El contenido a añadir a la lista de seguimiento.
- **Resultado**: El contenido se inserta en la lista de seguimiento, priorizando aquellos con más vistas.

---

### **Estructuras de Datos Utilizadas**

#### **`LinkedList`**
- Se utiliza para gestionar la lista de favoritos, permitiendo añadir, eliminar y buscar contenidos de manera eficiente.

#### **`Stack`**
- Se utiliza para gestionar el historial de contenidos vistos, garantizando que el contenido más reciente sea el primero en la pila.

#### **`MaxHeap`**
- Se utiliza para gestionar la lista de seguimiento, organizando los contenidos según la cantidad de vistas, con los contenidos más populares (mayor número de vistas) en la parte superior.

---

Esta clase permite gestionar las preferencias, el historial, los favoritos y la lista de seguimiento de un usuario dentro de una plataforma multimedia, utilizando diferentes estructuras de datos para optimizar las operaciones en cada caso.
