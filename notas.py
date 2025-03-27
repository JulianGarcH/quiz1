import json

# Archivo donde se guardarán las notas
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
    nota = input("Ingrese la nota (0 - 10): ")

    if not (nota.replace(".", "", 1).isdigit() and 0 <= float(nota) <= 10):
        print("⚠️ Nota inválida. Debe ser un número entre 0 y 10.")
        return

    if alumno not in notas:
        notas[alumno] = {}

    notas[alumno][materia] = float(nota)
    guardar_notas(notas)

    print(f"✅ Nota de {materia} para {alumno} registrada correctamente.")

# Función para que el alumno consulte sus notas
def consultar_notas(usuario):
    notas = cargar_notas()

    if usuario not in notas:
        print("⚠️ No hay notas registradas para este alumno.")
        return

    print(f"\n📖 Notas de {usuario}:")
    for materia, nota in notas[usuario].items():
        print(f"📌 {materia}: {nota}")
