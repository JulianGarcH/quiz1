import json

# Archivo donde se guardan los usuarios
USERS_FILE = "usuarios.json"

# Función para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    """Carga los usuarios desde el archivo JSON."""
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Función para guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    """Guarda los usuarios en el archivo JSON."""
    with open(USERS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

# Función para registrar un usuario nuevo
def registrar_usuario():
    """Permite registrar un usuario nuevo."""
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print("⚠️ El usuario ya existe. Intente con otro.")
        return
    
    contraseña = input("Ingrese una contraseña: ")
    tipo_usuario = input("Tipo de usuario (profesor/alumno): ").lower()
    
    if tipo_usuario not in ["profesor", "alumno"]:
        print("⚠️ Tipo de usuario inválido. Debe ser 'profesor' o 'alumno'.")
        return

    usuarios[usuario] = {"contraseña": contraseña, "tipo": tipo_usuario}
    guardar_usuarios(usuarios)
    
    print("✅ Registro exitoso.")

# Función para eliminar un usuario
def eliminar_usuario():
    """Permite eliminar un usuario del sistema."""
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese el nombre de usuario a eliminar: ")
    
    if usuario not in usuarios:
        print("⚠️ El usuario no existe.")
        return
    
    del usuarios[usuario]  # Eliminamos el usuario del diccionario
    guardar_usuarios(usuarios)  # Guardamos los cambios en usuarios.json
    
    print("✅ Usuario eliminado correctamente.")

# Función para iniciar sesión
def iniciar_sesion():
    """Permite a un usuario iniciar sesión."""
    usuarios = cargar_usuarios()

    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"✅ Inicio de sesión exitoso. Bienvenido {usuario}!")
        return usuarios[usuario]["tipo"]  # Retorna si es "profesor" o "alumno"
    else:
        print("⚠️ Usuario o contraseña incorrectos.")
        return None

# Menú Principal
def menu_principal():
    while True:
        print("\n--- Gestión de Notas ---")
        print("1) Registrar Usuario")
        print("2) Eliminar Usuario")
        print("3) Ingresar como Profesor")
        print("4) Ingresar como Alumno")
        print("5) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            eliminar_usuario()
        elif opcion == "3":
            print("Funcionalidad de profesor en desarrollo...")
        elif opcion == "4":
            print("Funcionalidad de alumno en desarrollo...")
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

# Ejecutar el menú si el archivo se ejecuta directamente
if __name__ == "__main__":
    menu_principal()
