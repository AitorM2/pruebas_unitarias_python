import pytest
from cine import Pelicula

pelicula1 = Pelicula("Bridget Jones: Loca por él", 100, 8)
pelicula2 = Pelicula("Captain America: Brave New World", 50, 10)
pelicula3 = Pelicula("Paddington in Peru", 75, 9)

def test_vender_entradas_con_suficientes_asientos():
    resultado = pelicula1.vender_entradas(3)
    assert resultado == "Has comprado 3 entradas para Bridget Jones: Loca por él. Total: $24"
    assert pelicula1.asientos_disponibles == 97

def test_vender_entradas_sin_suficientes_asientos():
    resultado = pelicula2.vender_entradas(60)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 50 asientos."
    assert pelicula2.asientos_disponibles == 50

def test_vender_entradas_con_cero_o_cantidad_negativa():
    resultado_0 = pelicula3.vender_entradas(0)
    assert resultado_0 == "Error: La cantidad de entradas debe ser mayor a cero."
    
    resultado_negativo = pelicula3.vender_entradas(-5)
    assert resultado_negativo == "Error: La cantidad de entradas debe ser mayor a cero."

if __name__ == "__main__":
    pytest.main()
