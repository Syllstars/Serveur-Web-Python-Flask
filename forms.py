from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Email, Length, ValidationError

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
    Protect_head = BooleanField('Protecteur du header')
    Generat_head_default_construct = BooleanField('Generer un constructeur par default')
    Generat_head_destruct = BooleanField('Generer un destructeur')
    auteur = StringField('auteur')
    creation_data = DateField('Date de creation', format='%y-%m-%d')
    class_role = StringField('Rôle de la classe')
    submit = SubmitField("Generer")

class ForgottenPassword(FlaskForm):
    email = EmailField('Donner votre email', validators = [DataRequired()])
    submit = SubmitField("Envoyer")

class ModifierClassGenerator(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    class_mere = StringField('Classe Mere')
    Protect_head = BooleanField('Protecteur du header')
    Generat_head_default_construct = BooleanField('Generer un constructeur par default')
    Generat_head_destruct = BooleanField('Generer un destructeur')
    auteur = StringField('auteur')
    creation_data = DateField('Date de creation', format='%y-%m-%d')
    class_role = StringField('Rôle de la classe')
    submit = SubmitField("Modifier")

class FormDataBanking(FlaskForm):
    name = StringField('Name', validators = [DataRequired()])
    numbercard = StringField('Card Number', validators = [DataRequired(), Length(min = 14, max = 14)])
    expirationdate = DateField('MM/YYYY', format='%m-%y', validators = [DataRequired()])
    visualcryptogram = PasswordField('***', validators = [DataRequired(), Length(min = 3, max = 3)])
    submit = SubmitField("")

class FormChangUserName(FlaskForm):
    name = StringField('New Name', validators = [DataRequired()])
    submit = SubmitField("Envoyer")

class FormChangUserEmail(FlaskForm):
    name = StringField('new E-mail', validators = [DataRequired()])
    submit = SubmitField("Envoyer")

class FormChangUserPassword(FlaskForm):
    name = StringField('New Password', validators = [DataRequired()])
    submit = SubmitField("Envoyer")
