Sistema de Biblioteca Universitaria
                             
                               
                               
                               Nombre del equipo: Equipo3

 
 
 Integrantes:
 Fátima Andrea Ochoa Amaya,
Gabriela Nicole Aquino Solí,
Diego Omar Landaverde Ayala, 
Katherine Yamileth Mancía Hernández,
Saira Stephanie Melgar Abrego,
Víctor Javier Vásquez Ceron 


Escenario seleccionado: A – Sistema de biblioteca




Descripción de la solución
Demostración de un sistema de biblioteca universitaria que representa dos tipos de recursos disponibles para préstamo: libros y revistas, cada uno con características y plazos de préstamo distintos. La solución tiene dos partes que se desarrollaron de forma independiente:
Python: modelos orientados a objetos (biblioteca.py) y un programa (main.py) que registra seis materiales y muestra su información y sus días de préstamo.
Frontend: una página web con el catálogo, el tipo de material, su disponibilidad y un botón para solicitar el préstamo.

Estructura del repositorio:


nombre-proyecto/
├── Python/
│   ├── biblioteca.py
│   └── main.py
├── Html/
│   ├── index.html
│   ├── styles.css
│   └── script.js
└── README.md
Cómo ejecutar
Python: desde la carpeta Python/, ejecutar python main.py.
Frontend: abrir Html/index.html en el navegado

Herencia y polimorfismo
Elemento
Detalle
Clase padre
MaterialBiblioteca, con los atributos titulo, codigo y disponibilidad
Clase hija 1
Libro, que agrega el atributo autor
Clase hija 2
Revista, que agrega el atributo numero_edicion
Métodos sobrescritos
mostrar_informacion() y calcular_dias_prestamo()
Plazos de préstamo
Libro = 7 días, Revista = 3 días

Herencia: Libro y Revista heredan de MaterialBiblioteca, por lo que reutilizan sus atributos comunes (título, código y disponibilidad). Cada clase hija llama a super().__init__(...) para inicializar esos datos y luego agrega únicamente lo propio: el autor en Libro y el número de edición en Revista. Así no se repite código.

Sobrescritura: la clase padre define mostrar_informacion() (imprime título, código y disponibilidad) y calcular_dias_prestamo() (sin implementación, con pass). Las clases hijas vuelven a definir estos métodos:
En mostrar_informacion(), cada hija llama primero a super().mostrar_informacion() para imprimir los datos comunes y después imprime su dato propio (autor o número de edición).

En calcular_dias_prestamo(), Libro devuelve 7 y Revista devuelve 3.
Polimorfismo: significa que objetos de distintas clases responden al mismo método, cada uno a su manera. En main.py se guardan tres libros y tres revistas en una sola lista llamada materiales. Al recorrerla con un for, se llama a material.mostrar_informacion() y material.calcular_dias_prestamo() sin verificar si el objeto es un libro o una revista. Python decide en tiempo de ejecución qué versión del método ejecutar:
Si el objeto es un Libro, se muestra el autor y los días de préstamo son 7.
Si el objeto es una Revista, se muestra el número de edición y los días de préstamo son 3.

Función de HTML, CSS y JavaScript
HTML (index.html): define la estructura de la página. Contiene el título del sistema ("Biblioteca Universitaria"), el encabezado "Catálogo de materiales" y cuatro tarjetas (div con clase material): dos libros (El Principito, Harry Potter) y dos revistas (National Geographic, Ciencia Hoy). Cada tarjeta muestra el título, el tipo, la disponibilidad y un botón "Solicitar préstamo".
CSS (styles.css): controla la presentación. Centra los títulos, organiza las tarjetas en una fila con display: flex (con flex-wrap para que bajen de línea si no caben), les da un ancho fijo, fondo gris, bordes redondeados y espacio entre ellas. También da estilo a los botones (color verde y un color más oscuro al pasar el cursor).

JavaScript (script.js): agrega la interacción. La función prestar(material) se ejecuta cuando el usuario presiona un botón (onclick) y muestra una ventana con el mensaje "Has seleccionado: " seguido del nombre del material elegido.

Responsabilidades de frontend y backend

Frontend (lo que ocurre en el navegador del usuario):
Mostrar el catálogo y aplicar el diseño visual (HTML y CSS).
Detectar las acciones del usuario, como presionar el botón "Solicitar préstamo".
Mostrar mensajes al usuario (la ventana con el material seleccionado).

Backend (lo que haría el servidor en una aplicación real):
Guardar el catálogo de materiales en una base de datos.
Verificar que el material realmente esté disponible al momento del préstamo.
Registrar el préstamo y actualizar la disponibilidad del material.
Calcular la fecha de devolución según el tipo de material (7 días o 3 días).
Enviar la respuesta al frontend, que la mostrará al usuario.

Flujo general: el usuario presiona el botón de préstamo → el frontend envía la petición al backend con el código del material → el backend valida, registra el préstamo y responde → el frontend muestra el resultado al usuario.


## Documentación del Proyecto
- [Diagrama de Clases](docs/diagrama-clases.jpg)
- [Modelo de Base de Datos](docs/modelo-base-datos.jpg)
- [Descripción de Clases Principales](docs/clases-principales.md 