import unittest

from fonctions import *

class TestFonctions(unittest.TestCase):

    # additionner
    def test_addition_cas_positif(self):
        resultat = additionner(2, 3)
        self.assertEqual(resultat, 5)

    def test_addition_cas_negatif(self):
        resultat = additionner(-2, -3)
        self.assertEqual(resultat, -5)

    def test_addition_cas_mixte(self):
        resultat = additionner(2, -3)
        self.assertEqual(resultat, -1)

    def test_addition_cas_zero(self):
        resultat = additionner(0, 0)
        self.assertEqual(resultat, 0)    

    # est pair
    def test_est_pair_cas_pair(self):
        self.assertTrue(est_pair(4))

    def test_est_pair_cas_impair(self):
        self.assertFalse(est_pair(5))

    def test_est_pair_cas_zero(self):
        self.assertTrue(est_pair(0))

    # email
    def test_valider_email_cas_valide(self):
        self.assertTrue(valider_email("test@example.com"))

    def test_valider_email_cas_invalide_sans_arobase(self):
        self.assertFalse(valider_email("testexample.com"))
        
    def test_valider_email_cas_invalide_sans_point(self):
        self.assertFalse(valider_email("test@examplecom"))

    # moyenne
    def test_calculer_moyenne_liste_normale(self):
        notes = [10, 15, 20]
        self.assertEqual(calculer_moyenne(notes), 15)

    def test_calculer_moyenne_liste_vide(self):
        notes = []
        self.assertEqual(calculer_moyenne(notes), 0)

    def test_calculer_moyenne_une_note(self):
        notes = [18]
        self.assertEqual(calculer_moyenne(notes), 18)

    # conversion temperature
    def test_convertir_temperature_zero(self):
        self.assertEqual(convertir_temperature(0), 32)

    def test_convertir_temperature_eau_bouillante(self):
        self.assertEqual(convertir_temperature(100), 212)
