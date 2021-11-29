import unittest
from INMUEBLES.inmuebles import consultar_inmuebles


class test_inmuebles(unittest.TestCase):

    def test_retornar_todos_los_datos(self):
        var = consultar_inmuebles()
        self.assertIsInstance(var, dict)

    def test_filtro_year_return_empty(self):
        var = consultar_inmuebles(2022)
        self.assertEqual(var["data"], [])

    def test_filtro_year_return_with_data(self):
        var = consultar_inmuebles(2011)
        self.assertNotEqual(var["data"], [])

    def test_filtro_year_city_return_empty(self):
        var = consultar_inmuebles(2011, 'caqueta')
        self.assertEqual(var["data"], [])

    def test_filtro_year_city_return_with_data(self):
        var = consultar_inmuebles(2011, 'medellin')
        self.assertNotEqual(var["data"], [])

    def test_filtro_year_city_state_return_empty(self):
        var = consultar_inmuebles(2011, 'medellin', 5)
        self.assertEqual(var["data"], [])

    def test_filtro_year_city_state_return_with_data(self):
        var = consultar_inmuebles(2011, 'medellin', 3)
        self.assertNotEqual(var["data"], [])


if __name__ == "__main__":
    unittest.main()
