from Librairie import *
from flask import Flask, request, jsonify

app = Flask(__name__)
 
@app.route("/nom")
def return_nom():
    return jsonify(Librairie.get_nom())

test = Librairie("Libre et riz", "1 place du truc")

# Ajouter des livres à la librairie
lelivre = str(input("Entrez un livre à ajouter: "))
test.ajouterLivre(lelivre)

# Afficher les livres de la librairie
livres = test.get_livre()
print("Livres dans la librairie:")
for livre in livres:
    print("-", livre)

# Ajouter des livres à la librairie
lelivre = str(input("Entrez un livre à supprimer : "))
test.supprimer_livre(lelivre)

# Afficher les livres de la librairie
livres = test.get_livre()
print("Livres dans la librairie:")
for livre in livres:
    print("-", livre)