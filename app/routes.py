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
def get_computer_data():
    url = "https://www.51talk.pro/t/60efd2f42b2ad/ajax/sokecheng/getOtherInfos?query=%E7%94%B5%E8%84%91IT&num=8&id=22&order=rand"

    data = {

    }
    if request.args.get("query"):
        data['query'] = request.args.get("query")
    data['num'] = request.args.get("num")
    data['id'] = request.args.get("id")
    res = requests.request("GET", url, headers=headers, params=data)
    result = {'msg': res.json()['msg'], 'state': res.json()['state'], 'data': []}
    for data in res.json()['data']:
        if data['list_img']:
            list_img = "https://www.51talk.pro" + data['list_img'] if data['list_img'].find("sokecheng") != -1 else \
                data[
                    'list_img']
            data['list_img'] = list_img
        if data['school_img']:
            school_img = "https://www.51talk.pro" + data['school_img'] if data['school_img'].find(
                "sokecheng") != -1 else \
                data['school_img']

            data['school_img'] = school_img

        school_jianjie = data['school_jianjie']
        if school_jianjie:
            data['school_jianjie'] = school_jianjie.replace("/sokecheng/image",
                                                            "https://www.51talk.pro/sokecheng/image")

        content = data['content']
        if content:
            data['content'] = content.replace("/sokecheng/image", "https://www.51talk.pro/sokecheng/image")
        result['data'].append(data)
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