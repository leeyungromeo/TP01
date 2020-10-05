from flask import Flask, render_template
from app import app
from app import routes

#app = Flask(__name__)
dico = {}


#@app.route('/')
#def index():
 #   return '<h1>Hello World ciao!</h1>'


if __name__ == '__main__':
    app.run(debug=True)
