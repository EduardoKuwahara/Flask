from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/Contatos')
def Contatos():
    return render_template('Contatos.html')
@app.route('/Quem Somos')
def QuemSomos():
    return render_template('Quem somos.html')