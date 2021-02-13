from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

backEnd = Flask(__name__)   #this file

#data base where stuff will be stored if we need it
backEnd.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@backEnd.route('/')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    backEnd.run(debug = True)
