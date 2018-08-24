# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from SolnaAndUppsalaOnTime import apiCall, clearJsonData
app = Flask(__name__, static_folder='static')

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

@app.route('/trains')
def show_trains():
    siteIdUppsala = "6086"
    siteIdSolna = "9509"
    
    jsoncallUppsala = apiCall(siteIdUppsala)
    jsoncallSolna = apiCall(siteIdSolna)
    cleanedJsonUppsala = clearJsonData(jsoncallUppsala)
    cleanedJsonSolna = clearJsonData(jsoncallSolna)

    data = cleanedJsonSolna + cleanedJsonUppsala

    return render_template('trains.html', data=data)
