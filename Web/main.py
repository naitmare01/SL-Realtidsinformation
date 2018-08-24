# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from SolnaAndUppsalaOnTime import apiCall, clearJsonData
app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/solna')
def show_solna():
    siteId = "9509"
    
    jsoncall = apiCall(siteId)
    cleanedJson = clearJsonData(jsoncall)

    for i in cleanedJson:
        return str(i["TrainOnTime"])

@app.route('/uppsala')
def show_uppsala():
    siteId = "6086"
    
    jsoncall = apiCall(siteId)
    cleanedJson = clearJsonData(jsoncall)

    #onTime = cleanedJson["trainOnTime"]

    return render_template('uppsala.html', data=cleanedJson)
