# coding: utf-8

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from datetime import datetime
import sqlite3 as sql

app = Flask(__name__)
# name of your database; add path if necessary
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
# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app, metadata=metadata)

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

    def __repr__(self):
        return '<User %r>' % self.name

class notifications(db.Model):
    idNotif = db.Column(db.Integer, primary_key=True, unique=True)
    typeNotif = db.Column(db.Text)
    Commentaire = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))

    def __repr__(self):
        return '<User %r>' % self.typeNotif

def convert_pic():
    filename = "profile.jpg"
    with open(filename, 'rb') as file:       
        photo = file.read()
    return photo

def creation_groupe(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS groupe(
        idGroupe INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	    name TEXT,
	    valeur INTEGER
        )
    """)
    conn.commit()

def creation_user(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user(
        idUsers INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	    name TEXT,
	    email TEXT,
	    password INTEGER,
	    vip_account INTEGER,
        nb_classe_Faite INTEGER,
        image_profil BLOB,
	    idgroupe INTEGER,
	    FOREIGN KEY(idgroupe) REFERENCES groupe(idGroupe)
        )
    """)
    conn.commit()

def creation_class(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classe(
        idClasse INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	    name TEXT,
	    classe_mere TEXT,
	    Protect_head INTEGER,
	    Generat_head_default_construct INTEGER,
	    Generat_head_destruct INTEGER,
        auteur TEXT,
        creation_data DATETIME,
        class_role TEXT,
        idUser INTEGER,
	    FOREIGN KEY(idUser) REFERENCES user(idUsers)
        )
    """)
    conn.commit()

def creation_notif(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(
        idNotif INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        typeNotif TEXT,
        Commentaire TEXT,
        idUser INTEGER,
        FOREIGN KEY(idUser) REFERENCES user(idUsers)
        )
    """)
    conn.commit()


def InitDataBase():
    try:
        conn = sql.connect('database.db')
        cursor = conn.cursor()
        #Greation des databases
        creation_user(conn)
        creation_groupe(conn)
        creation_class(conn)
        creation_notif(conn)
        cursor.execute("""SELECT * FROM user""")
        rows_user = cursor.fetchall()
        photo = convert_pic()
        if rows_user == []:
            users = []
            users.append(("Maxime PONTLEVOY", "maxime.pontlevoy@orange.fr", 157365218, 2, 4, photo, 1))
            users.append(("Support", "mpontlevoy2001@gmail.com", 124864582, 2, 4, photo, 2))
            users.append(("Commercial", "pmaxime2001@gmail.com", 811483498, 0, 0, photo, 3))
            users.append(("Olivier CORRIO", "olivier.corrio@univ-brest.fr", 123456789, 0, 4, photo, 4))
            users.append(("Client1", "client.personne@gmail.com", 0000, 1, 0, photo, 4))
            cursor.executemany("""INSERT INTO user(name, email, password, vip_account, nb_classe_Faite, image_profil, idgroupe) 
                VALUES(?, ?, ?, ?, ?, ?, ?)""", users)

        cursor.execute("""SELECT * FROM groupe""")
        rows_gr = cursor.fetchall()
        if rows_gr == []:
            group = []
            group.append(("admin", 10))
            group.append(("support", 9))
            group.append(("commercial", 5))
            group.append(("client", 1))
            cursor.executemany("""INSERT INTO groupe(name, valeur) 
                VALUES(?, ?)""", group)

        cursor.execute("""SELECT * from classe""")
        rows_classe = cursor.fetchall()
        if rows_classe == []:
            clas = []
            clas.append(("Personnage", "Entité", 1, 1, 1, "Maxime PONTLEVOY", "Classe des personnages", 1))
            clas.append(("Chasseur", "Personnage", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Chasseurs", 1))
            clas.append(("Chevalier", "Personnage", 1, 1, 1, "Maxime PONTLEVOY", "Classe des chevaliers", 1))
            clas.append(("Mage", "personnage", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Mages", 1))
            clas.append(("Démon", "Entité", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Démons", 2))
            clas.append(("Gobelin", "Démon", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Gobelins", 2))
            clas.append(("Ogre", "Démon", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Ogres", 2))
            clas.append(("Orc", "Démon", 1, 1, 1, "Maxime PONTLEVOY", "Classe des Orc", 2))
            clas.append(("Maison", "Batimnt", 1, 1, 1, "Olivier CORRIO", "Classe général de la maison", 4))
            clas.append(("Salon", "Maison", 1, 1, 1, "Olivier CORRIO", "Pièce 1", 4))
            clas.append(("Cuisine", "Maison", 1, 1, 1, "Olivier CORRIO", "Pièce 2", 4))
            clas.append(("Salle a manger", "Maison", 1, 1, 1, "Olivier CORRIO", "Pièce 3", 4))
            cursor.executemany("""INSERT INTO classe(name, classe_mere, Protect_head, Generat_head_default_construct, Generat_head_destruct, auteur, creation_data, class_role, idUser) 
                VALUES(?, ?, ?, ?, ?, ?, DATETIME(), ?, ?)""", clas)

        cursor.execute("""SELECT * FROM notifications""")
        rows_notif = cursor.fetchall()
        if rows_notif == []:
            notif = []
            notif.append(("Général", "Bienvenue sur le site de création de classe pour MMORPG, vous avez la capaciter de pouvoir créer actuellement 10 classes.", 0))
            notif.append(("Information", "Si jamais vous voulez créer d'autre classe rendez-vous dans l'onglet Boutique pour pouvoir acheter un grade supérieur.", 0))
            notif.append(("Classe", "La création des vos future classe est près a l'meploie!!!", 0))
            cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
                VALUES(?, ?, ?)""", notif)
        if rows_notif != []:
            notif = []
            notif.append(("Général", "Bienvenue sur le site de création de classe pour MMORPG, vous avez la capaciter de pouvoir créer actuellement 10 classes.", 0))
            notif.append(("Information", "Si jamais vous voulez créer d'autre classe rendez-vous dans l'onglet Boutique pour pouvoir acheter un grade supérieur.", 0))
            notif.append(("Classe", "La création des vos futures classes est près a l'emploie!!!", 0))
            cursor.execute("""DELETE FROM notifications""")
            cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser)
                VALUES(?, ?, ?)""", notif)


        #Fin de l'appel
        conn.commit()
    except sql.OperationalError:
        print('Erreur la table existe déjà')
    except Exception as e:
        print("Erreur")
        conn.rollback()
        # raise e
    finally:
        conn.close()

#-----------------------------------------
#----------Lancement de l'application-----
#-----------------------------------------
@app.route('/')
def testdb():
    try:
        #Version Complexe
        socks1 = groupe.query.order_by(groupe.name).all()
        sock_text = '<ul>'
        for sock1 in socks1:
            sock_text += '<li>' + str(sock1.name) + ', ' + str(sock1.valeur) + '</li>'
        sock_text += '</ul>'

        socks2 = user.query.order_by(user.name).all()
        sock_text += '<ul>'
        for sock2 in socks2:
            sock_text += '<li>' + str(sock2.name) + ', ' + str(sock2.email) + ', ' + str(sock2.password) + ', ' + str(sock2.vip_account) + '</li>'
        sock_text += '</ul>' 
      
        socks3 = classe.query.order_by(classe.name).all() 
        sock_text += '<ul>'
        for sock3 in socks3:
            sock_text += '<li>' + str(sock3.name) + ', ' + str(sock3.classe_mere) + ', ' + str(sock3.Protect_head) + ', ' + str(sock3.Generat_head_default_construct) + ', ' + str(sock3.Generat_head_destruct) + ', ' + str(sock3.auteur) + ', ' + str(sock3.creation_data) + ', ' + str(sock3.class_role) + '</li>'
        sock_text += '</ul>' 
        return sock_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" +  str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text
    
if __name__ == '__main__':
    InitDataBase()
    app.run(debug=True)

