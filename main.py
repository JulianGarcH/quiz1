import json
from usuarios import cargar_usuarios
from notas import ingresar_editar_nota, consultar_notas

# Función para iniciar sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()
    
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario in usuarios and usuarios[usuario]["contraseña"] == contraseña:
        print(f"✅ Bienvenido, {usuario} ({usuarios[usuario]['tipo']})")

        if usuarios[usuario]["tipo"] == "profesor":
            menu_profesor()
        elif usuarios[usuario]["tipo"] == "alumno":
            menu_alumno(usuario)
    else:
        print("⚠️ Usuario o contraseña incorrectos.")

# Menú del profesor
def menu_profesor():
    while True:
        print("\n--- 📚 Menú Profesor ---")
        print("1) Ingresar/Editar Notas")
        print("2) Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresar_editar_nota()
        elif opcion == "2":
            print("👋 Cerrando sesión...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

# Menú del alumno
def menu_alumno(usuario):
    while True:
        print("\n--- 🎓 Menú Alumno ---")
        print("1) Consultar Notas")
        print("2) Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_notas(usuario)
        elif opcion == "2":
            print("👋 Cerrando sesión...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

# Menú principal
def menu_principal():
    while True:
        print("\n--- 🔹 Gestión de Notas 🔹 ---")
        print("1) Iniciar Sesión")
        print("2) Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida, intente de nuevo.")

# Ejecutar el menú principal
if __name__ == "__main__":
    menu_principal()
