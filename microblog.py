"""
@version:1.0
@author: endaqa
@file microblog.py
@time 2021/8/30 16:48
"""
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 'User': User, 'Post': Post
    }
