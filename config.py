"""
@version:1.0
@author: endaqa
@file config.py
@time 2021/9/7 15:46
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'youwillnevergess'
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'root'
    PASSWORD = 'qwerty'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,
                                                                           PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or "smtp.sina.com"
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 465)
    MAIL_USE_TLS = 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "jiewei1989830@sina.com"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "b0b666f1826ac321"
    ADMINS = ['jiewei@junyanginfo.com', '258048759@qq.com']
    POSTS_PER_PAGE = 10
