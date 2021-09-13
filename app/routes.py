"""
@version:1.0
@author: endaqa
@file routes.py
@time 2021/8/30 16:45
"""
import json

from app import app
from flask import render_template, flash, redirect, url_for, request, make_response
from app.forms import LoginForm
import requests
from flask_cors import *
from app.models import School

CORS(app, supports_credentials=True, resources=r"/*")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers moive was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
