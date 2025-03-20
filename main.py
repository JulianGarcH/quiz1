import sys
import os

if os.name == "nt":  # Solo en Windows
    os.system("chcp 65001 > nul")  # Cambia la codificación a UTF-8python main.py
def menu():
    while True:
        print("\n📌 Menú Principal")
        print("1️⃣ Registrarse")
        print("2️⃣ Iniciar sesión")
        print("3️⃣ Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "3":
            print("👋 Saliendo del programa...")
            break
        else:
            print("⚠️ Funcionalidad en desarrollo.")

if __name__ == "__main__":
    menu()
