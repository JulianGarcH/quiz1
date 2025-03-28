import json

NOTAS_FILE = "notas.json"

# Función para cargar notas
def cargar_notas():
    try:
        with open(NOTAS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Función para guardar notas
def guardar_notas(notas):
    with open(NOTAS_FILE, "w") as file:
        json.dump(notas, file, indent=4)

# Función para ingresar o editar una nota
def ingresar_editar_nota():
    notas = cargar_notas()
    
    alumno = input("Ingrese el nombre del alumno: ")
    if alumno in notas:
        print(f"⚠️ {alumno} ya tiene una nota registrada: {notas[alumno]}")
        opcion = input("¿Desea editarla? (s/n): ").lower()
        if opcion != "s":
            print("✅ No se realizaron cambios.")
            return
    
    nueva_nota = input(f"Ingrese la nueva nota para {alumno}: ")
    notas[alumno] = nueva_nota
    guardar_notas(notas)
    print(f"✅ Nota guardada para {alumno}: {nueva_nota}")


# Función para consultar notas
def consultar_notas(alumno):
    notas = cargar_notas()
    
    if alumno in notas:
        print(f"📖 {alumno}, tu nota es: {notas[alumno]}")
    else:
        print("⚠️ No tienes una nota registrada.")
