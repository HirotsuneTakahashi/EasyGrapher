# -*- coding: utf-8 -*-
#
# available languages

class Config:
    SECRET_KEY = "^=ijahgw#acb_rqkmqf4&29b%#yfj$%hj65z4yk85crgf#-697"
    LANGUAGES = {
    'en': 'English',
    'ja': '日本語'
    }
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_TRANSLATION_DIRECTORIES = './translations'