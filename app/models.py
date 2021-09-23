"""
@version:1.0
@author: endaqa
@file models.py
@time 2021/9/7 18:11
"""
from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class School(db.Model):
    # s=db.Query.all()
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(255))
    school_img = db.Column(db.String(255))
    school_jianjie = db.Column(db.Text)
    phone = db.Column(db.String(255))
    address = db.Column(db.String(500))
    list_jieshao = db.Column(db.Text)
    __tablename__ = "shenhe_school"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    school = db.Column(db.String(255))
    maxprice = db.Column(db.String(255))
    minprice = db.Column(db.String(255))
    content = db.Column(db.Text)
    abstract = db.Column(db.Text)
    detailAddress = db.Column(db.String(255))
    show_tag = db.Column(db.Text)
    list_img = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    course_type=db.Column(db.String(255))
    __tablename__ = "shenhe_course"

    def __repr__(self):
        return '<Course {}>'.format(self.name)
