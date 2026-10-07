class MaterialBiblioteca:
    def __init__(self, titulo, codigo, disponibilidad):
        self.titulo = titulo
        self.codigo = codigo
        self.disponibilidad = disponibilidad

    def mostrar_informacion(self):
            print(f"Título: {self.titulo}")
            print(f"Código: {self.codigo}")
            print(f"Disponibilidad: {'Disponible' if self.disponibilidad else 'No disponible'}")

    def calcular_dias_prestamo(self):
        pass


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo, disponibilidad, autor):
        super().__init__(titulo, codigo, disponibilidad)
        self.autor = autor

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Autor: {self.autor}")

    def calcular_dias_prestamo(self):
        return 7


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo, disponibilidad, numero_edicion):
        super().__init__(titulo, codigo, disponibilidad)
        self.numero_edicion = numero_edicion

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Número de edición: {self.numero_edicion}")

    def calcular_dias_prestamo(self):
        return 3





