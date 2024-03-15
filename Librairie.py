class Librairie:
    def __init__(self, nom, adresse) :
        self.nom = nom
        self.adresse = adresse
        self.livre = []

    def ajouterLivre(self, livre):
        self.livre.append(livre)

    def get_nom(self):
        return self.nom

    def get_adresse(self):
        return self.adresse

    def get_livre(self):
        return self.livre

    def set_nom(self, nom):
        self.nom = nom

    def set_adresse(self, adresse):
        self.adresse = adresse
    
    def set_livres(self, livre):
        self.livre = livre

    def supprimer_livre(self, livre):
        if livre in self.livre:
            self.livre.remove(livre) 
        else:
            print("Ce livre n'est pas dans la librairie.")
