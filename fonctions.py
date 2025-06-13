def additionner(a, b):
    """Retourne la somme de a et b."""
    return a + b

def est_pair(n):
    """Retourne True si n est pair, sinon False."""
    return n % 2 == 0

def valider_email(email):
    """Valide un email basique."""
    if "@" not in email:
        return False
    if "." not in email:
        return False
    return True

def calculer_moyenne(notes):
    """Retourne la moyenne des notes dans la liste."""
    if len(notes) == 0:
        return 0
    return sum(notes) / len(notes)

def convertir_temperature(celsius):
    """Convertit une température de Celsius à Fahrenheit."""
    return (celsius * 9/5) + 32

def diviser(a, b):
    """Retourne le résultat de la division de a par b."""
    if b == 0:
        raise ValueError("Division par zéro n'est pas permise.")
    return a / b

def mot_de_passe(password):
    """Valide un mot de passe basique avec exceptions."""
    if len(password) < 8:
        raise ValueError("Le mot de passe doit contenir au moins 8 caractères.")
    if not any(char.isdigit() for char in password):
        raise ValueError("Le mot de passe doit contenir au moins un chiffre.")
    if not any(char.isalpha() for char in password):
        raise ValueError("Le mot de passe doit contenir au moins une lettre.")
    return True