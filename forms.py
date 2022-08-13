from random import choices
from secrets import choice
from tokenize import String
from types import MethodDescriptorType
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError
from flask_wtf.recaptcha import RecaptchaField

datatype = ["--Choose a type--",
            "char", "unsigned char", "short int", "unsigned short int", "int", "unsigned int", "long int", "unsigned long int",
            "float", "double", "long double", "bool"
            ]

notiftype = ["Général", "Information"]

class RegisterForm(FlaskForm):
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit = SubmitField("S'identifier")

class NewLoginForm(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    email = EmailField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired(), Length(min = 4, max = 10)])
    submit = SubmitField("S'inscrire")

    #Requete sur la DB
    def validate_email(self, email):

        if email.data == 'root@doomain.com':
            raise ValidationError('Cet email est déjà attribué.')
            
class NewClassGenerator(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    class_mere = StringField('Classe Mere')
    specialiter = StringField('spécialité')
    Image = FileField('New Image profil', validators = [FileAllowed(['jpg', 'png'], 'Images only!')])
    Protect_head = BooleanField('Protecteur du header')
    Generat_head_default_construct = BooleanField('Generer un constructeur par default')
    Generat_head_destruct = BooleanField('Generer un destructeur')
    Commentaire = BooleanField('Zone des commentaires')
    auteur = StringField('auteur')
    creation_data = DateField('Date de creation', format='%y-%m-%d')
    class_role = TextAreaField('Rôle de la classe')
    attribue = BooleanField('liste des attribues')

    public = BooleanField('Liste role public')
    type_public1 = SelectField('type var attribue public1', choices=datatype)
    public1 = StringField('Public1')
    type_public2 = SelectField('type var attribue public2', choices=datatype)
    public2 = StringField('Public2')
    type_public3 = SelectField('type var attribue public3', choices=datatype)
    public3 = StringField('Public3')
    type_public4 = SelectField('type var attribue public4', choices=datatype)
    public4 = StringField('Public4')
    type_public5 = SelectField('type var attribue public5', choices=datatype)
    public5 = StringField('Public5')
    type_public6 = SelectField('type var attribue public6', choices=datatype)
    public6 = StringField('Public6')
    type_public7 = SelectField('type var attribue public7', choices=datatype)
    public7 = StringField('Public7')
    type_public8 = SelectField('type var attribue public8', choices=datatype)
    public8 = StringField('Public8')

    protected = BooleanField('liste role proteger')
    type_protected1 = SelectField('type var attribue protected1', choices=datatype)
    protected1 = StringField('protected1')
    type_protected2 = SelectField('type var attribue protected2', choices=datatype)
    protected2 = StringField('protected2')
    type_protected3 = SelectField('type var attribue protected3', choices=datatype)
    protected3 = StringField('protected3')
    type_protected4 = SelectField('type var attribue protected4', choices=datatype)
    protected4 = StringField('protected4')
    type_protected5 = SelectField('type var attribue protected5', choices=datatype)
    protected5 = StringField('protected5')
    type_protected6 = SelectField('type var attribue protected6', choices=datatype)
    protected6 = StringField('protected6')
    type_protected7 = SelectField('type var attribue protected7', choices=datatype)
    protected7 = StringField('protected7')
    type_protected8 = SelectField('type var attribue protected8', choices=datatype)
    protected8 = StringField('protected8')  

    private = BooleanField('Liste role priver')
    type_private1 = SelectField('type de var attribue private1', choices=datatype)
    private1 = StringField('private1')
    type_private2 = SelectField('type de var attribue private2', choices=datatype)
    private2 = StringField('private2')
    type_private3 = SelectField('type de var attribue private3', choices=datatype)
    private3 = StringField('private3')
    type_private4 = SelectField('type de var attribue private4', choices=datatype)
    private4 = StringField('private4')
    type_private5 = SelectField('type de var attribue private5', choices=datatype)
    private5 = StringField('private5')
    type_private6 = SelectField('type de var attribue private6', choices=datatype)
    private6 = StringField('private6')
    type_private7 = SelectField('type de var attribue private7', choices=datatype)
    private7 = StringField('private7')
    type_private8 = SelectField('type de var attribue private8', choices=datatype)
    private8 = StringField('private8')

    methode = BooleanField('liste des méthodes')
    methode1 = StringField('methode1')
    methode2 = StringField('methode2')
    methode3 = StringField('methode3')
    methode4 = StringField('methode4')
    methode5 = StringField('methode5')
    methode6 = StringField('methode6')
    methode7 = StringField('methode7')
    methode8 = StringField('methode8')
    submit = SubmitField("Generer")

class ForgottenPassword(FlaskForm):
    email = EmailField('Donner votre email', validators = [DataRequired()])
    submit = SubmitField("Envoyer")

class ModifierClassGenerator(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    class_mere = StringField('Classe Mere')
    specialiter = StringField('spécialité')
    Protect_head = BooleanField('Protecteur du header')
    Generat_head_default_construct = BooleanField('Generer un constructeur par default')
    Generat_head_destruct = BooleanField('Generer un destructeur')
    Commentaire = BooleanField('Zone des commentaires')
    auteur = StringField('auteur')
    creation_data = DateField('Date de creation', format='%y-%m-%d')
    class_role = TextAreaField('Rôle de la classe')
    attribue = BooleanField('liste des attribues')

    public = BooleanField('Liste role public')
    type_public1 = SelectField('type var attribue public1', choices=datatype)
    public1 = StringField('Public1')
    type_public2 = SelectField('type var attribue public2', choices=datatype)
    public2 = StringField('Public2')
    type_public3 = SelectField('type var attribue public3', choices=datatype)
    public3 = StringField('Public3')
    type_public4 = SelectField('type var attribue public4', choices=datatype)
    public4 = StringField('Public4')
    type_public5 = SelectField('type var attribue public5', choices=datatype)
    public5 = StringField('Public5')
    type_public6 = SelectField('type var attribue public6', choices=datatype)
    public6 = StringField('Public6')
    type_public7 = SelectField('type var attribue public7', choices=datatype)
    public7 = StringField('Public7')
    type_public8 = SelectField('type var attribue public8', choices=datatype)
    public8 = StringField('Public8')

    protected = BooleanField('liste role proteger')
    type_protected1 = SelectField('type var attribue protected1', choices=datatype)
    protected1 = StringField('protected1')
    type_protected2 = SelectField('type var attribue protected2', choices=datatype)
    protected2 = StringField('protected2')
    type_protected3 = SelectField('type var attribue protected3', choices=datatype)
    protected3 = StringField('protected3')
    type_protected4 = SelectField('type var attribue protected4', choices=datatype)
    protected4 = StringField('protected4')
    type_protected5 = SelectField('type var attribue protected5', choices=datatype)
    protected5 = StringField('protected5')
    type_protected6 = SelectField('type var attribue protected6', choices=datatype)
    protected6 = StringField('protected6')
    type_protected7 = SelectField('type var attribue protected7', choices=datatype)
    protected7 = StringField('protected7')
    type_protected8 = SelectField('type var attribue protected8', choices=datatype)
    protected8 = StringField('protected8')  
    
    private = BooleanField('Liste role priver')
    type_private1 = SelectField('type de var attribue private1', choices=datatype)
    private1 = StringField('private1')
    type_private2 = SelectField('type de var attribue private2', choices=datatype)
    private2 = StringField('private2')
    type_private3 = SelectField('type de var attribue private3', choices=datatype)
    private3 = StringField('private3')
    type_private4 = SelectField('type de var attribue private4', choices=datatype)
    private4 = StringField('private4')
    type_private5 = SelectField('type de var attribue private5', choices=datatype)
    private5 = StringField('private5')
    type_private6 = SelectField('type de var attribue private6', choices=datatype)
    private6 = StringField('private6')
    type_private7 = SelectField('type de var attribue private7', choices=datatype)
    private7 = StringField('private7')
    type_private8 = SelectField('type de var attribue private8', choices=datatype)
    private8 = StringField('private8')

    methode = BooleanField('liste des méthodes')
    methode1 = StringField('methode1')
    methode2 = StringField('methode2')
    methode3 = StringField('methode3')
    methode4 = StringField('methode4')
    methode5 = StringField('methode5')
    methode6 = StringField('methode6')
    methode7 = StringField('methode7')
    methode8 = StringField('methode8')
    submit = SubmitField("Modifier")

class FormDataBanking(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    numbercard = StringField('Card Number', validators = [DataRequired(), Length(min = 14, max = 14)])
    expirationdate = DateField('MM/YYYY', format='%m-%y', validators = [DataRequired()])
    visualcryptogram = PasswordField('***', validators = [DataRequired(), Length(min = 3, max = 3)])
    submit = SubmitField("")

class FormChangUserName(FlaskForm):
    name = StringField('New Name', validators = [DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Envoyer")

class FormChangUserEmail(FlaskForm):
    name = StringField('new E-mail', validators = [DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Envoyer")

class FormChangUserPassword(FlaskForm):
    name = StringField('New Password', validators = [DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Envoyer")

class FormChangUserProfilImg(FlaskForm):
    Image = FileField('New Image profil', validators = [FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    recaptcha = RecaptchaField()
    submit = SubmitField("Envoyer")

class FormNewNotif(FlaskForm):
    type = SelectField('type de commentaire', choices=notiftype)
    commentaire = TextAreaField('Commentaire a écrire', validators = [DataRequired()])
    submit = SubmitField('envoyer le commentaire')

class FormCommandTerm(FlaskForm):
    commande = StringField('Commande pour la base de données', validators = [DataRequired()])
