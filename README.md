# Entrega Final - ViewFlix :movie_camera:

## Universidad Nacional Almirante Brown  
**Materia:** Estructuras de Datos :floppy_disk:   
**2do cuatrimestre, 2024**

---

### Integrantes del Grupo:  :two_men_holding_hands:  
- **Facundo Gonzalez** :sunglasses: 
- **Alejo Aliberti** :sunglasses:

**Lenguaje Utilizado:** Python :snake:

---

## Introducción: 

El proyecto **ViewFlix** se inspira en las principales plataformas de streaming para ofrecer una experiencia que simula la visualización y gestión de películas y series. Este trabajo final busca integrar y aplicar los conceptos de **estructuras de datos** aprendidos durante la cursada, trasladándolos a un entorno práctico y relevante.

---

## Objetivo: :dart:

El objetivo principal de **ViewFlix** es emular las funcionalidades esenciales de los servicios de streaming como:

- **Exploración de Contenido y sus catálogos:** Navegar entre películas y series organizadas por género.  
- **Gestión de usuarios:** Crear cuentas y permitir la gestión de hasta 5 perfiles por usuario.  
- **Creación y personalización de listas:** Permitir a los usuarios crear listas personalizadas de contenido favorito.  
- **Acceso al detalle de cada contenido:** Ofrecer información detallada sobre las películas y series disponibles.  
- **Búsqueda eficiente:** Implementar un buscador eficiente para encontrar contenido de forma rápida.  

---
## Diagrama de relaciones
![image](https://github.com/user-attachments/assets/98cd8d7f-8ba8-4bda-9935-03a393bf3d0a)

---

## 1. Clases Principales :books:

### 1.1 Catálogo (Catalog)

- **Estructura:** Combina múltiples estructuras de datos especializadas.  
- **Componentes:**
  - **movies:** Lista enlazada (LinkedList).  
  - **series:** Árbol general (GeneralTree).  
  - **most_popular:** Árbol binario de búsqueda (BinarySearchTree).  
  - **recommendations_graph:** Grafo ponderado no dirigido (Graph).  

#### Justificación:

- La lista enlazada para películas permite inserción O(1) y búsqueda lineal O(n).  
- El árbol general para series maneja eficientemente la jerarquía series > temporadas > episodios.  
- El árbol binario de búsqueda optimiza búsquedas de contenido popular en O(log n).  
- El grafo facilita recomendaciones basadas en similitud entre contenidos.  

---

### 1.2 Perfil de Usuario (User) :bust_in_silhouette:

- **Estructuras:**
  - **favorites:** Lista enlazada.  
  - **history:** Pila (Stack).  
  - **watchlist:** Montículo máximo (MaxHeap).  

#### Justificación:
- La pila para historial permite acceso LIFO eficiente O(1).  
- El montículo máximo optimiza la gestión de la lista de reproducción por prioridad.  
- La lista enlazada para favoritos permite modificaciones dinámicas eficientes.  

---
### 1.3 Clases de Contenido (MediaContent)
Estructura: La base de los datos de contenido multimedia se gestiona con una jerarquía de clases en Python.

### Componentes:
- MediaContent: Clase base que define las propiedades y comportamientos generales de cualquier contenido.
- Movie: Subclase que representa una película, heredando de MediaContent.
- Series: Subclase que representa una serie, con temporadas y episodios estructurados jerárquicamente.
- Episode: Clase independiente que representa un episodio de una serie.
  
#### Justificación:
- La clase MediaContent permite abstraer propiedades comunes como nombre, categoría, vistas y calificaciones.
- La herencia en Movie y Series facilita extender comportamientos específicos para cada tipo de contenido, manteniendo un diseño limpio y escalable.
- Los episodios se modelan de manera independiente para una representación más flexible dentro de las temporadas de una serie.
---

## 2. Algoritmos Clave

### 2.1 Sistema de Recomendaciones 
- Implementación de búsqueda **BFS** y **DFS** para diferentes tipos de recomendaciones.  
  - **BFS:** Proporciona recomendaciones más variadas.  
  - **DFS:** Encuentra recomendaciones más específicas dentro de un género.  

### 2.2 Búsqueda de Contenido :mag_right:
- Búsqueda por nombre en múltiples estructuras.  
- Ordenamiento por preferencias del usuario.  
- Implementa búsqueda parcial para mejor experiencia.  

---

## 3. Optimizaciones

### 3.1 Agregar Contenido Popular 
- Mantiene árbol binario de búsqueda para acceso rápido O(log n).  
- Separación entre películas y series populares.  
- Actualización periódica para mantener relevancia.  

### 3.2 Gestión de Dependencias
- Implementa ordenamiento topológico para series.  
- Maneja prerrequisitos entre episodios.  
- Evita ciclos en el orden de visualización.  

---

## 4. Complejidades Temporales

### Operaciones Frecuentes:
- **Búsqueda de contenido:** O(n).  
- **Inserción de nuevo contenido:** O(1) - O(log n).  
- **Obtener recomendaciones:** O(V + E).  
- **Actualizar historial:** O(1).  
- **Gestionar favoritos:** O(1) - O(n).  

---
## Conclusión:
 Los **árboles** fueron fundamentales para mejorar el rendimiento en las búsquedas de contenido, ya
 que, al implementar búsquedas binarias, se redujo la complejidad algorítmica, mientras que en la
 **carga de contenido**, particularmente en Movies, se usaron **árboles binarios** para ordenar los
 **contenidos más populares** según la cantidad de vistas. Además, los **grafos** permitieron establecer
 relaciones entre contenidos basándose en el rating y el elenco (cast), calculando el peso de las aristas,
 y el **ordenamiento topológico** facilitó encontrar la secuencia más óptima de visualización según las
 preferencias del usuario y el tiempo disponible. Para el **historial de contenido**, se utilizó una pila
 (stack) debido a su comportamiento **LIFO**, logrando que el último contenido visualizado fuera el
 primero en aparecer en la lista, obteniendo un historial cronológico. Por último, la implementación de
 un **árbol general** en las series permitió organizar jerárquicamente las series, temporadas y episodios.
  


