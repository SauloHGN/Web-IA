from flask import Flask, render_template, redirect, url_for
from src.principal_busca_grid import mapa, caminho, imagens

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', matriz=mapa, imagens=imagens)
    #return "Olá, Mundo!"

@app.route('/<path:subpath>', methods=['GET'])
def redirecionar(subpath):
   return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
