# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from SolnaAndUppsalaOnTime import apiCall, clearJsonData
import os, uuid
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    hostname = os.uname()[1]
    randomid = uuid.uuid4()
    return 'Container Hostname: ' + hostname + ' , ' + 'UUID: ' + str(randomid) + '\n'

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

if __name__ == '__main__':
    app.run(debug=True,port=80,host='0.0.0.0')
