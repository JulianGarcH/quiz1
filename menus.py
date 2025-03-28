from usuarios import iniciar_sesion
from notas import ingresar_editar_nota, consultar_notas

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
