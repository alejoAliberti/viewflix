# **Documentación de la Clase `Account`**

La clase `Account` representa una cuenta de usuario con múltiples perfiles asociados. Proporciona métodos para gestionar los atributos de la cuenta, como nombre de usuario, contraseña y perfiles.

---

## **Atributos**

- **`username`** (`str`): Nombre de usuario de la cuenta.
- **`password`** (`str`): Contraseña de la cuenta.
- **`profiles`** (`List[User]`): Lista de perfiles asociados a la cuenta (hasta un máximo de 5).
- **`id`** (`int`): Identificador único de la cuenta.

---

## **Métodos**

### **`__init__(self, username: str, password: str, profiles: List[User], id: int)`**
- **Descripción**: Constructor que inicializa una cuenta con los datos proporcionados.
- **Parámetros**:
  - `username` (`str`): Nombre de usuario.
  - `password` (`str`): Contraseña.
  - `profiles` (`List[User]`): Lista de perfiles iniciales.
  - `id` (`int`): ID único de la cuenta.
- **Resultado**: Crea una instancia de `Account`.

---

### **`add_profile(self, profile: User)`**
- **Descripción**: Añade un perfil a la lista de perfiles de la cuenta.
- **Parámetros**:
  - `profile` (`User`): Perfil a añadir.
- **Restricciones**: La cuenta puede tener un máximo de 5 perfiles.
- **Errores**: Lanza `ValueError` si ya hay 5 perfiles asociados.

---

### **`get_username(self) -> str`**
- **Descripción**: Obtiene el nombre de usuario de la cuenta.
- **Resultado**: Retorna el nombre de usuario como una cadena.

---

### **`get_password(self) -> str`**
- **Descripción**: Obtiene la contraseña de la cuenta.
- **Nota de Seguridad**: No es seguro exponer contraseñas en entornos de producción.
- **Resultado**: Retorna la contraseña como una cadena.

---

### **`get_profiles(self) -> List[User]`**
- **Descripción**: Obtiene la lista de perfiles asociados a la cuenta.
- **Resultado**: Retorna una lista de objetos `User`.

---

### **`get_id(self) -> int`**
- **Descripción**: Obtiene el identificador único de la cuenta.
- **Resultado**: Retorna el ID como un entero.

---

### **`set_username(self, username: str)`**
- **Descripción**: Actualiza el nombre de usuario.
- **Parámetros**:
  - `username` (`str`): Nuevo nombre de usuario.
- **Restricciones**: El nombre de usuario no puede estar vacío.
- **Errores**: Lanza `ValueError` si el nombre de usuario es una cadena vacía o contiene solo espacios.

---

### **`set_password(self, password: str)`**
- **Descripción**: Actualiza la contraseña de la cuenta.
- **Parámetros**:
  - `password` (`str`): Nueva contraseña.
- **Restricciones**: La contraseña debe tener al menos 8 caracteres.
- **Errores**: Lanza `ValueError` si la contraseña no cumple con la longitud mínima.
