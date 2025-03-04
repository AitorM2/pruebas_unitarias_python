import pytest
from biblioteca import Libro, Biblioteca

@pytest.fixture
def biblioteca():
    return Biblioteca()

@pytest.fixture
def libro_ejemplo():
    return Libro("El Principito", "Antoine de Saint-Exupéry", 1943)

@pytest.fixture
def libro_no_disponible():
    libro = Libro("1984", "George Orwell", 1949)
    libro.prestado = True
    return libro

def test_crear_libro(libro_ejemplo):
    assert libro_ejemplo.titulo == "El Principito"
    assert libro_ejemplo.autor == "Antoine de Saint-Exupéry"
    assert libro_ejemplo.anio == 1943
    assert libro_ejemplo.prestado == False

def test_libro_disponible(libro_ejemplo):
    assert str(libro_ejemplo) == "El Principito de Antoine de Saint-Exupéry (1943) - disponible"

def test_libro_prestado(libro_no_disponible):
    assert str(libro_no_disponible) == "1984 de George Orwell (1949) - prestado"

def test_agregar_libro(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0] == libro_ejemplo

def test_eliminar_libro(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    biblioteca.eliminar_libro("El Principito")
    assert len(biblioteca.libros) == 0

def test_eliminar_libro_inexistente(biblioteca):
    biblioteca.eliminar_libro("Libro Inexistente")
    assert len(biblioteca.libros) == 0

def test_buscar_libro_existente(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    libro_encontrado = biblioteca.buscar_libro("El Principito")
    assert libro_encontrado == libro_ejemplo

def test_buscar_libro_inexistente(biblioteca):
    libro_encontrado = biblioteca.buscar_libro("Libro Inexistente")
    assert libro_encontrado is None

def test_listar_libros(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    libros_listados = biblioteca.listar_libros()
    assert len(libros_listados) == 1
    assert libros_listados[0] == "El Principito de Antoine de Saint-Exupéry (1943) - disponible"

def test_prestar_libro(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    mensaje = biblioteca.prestar_libro("El Principito")
    assert mensaje == "Has pedido prestado el libro 'El Principito'."
    assert libro_ejemplo.prestado == True

def test_prestar_libro_ya_prestado(biblioteca, libro_no_disponible):
    mensaje = biblioteca.prestar_libro("1984")
    assert mensaje == "El libro '1984' ya está prestado."

def test_prestar_libro_inexistente(biblioteca):
    mensaje = biblioteca.prestar_libro("Libro Inexistente")
    assert mensaje == "El libro 'Libro Inexistente' no se encuentra en la biblioteca."

def test_devolver_libro(biblioteca, libro_no_disponible):
    biblioteca.agregar_libro(libro_no_disponible)
    mensaje = biblioteca.devolver_libro("1984")
    assert mensaje == "Has devuelto el libro '1984'."
    assert libro_no_disponible.prestado == False

def test_devolver_libro_no_prestado(biblioteca, libro_ejemplo):
    biblioteca.agregar_libro(libro_ejemplo)
    mensaje = biblioteca.devolver_libro("El Principito")
    assert mensaje == "El libro 'El Principito' no estaba prestado."

def test_devolver_libro_inexistente(biblioteca):
    mensaje = biblioteca.devolver_libro("Libro Inexistente")
    assert mensaje == "El libro 'Libro Inexistente' no se encuentra en la biblioteca."
    
if __name__ == "__main__":
    pytest.main()
