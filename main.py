#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Appel des différentes routes des frameworks
from flask import Flask, render_template, url_for, redirect
from flask import session, current_app, g, send_file,send_from_directory, request
from flask_mail import Mail, Message
from flask.cli import with_appcontext

from forms import RegisterForm, NewLoginForm, NewClassGenerator
from forms import ForgottenPassword, ModifierClassGenerator, FormDataBanking
from forms import FormChangUserName, FormChangUserEmail , FormChangUserPassword, FormChangUserProfilImg
from config import Config

from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

import sqlite3 as sql
import base64
import os
import sys

from datetime import datetime

#Configuration du serveur
app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = b'_\xd0\xe3`\x90nI\x0f`5?\x0b\xca\\\x14\xb8'

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Leo12sgAAAAAHp16Z2E4Vl7V58_1obEI_jCNLDT'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Leo12sgAAAAABV0BZlccst1gsHepAiWWknAsqyr'
app.config['RECAPTCHA_OPTION'] = {
    'theme': 'custom'
}

db_name = 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)

#Definition pour les images de la DataBase
def convert_pic():
    filename = "profile.jpg"
    with open(filename, 'rb') as file:       
        photo = file.read()
    return photo    

#Génération des classes pour la communication avec la database
class user(db.Model): 
    idUsers = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Integer)
    vip_account = db.Column(db.Integer)
    nb_classe_Faite = db.Column(db.Integer)
    image_profil = db.Column(db.LargeBinary)
    idgroupe = db.Column(db.Integer, db.ForeignKey('groupe.idGroupe'))

    def __repr__(self):
        return '<User %r>' % self.name

class user_banni(db.Model): 
    idUsers = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Integer)
    vip_account = db.Column(db.Integer)
    nb_classe_Faite = db.Column(db.Integer)
    image_profil = db.Column(db.LargeBinary)
    cause = db.Column(db.Text)
    idgroupe = db.Column(db.Integer, db.ForeignKey('groupe.idGroupe'))

    def __repr__(self):
        return '<User %r>' % self.name

class groupe(db.Model): 
    idGroupe = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    valeur = db.Column(db.Integer)

    def __repr__(self):
        return '<User %r>' % self.name

class classe(db.Model):
    idClasse = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    classe_mere = db.Column(db.Text)
    Protect_head = db.Column(db.Integer)
    Generat_head_default_construct = db.Column(db.Integer)
    Generat_head_destruct = db.Column(db.Integer)
    auteur = db.Column(db.Text)
    creation_data = db.Column(db.DateTime)
    class_role = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))

    def __repr__(self):
        return '<User %r>' % self.name


class classemodel(db.Model):
    idClasse = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    classe_mere = db.Column(db.Text)
    Protect_head = db.Column(db.Integer)
    Generat_head_default_construct = db.Column(db.Integer)
    Generat_head_destruct = db.Column(db.Integer)
    auteur = db.Column(db.Text)
    creation_data = db.Column(db.DateTime)
    class_role = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))

    def __repr__(self):
        return '<User %r>' % self.name

class creation_connexion_classmodel_user(db.Model):
    idTableConnexion = db.Column(db.Integer, primary_key=True, unique=True)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))
    idClasse = db.Column(db.Integer, db.ForeignKey('classemodel.idClasse'))
    connexion = db.Column(db.Integer)
    
    def __repr__(self):
        return '<User %r>' % self.idTableConnexion

class notifications(db.Model):
    idNotif = db.Column(db.Integer, primary_key=True, unique=True)
    typeNotif = db.Column(db.Text)
    Commentaire = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))

    def __repr__(self):
        return '<User %r>' % self.typeNotif

mail = Mail(app)

#-----------------------------------------
#--------Route retour mail new user-------
#-----------------------------------------
@app.route('/validation/<string:name_user>/<string:email_user>/<string:password_user>')
def validation(name_user, email_user, password_user):
    #envoie des donnée sur la DataBase
    int_password = int(password_user)
    #Connection à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    photo = convert_pic()
    users = []
    users.append((name_user, email_user, int_password, 0, photo, 4))
    cursor.executemany("""INSERT INTO user(name, email, password, vip_account, image_profil, idgroupe) VALUES(?, ?, ?, ?, ?, ?)""", users)
    cursor.execute("""SELECT idUsers FROM user 
        WHERE user.email =?""",(email_user,))
    idClient = cursor.fetchall()
    notif = []
    notif.append(("Général", "La création de votre compte à bien été enregistrer!!!", idClient[0][0]))
    cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
        VALUES(?, ?, ?)""", notif)
    cursor.execute("""SELECT COUNT(*) from classemodel""")
    nbclassemodel = cursor.fetchall()
    connexion = []
    #Création de la connexion entre les classe model et le nouvel utilisateur
    for i in range(nbclassemodel[0][0]):
        connexion.append((idClient[0][0], i))
    cursor.executemany("""INSERT INTO connexionclassuser VALUES (?, ?)""", connexion)

    #Execution des script dans la database
    conn.commit()
    #Fermeture de la database
    conn.close()
    #retour vers la page d'accueil
    return redirect(url_for('index'))

#-----------------------------------------
#----------Route gestion Login------------
#-----------------------------------------
#Route page de loginpour valider un nouvel utilisateur
@app.route('/', methods=['get', 'post'])
def index():	
    form_new = NewLoginForm()
    form_login = RegisterForm()
    if form_new.validate_on_submit():
        #Envoie d'un mail de validation
        conn =sql.connect('database.db')
        cursor = conn.cursor()
        name_user = form_new.name.data
        email_user = form_new.email.data
        password = form_new.password.data
        cursor.execute("""SELECT email, password FROM user WHERE user.email=? """, (email_user,))
        rows = cursor.fetchall()
        if rows == []:
            msg = Message('Confirmation de création de compte sur MMOGC -- Générateur de classe', 
                          recipients=[email_user])
            msg.body = "Bonjour Mr " + name_user + " Votre demande a été prise en compte.cliquer sur le lien suivant pour valider la création de votre compte : <a href='http://127.0.0.1:5000/validation/"+ name_user + "/" + email_user + "/" + password +  "'>Valider la connexion</a>"
            msg.html = "Bonjour Mr <b>" + name_user + "</b> <br /> Votre demande a été prise en compte.<br /> cliquer sur le lien suivant pour valider la création de votre compte : <br /><a href='http://127.0.0.1:5000/validation/"+ name_user + "/" + email_user + "/" + password + "'>Valider la connexion</a>"
            mail.send(msg)
            #Retour page de connexion
            return redirect(url_for('index'))
        elif rows!= []:
            print("Compte déja existant")
            #Message Flash 'Compte deja existant sur ce mail'
    return render_template("index.html", register_form = form_new, login_form = form_login)


#Route pour le login d'un utilisateur
@app.route('/login', methods=['get', 'post'])
def login():
    #Formulaire
    form_new = NewLoginForm()
    form_login = RegisterForm()
    if form_login.validate_on_submit():
        #Vérificartion dans la DataBase
        conn = sql.connect('database.db')
        cursor = conn.cursor()
        email = form_login.email.data
        mdp = form_login.password.data
        int_mdp = int(mdp)
        userlog = (email, int_mdp)
        #Récupération de l'identifiant correspondant a la demande
        cursor.execute("""SELECT  email, password, name, idGroupe, vip_account, idUsers FROM user 
            WHERE user.email=? """, (email,))
        conn.commit()
        rows = cursor.fetchall()
        #Creation d'une vue d'envoie de l'IDGroup de la personne
        cursor.execute("""DROP VIEW IF EXISTS Personne""")
        cursor.execute("CREATE VIEW Personne AS SELECT  email, password, name, idGroupe, vip_account, idUsers FROM user WHERE user.email='" + email + "'")  
        conn.commit()
        if (int_mdp == rows[0][1]):
            #Récupération de l'IDGroup de la personne
            cursor.execute("""SELECT groupe.valeur from Personne, groupe 
                WHERE Personne.idgroupe = groupe.idGroupe""")
            conn.commit()
            rows2 = cursor.fetchall()
            #Génération des logs de la sessions utilisateur
            session['user'] = {
                'username' : rows[0][2],
                'email' : email,
                'idGroup' : rows2[0][0],
                'vip_account': rows[0][4],
                'idUser' : rows[0][5]
                }
            #Ronvoie vers la page d'acceuil
            return redirect(url_for("acceuil"))
        else:
            #Sinon retour a la page de connexion
            return render_template("index.html", register_form = form_new, login_form = form_login)
        conn.close()

    
#Route pour le logout d'un utilisateur
@app.route('/logout')
def logout():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Destruction de la vue de gestion de l'IDGroup
    cursor.execute("""DROP VIEW IF EXISTS Personne""")
    conn.close()
    #Nétoyage de la session utilisateur
    session['user'].clear
    #Message flash Déconnexion  bien effecter
    return redirect(url_for('index'))

#Route pour accéder a la page d'oublie du mot de passe
@app.route('/forgottenpassword')
def forgotten_password():
    #Formulaire 
    form_password = ForgottenPassword()
    #Renvoie de la page 
    if form_password.validate_on_submit():
        email = form_password.email.data
        conn = sql.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * from user""")
        #Fermeture de la database
        conn.close()
    return render_template("changpassword.html", 
                            form_forgottenpassword = form_password)


#-----------------------------------------
#-----Gestion Utilisateur Connecter-------
#-----------------------------------------
#Route d'affichage de la page Utilisateur
@app.route('/user',  methods=['get', 'post'])
def user():
    #Formulaire
    form_User_name = FormChangUserName()
    form_User_mail = FormChangUserEmail()
    form_User_password = FormChangUserPassword()
    form_User_profil_img = FormChangUserProfilImg()
    #connexion à la DataBase
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération de toute les classes faites par l'utilisateur
    cursor.execute("""SELECT * from classe
        WHERE classe.idUser=?""",(session['user']['idUser'],))
    myclasse = cursor.fetchall()
    cursor.execute("""DROP VIEW IF EXISTS MaClasse""")
    cursor.execute("CREATE VIEW MaClasse AS SELECT * from classe WHERE classe.idUser=" + str(session['user']['idUser']))

    # Faire la requête pour donner la date de la dernière classe créer et de la première classe créer
    cursor.execute("""DROP VIEW IF EXISTS lastClasse""")
    cursor.execute("CREATE VIEW lastClasse AS SELECT name, classe_mere, Protect_head, Generat_head_default_construct, Generat_head_destruct, auteur, MAX(creation_data), class_role FROM MaClasse")
    cursor.execute("""SELECT name, classe_mere, Protect_head, Generat_head_default_construct, 
        Generat_head_destruct, auteur, MAX(creation_data), class_role FROM MaClasse""")
    dernière_classe = cursor.fetchall()

    cursor.execute("""DROP VIEW IF EXISTS firstClasse""")
    cursor.execute("CREATE VIEW firstClasse AS SELECT name, classe_mere, Protect_head, Generat_head_default_construct, Generat_head_destruct, auteur, MIN(creation_data), class_role FROM MaClasse")
    cursor.execute("""SELECT name, classe_mere, Protect_head, Generat_head_default_construct, 
        Generat_head_destruct, auteur, MIN(creation_data), class_role FROM MaClasse""")
    première_classe = cursor.fetchall()

    cursor.execute("""SELECT * from user 
        WHERE user.idUsers =?""",(session['user']['idUser'],))
    profil = cursor.fetchall()

    #Récupération de l'image de profil de l'utilisateur
    cursor.execute("""SELECT image_profil from user
        WHERE user.idUsers =?""",(session['user']['idUser'],))
    img = cursor.fetchall()
    image  = base64.b64encode(img[0][0])
    data = image.decode("UTF-8")
    #faire la requete pour savoir le nombre de classe faire au total
    #Donner le nombre classe possible que l'utilisateur peut créer
    conn.commit()
    conn.close()
    return render_template('user.html',
                           firts_classe = première_classe,
                           last_classe = dernière_classe,
                           myclasse = myclasse, 
                           profil = profil, image_profil = data,
                           form_user = form_User_name, form_mail = form_User_mail, 
                           form_pwd = form_User_password, form_img = form_User_profil_img,
                           idGroup = session['user']['idGroup'], idUser = session['user']['idUser'])

@app.route('/replacename/<int:idUser>', methods=['get', 'post'])
def replacename(idUser):
    #Formulaire
    form_User_name = FormChangUserName()
    form_User_mail = FormChangUserEmail()
    form_User_password = FormChangUserPassword()
    form_User_profil_img = FormChangUserProfilImg()
    #Connexion à la DataBase
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération du nouveau nom données par l'utilisateur
    name = form_User_name.name.data

    #Envoye du nom dans la DataBase
    conn.execute("""UPDATE user 
        SET name=? WHERE user.idUsers=?""", (name, idUser))
    conn.commit()

    #Fermeture de la connexion a la DataBase
    conn.close()
    return redirect(url_for('user'))

@app.route('/replacemail/<int:idUser>', methods=['get','post'])
def replacemail(idUser):
    #Formulaire
    form_User_name = FormChangUserName()
    form_User_mail = FormChangUserEmail()
    form_User_password = FormChangUserPassword()
    form_User_profil_img = FormChangUserProfilImg()
    #Connexion à la DataBase
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération du nouveau email données par l'utilisateur
    email = form_User_mail.name.data
    #Envoye de l'email dans la DataBase
    conn.execute("""UPDATE user 
        SET email=? WHERE user.idUsers=?""", (email, idUser))
    conn.commit()
    #Fermeture de la connexion a la DataBase
    conn.close()
    return redirect(url_for('user'))

@app.route('/replacepassword/<int:idUser>', methods=['get','post'])
def replacepassword(idUser):
    #Formulaire
    form_User_name = FormChangUserName()
    form_User_mail = FormChangUserEmail()
    form_User_password = FormChangUserPassword()
    form_User_profil_img = FormChangUserProfilImg()
    #Connexion à la DataBase
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération du nouveau nom données par l'utilisateur
    password = form_User_password.name.data
    #Envoye du password dans la DataBase
    conn.execute("""UPDATE user 
        SET password=? WHERE user.idUsers=?""", (password, idUser))
    conn.commit()
    #Fermeture de la connexion a la DataBase
    conn.close()
    return redirect(url_for('user'))

@app.route('/replaceimage/<int:idUser>', methods=['get','post'])
def replaceimage(idUser):
    #Formulaire
    form_User_name = FormChangUserName()
    form_User_mail = FormChangUserEmail()
    form_User_password = FormChangUserPassword()
    form_User_profil_img = FormChangUserProfilImg()
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération de la nouvelle image par l'utilisateur

    pic = request.files['Image']
    image = pic.read()

    #Envoye de l'image de profil dans la database
    conn.execute("""UPDATE user
        SET image_profil=? WHERE user.idUsers=?""", (image, idUser))
    conn.commit()
    #Fermeture de la connexion à la database
    conn.close()
    return redirect(url_for('user'))

#-----------------------------------------
#----------Téléchargement des fichiers----
#-----------------------------------------
#Route pour le fichier HPP
@app.route('/download_file_h')
def download_file_h():
    path = "h.txt"
    return send_file(path, as_attachment=True, download_name = "head.h")

#Route pour le fichier CPP    
@app.route('/download_file_cpp')
def download_file_cpp():
    path = "cpp.txt"
    return send_file(path, as_attachment=True, download_name = "main.cpp")

#-----------------------------------------
#----------Route access page--------------
#-----------------------------------------
##PAGE D'ACCEUIL##
#Route pour accéder a la page d'accueil
@app.route('/acceuil')
def acceuil():
    conn = sql.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM classe
        WHERE classe.idUser=?""",(session['user']['idUser'],))
    rows = cursor.fetchall()

    #Fermeture de la database
    conn.close()
    return render_template("acceuil.html", 
                           classe_liste = rows, idGroup = session['user']['idGroup'])

#Bouton de modification de la classe
@app.route('/modification/<int:idClass>', methods=['get', 'post'])
def modification(idClass):
    #Connexion a la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Recherche de la classe a modifier
    cursor.execute("""SELECT * FROM classe
        WHERE classe.idClasse = ?""",(idClass,))
    #Envoie des données a afficher
    class_modif = cursor.fetchall()
    #Fermeture de la connexion
    conn.close()

    #Formulaire
    form_generateur = ModifierClassGenerator()  
    return render_template("Modifieur.html", 
                           form_classe = form_generateur, donnees = class_modif, idClass = idClass,
                           idGroup = session['user']['idGroup'])


#gestion de la modification
@app.route('/modification/modifier/<int:idClass>', methods=['get', 'post'])
def modifier(idClass):
    #Connexion a la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT name from classe 
        WHERE idClasse =?
        """,(idClass,))
    nom = cursor.fetchall()
    form_modifieur = ModifierClassGenerator()
    if request.method == 'POST':
        #Modification de la classe
        name = request.form['name']
        classe_mere = request.form['class_mere']
        Protect_head = request.form.get('Protect_head')
        default_constructeur = request.form.get('Generat_head_default_construct')
        head_destructeur = request.form.get('Generat_head_destruct')
        auteur = request.form['auteur']
        commentaire = request.form['class_role']
        list_classe_modifier = []
        list_classe_modifier.append((name, classe_mere, Protect_head,
                            default_constructeur, head_destructeur, auteur, commentaire, idClass))
        cursor.executemany("""UPDATE classe
            SET name =?, classe_mere =?, Protect_head =?, Generat_head_default_construct =?, 
            Generat_head_destruct =?, auteur =?, creation_data =DATETIME(), class_role =?
            WHERE idClasse =?""", list_classe_modifier)

        #Création de la notifaction de la modification de la database
        notif = []
        texte = "La classe " + nom[0][0] + " a été modfier et à été renommé en : " + name + "."
        notif.append(("Classe", texte, session['user']['idUser']))
        cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
                VALUES(?, ?, ?)""", notif)
        conn.commit()
        conn.close()
        return redirect(url_for('acceuil'))

#bouton de suppression de la classe
@app.route('/supprimer/<int:idClass>')
def supprimer(idClass):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT name from classe 
        WHERE idClasse =?
        """,(idClass,))
    nom = cursor.fetchall()
    #Suppression de la ligne de la table
    cursor.execute("""DELETE FROM classe WHERE idClasse =?""",(idClass,))
    notif = []
    texte = "La classe " + nom[0][0] + " a été supprimer"
    notif.append(("Classe", texte, session['user']['idUser']))
    cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
                VALUES(?, ?, ?)""", notif)

    #Enlevez 1 dans la table de l'utilisateur
    cursor.execute("""SELECT nb_classe_Faite From user
        WHERE user.name =?""",(session['user']['username'],))
    validation = cursor.fetchall()
    nbclasse = validation[0][0] - 1
    cursor.execute("""UPDATE user SET nb_classe_Faite =? WHERE user.name=?""", 
                   (nbclasse,session['user']['username'])) 
    #Fermeture de la connexion
    conn.commit()
    conn.close()
    return redirect(url_for('acceuil'))

#bouton de génération du .h
@app.route('/genererh/<int:idClass>')
def genererh(idClass):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Demande de la classe a générer
    cursor.execute("""SELECT * FROM classe 
        WHERE classe.idClasse=?""",(idClass,))
    #Envoie de la données dans une varaible qui va traiter et écrire dans le fichier txt
    donnees = cursor.fetchall()   
    #Génération des données a écrire dans le fichier
    Protect_head = "#ifndef " + str(donnees[0][1])
    definition = "#define " + str(donnees[0][1])
    string = "#include <string>"
    name = "class " + donnees[0][1]
    ouverture = "{"
    public = "     public:"
    exemple_classe = "     void exemple();"
    private = "     private:"
    exemple_var = "     int exemple"
    fermeture = "};"
    fin = "#endif"
    #Ecriture du fichier
    file = open("h.txt", "w")
    file.write("%s \n%s \n\n%s \n\n%s \n%s \n%s \n\n%s \n\n%s \n\n%s \n%s \n%s" % 
               (Protect_head, definition, string, 
                name, ouverture, public, exemple_classe, 
                private, exemple_var, fermeture, fin)) 
    file.close()
    #Génération du fichier .h
    path = "h.txt"
    name = donnees[0][1] + ".hpp"
    #Fermeture de la database
    conn.close()
    return send_file(path, as_attachment=True, download_name = name)

#bouton de génération du .cpp
@app.route('/generercpp/<int:idClass>')
def generercpp(idClass):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Demande de la classe à générer
    cursor.execute("""SELECT * FROM classe 
        WHERE classe.idClasse=?""",(idClass,))
    #Envoie de la données dans une classe qui va traitENDIFer et écrire dans le fichier txt
    donnees2 = cursor.fetchall()
    #Génération des données à écrire dans le fichier
    tete = "#include"
    tete_name = '"' + donnees2[0][1] +'.hpp"'
    sous_tete = "#include <string>"
    sous_tete2 = "#include <iostream>"
    type = "using namespace std;"

    name = "void " + donnees2[0][1] + "::exemple()"
    ouverture = "{"
    fermeture = "}"

    #Ecriture du fichier
    file = open('cpp.txt', "w")
    file.write("%s %s \n%s \n%s \n\n%s \n\n%s \n%s \n\n%s" % 
               (tete, tete_name, sous_tete, sous_tete2, type, 
                name, ouverture, fermeture))
    file.close()
    #Gnération du fichier .cpp
    path = "cpp.txt"
    name = donnees2[0][1] + ".cpp"
    #Fermeture de la database
    conn.close()
    return send_file(path, as_attachment=True, download_name = name)


##NOTIFICATIONS##
#Route pour accéder a la page des Notification
@app.route('/notification')
def notification():
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupérations de tous les types de notification pour pouvoir les classer
    cursor.execute("""SELECT typeNotif from notifications
        GROUP BY notifications.typeNotif""")
    typenotif = cursor.fetchall()
    #Récupération des notifs de classe
    cursor.execute("""DROP VIEW IF EXISTS notifclasse""")
    cursor.execute("CREATE VIEW notifclasse AS SELECT * from notifications WHERE notifications.typeNotif =" + (typenotif[0][0]))
    cursor.execute("""SELECT * from notifications 
        WHERE notifications.typeNotif =? AND (notifications.idUser =? OR notifications.idUser =0)""", (typenotif[0][0], session['user']['idUser'],))
    notifclasse = cursor.fetchall()
    #Récupération des notifs général
    cursor.execute("""DROP VIEW IF EXISTS notifgene""")
    cursor.execute("CREATE VIEW notifgene AS SELECT * from notifications WHERE notifications.typeNotif =" + (typenotif[1][0]))
    cursor.execute("""SELECT * from notifications 
        WHERE notifications.typeNotif =?""", (typenotif[1][0],))
    notifgene = cursor.fetchall()
    #Récupération des notif d'informations
    cursor.execute("""DROP VIEW IF EXISTS notifinfo""")
    cursor.execute("CREATE VIEW notifinfo AS SELECT * from notifications WHERE notifications.typeNotif =" + (typenotif[2][0]))
    cursor.execute("""SELECT * from notifications 
        WHERE notifications.typeNotif =?""", (typenotif[2][0],))
    notifinfo = cursor.fetchall()
    #Récupération des données général et personnel des notifs
    cursor.execute("""SELECT * from notifications
        WHERE notifications.idUser = 0 or notifications.idUser =?""", (session['user']['idUser'],))
    notif = cursor.fetchall()
    #Fermeture de la database
    conn.commit()
    conn.close()
    return render_template("Notifications.html", 
                           donnees_notif = notif, 
                           typeofnotif = typenotif, 
                           general = notifgene, information = notifinfo, ofclasse = notifclasse,
                           idGroup = session['user']['idGroup'])


##GENERATEUR DE CLASSE##
#Route pour accéder a la page de generateur de classe    
@app.route('/generateur', methods=['get', 'post'])
def generateur():
    #Formulaire
    form_generateur = NewClassGenerator()  
    return render_template("Generateur.html", 
                           form_classe = form_generateur,
                           idGroup = session['user']['idGroup'])

@app.route('/generer', methods=['get', 'post'])
def generer():
    #Connexion a la database
    demande_valider = True
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Requète pour savoir le nombre de classe créer
    cursor.execute("""SELECT nb_classe_Faite From user
        WHERE user.name =?""",(session['user']['username'],))
    validation = cursor.fetchall()
    #Vérifiaction que la création est possible pour les deux niveaux de la boutique
    #Niveau Basic
    if (validation[0][0] >= 10 and session['user']['vip_account'] == 0):
        demande_valider = False
    #Niveau Classic
    if (validation[0][0] >= 50 and session['user']['vip_account'] == 1):
        demande_valider = False
    #Formulaire
    form_generer = NewClassGenerator()
    if request.method == 'POST':
        if (request.form['name'] != '' and demande_valider == True):
            name = request.form['name']
            classe_mere = request.form['class_mere']
            Protect_head = request.form.get('Protect_head')
            default_constructeur = request.form.get('Generat_head_default_construct')
            head_destructeur = request.form.get('Generat_head_destruct')
            auteur = request.form['auteur']
            commentaire = request.form['class_role']
            User = session['user']['idUser']
            list_classe = []
            list_classe.append((name, classe_mere, Protect_head,
                                default_constructeur, head_destructeur, auteur, commentaire, User))
            #Ecriture de la classe sur la base de données
            cursor.executemany("""INSERT INTO classe(name, classe_mere, Protect_head, Generat_head_default_construct, 
                Generat_head_destruct, auteur, creation_data, class_role, idUser) 
                VALUES(?, ?, ?, ?, ?, ?, DATETIME(), ?, ?)""", list_classe)  
            #Ajout d'une classe sur le compteur de l'utilisateur
            nbclasse = validation[0][0] + 1
            cursor.execute("""UPDATE user SET nb_classe_Faite =? WHERE user.name=?""", 
                           (nbclasse,session['user']['username']))        
            notif = []
            notif.append(("Classe", "Félicitation votre classe à été générer avec succés, aller à la page d'acceuil pour retrouver les détails de votre classe.", session['user']['idUser']))
            cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
                VALUES(?, ?, ?) """, notif)         
            conn.commit()
            conn.close()
    else:
        print("aucune demande de creation de classe")
    return redirect(url_for('generateur'))


##ZONE DE PAYEMENT##
#Route pour accéder a la page de la Boutique    
@app.route('/boutique')
def Boutique():
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération des classes générer par le serveur
    cursor.execute("""SELECT * from classemodel""")
    classe_can_be_like = cursor.fetchall()
    #Récupération des classes liké par l'utilisateur connecter
    cursor.execute("""SELECT * FROM connexionclassuser
        WHERE  iduser =?""", (session['user']['idUser'],))
    classe_like = cursor.fetchall()
    #fermeture de la connexion
    conn.close()
    #Renvoie de la page de la boutique
    return render_template("Boutique.html", 
                            classe_systeme = classe_can_be_like,
                            classe_like = classe_like,
                            vip_account = session['user']['vip_account'],
                            idGroup = session['user']['idGroup'])

#Route pour accéder a la zone de payement
@app.route('/payement/<float:prix>', methods=['get', 'post'])
def payement(prix):
    #Formulaire
    form_Banking = FormDataBanking()
    #Envoye de la page de payement
    return render_template("Payement.html", 
                           prix = prix, 
                           form_Banking = form_Banking,
                           idGroup = session['user']['idGroup'])

@app.route('/demandepayement/<float:prix>', methods=['get', 'post'])
def demandepayement(prix):
    #Formulaire
    form_Banking = FormDataBanking()
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Prise en compte du Payement
    if prix == 9.99:
        cursor.execute("""UPDATE user SET vip_account = '1' 
            WHERE idusers =?""", (session['user']['idUser'],))
    if prix == 49.99:
        cursor.execute("""UPDATE user SET vip_account = '2' 
            WHERE idusers =?""", (session['user']['idUser'],))
    conn.commit()
    conn.close()
    #retour vers la page de validation de payement
    return redirect(url_for('validation_payement'))

#Route de Retour de validation du payement
@app.route('/val_payement', methods=['get', 'post'])
def validation_payement():
    #Formulaire
    form_Banking = FormDataBanking()
    #Renvoie de la page de validation du payement
    return render_template("Validation_Payement.html", idGroup = session['user']['idGroup'])

#Route de like de classe
@app.route('/likeclasse/<int:idClasse>', methods=['get','post'])
def likeclasse(idClasse):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Affectation de la classe like dans la database
    donnees = []
    donnees.append((session['user']['idUser'], idClasse))
    cursor.executemany("""UPDATE connexionclassuser
        SET connexion = 1
        WHERE iduser =? and idclasse =?""", donnees)
    conn.commit()
    #Fermeture de la database
    conn.close()
    return redirect(url_for('Boutique'))

#Route de dislike de classe
@app.route('/dislikeclasse/<int:idClasse>', methods=['get','post'])
def dislikeclasse(idClasse):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Affectation de la classe like dans la database
    donnees = []
    donnees.append((session['user']['idUser'], idClasse))
    cursor.executemany("""UPDATE connexionclassuser
        SET connexion = 0
        WHERE iduser =? and idclasse =?""", donnees)
    conn.commit()
    #Fermeture de la database
    conn.close()
    return redirect(url_for('Boutique'))
#-----------------------------------------
#------Gestion des données sur le site----
#-----------------------------------------

@app.route('/gestiondata', methods=['get', 'post'])
def gestiondata():
    #Connexion a la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération de toute les classes créer par tous les utilisateurs
    cursor.execute("""SELECT * from classe""")
    classerequete = cursor.fetchall()
    #Récupération de tout les utilisateurs ayant validé leur compte sur ce site
    cursor.execute("""SELECT * from user""")
    userrequete = cursor.fetchall()
    #Récupération de la table des utilisateurs banni
    cursor.execute("""SELECT * from user_banni""")
    userbannirequete = cursor.fetchall()
    #Récupération de la moyenne du nombre de classe pour tous les utilisateurs
    cursor.execute("""DROP VIEW IF EXISTS moyenne_classe_all_user""")
    cursor.execute("CREATE VIEW moyenne_classe_all_user AS SELECT AVG(nb_classe_Faite) from user")
    cursor.execute("""SELECT AVG(nb_classe_Faite) from user""")
    moyenne_classe_all_user = cursor.fetchall()
    #Récupération du nombre d'itilisateurs suivant les différents type de compte proposé dans la boutique'
    cursor.execute("""DROP VIEW IF EXISTS nombre_type_compte""")
    cursor.execute("CREATE VIEW nombre_type_compte AS SELECT vip_account, COUNT(name) FROM user GROUP BY vip_account")
    cursor.execute("""SELECT vip_account, COUNT(name) FROM user
        GROUP BY vip_account""")
    nombre_type_compte = cursor.fetchall()

    #Fermeture de la connexion à la database
    conn.close()
    return render_template("GestionData.html",
                           allclasse = classerequete,
                           alluser = userrequete,
                           allbanuser = userbannirequete,
                           moyenne_classe_all_user = moyenne_classe_all_user,
                           nombre_type_compte = nombre_type_compte,
                           idUser = session['user']['idUser'],
                           idGroup = session['user']['idGroup'])

@app.route('/supprimeruser/<int:idUser>', methods=['get', 'post'])
def supprimeruser(idUser):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Suppression de l'utilisateur
    cursor.execute("""DELETE FROM user WHERE idUsers =?""",(idUser,))  
    cursor.execute("""DELETE FROM classe WHERE idUser =?""",(idUser,))
    cursor.execute("""DELETE FROM connexionclassuser  WHERE idUser =?""",(idUser,))
    cursor.execute("""DELETE FROM notifications WHERE idUser = ?""",(idUser,))
    conn.commit()
    #Supression des classes lié a l'utilisateurs

    #Fermeture de la connexion à la database
    conn.close()
    return redirect(url_for('gestiondata'))

@app.route('/banniruser/<int:idUser>', methods=['get','post'])
def banniruser(idUser):
    #Connexion à la DataBase
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération de toute les données de l'utilsateur a bannir
    cursor.execute("""SELECT * FROM user 
        WHERE user.idUsers=?""",(idUser,))
    user_for_ban = cursor.fetchall()
    #Déplacement de l'utilisateur dans la table des Utilisateurs bannis du site web
    cause = "Vous avez été banni pour abus sur ce site"
    personne_to_ban = []
    personne_to_ban.append((user_for_ban[0][1], user_for_ban[0][2], user_for_ban[0][3], user_for_ban[0][4], user_for_ban[0][5], user_for_ban[0][6], user_for_ban[0][7], cause))
    cursor.executemany("""INSERT INTO user_banni(name, email, password, vip_account, nb_classe_Faite, image_profil, idGroupe, cause) 
        VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", personne_to_ban)
    #Supprimer l'utilisateur de la table des utilisateurs
    cursor.execute("""DELETE FROM user WHERE idUsers =?""",(idUser,))
    #Execution des requêtes émisent
    conn.commit()
    #Récupération de l'ID du User pour switch les liaison des classes
    cursor.execute("""SELECT * from user_banni
        WHERE user_banni.name=?""", (user_for_ban[0][1],))
    the_user = cursor.fetchall()
    cursor.execute("""UPDATE classe
        SET idUser =0, idUserUnban =?
        WHERE classe.idUser =?""", (the_user[0][0], idUser,))
    cursor.execute("""UPDATE connexionclassuser
        SET idUser =0, idUserUnban =?
        WHERE connexionclassuser.idUser =?""", (the_user[0][0], idUser,))
    cursor.execute("""UPDATE notifications
        SET idUser =0, idUserUnban =?
        WHERE notifications.idUser =?""", (the_user[0][0], idUser,))
    conn.commit()
    #Fermeture de la connexion à  la database
    conn.close()
    return redirect(url_for('gestiondata'))

@app.route('/unbanuser/<int:idUser>', methods=['get','post'])
def unbanuser(idUser):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Récupération de la personne a déban
    cursor.execute("""SELECT * FROM user_banni 
        WHERE user_banni.idUsers=?""",(idUser,))
    unbaning_user = cursor.fetchall()
    #Déplacement de la personne dans la table des utilisateur
    personne_to_unban = []
    personne_to_unban.append((unbaning_user[0][1], unbaning_user[0][2], unbaning_user[0][3], unbaning_user[0][4], unbaning_user[0][5], unbaning_user[0][6], unbaning_user[0][8]))
    cursor.executemany("""INSERT INTO user(name, email, password, vip_account, nb_classe_Faite, image_profil, idGroupe) 
        VALUES(?, ?, ?, ?, ?, ?, ?)""", personne_to_unban)
    #Suppression de la personne dans la table des utilisateurs banni
    cursor.execute("""DELETE FROM user_banni WHERE idUsers =?""",(idUser,))   
    conn.commit()
    #Récupération de l'ID du User pour switch les liaison des classes
    cursor.execute("""SELECT * from user
        WHERE user.name=?""", (unbaning_user[0][1],))
    the_ubaning_user = cursor.fetchall()
    cursor.execute("""UPDATE classe
        SET idUserUnban =0, idUser =?
        WHERE classe.idUserUnban =?""", (the_ubaning_user[0][0], idUser,))
    cursor.execute("""UPDATE connexionclassuser
        SET idUserUnban =0, idUser =?
        WHERE connexionclassuser.idUserUnban =?""", (the_ubaning_user[0][0], idUser,))
    cursor.execute("""UPDATE notifications
        SET idUserUnban =0, idUser =?
        WHERE notifications.idUserUnban =?""", (the_ubaning_user[0][0], idUser,))
    conn.commit()
    #Fermeture de la connexion  à la database
    conn.close()
    return redirect(url_for('gestiondata'))

@app.route('/supprimeruserbanni/<int:idUser>', methods=['get', 'post'])
def supprimeruserbanni(idUser):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Suppression de l'utilisateur
    cursor.execute("""DELETE FROM user_banni WHERE idUsers =?""",(idUser,))
    cursor.execute("""DELETE FROM classe WHERE idUserUnban =?""",(idUser,))
    cursor.execute("""DELETE FROM connexionclassuser  WHERE idUser =?""",(idUser,))
    cursor.execute("""DELETE FROM notifications WHERE idUser = ?""",(idUser,))
    conn.commit()
    #Supression des classes lié a l'utilisateurs

    #Fermeture de la connexion à la database
    conn.close()
    return redirect(url_for('gestiondata'))

@app.route('/changergroupe/<int:idUser>/<int:groupe>', methods=['get','post'])
def changergroupe(idUser, groupe):
    #Connexion à la database
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    #Canger le groupe de l'utilisateur sélectionner
    new_group = []
    new_group.append((groupe, idUser))
    cursor.executemany("""UPDATE user
        SET idGroupe =?
        WHERE user.idUsers =?""", new_group)
    conn.commit()
    #Fermeture de la database
    conn.close()
    #Retour a la page de gestion Data
    return redirect(url_for('gestiondata'))
#-----------------------------------------
#----------Lancement de l'application-----
#-----------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
