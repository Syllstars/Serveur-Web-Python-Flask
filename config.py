from werkzeug.exceptions import HTTPException, default_exceptions, Aborter
import werkzeug.exceptions as ex
from flask import Flask, abort


class Config():
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    MAIL_DEBUG = False
    MAIL_SUPPRESS_SEND = False

    MAIL_USERNAME = 'mpontlevoy2001@gmail.com'
    MAIL_PASSWORD = 'bbujdcouojswajpj'

    MAIL_DEFAULT_SENDER = ('MMOGC -- Générateur de classe', 'maxime.pontlevoy@orange.fr')
    MAIL_MAX_EMAILS = None 
    MAIL_ASCII_ATTACHMENTS = False


class PayementRequired(ex.HTTPException):
    code = 402
    description = '<p>You Will pay for this !</p>'

