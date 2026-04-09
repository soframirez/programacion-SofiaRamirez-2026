def guardar_practica(ejercicios, nombre_archivo="practica.txt"):
    with open(nombre_archivo, "w") as f:
        f.write("PRACTICA DE MATEMATICAS\n")
        f.write("="*50 + "\n\n")
        for i, (a, op, b, _) in enumerate(ejercicios, 1):
            f.write(f"{i}) {a} {op} {b} = __________\n")

def guardar_respuestas(ejercicios, nombre_archivo="respuestas.txt"):
    with open(nombre_archivo, "w") as f:
        f.write("HOJA DE RESPUESTAS (SOLO PARA EL PROFESOR)\n")
        f.write("="*50 + "\n\n")
        for i, (a, op, b, res) in enumerate(ejercicios, 1):
            f.write(f"{i}) {a} {op} {b} = {res}\n")