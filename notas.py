import json

# Archivo donde se guardan las notas
NOTAS_FILE = "notas.json"

# Función para cargar las notas desde el archivo JSON
def cargar_notas():
    try:
        with open(NOTAS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Función para guardar las notas en el archivo JSON
def guardar_notas(notas):
    with open(NOTAS_FILE, "w") as file:
        json.dump(notas, file, indent=4)

# Función para que el profesor ingrese o edite notas
def ingresar_editar_nota():
    notas = cargar_notas()
    
    alumno = input("Ingrese el nombre del alumno: ")
    materia = input("Ingrese la materia: ")
    nota = input("Ingrese la nota: ")

    if alumno not in notas:
        notas[alumno] = {}

    notas[alumno][materia] = nota
    guardar_notas(notas)
    
    print("✅ Nota guardada exitosamente.")

# Función para que el alumno consulte sus notas
def consultar_notas(alumno):
    notas = cargar_notas()
    
    if alumno in notas:
        print(f"\n📚 Notas de {alumno}:")
        for materia, nota in notas[alumno].items():
            print(f"🔹 {materia}: {nota}")
    else:
        print("⚠️ No hay notas registradas para este alumno.")
