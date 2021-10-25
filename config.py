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
    DEBUG = True
    DIALECT = 'mysql'
    DRIVER = 'pymysql'
    USERNAME = 'zhiyuan_sd'
    PASSWORD = 'rYa+wq10dFTWzYz8FeZgsWRygyKfLKULSRdKfRnEgSk='
    HOST = '119.91.135.29'
    PORT = '3306'
    DATABASE = 'zhiyuan_sd'
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST,PORT, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
