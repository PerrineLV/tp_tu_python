import unittest

from fonctions import *

class TestFonctions(unittest.TestCase):

    def test_addition_cas_positif(self):
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_addition_cas_negatif(self):
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)

    def test_addition_cas_zero(self):
        resultat = additionner(0, 0)
        self.assertEqual(resultat, 0)    