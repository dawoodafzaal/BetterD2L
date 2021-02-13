from flask import Flask

backEnd = Flask(__name__)   #this file

@backEnd.route('/')

def index():
    return "Hello"

if __name__ == "__main__":
    backEnd.run(debug = True)
