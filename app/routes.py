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
from app.models import School, Course

CORS(app, supports_credentials=True, resources=r"/*")

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}


@app.route('/schools')
def get_data():  # put application's code here

    page = request.args.get('page', 1, type=int)
    schools = School.query.order_by(School.id).paginate(
        page, 10, False)
    result = {'msg': 'success', 'state': 200, 'pageCount': 23, 'data': []}
    for school in schools.items:
        result['data'].append({
            'school': school.school,
            'school_img': school.school_img,
            'school_jianjie': json.loads(school.school_jianjie),
            'phone': school.phone,
            'address': school.address,
            'list_jieshao': json.loads(school.list_jieshao),
        })
    return result


#     # return result

@app.route('/course')
def get_course():
    page = request.args.get('page', 1, type=int)
    page_number = request.args.get('num', 10, type=int)
    course_type = request.args.get('course_type', "餐饮", type=str)
    courses = Course.query.filter_by(course_type=course_type).order_by(Course.id).paginate(
        page, page_number, False)
    result = {'msg': 'success', 'state': 200, 'data': []}
    for course in courses.items:
        result['data'].append({
            'name': course.name,
            'school': course.school,
            'maxprice': course.maxprice,
            'minprice': course.minprice,
            'content': json.loads(course.content),
            'abstract': json.loads(course.abstract),
            'address': course.detailAddress,
            'show_tag': json.loads(course.show_tag),
            'list_img': course.list_img,
            'phone': course.phone
        })
    return result


@app.route('/training')
def get_training_course_data():
    page = request.args.get('page', 1, type=int)
    page_number = request.args.get('num', 10, type=int)
    courses = Course.query.order_by(Course.id).paginate(
        page, page_number, False)
    result = {'msg': 'success', 'state': 200, 'pageCount': 20, 'data': []}
    for course in courses.items:
        result['data'].append({
            'name': course.name,
            'school': course.school,
            'maxprice': course.maxprice,
            'minprice': course.minprice,
            'content': json.loads(course.content),
            'abstract': json.loads(course.abstract),
            'address': course.detailAddress,
            'show_tag': json.loads(course.show_tag),
            'list_img': course.list_img,
            'phone': course.phone
        })
    return result
