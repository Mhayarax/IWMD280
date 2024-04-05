from Librairie import *
from flask import Flask, request, jsonify

app = Flask(__name__)
 
@app.route("/nom")
def return_nom():
    return jsonify(test.get_nom())

test = Librairie("Libre et Riz","1 place de l'endroit")
test.ajouterLivre("Le guide du zizi sexuel")
test.ajouterLivre("Minecraft le livre")
test.ajouterLivre("La Bible")
 
@app.route('/librairie', methods=['GET'])
def afficher_librairie():
    librairie_info = {
        'nom': test.get_nom(),
        'adresse': test.get_adresse(),
        'livres': test.get_livre()
    }
    return jsonify(librairie_info)

@app.route('/ajout', methods=['GET'])
def ajouterLivre():
    librairie_info = {
        'nom': "test",
    }
    return jsonify(librairie_info)

@app.route('/librairie/livre', methods=['POST'])
def ajouter_livre():
    livre = request.json.get('livre')
    test.ajouter_livre(livre)
    return "Livre ajouté avec succès", 201

@app.route('/librairie/livre', methods=['DELETE'])
def supprimer_livre():
    livre = request.json.get('livre')
    if test.supprimer_livre(livre):
        return "Livre supprimé avec succès", 200
    else:
        return "Livre non trouvé dans la librairie", 404

if __name__ == '__main__':
    app.run(debug=True)