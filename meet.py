import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

## Configuration
DATABASE = '/tmp/meet.db'
DEBUF = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'ww'

app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])




@app.route('/', methods=['GET'])
def index(methods='GET'):
    return render_template('index.html',sth="3333333")
    
                                
                                
if __name__ =='__main__':
    app.run()
