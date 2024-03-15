def carre(nombre):
    return nombre ** 2

def exposant(nombre):
    exposant = int(input("Entrez l'exposant : "))
    return nombre ** exposant

def factoriel(nombre):
    fact = 1
    for i in range(1, nombre + 1):
        fact *= i
    return fact

def afficher_menu():
    print("1. Calculer le carré du nombre")
    print("2. Calculer l'exposant du nombre")
    print("3. Calculer le factoriel du nombre")
    print("4. Quitter")

nombre = int(input("Entrez un nombre : "))
continuer = True

while continuer:
    afficher_menu()
    choix = input("Choisissez une option : ")

    if choix == '1':
        print("Le carré de", nombre, "est", carre(nombre))
    elif choix == '2':
        print("Le nombre", nombre, "élevé à la puissance de l'exposant est", exposant(nombre))
    elif choix == '3':
        print("Le factoriel de", nombre, "est", factoriel(nombre))
    elif choix == '4':
        print("Au revoir !")
        continuer = False
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")