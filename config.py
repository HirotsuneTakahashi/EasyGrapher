import secrets
# -*- coding: utf-8 -*-
#
# available languages

class Config:
    SECRET_KEY = secrets.token_hex(16) 
    LANGUAGES = {
    'en': 'English',
    'ja': '日本語'
    }
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = './translations'