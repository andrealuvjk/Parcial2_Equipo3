from biblioteca import Libro, Revista

materiales = [
    Libro("Cien años de soledad", "L-001", True, "Gabriel García Márquez"),
    Libro("1984", "L-002", True, "George Orwell"),
    Libro("Don Quijote de la Mancha", "L-003", False, "Miguel de Cervantes"),
    Revista("National Geographic", "R-001", True, 145),
    Revista("Scientific American", "R-002", False, 312),
    Revista("Time", "R-003", True, 88)
]

print("=== REGISTRO DE MATERIALES DE LA BIBLIOTECA ===\n")

for material in materiales:
    material.mostrar_informacion()
    print(f"Días de préstamo: {material.calcular_dias_prestamo()}")
    print("-" * 30)