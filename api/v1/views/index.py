#!/usr/bin/python3
'''
Module that define the index
'''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    '''
    Method that return the status of api
    '''
    return jsonify({"status": "OK"})
