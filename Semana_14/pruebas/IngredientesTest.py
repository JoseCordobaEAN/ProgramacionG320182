import unittest
import Semana_14.clases.Ingrediente as i

class TestIngrediente(unittest.TestCase):

    def test_rep(self):
        sandia = i.Ingrediente("Sandia", "Dulce", 100)
        self.assertEqual('Sandia Dulce por 100', sandia.__repr__())


    def test_picar(self):
        sandia = i.Ingrediente("Sandia", "Dulce", 100)
        self.assertEqual(False, sandia.procesado)
        sandia.picar()
        self.assertEqual(sandia.cantidad, 80.0)
        self.assertEqual(True, sandia.procesado)


    def test_eq(self):
        sandia = i.Ingrediente("Sandia", "Dulce", 100)
        sandia2 = i.Ingrediente("Sandia", "Dulce", 100)
        self.assertEqual(True, sandia == sandia2)
        gengibre = i.Ingrediente("Gengibre", "Picante", 10)
        self.assertFalse(sandia == gengibre)
