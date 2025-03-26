import json

# Archivo donde se guardan los usuarios
USERS_FILE = "usuarios.json"

# Función para cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    try:
        with open(USERS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Función para guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open(USERS_FILE, "w") as file:
        json.dump(usuarios, file, indent=4)

# Función para registrar un usuario nuevo
def registrar_usuario():
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
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese el nombre de usuario a eliminar: ")
    
    if usuario not in usuarios:
        print("⚠️ El usuario no existe.")
        return
    
    del usuarios[usuario]
    guardar_usuarios(usuarios)
    
    print("✅ Usuario eliminado correctamente.")

# Función para iniciar sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"✅ Bienvenido, {usuario} ({usuarios[usuario]['tipo']})")
        return usuario, usuarios[usuario]["tipo"]
    else:
        print("⚠️ Usuario o contraseña incorrectos.")
        return None, None
