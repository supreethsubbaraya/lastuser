# -*- coding: utf-8 -*-

__version__ = '0.1'

from os import environ
from flask import Flask, Markup
from markdown import markdown
from coaster import configureapp

__MESSAGES = ['MESSAGE_FOOTER']

# These names are unavailable for use as usernames
RESERVED_USERNAMES = set([
    'app',
    'apps',
    'auth',
    'client',
    'confirm',
    'login',
    'logout',
    'new',
    'profile',
    'reset',
    'register',
    'token',
    'organizations',
    ])

app = Flask(__name__, instance_relative_config=True)
configureapp(app, 'LASTUSER_ENV')

for msg in __MESSAGES:
    app.config[msg] = Markup(markdown(app.config.get(msg, '')))


import lastuserapp.assets
import lastuserapp.mailclient
import lastuserapp.models
import lastuserapp.forms
import lastuserapp.views
if environ['LASTUSER_ENV'] == 'production':
    import lastuserapp.loghandler
