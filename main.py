"""
Projet TP1 | Compter le nombre mots dans une phrase
Nom: Noah Chamoiseau
Groupe: 4567
"""

def count_word(text):
    nb_mots = len(text.split())
    return nb_mots

word_count = count_word(input("Écrivez une phrase pour compter le nombre de mots: "))
print(f"Le nombre de mots dans la phrase est {word_count}")
