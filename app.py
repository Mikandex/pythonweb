# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 16:46:01 2022

@author: IfeanyiOnovo
"""

from flask import Flask, flash, render_template, request

import csv
app = Flask(__name__)

#app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n {email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', 'a') as csvdata:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file2 = csv.writer(csvdata,  quotechar=',', quoting=csv.QUOTE_MINIMAL)
        file2.writerow([email, subject, message])
        
        
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        #write_to_file(data)
        write_to_csv(data)
        
       # flash('Thank you for contacting us')
        return render_template('thankyou.html')
    else:
        return 'something went wrong'

