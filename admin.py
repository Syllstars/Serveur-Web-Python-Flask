# coding: utf-8

from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from datetime import datetime
from random import *
import sqlite3 as sql
import numpy
import random

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
    specialiter = db.Column(db.Text)
    Protect_head = db.Column(db.Integer)
    Generat_head_default_construct = db.Column(db.Integer)
    Generat_head_destruct = db.Column(db.Integer)
    Commentaire= db.Column(db.Integer)
    auteur = db.Column(db.Text)
    creation_data = db.Column(db.DateTime)
    class_role = db.Column(db.Text)
    attribue = db.Column(db.Integer)
    public = db.Column(db.Integer)
    public1 = db.Column(db.Text)
    public2 = db.Column(db.Text)
    public3 = db.Column(db.Text)
    public4 = db.Column(db.Text)
    public5 = db.Column(db.Text)
    public6 = db.Column(db.Text)
    public7 = db.Column(db.Text)
    public8 = db.Column(db.Text)
    protected = db.Column(db.Integer)
    protected1 = db.Column(db.Text)
    protected2 = db.Column(db.Text)
    protected3 = db.Column(db.Text)
    protected4 = db.Column(db.Text)
    protected5 = db.Column(db.Text)
    protected6 = db.Column(db.Text)
    protected7 = db.Column(db.Text)
    protected8 = db.Column(db.Text)
    private = db.Column(db.Integer)
    private1 = db.Column(db.Text)
    private2 = db.Column(db.Text)
    private3 = db.Column(db.Text)
    private4 = db.Column(db.Text)
    private5 = db.Column(db.Text)
    private6 = db.Column(db.Text)
    private7 = db.Column(db.Text)
    private8 = db.Column(db.Text)
    methode = db.Column(db.Integer)
    methode1 = db.Column(db.Text)
    methode2 = db.Column(db.Text)
    methode3 = db.Column(db.Text)
    methode4 = db.Column(db.Text)
    methode5 = db.Column(db.Text)
    methode6 = db.Column(db.Text)
    methode7 = db.Column(db.Text)
    methode8 = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))
    image_classe = db.Column(db.LargeBinary)

    def __repr__(self):
        return '<User %r>' % self.name


class classemodel(db.Model):
    idClasse = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.Text)
    classe_mere = db.Column(db.Text)
    specialiter = db.Column(db.Text)
    Protect_head = db.Column(db.Integer)
    Generat_head_default_construct = db.Column(db.Integer)
    Generat_head_destruct = db.Column(db.Integer)
    Commentaire = db.Column(db.Integer)
    auteur = db.Column(db.Text)
    creation_data = db.Column(db.DateTime)
    class_role = db.Column(db.Text)
    attribue = db.Column(db.Integer)
    public = db.Column(db.Integer)
    public1 = db.Column(db.Text)
    public2 = db.Column(db.Text)
    public3 = db.Column(db.Text)
    public4 = db.Column(db.Text)
    public5 = db.Column(db.Text)
    public6 = db.Column(db.Text)
    public7 = db.Column(db.Text)
    public8 = db.Column(db.Text)
    protected = db.Column(db.Integer)
    protected1 = db.Column(db.Text)
    protected2 = db.Column(db.Text)
    protected3 = db.Column(db.Text)
    protected4 = db.Column(db.Text)
    protected5 = db.Column(db.Text)
    protected6 = db.Column(db.Text)
    protected7 = db.Column(db.Text)
    protected8 = db.Column(db.Text)
    private = db.Column(db.Integer)
    private1 = db.Column(db.Text)
    private2 = db.Column(db.Text)
    private3 = db.Column(db.Text)
    private4 = db.Column(db.Text)
    private5 = db.Column(db.Text)
    private6 = db.Column(db.Text)
    private7 = db.Column(db.Text)
    private8 = db.Column(db.Text)
    methode = db.Column(db.Integer)
    methode1 = db.Column(db.Text)
    methode2 = db.Column(db.Text)
    methode3 = db.Column(db.Text)
    methode4 = db.Column(db.Text)
    methode5 = db.Column(db.Text)
    methode6 = db.Column(db.Text)
    methode7 = db.Column(db.Text)
    methode8 = db.Column(db.Text)
    idUser = db.Column(db.Integer, db.ForeignKey('user.idUsers'))
    idUserUnban = db.Column(db.Integer, db.ForeignKey('user_banni.idUsers'))
    image_classe = db.Column(db.LargeBinary)

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

class commande(db.Model):
    idCommande = db.Column(db.Integer, primary_key=True, unique=True)
    Commande = db.Column(db.Text)
    Reponse = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.Commande

class demandeCommande(db.Model):
    idDemandeCommande = db.Column(db.Integer, primary_key=True, unique=True)
    idCommande = db.Column(db.Integer, db.ForeignKey('commande.idCommande'))

    def __repr__(self):
        return '<User %r>' % self.idDemandeCommande


def convert_pic():
    x = random.randint(1,2)
    if x == 1:
        filename = "profil1.jpg"
    if x == 2:
        filename = "profil2.jpg"
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

def creation_user_banni(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_banni(
        idUsers INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	    name TEXT,
	    email TEXT,
	    password INTEGER,
	    vip_account INTEGER,
        nb_classe_Faite INTEGER,
        image_profil BLOB,
        cause TEXT,
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
        specialiter TEXT,
	    Protect_head INTEGER,
	    Generat_head_default_construct INTEGER,
	    Generat_head_destruct INTEGER,
        Commentaire INTEGER,
        auteur TEXT,
        creation_data DATETIME,
        class_role TEXT,
        attribue INTEGER,
        public INTEGER,
        public1 TEXT,
        public2 TEXT,
        public3 TEXT,
        public4 TEXT,
        public5 TEXT,
        public6 TEXT,
        public7 TEXT,
        public8 TEXT,
        protected INTEGER,
        protected1 TEXT,
        protected2 TEXT,
        protected3 TEXT,
        protected4 TEXT,
        protected5 TEXT,
        protected6 TEXT,
        protected7 TEXT,
        protected8 TEXT,
        private INTEGER,
        private1 TEXT,
        private2 TEXT,
        private3 TEXT,
        private4 TEXT,
        private5 TEXT,
        private6 TEXT,
        private7 TEXT,
        private8 TEXT,
        methode INTEGER,
        methode1 TEXT,
        methode2 TEXT,
        methode3 TEXT,
        methode4 TEXT,
        methode5 TEXT,
        methode6 TEXT,
        methode7 TEXT,
        methode8 TEXT,
        idUser INTEGER,
        idUserUnban INTEGER,
        image_classe BLOB,
	    FOREIGN KEY(idUser) REFERENCES user(idUsers),
        FOREIGN KEY(idUserUnban) REFERENCES user_banni(idUsers)
        )
    """)
    conn.commit()

def creation_class_model(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS classemodel(
        idClasse INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
	    name TEXT,
	    classe_mere TEXT,
        specialiter TEXT,
	    Protect_head INTEGER,
	    Generat_head_default_construct INTEGER,
	    Generat_head_destruct INTEGER,
        Commentaire INTEGER,
        auteur TEXT,
        creation_data DATETIME,
        class_role TEXT,
        attribue INTEGER,
        public INTEGER,
        public1 TEXT,
        public2 TEXT,
        public3 TEXT,
        public4 TEXT,
        public5 TEXT,
        public6 TEXT,
        public7 TEXT,
        public8 TEXT,
        protected INTEGER,
        protected1 TEXT,
        protected2 TEXT,
        protected3 TEXT,
        protected4 TEXT,
        protected5 TEXT,
        protected6 TEXT,
        protected7 TEXT,
        protected8 TEXT,
        private INTEGER,
        private1 TEXT,
        private2 TEXT,
        private3 TEXT,
        private4 TEXT,
        private5 TEXT,
        private6 TEXT,
        private7 TEXT,
        private8 TEXT,
        methode INTEGER,
        methode1 TEXT,
        methode2 TEXT,
        methode3 TEXT,
        methode4 TEXT,
        methode5 TEXT,
        methode6 TEXT,
        methode7 TEXT,
        methode8 TEXT,
        idUser INTEGER,
        idUserUnban INTEGER,
        image_classe BLOB,
	    FOREIGN KEY(idUser) REFERENCES user(idUsers),
        FOREIGN KEY(idUserUnban) REFERENCES user_banni(idUsers)
        )
    """)
    conn.commit()

def creation_connexion_classmodel_user(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS connexionclassuser(
        idUser INTEGER,
        idUserUnban INTEGER,
        idClasse INTEGER,
        connexion INTEGER,
        FOREIGN KEY(idUser) REFERENCES user(idUsers),
        FOREIGN KEY(idClasse) REFERENCES classemodel(idClasse),
        FOREIGN KEY(idUserUnban) REFERENCES user_banni(idUsers)
        )
    """)

def creation_notif(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notifications(
        idNotif INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        typeNotif TEXT,
        Commentaire TEXT,
        idUser INTEGER,
        idUserUnban INTEGER,
        FOREIGN KEY(idUser) REFERENCES user(idUsers),
        FOREIGN KEY(idUserUnban) REFERENCES user_banni(idUsers)
        )
    """)
    conn.commit()

def creation_commande(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS commande(
        idCommande INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Commande TEXT,
        Reponse TEXT
        )
    """)

def creation_demandecommande(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS demandecommande(
        idDemandeCommande INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        idCommande INTEGER,
        FOREIGN KEY(idCommande) REFERENCES commande(idCommande)
        )
    """)

def InitDataBase():
    try:
        conn = sql.connect('database.db')
        cursor = conn.cursor()
        #Greation des databases
        creation_user(conn)
        creation_user_banni(conn)
        creation_groupe(conn)
        creation_class(conn)
        creation_class_model(conn)
        creation_notif(conn)
        creation_commande(conn)
        creation_demandecommande(conn)
        creation_connexion_classmodel_user(conn)
        cursor.execute("""SELECT * FROM user""")
        rows_user = cursor.fetchall()
        if rows_user == []:
            users = []
            users.append(("Maxime PONTLEVOY", "maxime.pontlevoy@orange.fr", 157365218, 2, 4, convert_pic(), 1))
            users.append(("Support", "mpontlevoy2001@gmail.com", 124864582, 2, 4, convert_pic(), 2))
            users.append(("Commercial", "pmaxime2001@gmail.com", 811483498, 1, 0, convert_pic(), 3))
            users.append(("Olivier CORRIO", "olivier.corrio@univ-brest.fr", 123456789, 0, 4, convert_pic(), 4))
            users.append(("Client1", "client.personne@gmail.com", 0000, 1, 0, convert_pic(), 4))
            users.append(("Jean PHILIPPE","jean.philippe@gmail.com", 1846943, 0, 6, convert_pic(), 4))
            users.append(("Marc ABSIDE","marc.abside158@gmail.com", 12946285, 0, 9, convert_pic(), 4))
            users.append(("Jules CENDRIN","jules185.18cendrin15@gmail.com", 1864856, 0, 0, convert_pic(), 4))
            users.append(("Arthur AVNANT","avnant.arthur6485@gmail.com", 12584682, 1, 0, convert_pic(), 4))
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
            clas.append(("Personnage", "Entite", "", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des personnages", 1, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Chasseur", "Personnage", "discretion", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Chasseurs", 1, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Chevalier", "Personnage", "force", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des chevaliers", 1, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Mage", "personnage", "magie", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Mages", 1, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Démon", "Entité", "force", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Démons", 2, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Gobelin", "Démon", "discretion", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Gobelins", 2, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Ogre", "Démon", "force", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Ogres", 2, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Orc", "Démon", "force", 1, 1, 1, 1, "Maxime PONTLEVOY", "Classe des Orc", 2, 0, 1, 1, "int m_vie", "int m_mana", 0, 1, "bool estVivant", 1, "recevoirDegats", "attaquer", "boirePotionDeVie", "ChangerArme", convert_pic()))
            clas.append(("Maison", "Batimnt", "", 1, 1, 1, 1, "Olivier CORRIO", "Classe général de la maison", 4, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Salon", "Maison", "", 1, 1, 1, 1, "Olivier CORRIO", "Pièce 1", 4, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Cuisine", "Maison", "", 1, 1, 1, 1, "Olivier CORRIO", "Pièce 2", 4, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Salle a manger", "Maison", "", 1, 1, 1, 1, "Olivier CORRIO", "Pièce 3", 4, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 1", "Planête 1", "dessert", 1, 1, 1, 1, "Marc ABSIDE", "Planête 1 de la Galaxie 1", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 1", "Planête 2", "ocean", 1, 1, 1, 1, "Marc ABSIDE", "Planête 2 de la Galaxie 1", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 1", "Planête 3", "jungle", 1, 1, 1, 1, "Marc ABSIDE", "Planête 3 de la Galaxie 1", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 1", "Planête 4", "plaine", 1, 1, 1, 1, "Marc ABSIDE", "Planête 4 de la Galaxie 1", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 2", "Planête 1", "gazeux", 1, 1, 1, 1, "Marc ABSIDE", "Planête 1 de la Galaxie 2", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 2", "Planête 2", "invivable", 1, 1, 1, 1, "Marc ABSIDE", "Planête 2 de la Galaxie 2", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 2", "Planête 3", "sec", 1, 1, 1, 1, "Marc ABSIDE", "Planête 3 de la Galaxie 2", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 2", "Planête 4", "arude", 1, 1, 1, 1, "Marc ABSIDE", "Planête 4 de la Galaxie 2", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Galaxie 2", "Planête 5", "monde minier", 1, 1, 1, 1, "Marc ABSIDE", "Planête 5 de la Galaxie 2", 7, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot tourelle", "Enemy", "force", 1, 1, 1, 1, "Jean PHILIPPE", "Robot tourelle", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot sniper", "Enemy", "precision", 1, 1, 1, 1, "Jean PHILIPPE", "Robot sniper", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot assassin", "Enemy", "discretion", 1, 1, 1, 1, "Jean PHILIPPE", "Robot asssssin", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot général", "Enemy", "intelligence", 1, 1, 1, 1, "Jean PHILIPPE", "Robot général", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot caporal", "Enemy", "intelligence", 1, 1, 1, 1, "Jean PHILIPPE", "Robot caporal", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            clas.append(("Robot dirigeant", "Enemy", "force diplomatique", 1, 1, 1, 1, "Jean PHILIPPE", "Robot dirigeant", 6, 0, 0, 0, "", "", 0, 0, "", 0,"" , "", "" , "", convert_pic()))
            cursor.executemany("""INSERT INTO classe
                (name, classe_mere, specialiter, Protect_head, Generat_head_default_construct, Generat_head_destruct, 
                Commentaire, auteur, creation_data, class_role, idUser, idUserUnban, 
                attribue, 
                private, private1, private2, 
                protected, 
                public, public1,
                methode, 
                methode1, methode2, methode3, methode4,
                image_classe) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, DATETIME(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", clas)

        cursor.execute("""SELECT * from classemodel""")
        rows_classe = cursor.fetchall()
        if rows_classe == []:
            clasmodel = []
            clasmodel.append(("Personnage", "Entité", "", 1, 1, 1, 1, "Classe Générique", "Classe des personnages", 0, 0, convert_pic()))
            clasmodel.append(("Chasseur", "Personnage", "précision", 1, 1, 1, 1, "Classe Générique", "Classe des Chasseurs", 0, 0, convert_pic()))
            clasmodel.append(("Chevalier", "Personnage", "force", 1, 1, 1, 1, "Classe Générique", "Classe des chevaliers", 0, 0, convert_pic()))
            clasmodel.append(("Mage", "personnage", "magie", 1, 1, 1, 1, "Classe Générique", "Classe des Mages", 0, 0, convert_pic()))
            clasmodel.append(("Démon", "Entité", "", 1, 1, 1, 1, "Classe Générique", "Classe des Démons", 0, 0, convert_pic()))
            clasmodel.append(("Gobelin", "Démon", "discretion", 1, 1, 1, 1, "Classe Générique", "Classe des Gobelins", 0, 0, convert_pic()))
            clasmodel.append(("Ogres", "Démon", "force", 1, 1, 1, 1, "Classe Générique", "Classe des Orges", 0, 0, convert_pic()))
            clasmodel.append(("Chevalier noir", "Démon", "force", 1, 1, 1, 1, "Classe Générique", "Classe des Chevalier noir", 0, 0, convert_pic()))
            clasmodel.append(("Dragons", "Démon", "magie", 1, 1, 1, 1, "Classe Générique", "Classe des Dragons", 0, 0, convert_pic()))
            clasmodel.append(("Roi Démon", "Démon", "magie", 1, 1, 1, 1, "Classe Générique", "Classe du Roi démon", 0, 0, convert_pic()))
            clasmodel.append(("Armes", "", "", 1, 1, 1, 1, "Classe Générique", "Classe des Armes", 0, 0, convert_pic()))
            clasmodel.append(("Arme a main", "Armes", "", 1, 1, 1, 1, "Classe Générique", "Classe des Armes à main", 0, 0, convert_pic()))
            clasmodel.append(("Epée Longue", "Arme a main", "puissance", 1, 1, 1, 1, "Classe Générique", "Classe des Epee longue", 0, 0, convert_pic()))
            clasmodel.append(("Dague", "Arme a main", "rapidite", 1, 1, 1, 1, "Classe Générique", "Classe des Dagues", 0, 0, convert_pic()))
            clasmodel.append(("Sabre", "Arme a main", "puissance", 1, 1, 1, 1, "Classe Générique", "Classe des Sabres", 0, 0, convert_pic()))
            clasmodel.append(("Arme a feu", "Armes", "distance", 1, 1, 1, 1, "Classe Générique", "Classe des Armes a feu", 0, 0, convert_pic()))
            clasmodel.append(("pistolet", "Arme a feu", "distance", 1, 1, 1, 1, "Classe Générique", "Classe des pistolet", 0, 0, convert_pic()))
            clasmodel.append(("mousqueter", "Arme a feu", "distance", 1, 1, 1, 1, "Classe Générique", "Classe des mousqueter", 0, 0, convert_pic()))
            cursor.executemany("""INSERT INTO classemodel(name, classe_mere, specialiter, Protect_head, Generat_head_default_construct, Generat_head_destruct, 
                Commentaire, auteur, creation_data, class_role, 
                idUser, idUserUnban, image_classe) 
                VALUES(?, ?, ?, ?, ?, ?, ?, ?, DATETIME(), ?, ?, ?, ?)""", clasmodel)

        cursor.execute("""SELECT * from connexionclassuser""")
        rows_classe = cursor.fetchall()
        if rows_classe == []:
            connexion = []
            for x in range(1, 10):
                for i in range(1, 19):
                    connexion.append((x, i, randint(0, 1)))
            cursor.executemany("""INSERT INTO connexionclassuser(idUser, idUserUnban, idClasse, connexion)
                VALUES(?, 0, ?, ?)""", connexion)


        cursor.execute("""SELECT * FROM notifications""")
        rows_notif = cursor.fetchall()
        if rows_notif == []:
            notif = []
            notif.append(("Général", "Bienvenue sur le site de création de classe pour MMORPG, vous avez la capaciter de pouvoir créer actuellement 10 classes.", 0))
            notif.append(("Information", "Si jamais vous voulez créer d'autre classe rendez-vous dans l'onglet Boutique pour pouvoir acheter un grade supérieur.", 0))
            notif.append(("Classe", "La création des vos future classe est près a l'meploie!!!", 0))
            cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser, idUserUnban)
                VALUES(?, ?, ?, 0)""", notif)
        if rows_notif != []:
            notif = []
            notif.append(("Général", "Bienvenue sur le site de création de classe pour MMORPG, vous avez la capaciter de pouvoir créer actuellement 10 classes.", 0))
            notif.append(("Information", "Si jamais vous voulez créer d'autre classe rendez-vous dans l'onglet Boutique pour pouvoir acheter un grade supérieur.", 0))
            notif.append(("Classe", "La création des vos futures classes est près a l'emploie!!!", 0))
            cursor.execute("""DELETE FROM notifications""")
            cursor.executemany("""INSERT INTO notifications(typeNotif, Commentaire, idUser, idUserUnban)
                VALUES(?, ?, ?, 0)""", notif)

        cursor.execute("""SELECT * from commande""")
        rows_commande = cursor.fetchall()
        if rows_commande == []:
            commande = []
            commande.append(("help", "all commande"))
            commande.append(("table", ""))
            commande.append(("all table", ""))
            commande.append(("data table", ""))
            commande.append(("last sequence", ""))
            commande.append(("ping", ""))
            commande.append(("cls", ""))
            cursor.executemany("""INSERT INTO commande(Commande, Reponse)
                VALUES(?, ?)""", commande)

        cursor.execute("""SELECT * from demandecommande""")
        rows_demandecommande = cursor.fetchall()
        if rows_demandecommande != []:
            cursor.execute("""DELETE FROM demandecommande""")


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

