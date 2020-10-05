from app import app
from flask import render_template, redirect
from flask import url_for, request
from my_code import dico


@app.route('/')
def liste_taches():
    return render_template("list_tache.html", dico=dico.items(), taille=len(dico))


@app.route('/ajout_tache', methods=['POST'])
def ajout_tache():
    if request.method == 'POST':
        titre = request.form['titre']
        desc = request.form['desc']
        dico[titre] = desc
        return render_template("list_tache.html", dico=dico.items(), taille=len(dico))
    else:
        return render_template("list_tache.html", dico=dico.items(), taille=len(dico))


@app.route('/form_tache')
def form_tache():
    return render_template('form_tache.html')


@app.route('/tache/<string:titre>')
def tache(titre):
    desc = dico[titre]
    return render_template('tache.html', titre=titre, desc=desc)

@app.route('/supprimer/<string:titre>')
def supp(titre):
    del dico[titre]
    return render_template("list_tache.html", dico=dico.items(), taille=len(dico))
