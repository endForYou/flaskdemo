"""
@version:1.0
@author: endaqa
@file routes.py
@time 2021/8/30 16:45
"""
import json

from app import app
import subprocess

log_file_list = ['platform', 'evaluation', 'oms', 'user', 'security', 'subject', 'config', 'eureka',
                 'zuul', 'volunteer', 'login', 'enterprise', 'content']


@app.route('/backend/log/<string:name>')
def get_data(name):  # put application's code here
    if name not in log_file_list:
        return None
    return subprocess.getoutput("docker logs -f --tail 100 %s" % name)
