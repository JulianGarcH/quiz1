import json

# Función para mostrar el menú principal
def menu_principal():
    while True:
        print("\n--- Gestión de Notas ---")
        print("1) Ingresar como Profesor")
        print("2) Ingresar como Alumno")
        print("3) Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            print("Funcionalidad de profesor en desarrollo...")
        elif opcion == "2":
            print("Funcionalidad de alumno en desarrollo...")
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()
